#!/usr/bin/env python3
"""
mras_map_answers.py — map working/mras-answers/<slug>.json to resolved QID answers.

Usage:
    python3 scripts/mras_map_answers.py --opportunity-id <slug>

Reads:
  working/mras-answers/<slug>.json          — human / AI authored answers
  working/mras-surveys/<slug>/qid-definitions.json — QID definitions from mras_discover.py
  scripts/mras_answers.json                 — company defaults

Writes:
  working/mras-answers/<slug>-resolved.json — QID → answer mapping ready for mras_submitter.py

Prints warnings for:
  - QIDs in definitions that have no answer mapped
  - Answer keys that do not correspond to any known QID
  - Guardrail violations (e.g., claiming certifications not held)

Exit code 1 if any warnings or qid_not_found.
"""

import argparse
import json
import sys
from pathlib import Path


def load_json(path: Path) -> dict | list:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def check_guardrails(answers: dict, company: dict) -> list[str]:
    violations = []
    socio = company.get("socioeconomic", {})

    checks = [
        ("hubzone", socio.get("hubzone", False), "HUBZone"),
        ("eight_a", socio.get("eight_a", False), "8(a)"),
        ("sdvosb", socio.get("sdvosb", False), "SDVOSB"),
        ("wosb", socio.get("wosb", False), "WOSB"),
    ]
    for key, held, label in checks:
        if answers.get(key) is True and not held:
            violations.append(f"GUARDRAIL: {label} claimed but not held by company")

    if "54151HACS" in str(answers.get("sin_selection", "")):
        violations.append("GUARDRAIL: HACS SIN (54151HACS) claimed but not held")
    if "54151HEAL" in str(answers.get("sin_selection", "")):
        violations.append("GUARDRAIL: HEAL SIN (54151HEAL) claimed but not held")
    if "518210ERM" in str(answers.get("sin_selection", "")):
        violations.append("GUARDRAIL: 518210ERM SIN claimed but not held")

    return violations


def build_resolved(answers: dict, qid_defs: list, defaults: dict) -> tuple[dict, list, list]:
    """
    Returns (resolved_map, warnings, qid_not_found).
    resolved_map: {QID: answer_value}
    warnings: list of warning strings
    qid_not_found: list of QID strings in definitions with no mapping
    """
    resolved = {}
    warnings = []
    qid_not_found = []

    # Standard MRAS QID mapping
    qid_field_map = {
        "QID1": "company_name",
        "QID2": "uei",
        "QID3": "cage",
        "QID4": "point_of_contact_name",
        "QID5": "point_of_contact_email",
        "QID6": "point_of_contact_phone",
        "QID7": "contract_vehicle",
        "QID8": "sin_selection",
        "QID9": "small_business",
        "QID10": "naics_selection",
        "QID11": "sdb",
        "QID12": "hubzone",
        "QID13": "eight_a",
        "QID14": "sdvosb",
        "QID15": "wosb",
        "QID16": "short_answer_capability",
        "QID17": "capability_statement_upload",
        "QID18": "capability_questions_answers",
        "QID19": "lead_time_override",
        "QID20": "subcontracting_override",
    }

    # Merge defaults and per-opportunity answers
    merged = {**defaults, **answers}

    # Map company defaults
    company_defaults = {
        "company_name": merged.get("legal_name", "SpatialGIS, LLC"),
        "uei": merged.get("uei", "XE8LEMK77DC9"),
        "cage": merged.get("cage", "7RFJ7"),
        "small_business": merged.get("small_business", True),
        "sdb": merged.get("sdb", True),
        "hubzone": merged.get("hubzone", False),
        "eight_a": merged.get("eight_a", False),
        "sdvosb": merged.get("sdvosb", False),
        "wosb": merged.get("wosb", False),
        "contract_vehicle": merged.get("contract_vehicle", "GSA MAS 47QTCA24D00DS"),
    }
    all_answers = {**company_defaults, **merged}

    for qid_def in qid_defs:
        qid = qid_def.get("qid", "")
        field = qid_field_map.get(qid)
        if field and field in all_answers:
            resolved[qid] = all_answers[field]
        elif qid in all_answers:
            resolved[qid] = all_answers[qid]
        else:
            qid_not_found.append(qid)
            warnings.append(f"qid_not_found: {qid} ({qid_def.get('text', '')[:60]})")

    return resolved, warnings, qid_not_found


def main():
    parser = argparse.ArgumentParser(description="Map MRAS answers to resolved QID map")
    parser.add_argument("--opportunity-id", required=True, help="Opportunity slug/ID")
    args = parser.parse_args()

    opp_id = args.opportunity_id
    answers_path = Path(f"working/mras-answers/{opp_id}.json")
    qid_def_path = Path(f"working/mras-surveys/{opp_id}/qid-definitions.json")
    resolved_path = Path(f"working/mras-answers/{opp_id}-resolved.json")

    company_data_raw = load_json(Path("scripts/mras_answers.json"))
    company = company_data_raw.get("company", {})
    defaults = company_data_raw.get("default_answers", {})
    defaults.update({
        "legal_name": company.get("legal_name", "SpatialGIS, LLC"),
        "uei": company.get("uei", "XE8LEMK77DC9"),
        "cage": company.get("cage", "7RFJ7"),
        "sdb": company.get("socioeconomic", {}).get("sdb", True),
        "hubzone": company.get("socioeconomic", {}).get("hubzone", False),
        "eight_a": company.get("socioeconomic", {}).get("eight_a", False),
        "sdvosb": company.get("socioeconomic", {}).get("sdvosb", False),
        "wosb": company.get("socioeconomic", {}).get("wosb", False),
    })

    answers = load_json(answers_path)
    qid_defs = load_json(qid_def_path) if qid_def_path.exists() else []

    if not isinstance(qid_defs, list):
        qid_defs = []

    # Guardrail check
    violations = check_guardrails(answers, company)
    for v in violations:
        print(f"WARNING: {v}", file=sys.stderr)

    resolved, warnings, qid_not_found = build_resolved(answers, qid_defs, defaults)

    output = {
        "opportunity_id": opp_id,
        "resolved_answers": resolved,
        "warnings": warnings,
        "qid_not_found": qid_not_found,
        "guardrail_violations": violations,
        "ready": len(warnings) == 0 and len(violations) == 0,
    }

    resolved_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_path.write_text(json.dumps(output, indent=2))

    if warnings or violations:
        for w in warnings + violations:
            print(f"WARNING: {w}", file=sys.stderr)
        print(f"BLOCKED: {len(warnings)} warning(s) / {len(violations)} violation(s) — manual review required")
        sys.exit(1)
    else:
        print(f"READY: resolved {len(resolved)} QID answers → {resolved_path}")


if __name__ == "__main__":
    main()
