# MRAS Daily Queue — 2026-06-06

**Run date:** 2026-06-06  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads:** 7  
**New/reminder RFIs with survey URLs:** 5  
**POC confirmation emails (prior submissions):** 2  
**Submitted today:** 0  
**Rejected by Qualtrics:** 0  
**Blocked (needs user):** 1  
**Declined:** 4  

> **Environment note:** Outbound network access to `feedback.gsa.gov` is blocked by
> the cloud execution environment's network policy. `mras_discover.py` returned HTTP 403
> for all survey URLs. QID definitions, required NAICS/SINs, and attached RFI documents
> could not be fetched automatically. All five active opportunities are therefore flagged
> for manual browser-based follow-up by Kendrick.

---

## SUBMITTED-PRIOR (pre-pipeline confirmations)

### HHS — Enterprise Operations and Efficiency BPA
| Field | Value |
|---|---|
| Thread | `19e9a2410a714c10` |
| Date | 2026-06-05 23:35 UTC |
| Type | POC Confirmation (post-submission) |
| Agency POC | heather.greul@cms.hhs.gov |
| GSA POC | melissa.ramos@gsa.gov |
| Status | **SUBMITTED-PRIOR** — GSA sent POC info email confirming prior response; predates pipeline. No fill-report on file. |

### DOS — TrustAI in Southeast Asia
| Field | Value |
|---|---|
| Thread | `19e9a108d69d73aa` |
| Date | 2026-06-05 23:13 UTC |
| Type | POC Confirmation (post-submission) |
| Agency POC | HessBR@state.gov |
| GSA POC | mark.king@gsa.gov |
| Status | **SUBMITTED-PRIOR** — GSA sent POC info email confirming prior response; predates pipeline. No fill-report on file. |

---

## BLOCKED-NEEDS-USER

### DOJ FBI — Data Sharing Services Unit Program Support ⚠️
| Field | Value |
|---|---|
| Thread | `19e98be6121d7a05` |
| Slug | `doj-fbi-dssu-program-support` |
| Agency | DOJ / FBI CJIS Division |
| Survey ID | `SV_1EQyWZDkPl92FdY` |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_1EQyWZDkPl92FdY?Q_DL=n6WiNY1VbBzf601_1EQyWZDkPl92FdY_CGC_LNxOS2OB5k2VesP&Q_CHL=email` |
| Due Date | **2026-06-15** (9 days) |
| Triage Score | PASS (automated) — false positive likely |
| Status | **BLOCKED-NEEDS-USER** |
| Capability statement | Not drafted |
| Override file | Not created |

**Requirement description:** Support services in data science and analytics, business consulting, strategic planning, content management, operational engagement, systems integration and engineering, and operational support for FBI CJIS DSSU.

**Block reasons:**
1. **Network access blocked.** `mras_discover.py` returned HTTP 403 for `feedback.gsa.gov` — QID definitions, required NAICS (QID10), required SINs (QID8), and capability questions could not be fetched. Cannot draft correct answers or run `mras_submitter` without QID data.
2. **FBI CJIS clearance concern.** The FBI CJIS Security Policy requires background screening for all personnel with access to CJIS systems. SpatialGIS does not have a documented facility clearance or CJIS Security clearance on file in `my-company/`. Kendrick must confirm SpatialGIS can meet CJIS Access requirements before responding.
3. **Capability alignment uncertain.** The requirement spans data science, business consulting, content management, operational engagement — broad professional services. SpatialGIS's core capability is GIS/geospatial; these are adjacent-MAYBE capabilities at best. Without seeing the actual capability sub-questions (QID data), it is not possible to give substantively true Y/N answers.
4. **Triage false positive.** Automated PASS was triggered by "NGA" keyword — NGA does not appear in the email body. The match may be a substring artifact. Manual review of the survey is warranted.

**Recommended action:** Open the personalized survey link above in a browser before 2026-06-15, review the actual QID questions (especially QID10 NAICS and QID8 SINs), confirm CJIS clearance eligibility, and decide go/no-go. If proceeding: capture QIDs to `working/mras-surveys/doj-fbi-dssu-program-support/qid-definitions.json`, draft `working/mras-answers/doj-fbi-dssu-program-support.json`, and re-run the pipeline manually.

---

## DECLINED

### USAF — Fire & Emergency Information Management
| Field | Value |
|---|---|
| Thread | `19e9855af8ea0589` |
| Slug | `usaf-fire-emergency-information-management` |
| Agency | U.S. Air Force |
| Survey ID | `SV_3VjVTuII7tg6BcW` |
| Due Date | 2026-06-26 |
| Triage | DECLINE — no capability keyword match |
| Status | **DECLINED** |

**Decline rationale:** Customer seeks a **COTS product** (not services) for Fire and Emergency Services Information Management across the Air Force. SpatialGIS does not produce or resell a COTS emergency management product. While geospatial data can support emergency response, this RFI is a product evaluation, not a GIS services procurement. Responding would require claiming a COTS product SpatialGIS does not hold.

---

### DOC NIST — Federal Credit, Portfolio, and Financial Mgmt.
| Field | Value |
|---|---|
| Thread | `19e973d6ceddbd19` |
| Slug | `doc-nist-chips-federal-credit-portfolio-financial-mgmt` |
| Agency | DOC / NIST CHIPS Program Office |
| Survey ID | `SV_1Tdwj33LltKriC2` |
| Due Date | 2026-06-10 |
| Triage | DECLINE — hard-decline keyword: "financial management" |
| Status | **DECLINED** |

**Decline rationale:** CHIPS Program Office requires programmatic support for Federal credit, portfolio management, and financial management services. "Financial management" is a hard-decline keyword (guardrails: `never_claim_financial_management`). SpatialGIS has no substantive financial management or Federal credit portfolio capability.

---

### DHS CBP — Mobile Device Management Solution
| Field | Value |
|---|---|
| Thread | `19e973bea8b61c52` |
| Slug | `dhs-cbp-mobile-device-management` |
| Agency | DHS / CBP |
| Survey ID | `SV_5v7L6NMOeQZV7am` |
| Due Date | 2026-06-18 |
| Triage | DECLINE — hard-decline keyword match |
| Status | **DECLINED** |

**Decline rationale:** CBP seeks an MDM system solution with advanced technical support and migration services. SpatialGIS does not provide MDM products or MDM lifecycle management. This is a product/enterprise mobility management procurement, not a GIS or IT professional services engagement SpatialGIS can substantively support.

---

### Army — Project Management: Symphony Installation
| Field | Value |
|---|---|
| Thread | `19e973a7738dbc30` |
| Slug | `army-symphony-installation-project-management` |
| Agency | U.S. Army (library) |
| Survey ID | `SV_eWd3gcvfgDpYikS` |
| Due Date | 2026-06-10 |
| Triage | DECLINE — no capability keyword match |
| Status | **DECLINED** |

**Decline rationale:** The requirement is remote advisory consulting for installation of the **Symphony ILS** (Integrated Library System) and database migration to a STIG-hardened server. SpatialGIS has no Symphony ILS product expertise or library system implementation capability. This is a niche software product support engagement unrelated to GIS or SpatialGIS's IT portfolio.

---

## Action Items for Kendrick

1. **URGENT (due 2026-06-15):** Open the DOJ FBI DSSU survey link in your browser, review the QID questions, and decide whether SpatialGIS should respond. Key questions to answer:
   - What NAICS does the survey require (QID10)?
   - Does SpatialGIS hold those NAICS in SAM? (541370/541511/541512/541519 ✓)
   - What SIN does the survey require (QID8)? (54151S is the only one we hold)
   - Does this require CJIS background screening clearance? Can SpatialGIS personnel pass?
   - Is the capability scope (data science, analytics, content mgmt, systems integration) a substantive SpatialGIS fit?

2. **Pipeline note:** The cloud execution environment blocks outbound access to `feedback.gsa.gov`. To automate survey discovery in future runs, either: (a) configure outbound allowlist for `*.gsa.gov` in the environment's network policy, or (b) run the pipeline from a local machine or environment with unrestricted outbound access.

3. **Prior submissions not in pipeline:** The HHS Enterprise Operations and DOS TrustAI POC emails confirm two prior responses were submitted before this pipeline was set up. Consider manually logging those submissions in `working/mras-runs/` fill-reports if you want the dedup system to track them.
