"""
Dedupes a list of MRAS RFI email subject/date pairs into unique opportunities,
strips "Reminder: " prefix, and emits a list of unique opportunity slugs the
caller can then pass to mras_discover / mras_status_check.

Input file (working/mras-inbox/raw-subjects.json) is a list of
  { "subject": "...", "date": "ISO8601", "thread_id": "...", "snippet": "..." }
records pulled from Gmail via search_threads.

Output (working/mras-inbox/unique-opportunities.json) keys each unique subject
to: { slug, agency, latest_date, latest_thread_id, count, all_dates }

Slug rule: strip Reminder prefix, strip ' - MRAS', kebab-case, lowercase, alnum+hyphen.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def slugify(subject: str) -> str:
    s = re.sub(r"^Reminder:\s*", "", subject, flags=re.IGNORECASE)
    s = re.sub(r"\s*-\s*MRAS\s*$", "", s, flags=re.IGNORECASE)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s[:80]


def strip_reminder(subject: str) -> str:
    return re.sub(r"^Reminder:\s*", "", subject, flags=re.IGNORECASE).strip()


def agency_guess(subject: str) -> str:
    base = strip_reminder(subject)
    parts = base.split(" - ", 1)
    return parts[0].strip() if parts else "UNKNOWN"


def main(raw_path: Path, out_path: Path) -> None:
    raw = json.loads(raw_path.read_text())
    bucket: dict[str, dict] = {}
    for rec in raw:
        norm = strip_reminder(rec["subject"]).strip()
        slug = slugify(norm)
        cur = bucket.setdefault(
            slug,
            {
                "slug": slug,
                "subject_normalized": norm,
                "agency": agency_guess(rec["subject"]),
                "latest_date": rec["date"],
                "latest_thread_id": rec["thread_id"],
                "thread_ids": [],
                "all_dates": [],
                "count": 0,
            },
        )
        cur["count"] += 1
        cur["thread_ids"].append(rec["thread_id"])
        cur["all_dates"].append(rec["date"])
        if rec["date"] > cur["latest_date"]:
            cur["latest_date"] = rec["date"]
            cur["latest_thread_id"] = rec["thread_id"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(list(bucket.values()), indent=2))
    print(f"{len(raw)} emails -> {len(bucket)} unique opportunities. Saved to {out_path}")


if __name__ == "__main__":
    raw = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("working/mras-inbox/raw-subjects.json")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("working/mras-inbox/unique-opportunities.json")
    main(raw, out)
