#!/usr/bin/env python3
"""
mras_discover.py — fetch a Qualtrics MRAS survey and extract QID definitions.

Usage:
    python3 scripts/mras_discover.py --survey-url '<URL>' --opportunity-id <slug>

Downloads:
  - The Qualtrics survey HTML to extract question IDs (QIDs) and their text
  - Any file attachments referenced in the survey (DRD, RFI Technical Questions xlsx)

Writes:
  working/mras-surveys/<slug>/qid-definitions.json
  working/mras-surveys/<slug>/<attachment-filename>  (one per attachment)

QID definitions schema:
  [{"qid": "QID10", "type": "MC|TE|Matrix", "text": "...", "choices": [...]}, ...]

Notes:
- Qualtrics survey forms do not require authentication; they are publicly accessible
  via the direct survey link (SV_xxx).
- The personal link URL (Q_DL=...) is used to prepopulate respondent context.
- If the form returns "already completed", the survey is closed/already submitted.
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path


SV_RE = re.compile(r"SV_[A-Za-z0-9]+")


def extract_survey_id(url: str) -> str | None:
    m = SV_RE.search(url)
    return m.group(0) if m else None


def fetch_url(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (compatible; SpatialGIS-MRAS-Bot/1.0; "
                "+https://www.spatialgisservices.com)"
            )
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} fetching {url}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"URL error fetching {url}: {e.reason}") from e


def parse_qids_from_html(html: str) -> list[dict]:
    """
    Heuristic extraction of QID data from Qualtrics survey HTML.
    Qualtrics embeds survey data as JSON in a JS variable named 'Qualtrics.SurveyEngine.SurveyData'.
    """
    qids = []

    # Try to find the embedded survey JSON
    m = re.search(r"Qualtrics\.SurveyEngine\.SurveyData\s*=\s*(\{.*?\});", html, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            questions = data.get("Questions", {})
            for qid, q in questions.items():
                entry = {
                    "qid": qid,
                    "type": q.get("QuestionType", ""),
                    "text": re.sub(r"<[^>]+>", "", q.get("QuestionText", "")),
                    "choices": [],
                }
                choices = q.get("Choices", {})
                for key in sorted(choices.keys(), key=lambda k: int(k) if k.isdigit() else 0):
                    entry["choices"].append(
                        re.sub(r"<[^>]+>", "", choices[key].get("Display", ""))
                    )
                qids.append(entry)
            return qids
        except (json.JSONDecodeError, KeyError):
            pass

    # Fallback: scrape visible question text and IDs from HTML
    question_blocks = re.findall(
        r'id="(QID\d+[^"]*)"[^>]*>.*?<div[^>]*class="[^"]*QuestionText[^"]*"[^>]*>(.*?)</div>',
        html,
        re.DOTALL | re.IGNORECASE,
    )
    for qid, text in question_blocks:
        qids.append({
            "qid": qid.split("-")[0],
            "type": "unknown",
            "text": re.sub(r"<[^>]+>", " ", text).strip(),
            "choices": [],
        })

    return qids


def find_attachment_urls(html: str, base_url: str) -> list[str]:
    urls = []
    patterns = [
        r'href="([^"]*\.(xlsx|xls|docx|doc|pdf))"',
        r'src="([^"]*\.(xlsx|xls|docx|doc|pdf))"',
    ]
    for pattern in patterns:
        for m in re.finditer(pattern, html, re.IGNORECASE):
            url = m.group(1)
            if not url.startswith("http"):
                url = base_url.rstrip("/") + "/" + url.lstrip("/")
            if url not in urls:
                urls.append(url)
    return urls


def download_attachment(url: str, dest: Path) -> bool:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; SpatialGIS-MRAS-Bot/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            dest.write_bytes(resp.read())
        return True
    except Exception as e:
        print(f"  WARNING: Could not download {url}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Discover MRAS Qualtrics survey QIDs")
    parser.add_argument("--survey-url", required=True, help="Full Qualtrics survey URL")
    parser.add_argument("--opportunity-id", required=True, help="Opportunity slug/ID")
    args = parser.parse_args()

    survey_url = args.survey_url
    opp_id = args.opportunity_id

    sv_id = extract_survey_id(survey_url)
    if not sv_id:
        print(f"ERROR: Cannot extract SV_xxx from URL: {survey_url}", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(f"working/mras-surveys/{opp_id}")
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching survey {sv_id} for opportunity {opp_id}...")
    try:
        html = fetch_url(survey_url)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Check if already completed
    if "already completed" in html.lower() or "survey is now closed" in html.lower():
        print("NOTE: Survey appears already completed or closed.")
        (out_dir / "status.txt").write_text("already_completed")
        return

    qids = parse_qids_from_html(html)
    qid_path = out_dir / "qid-definitions.json"
    qid_path.write_text(json.dumps(qids, indent=2))
    print(f"Extracted {len(qids)} QID definitions → {qid_path}")

    # Save raw HTML for inspection
    (out_dir / "survey-raw.html").write_text(html)

    # Download attachments
    base_url = "https://feedback.gsa.gov"
    attachment_urls = find_attachment_urls(html, base_url)
    if attachment_urls:
        print(f"Found {len(attachment_urls)} attachment(s):")
        for url in attachment_urls:
            filename = url.split("/")[-1].split("?")[0] or "attachment"
            dest = out_dir / filename
            print(f"  Downloading {filename}...")
            download_attachment(url, dest)
    else:
        print("No file attachments found in survey.")

    # Write metadata
    meta = {
        "opportunity_id": opp_id,
        "survey_id": sv_id,
        "survey_url": survey_url,
        "qid_count": len(qids),
        "attachments": attachment_urls,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2))
    print(f"Discovery complete → {out_dir}")


if __name__ == "__main__":
    main()
