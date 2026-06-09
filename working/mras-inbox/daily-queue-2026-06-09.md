# MRAS Daily Queue — 2026-06-09

**Run date:** 2026-06-09  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads (last 24 h):** 12  
**After dedup:** 10 unique (2 removed: reminder duplicates for already-confirmed submissions)  
**New RFIs processed:** 3  
**Submitted today (auto):** 0  
**Rejected by Qualtrics:** 0  
**Newly blocked (needs user):** 1 (DOI FAD AI Assistant)  
**Declined today:** 6 (3 new RFIs + 2 reminders + 1 closed)  

> **Infrastructure note (persistent):** Outbound network access to `feedback.gsa.gov` is blocked by the cloud execution environment's network policy. `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics survey URLs from this environment. All QID discovery and form submission must be performed from a local machine or an environment with unrestricted outbound access.

> **Confirmed submissions (prior blocked items):** DOJ FBI DSSU and USAF Fire & Emergency Management both show response confirmation emails today — Kendrick manually submitted both. The FBI DSSU carryover is resolved. See section below.

---

## NEWLY BLOCKED — NEEDS USER

### DOI — Secure AI Assistant for Final Agency Decisions (FAD) ⚠️ 8 days remaining
| Field | Value |
|---|---|
| Thread | `19ea903ccbe53575` |
| Slug | `doi-secure-ai-assistant-for-final-agency-decisions-fad` |
| Agency | U.S. Department of the Interior, Office of Civil Rights (OCR) / OCIO |
| Survey ID | `SV_2t0C2zFWmiTg7hY` |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_2t0C2zFWmiTg7hY?Q_DL=MkZ3apJANgEkXIB_2t0C2zFWmiTg7hY_CGC_BqtLtq5qwXs2RLm&Q_CHL=email` |
| Due Date | **2026-06-17** — **8 days remaining** |
| Triage | DECLINE by classifier (snippet-only) → upgraded to BLOCK on full body review |
| Status | **BLOCKED-NEEDS-USER** |
| Capability statement | Not drafted |

**Requirement:** DOI OCR/OCIO seeks a contractor with "demonstrated expertise in Microsoft Power Platform, Azure AI services, and government IT delivery" to support production deployment, ongoing implementation, and long-term O&M of the Secure AI Assistant for Final Agency Decisions (FAD AI Assistant).

**Block reasons:**

1. **M365/Power Platform guardrail triggered.** The requirement explicitly calls for *demonstrated expertise in Microsoft Power Platform*. Per guardrails: "Teaming partner required (M365/Power Platform) but user hasn't named one in `my-company/` or session context." SpatialGIS does not document Power Platform expertise.
2. **No geospatial content.** The FAD AI Assistant serves DOI OCR administrative law decisions. Zero GIS/spatial relevance. SpatialGIS's core differentiators do not apply.
3. **Network blocked.** QID data (required NAICS/SINs, capability sub-questions) cannot be fetched from this environment to complete full guardrail evaluation.

**Required action before 2026-06-12 (to leave margin before the 06/17 close):**
1. Decide: does SpatialGIS have or intend to name a Microsoft Power Platform teaming partner?
2. If yes: open the survey URL above in a browser, confirm QIDs (NAICS, SINs, capability questions), draft `working/mras-answers/doi-secure-ai-assistant-for-final-agency-decisions-fad.json`, and run the pipeline from a local machine.
3. If no: decline and no further action needed.

**Fit assessment:** MAYBE at best. Azure is in SpatialGIS's MAYBE keywords; Power Platform specifically is not documented. Without a named teaming partner with Power Platform credentials, an honest capability response is unlikely to be competitive.

---

## NEWLY DECLINED TODAY

### USAF — DAF Damage Assessment Management Office (DAMO)
| Field | Value |
|---|---|
| Thread | `19ea991faa009921` |
| Slug | `usaf-daf-damage-assessment-management-office-damo` |
| Agency | U.S. Air Force / DAF DAMO |
| Survey ID | `SV_eWAKR8jjEsYg4Xc` |
| Due Date | 2026-06-22 |
| Triage | DECLINE |
| Status | **DECLINED** |

**Requirement:** Cyber damage assessments, cyber analytical analysis and program management, evaluating/monitoring/coordinating/reporting on DAF DAMO activities, triage analysis of cyber intrusion data. **TS/SCI clearance required.**

**Decline rationale:** Core work is cyber security damage assessment — not geospatial. Requires TS/SCI clearance, which SpatialGIS does not document in `my-company/`. No GIS or spatial content. Hard guardrail: undocumented clearance.

---

### USAF — USAFA Donor Funds Management IT Ecosystem
| Field | Value |
|---|---|
| Thread | `19ea98da807b961c` |
| Slug | `usaf-usafa-donor-funds-management-it-ecosystem` |
| Agency | U.S. Air Force Academy (USAFA) |
| Survey ID | `SV_cSUU0XStCTYfVGK` |
| Due Date | 2026-06-22 |
| Triage | DECLINE |
| Status | **DECLINED** |

**Requirement:** Gift Process Automation Tool (GPAT) within the AFNet Microsoft ecosystem — unified gift/donor fund management, workflow automation, financial ledger, AI decision support. Explicitly M365 ecosystem. Donor fund management program has grown 102% since 2020.

**Decline rationale:** M365/Power Platform financial workflow application for donor funds management — not geospatial. Guardrail triggers: requires Power Platform/M365 expertise with no named teaming partner. Financial management is outside SpatialGIS's documented capability.

---

### DHS CISA — IT Research and Support Services
| Field | Value |
|---|---|
| Thread | `19ea6af6238bf67c` |
| Slug | `dhs-cisa-it-research-and-support-services` |
| Agency | DHS / CISA |
| Survey ID | `SV_9vRIeIONIz7sgzY` |
| Due Date | 2026-06-12 |
| Triage | DECLINE |
| Status | **DECLINED** |

**Requirement:** Licensed access for 7 users to an online IT research database (CTO/CIO-level advisory content — Gartner/Forrester/IDC-type subscription). Seven user licenses for executive-level research/advice.

**Decline rationale:** This is a commercial software/database subscription product procurement, not professional services. SpatialGIS does not resell IT research database licenses (Gartner, IDC, Forrester, etc.). Responding would require claiming a product reseller relationship SpatialGIS does not hold.

---

### DHS CBP — Information Technology Refresh Program (ITRP)
| Field | Value |
|---|---|
| Thread | `19ea6ae20a244b88` |
| Slug | `dhs-cbp-information-technology-refresh-program-itrp-sup` |
| Agency | DHS / CBP |
| Survey ID | `SV_2t8nPOH7txaVaRw` |
| Due Date | 2026-06-11 |
| Triage | DECLINE |
| Status | **DECLINED** |

**Requirement:** Comprehensive lifecycle management for CBP enterprise technology assets — program management, hardware procurement assistance, storefront capability, planning/lifecycle management, deployment prep, infrastructure and endpoint management. ~24,700 end-user devices (desktops, laptops, non-cellular tablets) replaced annually.

**Decline rationale:** Large-scale hardware refresh and device lifecycle management program. SpatialGIS does not perform hardware procurement or manage device refresh at enterprise scale. No geospatial or IT professional services relevance. Responding would require claiming hardware/IT asset management capabilities SpatialGIS does not hold.

---

### ED — Update to Projections of Education Statistics *(CLOSED — past due)*
| Field | Value |
|---|---|
| Thread | `19ea6ad429e0264d` |
| Slug | `ed-update-to-projections-of-education-statistics` |
| Agency | Department of Education / IES |
| Survey ID | `SV_bPLfA0c57FFrpTo` |
| Due Date | **2026-06-08** — **PAST DUE** |
| Status | **SKIP-CLOSED** |

**Requirement:** Updated edition of Projections of Education Statistics extending projection horizon 2030→2035 (NCES 2024-034 format). Statistical modeling/publications work.

**Skip rationale:** Due date was 2026-06-08 (yesterday). Survey closed. Also, this is statistical modeling for education projections — outside SpatialGIS's domain entirely.

---

### Army — Project Management: Symphony Installation *(DECLINED 2026-06-06)*
| Field | Value |
|---|---|
| Thread | `19ea6b0a1b0149bc` |
| Agency | U.S. Army (library) |
| Due Date | 2026-06-10 |
| Status | **DECLINED** — first logged 2026-06-06 |

Previously declined. Reminder received today. No change. Niche Symphony ILS (library system) implementation — not geospatial.

---

## PRIOR SUBMISSIONS CONFIRMED TODAY

### DOJ FBI — Data Sharing Services Unit Program Support ✅ SUBMITTED-CONFIRMED
| Field | Value |
|---|---|
| Thread | `19ea7e2b253ddf09` |
| Agency | DOJ / FBI CJIS Division |
| Confirmation ID | `SV_1EQyWZDkPl92FdY-R_GoH1hDXLolaW9bW` |
| Date confirmed | 2026-06-08T15:38 UTC |
| Status | **SUBMITTED-CONFIRMED** — previously BLOCKED-NEEDS-USER (carried forward from 2026-06-06) |

Kendrick manually submitted the DSSU survey despite the pipeline block. Confirmation received. The long-running carryover item is **resolved**. No fill-report on file (submitted outside pipeline); consider adding a manual fill-report to `working/mras-runs/` for dedup tracking.

---

### USAF — Fire & Emergency Information Management ✅ SUBMITTED-CONFIRMED
| Field | Value |
|---|---|
| Thread | `19ea82034dd3c4d1` |
| Agency | U.S. Air Force |
| Confirmation ID | `SV_3VjVTuII7tg6BcW-R_GmJjA9MCctonVHV` |
| Date confirmed | 2026-06-08T16:45 UTC |
| Status | **SUBMITTED-CONFIRMED** — previously DECLINED by pipeline (2026-06-06) |

**Note:** The 2026-06-06 daily queue recommended DECLINE (requirement appeared to be a COTS product evaluation for Fire/EMS Information Management). Kendrick submitted manually regardless. Noting for calibration: if this was a services engagement, the pipeline's COTS-product decline logic may need tuning.

---

## PRIOR SUBMISSION — POC FOLLOW-UP

### USACE — MPBI Data Analytics Support *(POC information received)*
| Field | Value |
|---|---|
| Thread | `19ea80b0cb0e16f5` |
| Agency | U.S. Army Corps of Engineers (USACE) |
| Agency POC | **Giuseppe.G.Mirizzi@usace.army.mil** |
| Status | Prior submission confirmed; POC contact now available |

USACE has provided agency POC contact information for the MPBI Data Analytics Support RFI — a prior submission that predates this pipeline. If SpatialGIS is following up on this requirement, contact Giuseppe Mirizzi at the address above. GSA notes: "please do not provide additional information unless it is specifically requested."

---

## TRIAGE CLASSIFIER NOTE — REMINDER FOR FUTURE RUNS

Automated triage runs on subject line + snippet only. Three of today's new RFIs (DAMO, USAFA Donor Funds, DOI FAD) scored DECLINE on snippets but required full-body review to confirm. The body review confirmed DECLINE/BLOCK for all three — so results were conservative in the right direction. No false positives today.

---

## ACTION ITEMS FOR KENDRICK

1. **DECISION NEEDED — 2026-06-12 (5 days):** Review the DOI FAD AI Assistant opportunity (due 2026-06-17). Key questions:
   - Does SpatialGIS have a named Microsoft Power Platform teaming partner?
   - If yes: open survey URL in browser, review QIDs (NAICS/SINs/capability questions), then run pipeline locally.
   - Survey URL: `https://feedback.gsa.gov/jfe/form/SV_2t0C2zFWmiTg7hY?Q_DL=MkZ3apJANgEkXIB_2t0C2zFWmiTg7hY_CGC_BqtLtq5qwXs2RLm&Q_CHL=email`

2. **USACE MPBI follow-up (optional):** Agency POC is now known — Giuseppe.G.Mirizzi@usace.army.mil. If SpatialGIS wants to develop this relationship, contact only if additional information is specifically requested.

3. **Fill-report gaps:** Two submissions (DOJ FBI DSSU, USAF Fire & Emergency) were made outside the pipeline. Consider creating stub fill-reports in `working/mras-runs/` to prevent them from reappearing as candidates in future runs.

4. **USAF Fire & Emergency calibration note:** Pipeline recommended DECLINE (COTS product evaluation) but Kendrick submitted. If the requirement was actually services-eligible, review the 2026-06-06 decline logic for that opportunity to improve future triage accuracy.

5. **Environment (persistent):** To enable automated survey discovery and submission, configure outbound access to `*.gsa.gov` in the cloud environment's network policy, or run the MRAS pipeline locally.
