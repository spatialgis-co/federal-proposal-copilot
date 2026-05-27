"""
mras_map_answers — given:

  - scripts/mras_answers.json (canonical truth: SpatialGIS facts, no QID indices)
  - working/mras-discovery/<opp>-qid-definitions.json (Qualtrics QuestionDefinitions
    for this specific survey, with per-survey choice IDs)
  - working/mras-answers/<opp>.json (per-opportunity overrides:
    capability question answers, NAICS for this opportunity, SIN selection,
    capability statement path, any subcontracting/lead-time overrides)

emit a per-survey answer map that scripts/mras_submitter.py can consume:

  - identity field name -> value
  - QID full name (e.g., "QR~QID12~10") -> "checked" / value
  - plus a sanity report: which canonical-truth selections found / not-found,
    which choices were forbidden and correctly NOT selected, etc.

The output map is the SAFE replacement for the position-based autofill profile c7.
It refuses to select any choice whose label matches a forbidden_label_substring.

Usage:
    python scripts/mras_map_answers.py \\
        --opportunity-id hud-oig-database \\
        [--canonical scripts/mras_answers.json] \\
        [--qid-definitions working/mras-discovery/hud-oig-database-qid-definitions.json] \\
        [--overrides working/mras-answers/hud-oig-database.json] \\
        [--output working/mras-answers/hud-oig-database-resolved.json]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def strip_html(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()


def find_choice_ids_by_substring(choices: dict, substrings: list[str], case_insensitive: bool = True) -> list[str]:
    """Return Qualtrics choice IDs whose Display label contains any of the substrings."""
    out = []
    for cid, c in (choices or {}).items():
        label = ""
        if isinstance(c, dict):
            label = strip_html(c.get("Display", ""))
        else:
            label = str(c)
        haystack = label.lower() if case_insensitive else label
        for sub in substrings:
            needle = sub.lower() if case_insensitive else sub
            if needle in haystack:
                out.append(cid)
                break
    return out


def find_choice_ids_by_exact_label(choices: dict, target_labels: list[str], case_insensitive: bool = True) -> list[str]:
    out = []
    for cid, c in (choices or {}).items():
        label = ""
        if isinstance(c, dict):
            label = strip_html(c.get("Display", ""))
        else:
            label = str(c)
        if case_insensitive:
            if label.lower() in [t.lower() for t in target_labels]:
                out.append(cid)
        else:
            if label in target_labels:
                out.append(cid)
    return out


def get_choices(qdef: dict) -> dict:
    """Qualtrics stores choices under Language.EN.Choices or directly under Choices."""
    lang_choices = qdef.get("Language", {}).get("EN", {}).get("Choices")
    if lang_choices:
        return lang_choices
    return qdef.get("Choices") or {}


def map_answers(
    *,
    opportunity_id: str,
    canonical: dict,
    qid_defs_block: dict,
    overrides: dict,
) -> dict:
    qdefs = qid_defs_block["QuestionDefinitions"]
    identity = canonical["identity"]
    truth = canonical["canonical_truth"]
    report: dict[str, Any] = {
        "opportunity_id": opportunity_id,
        "identity": dict(identity),
        "qid_selections": {},
        "qid_skipped_forbidden": {},
        "qid_not_found": {},
        "warnings": [],
    }
    selections: dict[str, str] = {}

    def select(qid: str, choice_ids: list, kind: str) -> None:
        if not choice_ids:
            report["qid_not_found"][qid] = kind
            return
        for cid in choice_ids:
            selections[f"QR~{qid}~{cid}"] = "checked"
            report["qid_selections"].setdefault(qid, []).append(f"{cid} ({kind})")

    def value(qid: str, val: str) -> None:
        selections[f"QR~{qid}~{val}"] = "selected"
        report["qid_selections"].setdefault(qid, []).append(f"{val} (single-select)")

    for qid, qdef in qdefs.items():
        qtext = strip_html(qdef.get("Language", {}).get("EN", {}).get("QuestionText", ""))
        choices = get_choices(qdef)
        qt_lower = qtext.lower()
        qtype = qdef.get("QuestionType", "")
        sel = qdef.get("Selector", "")

        if qtype == "TE" and sel == "SL" and "capability website" in qt_lower:
            url = overrides.get("capability_website") or identity.get("Company Website (URLs only)") or "https://www.spatialgisservices.com"
            selections[f"QR~{qid}"] = url
            report["qid_selections"].setdefault(qid, []).append(f"text:{url}")
            continue

        if qtype == "TE" and sel == "ESTB":
            short = overrides.get("short_answer_responses", {}).get(qid)
            if not short:
                short = overrides.get("short_answer_responses", {}).get(f"{qid}_default")
            if short:
                selections[f"QR~{qid}"] = short[:500] if "optional" not in qt_lower else short
                report["qid_selections"].setdefault(qid, []).append(f"text:{len(short)} chars")
            else:
                report["warnings"].append(f"{qid} ({qtype}/{sel}) has no short_answer_responses entry. Question: {qtext[:120]}")
            continue

        if not choices:
            continue

        if (
            "socio-economic" in qt_lower
            or "socioeconomic" in qt_lower
            and ("select all" in qt_lower or "categor" in qt_lower)
        ):
            forbidden_subs = truth["socioeconomic_indicators"]["forbidden_codes"]
            forbidden_ids = []
            for fcode in forbidden_subs:
                forbidden_ids += [
                    cid for cid in choices
                    if strip_html(choices[cid].get("Display", "") if isinstance(choices[cid], dict) else "").lower().startswith(fcode.lower())
                    or strip_html(choices[cid].get("Display", "") if isinstance(choices[cid], dict) else "").lower() == fcode.lower()
                ]
            report["qid_skipped_forbidden"][qid] = sorted(set(forbidden_ids))
            allowed_codes = truth["socioeconomic_indicators"]["allowed_codes"]
            allowed = find_choice_ids_by_exact_label(choices, allowed_codes)
            select(qid, allowed, f"socioeconomic:{','.join(allowed_codes)}")
            continue

        if qt_lower.strip().startswith("business size") or (
            len(choices) <= 3
            and any("small business" in strip_html(c.get("Display", "") if isinstance(c, dict) else "").lower() for c in choices.values())
        ):
            ids = [
                cid for cid, c in choices.items()
                if "small business" in strip_html(c.get("Display", "") if isinstance(c, dict) else "").lower()
                and "other than" not in strip_html(c.get("Display", "") if isinstance(c, dict) else "").lower()
            ]
            if ids:
                value(qid, ids[0])
            else:
                report["qid_not_found"][qid] = "business_size:s"
            continue

        if "gsa contracts that your company holds" in qt_lower or "gsa contract solution" in qt_lower:
            forbidden = truth["gsa_contracts_held"]["forbidden_label_substrings"]
            for_ids = find_choice_ids_by_substring(choices, forbidden)
            report["qid_skipped_forbidden"][qid] = for_ids
            allowed = find_choice_ids_by_substring(choices, truth["gsa_contracts_held"]["allowed_labels"])
            allowed = [a for a in allowed if a not in for_ids]
            select(qid, allowed, "gsa_contracts:MAS")
            continue

        if "based solely on the gsa contracts" in qt_lower:
            for_ids = find_choice_ids_by_substring(choices, truth["gsa_sin_eligibility"]["forbidden_label_substrings"])
            report["qid_skipped_forbidden"][qid] = for_ids
            sin_targets = overrides.get("sin_selection") or truth["gsa_sin_eligibility"]["held_sins"]
            allowed = find_choice_ids_by_substring(choices, sin_targets)
            allowed = [a for a in allowed if a not in for_ids]
            select(qid, allowed, "gsa_sins")
            continue

        if "naics code" in qt_lower:
            requested = overrides.get("naics_selection") or []
            if requested:
                ids = find_choice_ids_by_substring(choices, requested)
                select(qid, ids, "naics_override")
            else:
                ids = find_choice_ids_by_substring(choices, truth["naics_self_qualified"]["registered_naics"])
                if ids:
                    select(qid, ids[:1], "naics_first_match")
                else:
                    report["qid_not_found"][qid] = "naics"
            continue

        if "would your company submit a quote" in qt_lower:
            ids = find_choice_ids_by_exact_label(choices, ["Yes"])
            if ids:
                value(qid, ids[0])
            continue

        if "provide this service and/or product commercially" in qt_lower:
            answer = truth.get("commercial_item_far_part_12", {}).get("answer", "Yes")
            ids = find_choice_ids_by_exact_label(choices, [answer])
            if ids:
                value(qid, ids[0])
            continue

        if "subcontract" in qt_lower:
            answer = overrides.get("subcontracting_override") or truth["subcontracting_intent_default"]["answer"]
            ids = find_choice_ids_by_substring(choices, [answer])
            if ids:
                value(qid, ids[0])
            continue

        if "lead time" in qt_lower:
            answer = overrides.get("lead_time_override") or truth["lead_time_default"]["answer"]
            ids = find_choice_ids_by_substring(choices, [answer])
            if ids:
                value(qid, ids[0])
            continue

        if qtype == "MC" and ("response time" in qt_lower or "fedramp" in qt_lower or "realistic" in qt_lower):
            override_key = "response_time" if "response time" in qt_lower or "realistic" in qt_lower else "fedramp_status"
            override_value = overrides.get(override_key)
            if override_value:
                ids = find_choice_ids_by_substring(choices, [override_value])
                if ids:
                    value(qid, ids[0])
                else:
                    report["warnings"].append(f"{qid} {override_key} override '{override_value}' did not match any choice")
            else:
                report["warnings"].append(f"{qid} MC narrative question needs override key '{override_key}' in per-opportunity file. Choices: {[strip_html(c.get('Display','') if isinstance(c,dict) else '') for c in choices.values()]}")
            continue

        if "technical question" in qt_lower and "yes/no" in qt_lower:
            cap_answers = overrides.get("capability_questions_answers") or {}
            for cid, c in (choices or {}).items():
                label = strip_html(c.get("Display", "") if isinstance(c, dict) else "")
                m = re.match(r"^(\d+)\.\s", label)
                if not m:
                    continue
                q_num = m.group(1)
                user_answer = cap_answers.get(q_num) or cap_answers.get(f"QID14_{q_num}") or cap_answers.get(f"q{q_num}")
                if not user_answer:
                    report["warnings"].append(f"QID14 sub {q_num}: no per-opportunity answer; defaulting to 'Yes'. Set explicitly in overrides.")
                    user_answer = "Yes"
                user_answer = "Yes" if str(user_answer).strip().lower() in ("yes", "y", "true", "1") else "No"
                selections[f"QR~{qid}~{cid}"] = user_answer
                report["qid_selections"].setdefault(qid, []).append(f"{cid} -> {user_answer}")
            continue

    return {
        "opportunity_id": opportunity_id,
        "identity": identity,
        "qid_selections_for_submitter": selections,
        "report": report,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--opportunity-id", required=True)
    parser.add_argument("--canonical", type=Path, default=Path("scripts/mras_answers.json"))
    parser.add_argument("--qid-definitions", type=Path)
    parser.add_argument("--overrides", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    qid_path = args.qid_definitions or Path(f"working/mras-discovery/{args.opportunity_id}-qid-definitions.json")
    overrides_path = args.overrides or Path(f"working/mras-answers/{args.opportunity_id}.json")
    output_path = args.output or Path(f"working/mras-answers/{args.opportunity_id}-resolved.json")

    canonical = json.loads(args.canonical.read_text())
    qid_defs_block = json.loads(qid_path.read_text())
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}

    resolved = map_answers(
        opportunity_id=args.opportunity_id,
        canonical=canonical,
        qid_defs_block=qid_defs_block,
        overrides=overrides,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(resolved, indent=2))
    print(json.dumps(resolved["report"], indent=2))


if __name__ == "__main__":
    main()
