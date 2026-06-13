# MRAS Daily Queue — 2026-06-13

**Run date:** 2026-06-13  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads (last 24 h):** 11  
**After dedup:** 9 unique (2 removed — matched existing mras-runs stubs)  
**New RFIs processed:** 2  
**Reminders processed:** 4  
**Confirmation emails:** 3 (prior MAYBE/new submissions confirmed)  
**Submitted today (auto):** 0  
**Rejected by Qualtrics:** 0  
**Newly BLOCKED-NEEDS-USER:** 0  
**Declined today:** 9 (2 new RFIs + 4 reminders + 3 confirmations classified skip)  
**Stub fill-reports created:** 3 (for Kendrick's 3 manual submissions confirmed yesterday)  

> **Infrastructure note (persistent):** Outbound network access to `feedback.gsa.gov` is blocked by the cloud execution environment's network policy. `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics survey URLs from this environment. All QID discovery and form submission must be performed from a local machine or an environment with unrestricted outbound access.

---

## CONFIRMED SUBMISSIONS — 3 NEW (Kendrick submitted manually 2026-06-12)

All three surveys confirmed via GSA response receipt emails. Stub fill-reports created.

### 1. DHS USCG — Program Management and Analysis ✅ SUBMITTED-CONFIRMED
| Field | Value |
|---|---|
| Slug | `dhs-uscg-program-management-and-analysis` |
| Survey ID | `SV_3EGTKhYQc0HcFE2` |
| Response ID | `R_GCFkAX9l4HvHXZD` |
| Agency | DHS / U.S. Coast Guard |
| Due Date | 2026-06-18 |
| NAICS | 541611 |
| SINs | 541611, 10101, 60101, 10213, 60213 |
| Prior status | MAYBE (2026-06-12 queue — awaiting Kendrick decision) |
| Status | **SUBMITTED-CONFIRMED** (Kendrick resolved manually 2026-06-12) |
| Fill-report | `working/mras-runs/dhs-uscg-program-management-and-analysis-fill-report.json` |

**Note:** This was the MAYBE flagged in the 06-12 queue with a decision deadline of 2026-06-15. Kendrick submitted the same day the queue was written. The scope (PM, Strategic Planning/Analysis, Business Transformation, Data/IT Architecture, System Engineering, Real Property, Governance, Analytical Services) is confirmed fit for SpatialGIS under MAS SIN 541611.

---

### 2. USAF — DAF Damage Assessment Management Office (DAMO) ✅ SUBMITTED-CONFIRMED
| Field | Value |
|---|---|
| Slug | `usaf-daf-damage-assessment-management-office-damo` |
| Survey ID | `SV_eWAKR8jjEsYg4Xc` |
| Response ID | `R_GPv56z6dsRX4Wx7` |
| Agency | USAF / DAF |
| Due Date | 2026-06-22 |
| NAICS | 541519, 541990 |
| SINs | 54151S |
| Status | **SUBMITTED-CONFIRMED** (Kendrick submitted 2026-06-12) |
| Fill-report | `working/mras-runs/usaf-daf-damage-assessment-management-office-damo-fill-report.json` |

**Scope:** Cyber damage assessments, cyber analytical analysis and program management, DAF DAMO activities evaluation/monitoring/coordination/reporting, triage analysis of cyber intrusion data, TS/SCI clearance. SpatialGIS holds TS FCL; USTRANSCOM EADE and other clearanced engagements cited as anchors.

---

### 3. DOI — Secure AI Assistant for Final Agency Decisions (FAD) ✅ SUBMITTED-CONFIRMED
| Field | Value |
|---|---|
| Slug | `doi-secure-ai-assistant-for-final-agency-decisions-fad` |
| Survey ID | `SV_2t0C2zFWmiTg7hY` |
| Response ID | `R_GDNv5mvHN2ZGcSN` |
| Agency | DOI / OCR / OCIO |
| Due Date | 2026-06-17 |
| NAICS | 518210 |
| SINs | 54151S |
| Status | **SUBMITTED-CONFIRMED** (Kendrick submitted 2026-06-12) |
| Fill-report | `working/mras-runs/doi-secure-ai-assistant-for-final-agency-decisions-fad-fill-report.json` |

**Scope:** Microsoft Power Platform, Azure AI services, government IT delivery, production deployment + O&M of FAD AI Assistant for DOI OCR. SpatialGIS cited active DOI FCHS2 MA-IDIQ subcontract under IBM and USTRANSCOM EADE (Power Platform + Azure at DoD scale) as anchors.

---

## NEW RFIs — DECLINED (2)

### 1. DHS USCG — Boating Safety Public Health Effort
| Field | Value |
|---|---|
| Thread | `19ebd14862e8bbd2` |
| Slug | `dhs-uscg-boating-safety-public-health-effort` |
| Agency | DHS / U.S. Coast Guard |
| Survey ID | `SV_0NEMo6QwKVPmH0q` |
| Due Date | 2026-06-23 |
| Classifier | DECLINE (no keyword match) |
| Manual override | **DECLINE** (content review confirmed) |
| Status | **DECLINED** |

**Requirement:** Transitioning USCG grant-funded public health/boating safety pilot programs to scalable federal contracts. Five detailed technical questions: (1) transitioning public health pilots to sustainable programs; (2) facilitating Data Use Agreements between State Boating Law Administrators and State Departments of Health; (3) integrating non-profit/medical society expertise; (4) epidemiological analysis of NEMSIS, NSSP, ESSENCE, State Hospital Discharge, ED, and Urgent Care databases; (5) translating epidemiological data into injury prevention campaigns.

**Decline rationale:** Public health epidemiology specialist requirement. The core work is syndromic surveillance definition, DUA facilitation between state health agencies, medical society collaboration, and NEMSIS/NSSP/ESSENCE clinical database analysis. SpatialGIS is a GIS professional services firm; while Q5 mentions "geographic hotspots" as one minor example, the requirement is led by public health/clinical expertise SpatialGIS does not hold. Answering Yes to the 5 technical questions would constitute unsupported claims. Hard-decline category: healthcare IT / clinical / public health epidemiology.

---

### 2. DOE — Office of Secure Transportation Logistics
| Field | Value |
|---|---|
| Thread | `19ebcafdb2a99f1f` |
| Slug | `doe-office-of-secure-transportation-logistics` |
| Agency | DOE / NNSA / Office of Secure Transportation (OST) |
| Survey ID | `SV_6y4QJoBQtJOauEe` |
| Due Date | **2026-06-18** — 5 days remaining |
| Classifier | DECLINE (no keyword match) |
| Manual override | **DECLINE** (content review confirmed) |
| Status | **DECLINED** |

**Requirement:** DOE/NNSA/OST Logistics and Property Management Branch requires contract logistics support: Logistics Planning and Support, Personal Property Management, **Munitions Management**, **Armory Operations/Firearms Management**, Motor Vehicle Operations and Fleet Management, Purchasing Support.

**Decline rationale:** Nuclear weapons transportation logistics specialist requirement (NNSA OST transports nuclear weapons and components). Requires munitions management and armory operations/firearms management — outside SpatialGIS capabilities entirely. Hard-decline keyword match: weapons/armory/munitions content. No GIS content.

---

## REMINDERS — DECLINED (4)

### 1. USAF — DAF Damage Assessment Management Office (DAMO) *(reminder for now-confirmed submission)*
| Field | Value |
|---|---|
| Thread | `19ebb4c6096aa879` |
| Slug | `usaf-daf-damage-assessment-management-office-damo` |
| Status | **SKIP — already submitted** (confirmation received 2026-06-12) |

---

### 2. USMC — MCSC — Software License and On-Site Support
| Field | Value |
|---|---|
| Thread | `19ebb4a24b7b7e8b` |
| Slug | `usmc-mcsc-software-license-and-on-site-support` |
| Agency | USMC / Marine Corps Systems Command |
| Classifier | DECLINE (no keyword match) |
| Status | **DECLINED** |

**Decline rationale:** MCSC (Marine Corps Systems Command) software license and on-site maintenance support — commercial software product licensing and maintenance, not GIS professional services. No keyword match; no geospatial content evident from title. First pipeline sighting as reminder — preexisting RFI.

---

### 3. HHS — Program Monitoring and Evaluation Support Services
| Field | Value |
|---|---|
| Thread | `19ebb4a07f6ec6f9` |
| Slug | `hhs-program-monitoring-and-evaluation-support-services` |
| Agency | HHS |
| Classifier | DECLINE (no keyword match) |
| Status | **DECLINED** |

**Decline rationale:** HHS program monitoring and evaluation is public health program management / performance evaluation — social services program assessment domain. No GIS content from title. "Evaluation Support Services" for HHS is a different domain than IT professional services. First pipeline sighting as reminder.

---

### 4. DOI — Secure AI Assistant for Final Agency Decisions (FAD) *(reminder for now-confirmed submission)*
| Field | Value |
|---|---|
| Thread | `19ebb4921e9227d2` |
| Slug | `doi-secure-ai-assistant-for-final-agency-decisions-fad` |
| Status | **SKIP — already submitted** (confirmation received 2026-06-12) |

---

### 5. DOC NIST — Gaithersburg, MD Data Center Co-Location
| Field | Value |
|---|---|
| Thread | `19ebb487e193e56a` |
| Slug | `doc-nist-gaithersburg-md-data-center-co-location` |
| Agency | DOC / NIST |
| Classifier | DECLINE (no keyword match) |
| Status | **DECLINED** |

**Decline rationale:** Data center co-location infrastructure (physical space, power, cooling, network connectivity at NIST Gaithersburg campus). SpatialGIS is not a data center facility provider. No GIS content.

---

### 6. GSA OGP — Phishing Resistant Authenticator *(repeat decline)*
| Field | Value |
|---|---|
| Thread | `19ebb480dfcf2b77` |
| Slug | `gsa-ogp-phishing-resistant-authenticator` |
| Agency | GSA / OGP |
| Classifier | DECLINE |
| Status | **DECLINED** (previously declined 2026-06-12) |

Authentication product vendor market research. Previously declined. No change.

---

## PIPELINE SUMMARY

| Category | Count |
|---|---|
| Total threads pulled (last 24 h) | 11 |
| After dedup | 9 |
| Confirmation emails (prior submissions) | 3 |
| New RFIs | 2 |
| Reminders | 4 |
| PASS | **0** |
| MAYBE | **0** |
| DECLINE | **9** |
| Submitted today (auto) | **0** |
| Rejected by Qualtrics | **0** |
| BLOCKED-NEEDS-USER | **0** |
| New stub fill-reports created | **3** (USCG Program Mgmt, USAF DAMO, DOI FAD) |

---

## RUNNING SUBMISSION TALLY (all confirmed)

| Slug | Submitted | Survey ID | Response ID |
|---|---|---|---|
| dhs-uscg-program-management-and-analysis | 2026-06-12 (manual) | SV_3EGTKhYQc0HcFE2 | R_GCFkAX9l4HvHXZD |
| usaf-daf-damage-assessment-management-office-damo | 2026-06-12 (manual) | SV_eWAKR8jjEsYg4Xc | R_GPv56z6dsRX4Wx7 |
| doi-secure-ai-assistant-for-final-agency-decisions-fad | 2026-06-12 (manual) | SV_2t0C2zFWmiTg7hY | R_GDNv5mvHN2ZGcSN |
| hhs-cdc-technical-support-for-vehss | pre-pipeline (manual) | — | — |
| army-real-property-remediation-support-services | pre-pipeline (manual) | — | — |
| usmc-infads-professional-services-contract | pre-pipeline (manual) | — | — |
| navy-itgms | pre-pipeline (manual) | — | — |
| doj-fbi-dssu-program-support | pre-pipeline (manual) | — | — |
| usaf-fire-emergency-information-management | pre-pipeline (manual) | — | — |
| usaf-usafa-donor-funds-management-it-ecosystem | pre-pipeline (manual) | — | — |
| usace-mpbi-data-analytics-support | pre-pipeline (manual) | — | — |

**Total confirmed submissions tracked:** 11

---

## ACTION ITEMS FOR KENDRICK

**None today.** All opportunities reviewed; no new BLOCKED or MAYBE items. The 3 submissions Kendrick made manually yesterday (DHS USCG Program Mgmt, USAF DAMO, DOI FAD) are confirmed and stubs created. Pipeline is current.

> **Environment (persistent):** Configure outbound access to `*.gsa.gov` in the cloud environment's network policy (see [remote execution environment docs](https://code.claude.com/docs/en/claude-code-on-the-web)) or run the MRAS pipeline locally to enable automated QID discovery and submission.
