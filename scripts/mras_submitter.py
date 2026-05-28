#!/usr/bin/env python3
"""
mras_submitter.py — submit a resolved MRAS answer set to a Qualtrics survey.

Usage:
    # Dry run (validation only, no submission)
    python3 scripts/mras_submitter.py \
        --resolved working/mras-answers/<slug>-resolved.json \
        --overrides working/mras-answers/<slug>.json

    # Actual submission (requires ok_to_submit: true in scripts/mras_answers.json)
    python3 scripts/mras_submitter.py \
        --resolved working/mras-answers/<slug>-resolved.json \
        --overrides working/mras-answers/<slug>.json \
        --submit

Writes:
    working/mras-runs/<slug>-fill-report.json

Fill report schema:
    {
      "opportunity_id": "...",
      "survey_id": "SV_xxx",
      "submitted": true/false,
      "dry_run": true/false,
      "skipped": [],        // QIDs skipped (no answer)
      "not_found": [],      // QIDs in resolved but not in form
      "filled": [],         // QIDs successfully filled
      "submission_status": "SUBMITTED-CONFIRMED" | "REJECTED-BY-QUALTRICS" | "DRY-RUN" | "NOT-SUBMITTED",
      "confirmation_id": "...",  // if confirmed
      "timestamp": "..."
    }

NOTE: Actual Qualtrics POST submission uses the undocumented Qualtrics survey
      response API endpoint. This requires the survey's embedded data structure.
      In environments without browser automation, --submit performs a best-effort
      HTTP POST to the Qualtrics response endpoint.
"""

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path


def load_json(path: Path) -> dict:
    if not path.exists():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    return json.loads(path.read_text())


def check_authorization() -> bool:
    answers_path = Path("scripts/mras_answers.json")
    if not answers_path.exists():
        print("ERROR: scripts/mras_answers.json not found — cannot verify authorization", file=sys.stderr)
        return False
    data = json.loads(answers_path.read_text())
    return data.get("ok_to_submit", False) is True


def build_qualtrics_post_payload(resolved_answers: dict, survey_id: str, dl_token: str) -> dict:
    """
    Build the POST body for Qualtrics embedded survey response submission.
    Qualtrics accepts responses via its public survey POST endpoint.
    """
    payload = {
        "SurveyID": survey_id,
        "Q_DL": dl_token,
    }
    for qid, value in resolved_answers.items():
        if isinstance(value, bool):
            payload[qid] = "1" if value else "0"
        elif isinstance(value, (int, float)):
            payload[qid] = str(value)
        else:
            payload[qid] = str(value)
    return payload


def submit_to_qualtrics(
    survey_url: str, resolved_answers: dict, survey_id: str
) -> tuple[bool, str]:
    """
    Attempt to submit to Qualtrics. Returns (success, status_message).
    """
    # Extract distribution link token
    dl_match = urllib.parse.urlparse(survey_url)
    params = urllib.parse.parse_qs(dl_match.query)
    dl_token = params.get("Q_DL", [""])[0]

    post_url = f"https://feedback.gsa.gov/jfe/form/{survey_id}"
    payload = build_qualtrics_post_payload(resolved_answers, survey_id, dl_token)
    data = urllib.parse.urlencode(payload).encode("utf-8")

    req = urllib.request.Request(
        post_url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (compatible; SpatialGIS-MRAS-Bot/1.0)",
            "Referer": survey_url,
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace").lower()
            if "thank you" in body or "response has been recorded" in body or "already completed" in body:
                # Extract confirmation ID if present
                import re
                m = re.search(r"confirmation id[:\s]+([A-Z0-9_\-]+)", body, re.IGNORECASE)
                conf_id = m.group(1) if m else "unknown"
                return True, f"SUBMITTED-CONFIRMED (confirmation: {conf_id})"
            else:
                return False, "REJECTED-BY-QUALTRICS (no confirmation found in response)"
    except urllib.error.HTTPError as e:
        return False, f"REJECTED-BY-QUALTRICS (HTTP {e.code})"
    except Exception as e:
        return False, f"REJECTED-BY-QUALTRICS ({e})"


def main():
    parser = argparse.ArgumentParser(description="Submit MRAS resolved answers to Qualtrics")
    parser.add_argument("--resolved", required=True, help="Path to <slug>-resolved.json")
    parser.add_argument("--overrides", required=True, help="Path to <slug>.json (overrides/metadata)")
    parser.add_argument("--submit", action="store_true", help="Actually submit (default: dry run)")
    args = parser.parse_args()

    resolved_path = Path(args.resolved)
    overrides_path = Path(args.overrides)

    resolved_data = load_json(resolved_path)
    overrides = load_json(overrides_path)

    opp_id = resolved_data.get("opportunity_id", resolved_path.stem.replace("-resolved", ""))
    resolved_answers = resolved_data.get("resolved_answers", {})

    # Check for blockers
    if not resolved_data.get("ready", True):
        warnings = resolved_data.get("warnings", [])
        violations = resolved_data.get("guardrail_violations", [])
        print(f"ERROR: Resolved answers not ready — {len(warnings)} warnings, {len(violations)} violations", file=sys.stderr)
        print("Run mras_map_answers.py first and resolve all warnings.", file=sys.stderr)
        sys.exit(1)

    # Load survey metadata
    meta_path = Path(f"working/mras-surveys/{opp_id}/meta.json")
    meta = load_json(meta_path) if meta_path.exists() else {}
    survey_id = meta.get("survey_id", overrides.get("survey_id", ""))
    survey_url = overrides.get("survey_url", meta.get("survey_url", ""))

    if not survey_id:
        print(f"ERROR: No survey_id found for {opp_id}", file=sys.stderr)
        sys.exit(1)

    # Count filled / skipped
    filled = list(resolved_answers.keys())
    skipped = resolved_data.get("qid_not_found", [])

    dry_run = not args.submit

    report = {
        "opportunity_id": opp_id,
        "survey_id": survey_id,
        "submitted": False,
        "dry_run": dry_run,
        "skipped": skipped,
        "not_found": [],
        "filled": filled,
        "submission_status": "DRY-RUN" if dry_run else "NOT-SUBMITTED",
        "confirmation_id": None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    if dry_run:
        if skipped:
            print(f"DRY-RUN WARNING: {len(skipped)} QID(s) have no answer: {skipped}")
        else:
            print(f"DRY-RUN OK: {len(filled)} QIDs ready, 0 skipped")
    else:
        # Verify authorization
        if not check_authorization():
            print("ERROR: ok_to_submit is not true in scripts/mras_answers.json — submission blocked", file=sys.stderr)
            sys.exit(1)

        print(f"Submitting {opp_id} to Qualtrics survey {survey_id}...")
        success, status = submit_to_qualtrics(survey_url, resolved_answers, survey_id)

        report["submitted"] = success
        report["submission_status"] = status if success else "REJECTED-BY-QUALTRICS"

        if success:
            # Try to extract confirmation ID from status message
            import re
            m = re.search(r"confirmation:\s*([A-Z0-9_\-]+)", status, re.IGNORECASE)
            if m:
                report["confirmation_id"] = m.group(1)
            print(f"SUCCESS: {status}")
        else:
            print(f"FAILED: {status}", file=sys.stderr)

    runs_dir = Path("working/mras-runs")
    runs_dir.mkdir(parents=True, exist_ok=True)
    report_path = runs_dir / f"{opp_id}-fill-report.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(f"Fill report → {report_path}")

    if not dry_run and not report["submitted"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
