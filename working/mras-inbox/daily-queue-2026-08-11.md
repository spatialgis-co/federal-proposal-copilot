# MRAS Daily Queue — 2026-08-11

**Run summary:** 6 emails from rfi@research.gsa.gov (2 new + 4 reminders) | 6 unique after dedup | PASS=0 MAYBE=0 DECLINE=6 (automated) | Submitted=0 Rejected=0 Blocked=1 (proxy)

> **Proxy block still in effect.** `feedback.gsa.gov:443` unreachable from automated environment since 2026-07-23. No automated submissions possible. All PASS items require manual browser submission by Kendrick.

---

## ⚠ BLOCKED-NEEDS-USER — Manual Submission Required

### DHS USCG — Boating Activity Imagery Study

| Field | Value |
|-------|-------|
| **Thread ID** | 19feb1e44cbf1767 (reminder; original 19fd88cfde4128c8) |
| **Date first seen** | 2026-08-07 |
| **Survey URL** | https://feedback.gsa.gov/jfe/form/SV_8vKnsxWjRO4UGkC |
| **Survey ID** | SV_8vKnsxWjRO4UGkC |
| **Responses Due** | **2026-08-19** (8 days) |
| **Slug** | `dhs-uscg-boating-activity-imagery-study` |
| **Agency** | DHS / U.S. Coast Guard |
| **Status** | **PASS — awaiting manual browser submission** |

**Requirement (from email body):**
> "The primary objective of this work is to conduct research in imagery analysis specifically for boating activity on a chosen waterbody and make publicly available resources for state boating agencies and researchers to conduct similar research."

**Fit assessment:**

| Factor | Assessment |
|--------|------------|
| Scope | Imagery analysis of waterbodies — satellite/aerial remote sensing for maritime activity monitoring |
| GIS fit | Direct match: "imagery analysis", "waterbody" = geospatial/remote sensing core capability |
| NAICS | 541370 (Surveying and Mapping) or 541512 (Computer Systems Design) — both held |
| SIN | 54151S covers IT/GIS professional services including data analytics and remote sensing |
| Contract vehicle | GSA MAS 47QTCA24D00DS |
| Certifications needed | None flagged (CMMC, FedRAMP, or POLARIS not indicated by description) |
| Socioeconomic | SDB (d-cert) |

**Why BLOCKED:** Automated survey discovery (`mras_discover.py`) cannot reach `feedback.gsa.gov` due to environment proxy block in place since 07/23. Script-based submission unavailable.

**Action required:**
1. Open https://feedback.gsa.gov/jfe/form/SV_8vKnsxWjRO4UGkC in browser
2. Review QID structure — confirm NAICS options, SIN options, capability questions
3. Select NAICS 541370, SIN 54151S, contract vehicle 47QTCA24D00DS
4. Draft capability statement emphasizing: satellite/aerial imagery analysis, waterbody monitoring, remote sensing, spatial data publication, GIS analyst support
5. Submit before 2026-08-19

---

## DECLINE — New Opportunities

### 1. EPA — Digital Pesticide Labeling Platform Pilot

| Field | Value |
|-------|-------|
| **Thread ID** | 19feda1456ea3540 |
| **Date** | 2026-08-10T21:43:10Z |
| **Survey URL** | SV_29Q8Y4BIwQVvCRw |
| **Due Date** | 2026-08-17 |
| **Slug** | `epa-digital-pesticide-labeling-platform-pilot` |
| **Triage** | DECLINE |

**Requirement:** "The contractor shall provide a pilot of their digital pesticide labeling platform that can be used to develop, submit, review, and approve pesticide labeling at both the federal and state labels more efficiently."

**Decline rationale:** Regulatory pesticide label management software. Specialized domain (EPA/FIFRA labeling workflow), no geospatial or GIS component. SpatialGIS has no capability in pesticide regulatory systems.

---

### 2. DOJ USMS — Executive, Administrative and Professional Support

| Field | Value |
|-------|-------|
| **Thread ID** | 19fecc055a6fdf8f |
| **Date** | 2026-08-10T17:37:32Z |
| **Survey URL** | SV_3eDjX6gv8DZFJMG |
| **Due Date** | 2026-08-18 |
| **Slug** | `doj-usms-executive-administrative-and-professional-support` |
| **Triage** | DECLINE |

**Requirement:** "Provide Executive, Administrative and Professional Support Services across more than thirty (30) professional disciplines in support of the law enforcement activities of the USMS."

**Decline rationale:** Broad staffing/professional services BPA across 30+ disciplines for law enforcement support. No GIS, no IT-specific component. Outside SpatialGIS's NAICS portfolio and capabilities.

---

## DECLINE — Reminder Emails (Previously Triaged)

| # | Slug | Agency | Due | Prior Queue | Rationale |
|---|------|--------|-----|-------------|-----------|
| 1 | `dhs-av-system-upgrade-potomac-hall-harpers-ferry-wv` | DHS FLETC | 2026-08-18 | 08-08: DECLINE | AV hardware installation — classrooms. No GIS/IT. |
| 2 | `army-human-performance-and-student-management-system` | Army | Unknown | 08-07: DECLINE | Student/HR management system. No GIS fit. |
| 3 | `treas-irs-complex-structure-graph-analytics-platform-enhance` | IRS | Unknown | 08-05: DECLINE | Tax/financial graph analytics. Not geospatial. |
| 4 | `dhs-uscg-boating-activity-imagery-study` | DHS USCG | 2026-08-19 | 08-07: Human review → **PASS** | See BLOCKED section above — needs manual submit. |

---

## Open MAYBEs — Still Available for Human Review

| Slug | Agency | Due | Note |
|------|--------|-----|------|
| `hhs-acf-child-welfare-technology-solutions-and-services` | HHS/ACF | 2026-08-13 | **CLOSING IN 2 DAYS** — child welfare technology, no direct GIS fit |
| `doe-operation-program-support-services-opss` | DOE/NNSA | 2026-08-18 | Broad admin BPA — no GIS fit identified |
| `omb-eop-verification-validation-process-improvement` | OMB/OFPP | 2026-08-19 | SAM.gov data V&V — false-positive on "reporting" keyword |
| `doj-eousa-victim-notification-system-operations-and-maintenance` | DOJ EOUSA | 2026-08-24 | IT O&M — no clear GIS angle |

---

## Summary

| Bucket | Count | Next Action |
|--------|-------|-------------|
| PASS (auto) | 0 | — |
| PASS (manual-submit needed) | 1 | **Kendrick: open SV_8vKnsxWjRO4UGkC before 08/19** |
| MAYBE | 0 | — |
| DECLINE (new) | 2 | No action |
| DECLINE (reminders, confirmed) | 3 | No action |
| **Submitted** | **0** | — |
| **Blocked (proxy)** | **1** | Manual browser required |

**Proxy block status:** In effect since 2026-07-23. `feedback.gsa.gov:443` unreachable from automated environment. Total automated submissions to date: 29. Manual submissions by Kendrick: ~2 (USAF AAS + USDA APHIS, confirmed 08/05-06).
