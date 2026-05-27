"""
MRAS Qualtrics submitter.

Consumes a per-opportunity *resolved-answer* file produced by
`scripts/mras_map_answers.py`. The resolved file already contains:

  - identity field name -> value
  - QID selections in Qualtrics form-name format (e.g. "QR~QID12~10" -> "checked")
    with forbidden choices already filtered out by the mapper

This replaces the prior position-based autofill approach, which was retired on
2026-05-27 after it was found to be making false SBA-certification and
contract-vehicle claims (see working/mras-autofill-audit.md).

Usage:
    python scripts/mras_submitter.py \\
        --resolved working/mras-answers/hud-oig-database-resolved.json \\
        --overrides working/mras-answers/hud-oig-database.json \\
        --canonical scripts/mras_answers.json \\
        [--submit]   # without this flag = dry run
        [--headed]   # show browser window
        [--output-dir working/mras-runs]

Safety:
- Dry run by default (no Submit click)
- Refuses to run if the capability statement file is missing
- Refuses to --submit unless canonical's OK_TO_SUBMIT is true (set per-session)
- Logs every fill and every miss, plus a full-page screenshot
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

from playwright.async_api import Page, async_playwright


@dataclass
class FillReport:
    opportunity_id: str
    survey_url: str
    filled: dict[str, str] = field(default_factory=dict)
    skipped: dict[str, str] = field(default_factory=dict)
    not_found: list[str] = field(default_factory=list)
    capability_statement: str = ""
    submitted: bool = False
    dry_run: bool = True
    screenshot_path: str = ""

    def to_json(self) -> str:
        return json.dumps(
            {
                "opportunity_id": self.opportunity_id,
                "survey_url": self.survey_url,
                "dry_run": self.dry_run,
                "submitted": self.submitted,
                "capability_statement": self.capability_statement,
                "filled_count": len(self.filled),
                "skipped_count": len(self.skipped),
                "not_found_count": len(self.not_found),
                "filled": self.filled,
                "skipped": self.skipped,
                "not_found": self.not_found,
                "screenshot_path": self.screenshot_path,
            },
            indent=2,
        )


async def _fill_identity(page: Page, identity: dict[str, str], report: FillReport) -> None:
    for label, value in identity.items():
        if not value:
            report.skipped[f"identity:{label}"] = "empty value"
            continue
        located = False
        for strategy in (
            lambda l=label: page.get_by_label(l, exact=False),
            lambda l=label: page.locator(f'input[aria-label*="{l}"]'),
            lambda l=label: page.locator(f'input[placeholder*="{l}"]'),
        ):
            try:
                el = strategy().first
                if await el.count() > 0:
                    await el.fill(value, timeout=2000)
                    report.filled[f"identity:{label}"] = value
                    located = True
                    break
            except Exception:
                continue
        if not located:
            report.not_found.append(f"identity:{label}")


async def _fill_qid_selection(page: Page, name: str, action: str, report: FillReport) -> None:
    """Qualtrics inputs are hidden behind custom UI (label spans). Three shapes:
    - Multi-select checkbox: id == name == "QR~QID12~10"
    - Single-select radio:   id == "QR~QID11~1", name == "QR~QID11", value=="1"
    - Matrix Yes/No row:     id == "QR~QID14~1~1" (Yes) / "QR~QID14~1~2" (No)
    Strategy: resolve to a target element id, then check via JS (bypasses visibility)
    and dispatch a change event so Qualtrics' runtime-checked binding fires.
    """
    target_id = name
    if action in ("Yes", "No"):
        target_id = f"{name}~{1 if action == 'Yes' else 2}"
    is_text_fill = action not in ("checked", "selected", "Yes", "No")
    try:
        if is_text_fill:
            result = await page.evaluate(
                """
                ([id, value]) => {
                  const el = document.getElementById(id);
                  if (!el) return { ok: false, reason: 'not_found' };
                  const tag = el.tagName.toLowerCase();
                  if (tag !== 'input' && tag !== 'textarea') return { ok: false, reason: `unexpected tag ${tag}` };
                  el.focus();
                  el.value = value;
                  el.dispatchEvent(new Event('input', { bubbles: true }));
                  el.dispatchEvent(new Event('change', { bubbles: true }));
                  el.blur();
                  return { ok: true, value: el.value.substring(0, 60), tag: tag };
                }
                """,
                [target_id, str(action)],
            )
        else:
            result = await page.evaluate(
                """
                (id) => {
                  const el = document.getElementById(id);
                  if (!el) return { ok: false, reason: 'not_found' };
                  const lbl = document.querySelector(`label[for="${id}"]`);
                  if (!el.checked) {
                    if (lbl) { lbl.click(); } else { el.click(); }
                  }
                  if (!el.checked) {
                    el.checked = true;
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                    el.dispatchEvent(new Event('click', { bubbles: true }));
                  }
                  return { ok: true, checked: el.checked, tag: el.tagName, type: el.type };
                }
                """,
                target_id,
            )
        if not result or not result.get("ok"):
            report.not_found.append(target_id)
            return
        report.filled[target_id] = f"{action} (checked={result.get('checked')})"
    except Exception as exc:
        report.skipped[target_id] = f"error: {exc}"


async def _upload_capability_statement(page: Page, capability_path: Path, report: FillReport) -> None:
    file_input = page.locator('input[type="file"]')
    try:
        if await file_input.count() == 0:
            report.not_found.append("capability_statement_upload")
            return
        await file_input.first.set_input_files(str(capability_path))
        report.filled["capability_statement_upload"] = str(capability_path)
    except Exception as exc:
        report.skipped["capability_statement_upload"] = f"error: {exc}"


async def submit_mras(
    *,
    resolved_path: Path,
    overrides_path: Path,
    canonical_path: Path,
    submit: bool,
    headed: bool,
    output_dir: Path,
) -> FillReport:
    resolved = json.loads(resolved_path.read_text())
    overrides = json.loads(overrides_path.read_text())
    canonical = json.loads(canonical_path.read_text())

    opportunity_id = resolved["opportunity_id"]
    identity = resolved["identity"]
    selections = resolved["qid_selections_for_submitter"]
    survey_url = overrides["survey_url"]
    capability_path = Path(overrides["capability_statement_path"])

    if not capability_path.exists():
        raise SystemExit(f"[{opportunity_id}] capability statement not found: {capability_path}")
    missing_identity = [k for k, v in identity.items() if not v]
    if missing_identity:
        raise SystemExit(f"[{opportunity_id}] identity fields missing values: {missing_identity}")

    if submit and not canonical.get("OK_TO_SUBMIT"):
        print(
            f"[{opportunity_id}] REFUSING --submit: OK_TO_SUBMIT is false in {canonical_path}. "
            "Set it to true (with date + opportunity scope) only after human review.",
            file=sys.stderr,
        )
        submit = False

    report = FillReport(
        opportunity_id=opportunity_id,
        survey_url=survey_url,
        capability_statement=str(capability_path),
        dry_run=not submit,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = output_dir / f"{opportunity_id}-filled.png"
    report_path = output_dir / f"{opportunity_id}-fill-report.json"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=not headed)
        context = await browser.new_context()
        page = await context.new_page()

        print(f"[{opportunity_id}] navigating to survey", file=sys.stderr)
        await page.goto(survey_url, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(2500)

        await _fill_identity(page, identity, report)
        for name, action in selections.items():
            await _fill_qid_selection(page, name, action, report)
        await _upload_capability_statement(page, capability_path, report)

        report.screenshot_path = str(screenshot_path)
        await page.screenshot(path=str(screenshot_path), full_page=True)

        if submit:
            advance_ids = await page.evaluate(
                "() => Array.from(document.querySelectorAll('input.AdvanceButton, input[id$=\"-Advance\"]')).map(b => b.id)"
            )
            print(f"[{opportunity_id}] clicking {len(advance_ids)} Advance buttons", file=sys.stderr)
            for aid in advance_ids:
                try:
                    await page.evaluate(
                        "(id) => { const b = document.getElementById(id); if (b) b.click(); }",
                        aid,
                    )
                    await page.wait_for_timeout(300)
                except Exception:
                    pass

            await page.wait_for_timeout(1500)

            url_before = page.url
            html_before = await page.content()

            submit_result = await page.evaluate(
                """
                () => {
                  const btn = document.getElementById('NextButton');
                  if (!btn) return { ok: false, reason: 'NextButton not found' };
                  const disabled = btn.disabled || btn.getAttribute('aria-disabled') === 'true';
                  if (disabled) return { ok: false, reason: 'NextButton disabled', value: btn.value };
                  btn.click();
                  return { ok: true, value: btn.value };
                }
                """
            )
            print(f"[{opportunity_id}] NextButton click: {submit_result}", file=sys.stderr)
            await page.wait_for_timeout(5000)
            try:
                await page.wait_for_load_state("networkidle", timeout=20000)
            except Exception:
                pass

            url_after = page.url
            html_after = await page.content()
            text_after = await page.evaluate("() => document.body.innerText")
            navigated = url_before != url_after or "EndOfSurvey" in url_after
            thanks = any(
                phrase in text_after.lower()
                for phrase in [
                    "thank you for your response",
                    "thank you for completing",
                    "your response has been recorded",
                    "submission has been received",
                    "thanks for your response",
                    "end of survey",
                ]
            )
            verified = bool(submit_result.get("ok") and (navigated or thanks))

            print(
                f"[{opportunity_id}] post-submit verify: url_changed={url_before != url_after}, "
                f"navigated={navigated}, thanks_text={thanks}, verified={verified}",
                file=sys.stderr,
            )

            if not submit_result.get("ok"):
                report.skipped["submit"] = submit_result.get("reason", "unknown")
            elif not verified:
                report.skipped["submit_verify"] = (
                    f"NextButton clicked but no navigation or thank-you message detected. "
                    f"URL: {url_after}. First 300 chars of body: {text_after[:300]!r}"
                )
                report.submitted = False
            else:
                report.submitted = True
            await page.screenshot(path=str(output_dir / f"{opportunity_id}-confirmation.png"), full_page=True)
            Path(output_dir / f"{opportunity_id}-confirmation.html").write_text(html_after)
        else:
            print(
                f"[{opportunity_id}] dry-run complete. "
                f"Filled: {len(report.filled)} | Skipped: {len(report.skipped)} | Not found: {len(report.not_found)}",
                file=sys.stderr,
            )

        await browser.close()

    report_path.write_text(report.to_json())
    print(report.to_json())
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--resolved", type=Path, required=True)
    parser.add_argument("--overrides", type=Path, required=True)
    parser.add_argument("--canonical", type=Path, default=Path("scripts/mras_answers.json"))
    parser.add_argument("--submit", action="store_true")
    parser.add_argument("--headed", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=Path("working/mras-runs"))
    args = parser.parse_args()

    asyncio.run(
        submit_mras(
            resolved_path=args.resolved,
            overrides_path=args.overrides,
            canonical_path=args.canonical,
            submit=args.submit,
            headed=args.headed,
            output_dir=args.output_dir,
        )
    )


if __name__ == "__main__":
    main()
