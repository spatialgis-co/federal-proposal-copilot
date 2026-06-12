# MRAS Daily Queue — 2026-06-12

**Run date:** 2026-06-12  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads (last 24 h):** 9  
**After dedup:** 9 unique (0 removed — no mras-runs/ slug matches)  
**New RFIs processed:** 3  
**Reminders processed:** 2  
**POC confirmation emails:** 4 (prior submissions confirmed; agency POC contacts captured)  
**Submitted today (auto):** 0  
**Rejected by Qualtrics:** 0  
**Newly BLOCKED-NEEDS-USER:** 0  
**Declined today:** 4 (2 new RFIs + 2 reminders)  
**MAYBE (flag for Kendrick):** 1 (DHS USCG — manual upgrade from classifier DECLINE)  
**Housekeeping completed:** 8 stub fill-reports created in `working/mras-runs/` (4 new POC confirmations + 4 prior known manual submissions)

> **Infrastructure note (persistent):** Outbound network access to `feedback.gsa.gov` is blocked by the cloud execution environment's network policy. `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics survey URLs from this environment. All QID discovery and form submission must be performed from a local machine or an environment with unrestricted outbound access.

> **Classifier notes:** The triage script produced 3 raw MAYBE results. Two are false positives overridden to DECLINE: (1) GSA OGP Phishing Resistant Authenticator — keyword "cybersecurity" matched but requirement is authentication product research, not professional services SpatialGIS can supply; (2) DHS CBP MDM — keyword "technical support" matched but requirement is an MDM product (Intune/Workspace ONE class), outside SpatialGIS scope. One classifier DECLINE (DHS USCG) is upgraded to MAYBE on content review — see below.

---

## POC CONFIRMATIONS — 4 PRIOR SUBMISSIONS NOW HAVE AGENCY POC

GSA provided agency POC contact information for 4 RFIs Kendrick submitted prior to pipeline tracking. Stub fill-reports created for all 4 to prevent future dedup false positives.

### 1. HHS CDC — Technical Support for VEHSS
| Field | Value |
|---|---|
| Thread | `19eb9c7da356c898` |
| Agency | HHS / CDC |
| Agency POC | **won5@cdc.gov** |
| GSA POC | char.milan@gsa.gov |
| Stub fill-report | `working/mras-runs/hhs-cdc-technical-support-for-vehss-fill-report.json` |

---

### 2. Army — Real Property Remediation Support Services
| Field | Value |
|---|---|
| Thread | `19eb9c4e46e69f0d` |
| Agency | Army National Guard Bureau |
| Agency POC | **venson.m.wilkins.civ@army.mil** |
| GSA POC | michelle.breitbach@gsa.gov |
| Stub fill-report | `working/mras-runs/army-real-property-remediation-support-services-fill-report.json` |

---

### 3. USMC — iNFADS Professional Services Contract
| Field | Value |
|---|---|
| Thread | `19eb9b80911b931c` |
| Agency | U.S. Marine Corps |
| Agency POC | **christina.e.neto.civ@usmc.mil** |
| GSA POC | john.smithson@gsa.gov |
| Stub fill-report | `working/mras-runs/usmc-infads-professional-services-contract-fill-report.json` |

---

### 4. Navy — Information Technology Governance and Mission Support (ITGMS)
| Field | Value |
|---|---|
| Thread | `19eb9b3362079444` |
| Agency | U.S. Navy |
| Agency POC | **charlie.w.williams3.civ@us.navy.mil** |
| GSA POC | charles.mcconnell@gsa.gov |
| Stub fill-report | `working/mras-runs/navy-information-technology-governance-and-mission-support-itgms-fill-report.json` |

---

## NEW RFIs — MAYBE (1) — FLAG FOR KENDRICK

### DHS USCG — Program Management and Analysis ⚠️ 6 days remaining
| Field | Value |
|---|---|
| Thread | `19eb84992dda6163` |
| Slug | `dhs-uscg-program-management-and-analysis` |
| Agency | DHS / U.S. Coast Guard |
| Survey ID | `SV_3EGTKhYQc0HcFE2` |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_3EGTKhYQc0HcFE2?Q_DL=vOUIMFQgQmgkVIl_3EGTKhYQc0HcFE2_CGC_xhGyF2RtJ43gYFA&Q_CHL=email` |
| Due Date | **2026-06-18** — **6 days remaining** |
| Classifier triage | DECLINE (no keyword match) |
| Manual override | **MAYBE** — content review |
| Status | **MAYBE — awaiting Kendrick decision** |

**Requirement (full email body):** Project Mgmt, Strategic Planning/Analysis, Business Transformation/Process Improvement, Change Mgmt and Strategic Communications, Data and IT Architecture Transformation, System Engineering Lifecycle Process Support, Owners Rep Services, Governance Support, Analytical Services, Real Property, etc.

**Manual assessment:** The email body is unusually terse — 35 words and "etc." suggesting a broad IDIQ-style umbrella MRAS. The scope includes "Analytical Services," "Data and IT Architecture Transformation," and "Real Property" — three areas where SpatialGIS's GIS analytics, geospatial data management, and real property spatial analysis capabilities are directly relevant to USCG missions (port security, maritime domain awareness, facility siting).

The classifier scored DECLINE (no exact keyword match for GIS or broad-IT terms in the terse description). However, content review shows this warrants human evaluation before dismissal. Network block prevents QID discovery to confirm NAICS/SINs and capability sub-questions.

**Required action before 2026-06-15 (3 days — to leave margin before the 06/18 close):**
1. Open the survey URL in a browser.
2. Confirm required NAICS (QID10) — 541370/541511/541512/541519 are the SpatialGIS portfolio.
3. Confirm required SIN (QID8) — 54151S is the only SIN SpatialGIS holds.
4. Review capability sub-questions for GIS/geospatial content.
5. If fit confirmed: run pipeline locally (`mras_discover.py`, then `mras_submitter.py`).
6. If no GIS content: decline, no further action.

---

## NEW RFIs — DECLINED (2)

### 1. GSA OGP — Phishing Resistant Authenticator
| Field | Value |
|---|---|
| Thread | `19eb8bddbbe9f949` |
| Slug | `gsa-ogp-phishing-resistant-authenticator` |
| Agency | GSA / Office of Government-wide Policy (OGP) |
| Survey ID | `SV_5umIjXWvmFzNFD8` |
| Due Date | 2026-06-23 |
| Classifier triage | MAYBE (keyword: cybersecurity) |
| Manual override | **DECLINE** |
| Status | **DECLINED** |

**Requirement:** GSA OGP / Federal Identity and Cybersecurity (FICS) Division is developing product criteria to identify vendor products that are phishing-resistant per OMB Memo 22-09. Market research to identify authentication methods resistant to credential replay, push bombing, SS7 vulnerabilities, and SIM swap attacks — to help agencies replace insufficient methods with phishing-resistant or passwordless alternatives.

**Decline rationale:** This is a product vendor market research — GSA is looking for vendors that sell phishing-resistant authenticator products (FIDO2 keys, PIV-compliant hardware tokens, passkey platforms, biometric authenticators). SpatialGIS is a GIS professional services firm; it does not manufacture or resell authentication hardware/software products. The "cybersecurity" keyword match is a false positive — the requirement is authentication product-specific, not IT security professional services. Responding would require claiming authenticator product capabilities SpatialGIS does not hold.

---

### 2. DHS CBP — Apache ActiveMQ Escalation Support Services
| Field | Value |
|---|---|
| Thread | `19eb7bb269b37b1c` |
| Slug | `dhs-cbp-apache-activemq-escalation-support-services` |
| Agency | DHS / CBP |
| Survey ID | `SV_3NMrzjoJDuH1OrI` |
| Due Date | 2026-06-23 |
| Classifier triage | DECLINE (no keyword match) |
| Status | **DECLINED** |

**Requirement:** Dedicated toll-free number for critical issue escalation pertaining to Apache ActiveMQ, plus online service request management (open/view/update/close). Enterprise Service Desk on 24/7/365 basis.

**Decline rationale:** Apache ActiveMQ is an open-source message broker/middleware platform. This requires a specialist vendor with deep Apache ActiveMQ expertise and an established 24/7/365 service desk infrastructure. SpatialGIS does not provide Apache middleware support. No geospatial content. Responding would require claiming specialized middleware escalation support SpatialGIS does not hold.

---

## REMINDERS — DECLINED (2)

### 1. DHS CBP — Mobile Device Management Solution *(first pipeline sighting)*
| Field | Value |
|---|---|
| Thread | `19eb62188703953a` |
| Slug | `dhs-cbp-mobile-device-management-solution` |
| Agency | DHS / CBP |
| Survey ID | `SV_5v7L6NMOeQZV7am` |
| Due Date | **2026-06-18** — 6 days remaining |
| Classifier triage | MAYBE (keyword: "technical support") |
| Manual override | **DECLINE** |
| Status | **DECLINED** |

**Requirement:** Mobile Device Management system solution to include advanced technical support and migration services from the current environment. CBP has an attached spreadsheet with technical questions.

**Decline rationale:** This is an MDM platform procurement (Microsoft Intune, VMware Workspace ONE, or equivalent). SpatialGIS does not offer MDM solutions or enterprise mobile device management infrastructure. The "technical support" keyword match is a false positive — MDM is a product procurement, not general IT professional services. An attached technical questions spreadsheet exists but cannot be retrieved from this environment (network block). No geospatial content. First sighting as reminder — appears to predate current pipeline.

---

### 2. DHS CBP — Enterprise Support Software and Database Tools *(FY26 IBM renewal)*
| Field | Value |
|---|---|
| Thread | `19eb621449f4842c` |
| Slug | `dhs-fy26-cbp-enterprise-support-software-and-database-tools` |
| Agency | DHS / CBP Office of Information and Technology |
| Survey ID | `SV_4N399D3IknIhw34` |
| Due Date | 2026-06-19 |
| Classifier triage | DECLINE (hard-decline keyword: "IBM p-series") |
| Status | **DECLINED** |

**Requirement:** Software maintenance renewals (licenses, upgrades, OEM support) and hardware maintenance for IBM p-series servers, hardware management consoles, and associated firmware/software. 24x7x365 and M-F 0730-1600 support tiers. Alternative software solutions acceptable if IBM-compatible.

**Decline rationale:** IBM p-series server hardware maintenance and software license renewal program. Hard-decline keyword match: "IBM p-series." SpatialGIS does not maintain or resell IBM enterprise server infrastructure. First pipeline sighting as reminder — appears to predate current pipeline.

---

## HOUSEKEEPING COMPLETED — 8 STUB FILL-REPORTS CREATED

The following `submitted: true` stubs were written to `working/mras-runs/` to prevent future dedup misses. Reminders for these RFIs will now be correctly skipped by the pipeline.

| Slug | Submitted By | Notes |
|---|---|---|
| `hhs-cdc-technical-support-for-vehss` | Manual (Kendrick) | POC confirmed today |
| `army-real-property-remediation-support-services` | Manual (Kendrick) | POC confirmed today |
| `usmc-infads-professional-services-contract` | Manual (Kendrick) | POC confirmed today |
| `navy-information-technology-governance-and-mission-support-itgms` | Manual (Kendrick) | POC confirmed today |
| `doj-fbi-dssu-program-support` | Manual (Kendrick) | Confirmed 2026-06-09; housekeeping from 2026-06-11 queue action item |
| `usaf-fire-emergency-information-management` | Manual (Kendrick) | Confirmed 2026-06-09; slug approximate |
| `usaf-usafa-donor-funds-management-it-ecosystem` | Manual (Kendrick) | Confirmed 2026-06-10; housekeeping from 2026-06-11 queue action item |
| `usace-mpbi-data-analytics-support` | Manual (Kendrick) | POC confirmed 2026-06-09; predates pipeline |

---

## PIPELINE SUMMARY

| Category | Count |
|---|---|
| Total threads pulled (last 24 h) | 9 |
| After dedup | 9 |
| POC confirmation emails | 4 |
| New RFIs | 3 |
| Reminders | 2 |
| PASS | **0** |
| MAYBE (flag for Kendrick) | **1** (DHS USCG — manual upgrade) |
| DECLINE | **8** (4 POC-skip + 2 new RFI + 2 reminder) |
| Submitted today (auto) | **0** |
| Rejected by Qualtrics | **0** |
| Newly BLOCKED-NEEDS-USER | **0** |
| Stub fill-reports created | **8** |

---

## ACTION ITEMS FOR KENDRICK

1. **DECISION NEEDED — by 2026-06-15 (3 days):** DHS USCG Program Management and Analysis (due 2026-06-18). Brief description contains "Analytical Services," "Data and IT Architecture Transformation," and "Real Property" — potential GIS fit. Open the survey URL in a browser to check NAICS, SINs, and capability sub-questions. Survey URL: `https://feedback.gsa.gov/jfe/form/SV_3EGTKhYQc0HcFE2?Q_DL=vOUIMFQgQmgkVIl_3EGTKhYQc0HcFE2_CGC_xhGyF2RtJ43gYFA&Q_CHL=email`

2. **POC follow-up (optional):** Four agency POC email addresses are now on file (above). If any of these opportunities warrant follow-up, contact the POC only if additional information is specifically requested.

3. **Environment (persistent):** Configure outbound access to `*.gsa.gov` in the cloud environment's network policy (see [remote execution environment docs](https://code.claude.com/docs/en/claude-code-on-the-web)) or run the MRAS pipeline locally to enable automated QID discovery and submission.
