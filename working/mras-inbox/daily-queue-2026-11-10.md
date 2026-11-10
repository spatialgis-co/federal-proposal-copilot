# MRAS Daily Queue — 2026-11-10

**Run timestamp:** 2026-11-10T00:00:00Z  
**Gmail query:** `from:rfi@research.gsa.gov newer_than:1d`  
**Result:** 6 threads found (3 reminder emails + 3 response-confirmation emails for the same 3 HHS/CDC opportunities)

## Summary

| Metric | Count |
|--------|-------|
| Emails retrieved | 6 |
| Unique opportunities (after dedup) | 0 |
| PASS | 0 |
| MAYBE | 0 |
| DECLINE | 0 |
| Submitted today | 0 |
| Previously submitted (confirmed) | 3 |
| Blocked | 0 |

---

## Previously Submitted — Confirmed by Response Email

All 3 opportunities below were submitted on **2026-11-09** outside the automated pipeline (no prior fill reports existed). Fill reports have been retrospectively created today. The pipeline correctly identified all 3 as already-submitted and excluded them from processing.

### 1. HHS CDC — Technical Assistance for Program Implementation

| Field | Value |
|---|---|
| **Agency** | HHS / Centers for Disease Control and Prevention (CDC) |
| **Slug** | `hhs-cdc-technical-assistance-for-program-implementation` |
| **Survey ID** | SV_2o6pwPXXOkXRrrE |
| **Response ID** | R_GqKgX5YeJRcps8m |
| **Confirmation ID** | SV_2o6pwPXXOkXRrrE-R_GqKgX5YeJRcps8m |
| **Submitted** | 2026-11-09 ~20:25 UTC |
| **Due Date** | 2026-11-10 |
| **Submission Status** | **SUBMITTED-CONFIRMED** |
| **NAICS** | 541611 |
| **SIN** | 541611 |
| **Teaming Partner** | BeVera Solutions (CDC 8(a), CDC Data Science Academy) |
| **Fill Report** | `working/mras-runs/hhs-cdc-technical-assistance-for-program-implementation-fill-report.json` |

**Scope:** CDC seeks sources for public-health technical assistance supporting implementation science, program evaluation, Tribal engagement, capacity building, health education, scientific messaging, and translation of evidence-based nutrition/physical activity/obesity-prevention strategies.

**Response approach (from confirmation email):** SpatialGIS primed 541611 program-management + analytical + evaluation + Tribal-engagement core. BeVera Solutions as teaming sub (~40–50% TO mix) for CDC implementation-science + nutrition/PA/obesity SME. References cited: HHS CMS DPSC (R_GGIjpBUDHSCuqgc), HHS NIH NCI ITRC (R_GM0eRxaqNNhDSno).

---

### 2. HHS CDC — DNAPO Epidemiology and Surveillance Support Services

| Field | Value |
|---|---|
| **Agency** | HHS / Centers for Disease Control and Prevention (CDC) |
| **Slug** | `hhs-cdc-dnapo-epidemiology-and-surveillance-support-services` |
| **Survey ID** | SV_esXRmrCNCmXd3Bs |
| **Response ID** | R_GhDO0iHbN9qfqKS |
| **Confirmation ID** | SV_esXRmrCNCmXd3Bs-R_GhDO0iHbN9qfqKS |
| **Submitted** | 2026-11-09 ~20:26 UTC |
| **Due Date** | 2026-11-10 |
| **Submission Status** | **SUBMITTED-CONFIRMED** |
| **Fill Report** | `working/mras-runs/hhs-cdc-dnapo-epidemiology-and-surveillance-support-services-fill-report.json` |

**Scope:** Division of Nutrition, Physical Activity, and Obesity (DNPAO). CDC seeks sources for scientific and technical consulting support for epidemiology, surveillance, data analysis and modernization, statistical modeling, evidence reviews, program evaluation, and reporting related to nutrition, physical activity, obesity, and chronic disease prevention.

---

### 3. HHS CDC — DNPAO Technical Assistance

| Field | Value |
|---|---|
| **Agency** | HHS / Centers for Disease Control and Prevention (CDC) |
| **Slug** | `hhs-cdc-dnpao-technical-assistance` |
| **Survey ID** | SV_efUsePnDoPlRAGy |
| **Response ID** | R_G3NvgnvvSPsSxe9 |
| **Confirmation ID** | SV_efUsePnDoPlRAGy-R_G3NvgnvvSPsSxe9 |
| **Submitted** | 2026-11-09 ~20:27 UTC |
| **Due Date** | 2026-11-10 |
| **Submission Status** | **SUBMITTED-CONFIRMED** |
| **Fill Report** | `working/mras-runs/hhs-cdc-dnpao-technical-assistance-fill-report.json` |

**Scope:** Division of Nutrition, Physical Activity, and Obesity (DNPAO). CDC seeks sources for scientific and technical assistance, subject-matter expertise, capacity building, training, communications, and program support for nutrition, physical activity, obesity prevention, breastfeeding, healthy weight, and Tribal health initiatives.

---

## Carry-Forward — Needs Human Decision

### DOT — VISTA/SPIN (Vehicle Importation Safety Tracking)

From the **2026-11-08 queue** — still open (due 2026-11-20). Pending human review.

| Field | Value |
|---|---|
| **Slug** | `dot-vista-spin-vehicle-importation-safety-tracking` |
| **Due Date** | 2026-11-20 |
| **Triage** | MAYBE |
| **Issue** | Salesforce SaaS + AWS platform — not GIS-centric. Needs Salesforce teaming partner to respond credibly. |

Kendrick: please review the Nov 8 queue for the action item. Run `python3 scripts/mras_discover.py` if scoping has changed.

---

## Pipeline Notes

- **No daily run occurred on 2026-11-09.** The 3 CDC submissions were made manually or via an out-of-band process. No `daily-queue-2026-11-09.md` or corresponding raw/unique/triage files were produced.
- Retrospective fill reports created today for all 3 CDC items to ensure future dedup works correctly.
- All 3 CDC responses were confirmed by Qualtrics "Response Received" emails; no resubmission needed.

---

*No items were auto-submitted today (all opportunities already confirmed).*
