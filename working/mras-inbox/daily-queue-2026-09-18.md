# MRAS Daily Queue — 2026-09-18

**Run summary:** 9 emails in last 24h | 2 new invitations + 1 response confirmation + 5 reminders | PASS=0 | MAYBE=0 | DECLINE=8 | Submitted=0 | Blocked=0

---

## New Opportunities

### 1. OSW — DCMA — AI Supply Chain Risk Analytics SaaS

| Field | Value |
|---|---|
| **Agency** | Defense Contract Management Agency (DCMA) via Other Service / Work |
| **Type** | NEW INVITATION |
| **Date** | 2026-09-17T20:30:41Z |
| **Thread ID** | 1a0b110f3575d6be |
| **Triage** | **DECLINE** |
| **Submission Status** | N/A — Declined |

**Requirement summary:** DCMA is seeking a SaaS-based AI supply chain risk analytics platform. Framed as a commercial software/product acquisition, not professional GIS services.

**Decline rationale:** No capability keyword match. This is an AI SaaS product RFI — DCMA wants a commercial software product that performs supply chain risk analytics. SpatialGIS is a professional services company (NAICS 541370/541511/541512) without a licensable SaaS product. Even if the platform has geospatial components, this procurement is product-oriented (SaaS license/subscription), not a services contract where SpatialGIS could compete on MAS 54151S. Hard DECLINE.

---

### 2. USAF — Hurlburt Field Civil Engineer Real Property and Budget Analyst Support

| Field | Value |
|---|---|
| **Agency** | U.S. Air Force, Hurlburt Field |
| **Type** | NEW INVITATION |
| **Date** | 2026-09-17T17:29:09Z |
| **Thread ID** | 1a0b06a77e444656 |
| **Triage** | **DECLINE** |
| **Submission Status** | N/A — Declined |

**Requirement summary:** Administrative and budgetary analyst support for Hurlburt Field Civil Engineer squadron. Covers real property accounting, budget analysis, and CE administrative functions.

**Decline rationale:** No capability keyword match. Civil engineer administrative and budget support is personnel/functional support for USAF base CE operations — not GIS, not IT, not geospatial. No overlap with SpatialGIS's 541370/541511/541512/541519 NAICS portfolio. Hard DECLINE.

---

## Submission Confirmation Received

### DOL ILAB — Monitoring, Evaluation, and Data Services

| Field | Value |
|---|---|
| **Agency** | Department of Labor / Bureau of International Labor Affairs |
| **Survey ID** | `SV_0rer9UeYNDRBrMi` |
| **Confirmation ID** | `R_GmtJWXYM3qmBR8B` |
| **Submitted** | 2026-09-17T17:36:25Z |
| **Thread ID** | 1a0b070ea5e4647d |

**Note:** Honest-disclosure response submitted on prior run. SpatialGIS answered Q10 (technical capability) = No, Q21 (would submit proposal) = No. Correctly cited out-of-lane scope (international-development M&E for ILAB-funded projects) while noting in-lane capability for Scenario 3 (Excel data QC + Power Query + Tableau dashboard). No fill report exists in `mras-runs/` for this submission — prior run may have submitted via dry-run or manually without writing a fill report. **Action for Kendrick:** Verify that `working/mras-runs/dol-ilab-monitoring-evaluation-and-data-services-fill-report.json` does not need to be backfilled for tracking purposes.

---

## Reminder Items (Previously Declined)

These RFIs issued reminders today. All were previously triaged and declined on prior runs; no new action taken.

| # | Subject | Decline Reason |
|---|---|---|
| 1 | HHS NIH — Bioinformatics and Computational Biosciences Support | No capability match — bioinformatics / computational biology specialty |
| 2 | HHS — Rapid Medical Examinations & Medical Qualification | Hard decline — healthcare/clinical |
| 3 | USSF NSIC — COSMOS AAS | No capability match — space systems / astrodynamics |
| 4 | HHS ACF — Real Property Facilities Initiative | Hard decline — facilities/real property |
| 5 | GSA OCAS — 232 ORCF Asset Management Support Services | No capability match — asset management for HUD residential care facilities (also declined 2026-09-17) |

---

## Summary

| Status | Count |
|---|---|
| PASS → submitted | 0 |
| PASS → rejected by Qualtrics | 0 |
| BLOCKED → needs human review | 0 |
| MAYBE → needs human decision | 0 |
| DECLINE (new) | 2 (DCMA AI SaaS, USAF Hurlburt CE budget support) |
| Submission confirmations received | 1 (DOL ILAB — prior submission confirmed) |
| Reminder items (previously declined) | 5 |
| Total threads processed | 9 |

**Note for Kendrick:** No submissions made today. Two new opportunities were declined — DCMA AI Supply Chain SaaS (product RFI, not services) and USAF Hurlburt CE Budget Analyst (administrative support, no GIS fit). One prior DOL ILAB submission was confirmed by GSA. Five reminders for previously-declined RFIs received. Check whether DOL ILAB needs a backfill fill-report in `mras-runs/`.
