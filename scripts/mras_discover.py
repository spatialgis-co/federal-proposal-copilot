"""
MRAS survey discovery — opens a Qualtrics survey URL and harvests:

  - All Qualtrics form field names (QID inventory)
  - All visible label/question text
  - All anchor links + file attachments (Draft Requirements Document candidates)
  - Full page HTML and a screenshot

Does NOT fill or submit anything — read-only discovery.

Usage:
    python scripts/mras_discover.py \\
        --survey-url "https://feedback.gsa.gov/jfe/form/SV_..." \\
        --opportunity-id hud-oig-database \\
        [--output-dir working/mras-discovery]
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

from playwright.async_api import async_playwright


async def discover(*, survey_url: str, opportunity_id: str, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    html_path = output_dir / f"{opportunity_id}.html"
    text_path = output_dir / f"{opportunity_id}.txt"
    screenshot_path = output_dir / f"{opportunity_id}.png"
    inventory_path = output_dir / f"{opportunity_id}-inventory.json"
    attachments_dir = output_dir / f"{opportunity_id}-attachments"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        print(f"[{opportunity_id}] loading {survey_url}", file=sys.stderr)
        await page.goto(survey_url, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(2000)

        html = await page.content()
        html_path.write_text(html)

        text = await page.evaluate("() => document.body.innerText")
        text_path.write_text(text)

        await page.screenshot(path=str(screenshot_path), full_page=True)

        qid_names = await page.evaluate(
            """
            () => {
              const out = new Set();
              document.querySelectorAll('input, select, textarea').forEach(el => {
                if (el.name && el.name.startsWith('QR~')) out.add(el.name);
              });
              return Array.from(out);
            }
            """
        )

        questions = await page.evaluate(
            """
            () => {
              const blocks = [];
              document.querySelectorAll('.QuestionText, .QuestionBody, label').forEach(el => {
                const t = (el.innerText || '').trim();
                if (t && t.length > 4) blocks.push(t);
              });
              return blocks;
            }
            """
        )

        links = await page.evaluate(
            """
            () => Array.from(document.querySelectorAll('a[href]')).map(a => ({
              href: a.href,
              text: (a.innerText || '').trim()
            }))
            """
        )

        attachment_exts = (".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".zip")
        attachment_candidates = [
            l for l in links
            if any(l["href"].lower().endswith(ext) for ext in attachment_exts)
            or "qualtricscontent" in l["href"].lower()
            or "file" in (l["text"] or "").lower()
            or "attachment" in (l["text"] or "").lower()
            or "draft" in (l["text"] or "").lower()
            or "requirement" in (l["text"] or "").lower()
            or "rfi" in (l["text"] or "").lower()
        ]

        downloaded = []
        if attachment_candidates:
            attachments_dir.mkdir(parents=True, exist_ok=True)
        for cand in attachment_candidates:
            href = cand["href"]
            try:
                parsed = urlparse(href)
                fname = Path(parsed.path).name or "attachment"
                fname = re.sub(r"[^A-Za-z0-9._-]+", "_", fname)
                dest = attachments_dir / fname
                req = urllib.request.Request(href, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=30) as resp, open(dest, "wb") as out:
                    out.write(resp.read())
                downloaded.append({"url": href, "path": str(dest), "text": cand["text"]})
            except Exception as exc:
                downloaded.append({"url": href, "error": str(exc), "text": cand["text"]})

        await browser.close()

    inventory = {
        "opportunity_id": opportunity_id,
        "survey_url": survey_url,
        "html_path": str(html_path),
        "text_path": str(text_path),
        "screenshot_path": str(screenshot_path),
        "qid_inventory": sorted(qid_names),
        "qid_count": len(qid_names),
        "question_blocks": questions[:200],
        "all_links": links,
        "attachment_candidates": downloaded,
    }
    inventory_path.write_text(json.dumps(inventory, indent=2))
    print(json.dumps({
        "opportunity_id": opportunity_id,
        "qid_count": len(qid_names),
        "attachment_count": len(downloaded),
        "inventory": str(inventory_path),
    }, indent=2))
    return inventory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--survey-url", required=True)
    parser.add_argument("--opportunity-id", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("working/mras-discovery"))
    args = parser.parse_args()
    asyncio.run(discover(survey_url=args.survey_url, opportunity_id=args.opportunity_id, output_dir=args.output_dir))


if __name__ == "__main__":
    main()
