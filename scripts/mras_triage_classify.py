"""
Classifies unique MRAS opportunities into PASS / MAYBE / DECLINE based on
SpatialGIS's NAICS coverage + capability profile + standing no-bid patterns.

Input: working/mras-inbox/unique-opportunities.json
Output: working/mras-inbox/triage-classified.json

Classification heuristics applied to subject text. Three buckets:

  PASS    — clearly within SpatialGIS's scope (data analytics, GIS, secure cloud,
            DevSecOps, custom programming, EA, AI/ML, cyber, NGA/Army/Navy/USACE
            mission). Auto-prep for submission.
  MAYBE   — could fit pending DRD review (generic IT, generic consulting, niche
            scope that may map to SpatialGIS capabilities). Surface for manual
            decision.
  DECLINE — product-reseller, niche domain expertise gap (medical/legal/PREA/
            education-program-evaluation), single-staff aug, legacy-tech
            (ColdFusion), foreign deployment, training-delivery (per AFRL no-bid
            STEM pattern), advertising/creative (per AmeriCorps no-bid).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


PASS_KEYWORDS = [
    "data analytics", "data analysis", "data integration", "data scientist",
    "data engineering", "geospatial", "gis", "geoint", "mapping",
    "ai requirement", "ai/ml", "ai-assisted",
    "secure cloud", "cloud migration", "cloud engineering",
    "devsecops", "devops", "cybersecurity", "information assurance", "cyber ",
    "enterprise architecture", "it portfolio", "portfolio governance",
    "custom programming", "custom computer", "software development",
    "mission advocacy",
    "abandoned mine land inventory",
    "jwics", "army vantage", "mpbi",
    "ux designer", "ui/ux",
]

MAYBE_KEYWORDS = [
    "professional support", "professional services",
    "business management", "business mgmt", "biz ops",
    "management support",
    "team facilitator", "consulting",
    "rsa archer", "salesforce", "archer",
    "open architecture",
    "elmr", "ess support",
    "desktop as a service", "daas",
    "marine minerals business data",
    "287(g) data management", "287g data",
    "content evaluation", "content development",
    "budget program support",
    "data integrity", "analysis support",
    "elms", "learning management",  # depends on whether training delivery or platform admin
    "mpacs", "agile software",  # could be Microsoft stack like FMCS
]

DECLINE_KEYWORDS = [
    # Product reseller / hardware-software resale
    "oracle hardware", "fortinet hardware", "fortinet recompete",
    "vmware", "vmware hfdf", "datadog software", "axiom hardware",
    "zpro lease", "maximo application suite", "salesforce licenses",
    "datadog deployment", "vtc equipment upgrade",
    "video telematics", "joint tactical terminals",
    "video engineering and maintenance",
    # Niche domain expertise (medical / legal / research / education evaluation)
    "medical expeditionary", "cancer surveillance", "aids research", "oar professional",
    "adolescent development", "head start", "lyme disease",
    "chafee sota", "peer monitoring", "psob legal", "prea ", "prison rape",
    # Education program evaluation (AFRL no-bid pattern)
    "next national evaluation", "evaluation of next cycle", "evaluation of the dc osp",
    "evaluation of the iada", "next evaluation of",
    # Training delivery
    "virtual training", "joint training requirements", "team facilitator bpa",
    "learning management system saas",
    # Single-person staff aug / niche admin
    "security management assistant", "grants management specialist",
    "usar analyst", "usmtm information technology", "riyadh",
    "digital volunteer management",
    # Trade/Inspection/Auditing services with no GIS hook
    "trade data research", "inspection capability",
    "auditing service", "usabudget",
    # Legacy tech / niche tech stack
    "coldfusion",
    # Comms equipment
    "conference room", "telematics", "vehicle transportation",
    # Call center
    "call tracking", "uac sponsors",
    # EEO HR case management (niche HR SaaS)
    "eeo case management",
    # FMC multi-system / DOT TTP narrow scope without GIS hook
    "multi-system requirements development",
    "technology transfer program",
    # Retirement/Benefits SaaS
    "retirement and benefits software",
    # DOC NIST content evaluation - publishing/curriculum-class scope
    "content evaluation, development",
]


def classify(subject_normalized: str) -> tuple[str, str]:
    s = subject_normalized.lower()
    for kw in DECLINE_KEYWORDS:
        if kw in s:
            return "DECLINE", f"matched DECLINE keyword: '{kw}'"
    for kw in PASS_KEYWORDS:
        if kw in s:
            return "PASS", f"matched PASS keyword: '{kw}'"
    for kw in MAYBE_KEYWORDS:
        if kw in s:
            return "MAYBE", f"matched MAYBE keyword: '{kw}'"
    return "MAYBE", "no keyword match — needs DRD review"


def main(in_path: Path, out_path: Path, submitted_slugs: set[str]) -> None:
    opps = json.loads(in_path.read_text())
    classified = []
    for o in opps:
        if o["slug"] in submitted_slugs:
            o["triage"] = "SUBMITTED"
            o["triage_reason"] = "already submitted in this session"
        else:
            o["triage"], o["triage_reason"] = classify(o["subject_normalized"])
        classified.append(o)
    classified.sort(key=lambda x: (x["triage"], x["latest_date"]), reverse=False)
    out_path.write_text(json.dumps(classified, indent=2))

    by_bucket = {}
    for o in classified:
        by_bucket.setdefault(o["triage"], []).append(o)
    print("Triage results:")
    for bucket in ("SUBMITTED", "PASS", "MAYBE", "DECLINE"):
        items = by_bucket.get(bucket, [])
        print(f"\n=== {bucket} ({len(items)}) ===")
        for o in items:
            print(f"  {o['latest_date'][:10]}  {o['subject_normalized'][:80]}")
            if bucket in ("PASS", "MAYBE"):
                print(f"      reason: {o['triage_reason']}")


if __name__ == "__main__":
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("working/mras-inbox/unique-opportunities.json")
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("working/mras-inbox/triage-classified.json")
    submitted = {
        "gsa-fmcs-application-development-support-services",
        "gsa-ocas-database-and-analytic-api-support",
        "doj-it-portfolio-architecture",
        "osw-whs-data-analytics-support-services",
    }
    main(in_path, out_path, submitted)
