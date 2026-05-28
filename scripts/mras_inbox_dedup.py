#!/usr/bin/env python3
"""
mras_inbox_dedup.py — deduplicate a raw MRAS inbox JSON file.

Usage:
    python3 scripts/mras_inbox_dedup.py <raw-json> <unique-json>

The script:
1. Generates a slug for each thread from its subject line.
2. Removes duplicate slugs, keeping the newest message per slug.
3. Skips entries whose slug already has submitted:true in any
   working/mras-runs/*-fill-report.json.
4. Writes the deduplicated list to <unique-json>.
"""

import json
import re
import sys
from pathlib import Path


def slugify(subject: str) -> str:
    s = subject.lower()
    s = re.sub(r"\s*-\s*mras\s*$", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^(reminder|response received):\s*", "", s, flags=re.IGNORECASE)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s


def load_submitted_slugs(runs_dir: Path) -> set:
    submitted = set()
    for report_path in runs_dir.glob("*-fill-report.json"):
        try:
            data = json.loads(report_path.read_text())
            if data.get("submitted") is True:
                slug = data.get("opportunity_id") or data.get("slug")
                if slug:
                    submitted.add(slug)
        except Exception:
            pass
    return submitted


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <raw-json> <unique-json>", file=sys.stderr)
        sys.exit(1)

    raw_path = Path(sys.argv[1])
    unique_path = Path(sys.argv[2])

    if not raw_path.exists():
        print(f"ERROR: {raw_path} not found", file=sys.stderr)
        sys.exit(1)

    threads = json.loads(raw_path.read_text())

    runs_dir = Path("working/mras-runs")
    submitted_slugs = load_submitted_slugs(runs_dir)

    seen_slugs: dict = {}
    for t in threads:
        slug = slugify(t.get("subject", ""))
        t["slug"] = slug
        if slug in submitted_slugs:
            t["skip_reason"] = "already_submitted"
            continue
        existing = seen_slugs.get(slug)
        if existing is None or t.get("date", "") > existing.get("date", ""):
            seen_slugs[slug] = t

    unique_threads = list(seen_slugs.values())
    unique_path.parent.mkdir(parents=True, exist_ok=True)
    unique_path.write_text(json.dumps(unique_threads, indent=2))
    print(
        f"Dedup complete: {len(threads)} → {len(unique_threads)} unique "
        f"(skipped {len(threads) - len(unique_threads)} duplicates/already-submitted)"
    )


if __name__ == "__main__":
    main()
