# MRAS Daily Queue — 2026-08-07

**Run summary:** 16 threads from last 24 h | PASS=0 | MAYBE=0 | DECLINE=16 | Submitted=0 | Blocked=0

---

## POC Information Emails (5) — Informational Only

These confirm prior SpatialGIS submissions were received by GSA and agency POC contact information is available. No action required.

| Subject | Thread ID | Date |
|---|---|---|
| OSW - DeCA IT Group Contracts Audit | 19fd9ee6e83febe5 | 2026-08-07T01:55Z |
| DOT - Crash Data Acquisition Network (CDAN) DME | 19fd9edd3bc8da8d | 2026-08-07T01:54Z |
| GSA FAS - Evaluation and Post-Award Administration Support | 19fd9ed57c52a220 | 2026-08-07T01:53Z |
| EPA - Partnership Acquisition of Services | 19fd9ecb1a4e554f | 2026-08-07T01:53Z |
| USAF - Chief Data and Artificial Intelligence Office Support Services | 19fd9eb576c8e4f6 | 2026-08-07T01:51Z |

---

## New RFI Invitations (6) — All DECLINE

Triage: keyword-only match on subject line. None contain GIS, geospatial, spatial, mapping, imagery analysis, GEOINT, or broad-IT keywords that meet the PASS or MAYBE threshold.

| # | Slug | Agency/Title | Triage | Rationale |
|---|---|---|---|---|
| 1 | hhs-cdc-automated-labeler-support | HHS CDC — Automated Labeler Support | DECLINE | No GIS/IT keyword match. "Labeler" likely refers to physical label printing or lab labeling equipment, not geospatial or IT services. |
| 2 | army-human-performance-and-student-management-system | Army — Human Performance and Student Management System | DECLINE | No GIS/IT keyword match. Student/HR management system outside SpatialGIS core capability. |
| 3 | dhs-uscg-boating-activity-imagery-study | DHS USCG — Boating Activity Imagery Study | DECLINE | No exact PASS keyword match from subject alone. **⚠ HUMAN REVIEW RECOMMENDED:** "imagery" in subject may indicate maritime/satellite/aerial imagery analysis (GIS capability area). Fetch thread body before final decision. Classified DECLINE by automated triage; upgrade to MAYBE or PASS if body confirms geospatial imagery scope. |
| 4 | hhs-acf-ocse-child-support-systems | HHS ACF — OCSE Child Support Systems | DECLINE | No GIS/IT keyword match. Child support case management system outside SpatialGIS scope. |
| 5 | hhs-omhrc-streamlining-support | HHS — OMHRC Streamlining Support | DECLINE | No GIS/IT keyword match. Office of Minority Health Resource Center support, outside SpatialGIS scope. |
| 6 | doj-eousa-victim-notification-system-operations-and-maintenance | DOJ EOUSA — Victim Notification System O&M | DECLINE | No GIS/IT keyword match. Victim notification platform O&M outside SpatialGIS scope. |

---

## Reminder Emails (5) — All DECLINE

| # | Slug | Subject | Triage | Rationale |
|---|---|---|---|---|
| 1 | hhs-ihs-ibm-aix-maintenance-service-support | HHS IHS — IBM AIX Maintenance Service Support | DECLINE | IBM AIX hardware/OS maintenance; "IBM software maintenance" adjacent to decline keyword. Clearly out of scope. |
| 2 | dhs-uscis-enterprise-contact-center | DHS — USCIS Enterprise Contact Center | DECLINE | Contact center operations, not GIS/geospatial. No prior fill report found — opportunity may have arrived before pipeline; confirming DECLINE. |
| 3 | treas-irs-creation-of-qualified-opportunity-zone | TREAS IRS — Creation of Qualified Opportunity Zone | DECLINE | Tax/financial program management. Not GIS (note: separate from `treas-irs-international-tax-modeling-tool-imit` which was previously submitted). |
| 4 | hhs-medknowledge | HHS — Medknowledge | DECLINE | Healthcare knowledge management system. Healthcare IT area flagged as out-of-scope in guardrails. |
| 5 | army-adn-mcn-fiber-install | Army — ADN-MCN FIBER INSTALL | DECLINE | Physical fiber installation/infrastructure. Not IT professional services or GIS. |

---

## Action Items for Human Review

1. **DHS USCG - Boating Activity Imagery Study** — Fetch thread `19fd88cfde4128c8` body and confirm whether this is geospatial/satellite/aerial imagery analysis (PASS candidate) or CCTV/video surveillance (confirm DECLINE). Survey URL in thread body.

2. **DHS - USCIS Enterprise Contact Center** — No fill report found in `working/mras-runs/`. Confirm this was previously reviewed and declined. If not, evaluate based on body.

---

## Notes

- Proxy block on `feedback.gsa.gov` continues to prevent survey discovery via `mras_discover.py` for any opportunities that would have been PASS. No PASS opportunities received today.
- 5 POC confirmations received (DeCA Audit, CDAN DME, GSA FAS Eval Support, EPA Partnership, USAF CDAO Support) — these confirm prior submissions are in agency hands.
