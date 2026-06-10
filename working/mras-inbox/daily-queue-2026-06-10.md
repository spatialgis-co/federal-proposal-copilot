# MRAS Daily Queue — 2026-06-10

**Run date:** 2026-06-10  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads (last 24 h):** 11  
**After dedup:** 11 unique (0 removed)  
**New RFIs processed:** 4  
**Submitted today (auto):** 0  
**Rejected by Qualtrics:** 0  
**Newly blocked (needs user):** 0 new (1 carried forward — DOI FAD)  
**Declined today:** 4 new RFIs + 5 reminders assessed  
**Confirmation emails noted:** 1 (USAF USAFA Donor Funds — Kendrick submitted)

> **Infrastructure note (persistent):** Outbound network access to `feedback.gsa.gov` is blocked by the cloud execution environment's network policy. `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics survey URLs from this environment. All QID discovery and form submission must be performed from a local machine or an environment with unrestricted outbound access.

---

## NEW RFIs — DECLINED (4)

### 1. DOC NIST — Gaithersburg, MD Data Center Co-Location
| Field | Value |
|---|---|
| Thread | `19eaece38ea6e29d` |
| Slug | `doc-nist-gaithersburg-md-data-center-co-location` |
| Agency | DOC / NIST — Computer Facility Services Team (CFST) |
| Survey ID | `SV_e2QwibOi1b6S1NQ` |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_e2QwibOi1b6S1NQ?Q_DL=5hVdlUrzZ3TuL1C_e2QwibOi1b6S1NQ_CGC_Wh5b6AH1kn3cBBu&Q_CHL=email` |
| Due Date | **2026-06-22** |
| Triage | DECLINE |
| Status | **DECLINED** |

**Requirement:** Physical data center co-location facility within 50 miles of NIST Gaithersburg, MD campus. Must support HPC resources — up to 3 racks, minimum 250kW power capacity. Liquid cooling capabilities may be required depending on equipment selected.

**Decline rationale:** This is a physical data center facilities procurement — rack space, power, cooling. SpatialGIS is an IT professional services firm; it does not own or operate data center real estate. Responding would require claiming a physical facilities capability SpatialGIS does not hold. No GIS or IT professional services relevance.

---

### 2. HHS — Program Monitoring and Evaluation Support Services
| Field | Value |
|---|---|
| Thread | `19eaeb976bc905a8` |
| Slug | `hhs-program-monitoring-and-evaluation-support-services` |
| Agency | HHS |
| Survey ID | `SV_eyZj4YsOezaZcDI` |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_eyZj4YsOezaZcDI?Q_DL=x4qEF0iQePv0Mo5_eyZj4YsOezaZcDI_CGC_bVQBzybDH0uGH7J&Q_CHL=email` |
| Due Date | **2026-06-17** |
| Triage | DECLINE (classifier) |
| Status | **DECLINED** |

**Requirement:** Assess progress, effectiveness, efficiency, and impact of resources supporting public health capacity for outbreak prevention, detection, and response systems. Program monitoring and evaluation support for HHS.

**Decline rationale:** Program monitoring and evaluation for public health infrastructure. No explicit geospatial content in the email body. SpatialGIS's documented capabilities do not include public health program M&E, epidemiology, or public health outcome evaluation. Responding without a clear GIS/spatial hook would require claiming program evaluation expertise SpatialGIS cannot substantiate.

> **Note for Kendrick:** If SpatialGIS has prior work in health-related geospatial analytics (e.g., disease mapping, spatial epidemiology, public health GIS), this could be a MAYBE. The email is terse and QIDs are unknown. If relevant past performance exists, manually review the survey before 2026-06-14 (3 days before close).

---

### 3. USAF — iPad Air MIL-STD-(810/461) Testing
| Field | Value |
|---|---|
| Thread | `19eae3098d42aa68` |
| Slug | `usaf-ipad-air-mil-std-810-461-testing` |
| Agency | U.S. Air Force / HQ AFRC HERO |
| Survey ID | `SV_7R6qslmoMcol2Gq` |
| Due Date | **2026-06-26** |
| Triage | DECLINE |
| Status | **DECLINED** |

**Requirement:** Military standard environmental and EMI/EMC testing of candidate iOS devices (iPad Air) for AFRC HERO program. Tests required: MIL-STD-810H (explosive atmosphere, decompression, thermal shock/limits) and MIL-STD-461H (emissions RE102/CE102, susceptibility RS103/CS101/CS114-116).

**Decline rationale:** Specialized defense hardware environmental and electromagnetic compatibility testing. Requires accredited MIL-STD test laboratory equipment and certifications. SpatialGIS does not operate a hardware test facility. No GIS or IT professional services relevance.

---

### 4. USMC MCSC — Software License and On-Site Support
| Field | Value |
|---|---|
| Thread | `19ead31d4ec7b56c` |
| Slug | `usmc-mcsc-software-license-and-on-site-support` |
| Agency | U.S. Marine Corps / MCSC |
| Survey ID | `SV_eUT6B0IiK6f2bbM` |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_eUT6B0IiK6f2bbM?Q_DL=p7skM9zHieGLCyx_eUT6B0IiK6f2bbM_CGC_FLCkzAcfJdZFGO7&Q_CHL=email` |
| Due Date | **2026-06-19** |
| Triage | DECLINE (classifier) |
| Status | **DECLINED** |

**Requirement:** Procurement of 3 separate software licenses including maintenance, training and support. No further detail provided in the email body.

**Decline rationale:** Software resale/procurement is outside SpatialGIS's scope under SIN 54151S (IT professional services). The email provides zero detail on which 3 software licenses — the requirement could be for anything from network appliances to financial software to ERP platforms. Responding with capability claims when the software is unidentified would be unfounded.

> **Note for Kendrick:** If you have visibility into what USMC MCSC is procuring (e.g., ArcGIS/ESRI licenses or geospatial platform licenses), and if it's software SpatialGIS can deliver, this may be worth a manual survey review before 2026-06-16 (3 days before close). SIN 54151S covers IT products and services under the GSA MAS.

---

## CONFIRMATION EMAIL NOTED

### USAF — USAFA Donor Funds Management IT Ecosystem ✅ SUBMITTED-CONFIRMED (by Kendrick)
| Field | Value |
|---|---|
| Thread | `19eadcfccc45828c` |
| Slug | `usaf-usafa-donor-funds-management-it-ecosystem` |
| Confirmation ID | `SV_cSUU0XStCTYfVGK-R_GIEhXWladDwzFYq` |
| Confirmed | 2026-06-09T19:15:35Z |
| Prior pipeline status | DECLINED (2026-06-09) — M365/Power Platform, donor fund management, not geospatial |
| Current status | **SUBMITTED-CONFIRMED** — Kendrick submitted manually |

This is the third pipeline-DECLINED item Kendrick has submitted manually (prior: DOJ FBI DSSU, USAF Fire & Emergency). The pipeline assessed this as non-fit (M365 donor fund management ecosystem), but the submission has been recorded. Consider whether the MCSC and HHS M&E items above warrant a similar manual review.

---

## REMINDERS PROCESSED

### Reminder: DHS CBP — Oracle Cloud Infrastructure
| Field | Value |
|---|---|
| Thread | `19eabd8e31778df0` |
| Agency | DHS / CBP |
| Triage | DECLINE |
| Status | **DECLINED** — first pipeline sighting as reminder |

**Decline rationale:** Oracle Cloud Infrastructure procurement — hardware/software platform maintenance or licensing. "Oracle maintenance" and "Oracle license renewal" are hard-decline keywords. SpatialGIS does not manage or resell Oracle infrastructure. Never appeared in pipeline before as a new RFI (pre-dates pipeline or arrived outside the 24h window).

---

### Reminder: DOI — Secure AI Assistant for Final Agency Decisions (FAD) ⚠️ 7 days remaining
| Field | Value |
|---|---|
| Thread | `19eabd6e2bf67008` |
| Agency | U.S. Department of the Interior, OCR / OCIO |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_2t0C2zFWmiTg7hY?Q_DL=MkZ3apJANgEkXIB_2t0C2zFWmiTg7hY_CGC_BqtLtq5qwXs2RLm&Q_CHL=email` |
| Due Date | **2026-06-17** — **7 days remaining** |
| First logged | 2026-06-09 as BLOCKED-NEEDS-USER |
| Status | **BLOCKED-NEEDS-USER — carried forward** |

Action still needed before 2026-06-12 (decision deadline). See 2026-06-09 queue for full block rationale (M365/Power Platform guardrail + no geospatial content). Key question: does SpatialGIS have a named Power Platform teaming partner?

---

### Reminder: HHS NLM — Integrated Research Library
| Field | Value |
|---|---|
| Thread | `19eabd6367ad6505` |
| Agency | HHS / National Library of Medicine |
| Status | **DECLINED** — first pipeline sighting as reminder |

**Decline rationale:** NLM Integrated Research Library — likely a library information management or digital repository system. SpatialGIS's IT professional services capability does not include library management systems. Not geospatial.

---

### Reminder: USAF — 56 RMO Weapons Integration SME
| Field | Value |
|---|---|
| Thread | `19eabd6345231ea3` |
| Agency | U.S. Air Force / 56th Range Management Office |
| Status | **DECLINED** — hard-decline keyword: `weapons integration` |

**Decline rationale:** Hard-decline keyword triggered: "weapons integration." SpatialGIS does not provide weapons systems integration subject matter expertise. First pipeline sighting as reminder.

---

### Reminder: DOC NIST — Federal Credit, Portfolio, and Financial Mgmt. *(PAST DUE)*
| Field | Value |
|---|---|
| Thread | `19eabd5f30ea8bb9` |
| Agency | DOC / NIST CHIPS Program Office |
| Due Date | **2026-06-10** — **PAST DUE as of today** |
| Status | **SKIP-CLOSED** — already DECLINED 2026-06-06 |

Survey closed. No action.

---

### Reminder: USACE — RCM Training and Pilot Study
| Field | Value |
|---|---|
| Thread | `19eabd4b7ace65f2` |
| Agency | U.S. Army Corps of Engineers |
| Status | **DECLINED** — first pipeline sighting as reminder |

**Decline rationale:** RCM = Reliability Centered Maintenance. Training and pilot study for asset/equipment maintenance methodology. Not geospatial; not an IT professional services engagement within SpatialGIS's scope. First pipeline sighting as reminder.

---

## PIPELINE SUMMARY

| Category | Count |
|---|---|
| Total threads pulled | 11 |
| After dedup | 11 |
| New RFIs | 4 |
| New RFIs — PASS | **0** |
| New RFIs — MAYBE | **0** |
| New RFIs — DECLINE | 4 |
| Submitted today (auto) | **0** |
| Rejected by Qualtrics | **0** |
| Newly BLOCKED-NEEDS-USER | **0** |
| Carried forward BLOCKED | 1 (DOI FAD, due 2026-06-17) |
| Confirmation emails | 1 (USAF USAFA Donor Funds — confirmed by Kendrick) |
| Reminders assessed | 6 |

---

## ACTION ITEMS FOR KENDRICK

1. **DECISION NEEDED — by 2026-06-12 (2 days):** DOI FAD AI Assistant (due 2026-06-17). Does SpatialGIS have a named Microsoft Power Platform teaming partner? If yes, open survey URL in browser and run pipeline locally. If no, decline. Survey URL in the 2026-06-09 queue.

2. **Optional — HHS Program M&E (due 2026-06-17):** If SpatialGIS has health-related geospatial analytics experience (disease mapping, spatial epidemiology, public health GIS), manually review the survey before 2026-06-14. Survey URL: `https://feedback.gsa.gov/jfe/form/SV_eyZj4YsOezaZcDI?Q_DL=x4qEF0iQePv0Mo5_eyZj4YsOezaZcDI_CGC_bVQBzybDH0uGH7J&Q_CHL=email`

3. **Optional — USMC MCSC Software License (due 2026-06-19):** If you know which 3 software licenses MCSC is buying and they include geospatial software (ArcGIS, etc.), manually review before 2026-06-16. Survey URL: `https://feedback.gsa.gov/jfe/form/SV_eUT6B0IiK6f2bbM?Q_DL=p7skM9zHieGLCyx_eUT6B0IiK6f2bbM_CGC_FLCkzAcfJdZFGO7&Q_CHL=email`

4. **USAF USAFA Donor Funds (confirmed submitted):** Add a stub fill-report to `working/mras-runs/usaf-usafa-donor-funds-management-it-ecosystem-fill-report.json` with `submitted: true` so the dedup system won't flag reminders as candidates. (Same for DOJ FBI DSSU and USAF Fire & Emergency if not already done.)

5. **Environment (persistent):** Configure outbound access to `*.gsa.gov` in the cloud environment network policy or run MRAS pipeline locally to enable automated QID discovery and submission.
