#!/usr/bin/env python3
"""
mras_triage_classify.py — classify MRAS opportunities as PASS / MAYBE / DECLINE.

Usage:
    python3 scripts/mras_triage_classify.py <unique-json> <triage-json>

Classification rules (applied in order):
  SKIP_CLOSED  — response due date is in the past
  DECLINE      — subject or description matches a hard-decline keyword
  PASS         — subject or description matches a core-capability keyword
  MAYBE        — subject or description matches a broad-IT keyword
  DECLINE      — default if no keyword match (conservative)

Reads keyword lists from scripts/mras_answers.json.
"""

import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path


def _word_boundary_match(text_lower: str, keyword_lower: str) -> bool:
    # Use word boundaries for short acronyms to prevent substring false positives
    # (e.g. "NGA" inside "engagement", "GIS" inside "logistics")
    return bool(re.search(r"\b" + re.escape(keyword_lower) + r"\b", text_lower))


def load_answers() -> dict:
    p = Path("scripts/mras_answers.json")
    if p.exists():
        return json.loads(p.read_text())
    return {}


def parse_due_date(body: str) -> date | None:
    m = re.search(r"Responses Due:\s*(\d{2}/\d{2}/\d{4})", body or "")
    if m:
        try:
            return datetime.strptime(m.group(1), "%m/%d/%Y").date()
        except ValueError:
            pass
    return None


def keywords_match(text: str, keywords: list[str]) -> list[str]:
    text_lower = text.lower()
    return [kw for kw in keywords if _word_boundary_match(text_lower, kw.lower())]


def classify(thread: dict, answers: dict, today: date) -> dict:
    subject = thread.get("subject", "")
    description = thread.get("description", "")
    due_date_str = thread.get("due_date", "")
    combined = f"{subject} {description}"

    # Parse due date
    due = thread.get("due_date_parsed")
    if not due and due_date_str:
        try:
            due = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            pass
    if due is None:
        due = parse_due_date(combined)

    # SKIP_CLOSED: already past
    if due and due < today:
        return {**thread, "triage": "SKIP_CLOSED", "triage_reason": f"Due {due} is in the past"}

    decline_kws = answers.get("capability_keywords_decline", [])
    pass_kws = answers.get("capability_keywords_pass", [])
    maybe_kws = answers.get("capability_keywords_maybe", [])

    # DECLINE: hard-decline keyword match
    matched_decline = keywords_match(combined, decline_kws)
    if matched_decline:
        return {
            **thread,
            "triage": "DECLINE",
            "triage_reason": f"Hard-decline keyword(s): {matched_decline[:3]}",
        }

    # PASS: core capability keyword match
    matched_pass = keywords_match(combined, pass_kws)
    if matched_pass:
        return {
            **thread,
            "triage": "PASS",
            "triage_reason": f"Core capability keyword(s): {matched_pass[:3]}",
        }

    # MAYBE: broad IT keyword match
    matched_maybe = keywords_match(combined, maybe_kws)
    if matched_maybe:
        return {
            **thread,
            "triage": "MAYBE",
            "triage_reason": f"Broad IT keyword(s): {matched_maybe[:3]}",
        }

    # Default: DECLINE (conservative — if we can't find a fit, don't respond)
    return {
        **thread,
        "triage": "DECLINE",
        "triage_reason": "No capability keyword match — conservative decline",
    }


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <unique-json> <triage-json>", file=sys.stderr)
        sys.exit(1)

    unique_path = Path(sys.argv[1])
    triage_path = Path(sys.argv[2])

    if not unique_path.exists():
        print(f"ERROR: {unique_path} not found", file=sys.stderr)
        sys.exit(1)

    threads = json.loads(unique_path.read_text())
    answers = load_answers()
    today = date.today()

    classified = [classify(t, answers, today) for t in threads]

    counts = {"PASS": 0, "MAYBE": 0, "DECLINE": 0, "SKIP_CLOSED": 0}
    for t in classified:
        counts[t["triage"]] = counts.get(t["triage"], 0) + 1

    triage_path.parent.mkdir(parents=True, exist_ok=True)
    triage_path.write_text(json.dumps(classified, indent=2))

    print(
        f"Triage complete: {len(classified)} opportunities — "
        f"PASS={counts['PASS']} MAYBE={counts['MAYBE']} "
        f"DECLINE={counts['DECLINE']} SKIP_CLOSED={counts['SKIP_CLOSED']}"
    )


if __name__ == "__main__":
    main()
