# MRAS Daily Queue — 2026-07-19

**Run date:** 2026-07-19  
**Inbox window:** newer_than:3d (catch-up — last run was 2026-07-16; pipeline ran `newer_than:3d` to recover missed days 2026-07-17–19)  
**Totals:** 22 emails received | 8 new RFIs | 9 reminders | 5 POC confirmations  
**Dedup:** 22 → 19 unique (3 removed as already-submitted)  
**Triage result:** 1 PASS | 7 DECLINE | 9 reminders logged | 5 POC info logged  
**Submissions:** 0 submitted (1 BLOCKED — Qualtrics proxy issue) | 0 SUBMITTED-CONFIRMED | 0 REJECTED  

---

## ⚠️ BLOCKED — DOJ OUSA - Professional IT Support Services

**Thread:** 19f70e71e0e51156  
**Date received:** 2026-07-17T16:26:55Z  
**Due:** 07/24/2026 (5 days away — **ACTION REQUIRED**)  
**Slug:** `doj-ousa-professional-it-support-services`  
**Survey:** SV_0JQQzmimQF4B9TU  
**Triage:** PASS — confirmed fit for SpatialGIS  

**Requirement summary:**  
EOUSA Data Integrity and Analysis group seeks contractor support to develop and generate reports and analyses from USAOs' data stored in Microsoft SQL Server 2019, accessible via SQL, PL-SQL, and T-SQL.  

**Fit assessment:**  
- SQL Server 2019 / T-SQL / PL-SQL → direct SpatialGIS capability (NAICS 541511)  
- Data integrity analysis and reporting → direct match  
- GSA MAS 47QTCA24D00DS / SIN 54151S → acquisition vehicle confirmed  
- Small Business + SDB (d-cert) → socioeconomic fit  
- No guardrail violations  

**Why BLOCKED:**  
The Qualtrics survey URL (`feedback.gsa.gov`) returns HTTP 403 via the pipeline's proxy. `mras_discover.py` cannot fetch QID definitions. Without QID structure, `mras_map_answers.py` cannot run and auto-submit is blocked per hard guardrails.  

**What's ready:**  
- Capability statement: `working/mras-capabilities/doj-ousa-professional-it-support-services-capability.md`  
- DOCX: `final/docx/mras/doj-ousa-professional-it-support-services-capability.docx`  
- Answers JSON: `working/mras-answers/doj-ousa-professional-it-support-services.json`  
- Survey link (from email): [Take the survey](https://feedback.gsa.gov/jfe/form/SV_0JQQzmimQF4B9TU)  

**Action needed by Kendrick (by 07/24/2026):**  
Open the survey link above, upload the capability statement DOCX, and complete the form using the answers in `working/mras-answers/doj-ousa-professional-it-support-services.json`. Key selections: NAICS 541511, SIN 54151S, Small Business Yes, SDB Yes.

---

## DECLINE Items — New RFIs

### 1. GSA OCAS - FedHub Managed Service Office (MSO) Operations

**Thread:** 19f72410b96bc1c3 | **Date:** 2026-07-17T22:44 | **Due:** 07/31/2026  
**Slug:** `gsa-ocas-fedhub-managed-service-office-mso-operations`  
**Triage:** DECLINE  

**Decline rationale:** PMO and management board support for FedHub/XMS (GSA's procurement system) at HHS. Requires specialized FedHub/XMS implementation knowledge. No GIS component. SpatialGIS has no FedHub/XMS past performance. Hard DECLINE.

---

### 2. DHS USCG - Strategic Services

**Thread:** 19f71ad4345343e0 | **Date:** 2026-07-17T20:03 | **Due:** 07/24/2026  
**Slug:** `dhs-uscg-strategic-services`  
**Triage:** DECLINE  

**Decline rationale:** Management consulting — "integrated strategic analysts" for USCG CIO organizational gap analysis and stakeholder alignment. Strategy consulting / executive advisory role, not IT professional services. No GIS/technical work. DECLINE.

---

### 3. DOJ BOP - Training and Support Services FSA Time Credit Administration

**Thread:** 19f70eec6752063d | **Date:** 2026-07-17T16:35 | **Due:** 07/23/2026  
**Slug:** `doj-bop-training-and-support-services-fsa-time-credit-administration`  
**Triage:** DECLINE  

**Decline rationale:** "Software development support" appears but the entire scope is embedded in First Step Act (FSA) prisoner time credit administration — criminal justice domain requiring deep BOP system knowledge (distinct from `doj-bop-fsa-time-credit-calculation-model`, which was previously submitted). SpatialGIS has no BOP/criminal justice IT past performance. DECLINE — domain specificity overrides IT keyword. Note: automated classifier flagged as MAYBE on "software development" keyword; human override to DECLINE.

---

### 4. HHS CMS - CRM Enterprise Transformation and System Testing

**Thread:** 19f6d34a3c7bc7b9 | **Date:** 2026-07-16T23:13 | **Due:** 07/29/2026  
**Slug:** `hhs-cms-crm-enterprise-transformation-and-system-testing`  
**Triage:** DECLINE  

**Decline rationale:** CMS Virtual Center Strategy (VCS) application testing and NGD Change Control Board management. Highly CMS-specific: requires in-depth knowledge of VCS contractor ecosystem and NGD applications. Not a general IT opportunity. Healthcare IT adjacent. DECLINE.

---

### 5. USAF - Pilot Training Transformation Device Support Services IV

**Thread:** 19f6cce9ae8c6e41 | **Date:** 2026-07-16T21:21 | **Due:** 07/27/2026  
**Slug:** `usaf-pilot-training-transformation-device-support-services-iv`  
**Triage:** DECLINE  

**Decline rationale:** Install, maintain, support flight training simulator hardware (cITD, eITD, Helicopter ITD). Aviation training device hardware — outside SpatialGIS capabilities. Hard DECLINE.

---

### 6. GSA AAS - CALM Recompete

**Thread:** 19f6cc53aadcc60a | **Date:** 2026-07-16T21:11 | **Due:** 07/24/2026  
**Slug:** `gsa-aas-calm-recompete`  
**Triage:** DECLINE  

**Decline rationale:** Software licensing and Help Desk for PRISM (contract management), Bizagi (BPM), AWS, and stackArmor. DM&E staffing for GSA solicitation support. Requires PRISM/Bizagi/stackArmor expertise SpatialGIS doesn't hold. Hard DECLINE.

---

### 7. Navy - SSP - Personnel Reliability Program (PRP) Administration

**Thread:** 19f6c424066bbb09 | **Date:** 2026-07-16T18:48 | **Due:** 07/23/2026  
**Slug:** `navy-ssp-personnel-reliability-program-prp-administration`  
**Triage:** DECLINE  

**Decline rationale:** On-site administrative support for nuclear weapons PRP offices at Kings Bay, GA. Day-to-day HR/administrative functions for nuclear security personnel program. "Database management" is a minor component within a primarily administrative/physical-presence requirement. Not SpatialGIS work. Hard DECLINE.

---

## Reminder Items (No Action)

| Subject | Slug | Prior Status |
|---|---|---|
| Reminder: GSA AAS - CALM Recompete | `gsa-aas-calm-recompete` | DECLINE (new RFI this run also declined) |
| Reminder: HHS CMS - CRM Enterprise Transformation | `hhs-cms-crm-enterprise-transformation-and-system-testing` | DECLINE (new RFI this run also declined) |
| Reminder: Navy SSP - PRP Administration | `navy-ssp-prp-administration` | DECLINE (new RFI this run also declined) |
| Reminder: USAF - JBLM Premise Wiring Bldg 12 | `usaf-jblm-premise-wiring-bldg-12` | DECLINE (facilities/premise wiring) |
| Reminder: EPA - Information Management Program Support Services | `epa-information-management-program-support-services` | Not previously processed — MAYBE; note for human review if Kendrick wants to pursue |
| Reminder: USACE - Professional Support Services | `usace-usace-professional-support-services` | SUBMITTED (in mras-runs, deduped) |
| Reminder: TREAS NETCOM CS2100 PRI Provisioning & PSAP Routing Config | `treas-netcom-cs2100-pri-provisioning-psap-routing-config` | DECLINE (telecom circuit routing, not GIS routing — classifier false-positive on "routing" keyword) |
| Reminder: Army - CMAOD Admin Services Support | `army-cmaod-admin-services-support` | DECLINE (administrative support staffing) |
| Reminder: OSW WHS - Security Support Services | `osw-whs-security-support-services` | DECLINE (TS/SCI security analysts, previously in 2026-07-16 queue) |

---

## POC Information Emails (Informational — No Action Required)

| Subject | Status |
|---|---|
| POC Information: DHS USCG - Geospatial Support Services CG | ✅ Previously submitted. GSA provided vendor POC. No action. |
| POC Information: Navy - ServiceNow SPM Implementation | ✅ Previously submitted. GSA provided vendor POC. No action. |
| POC Information: Navy - ServiceNow HRSD Implementation | ✅ Previously submitted. GSA provided vendor POC. No action. |
| POC Information: Army - Management Support Services | ✅ Previously submitted. GSA provided vendor POC. No action. |
| POC Information: DOJ DEA - Spectrum ACR & Video Surveillance Program | ✅ Previously submitted. GSA provided vendor POC. No action. |

---

## Summary Table

| # | Opportunity | Status | Due Date | Note |
|---|---|---|---|---|
| 1 | DOJ OUSA - Professional IT Support Services | ⚠️ BLOCKED-NEEDS-USER | 07/24/2026 | Manual submission needed — capability statement ready |
| 2 | GSA OCAS - FedHub MSO Operations | DECLINE | 07/31/2026 | PMO for FedHub/XMS, no fit |
| 3 | DHS USCG - Strategic Services | DECLINE | 07/24/2026 | Management consulting, no IT/GIS |
| 4 | DOJ BOP - FSA Training and Support | DECLINE | 07/23/2026 | Criminal justice admin domain |
| 5 | HHS CMS - CRM App Testing | DECLINE | 07/29/2026 | CMS-specific VCS system |
| 6 | USAF - Pilot Training Devices IV | DECLINE | 07/27/2026 | Aviation hardware |
| 7 | GSA AAS - CALM Recompete | DECLINE | 07/24/2026 | PRISM/Bizagi/stackArmor specialty |
| 8 | Navy SSP - PRP Administration | DECLINE | 07/23/2026 | Nuclear personnel HR, on-site |
| 9–17 | Reminders (9 items) | LOGGED | varies | See table above |
| 18–22 | POC Confirmations (5 items) | INFORMATIONAL | N/A | Prior submissions confirmed |

**No autonomous submissions made this run.** 1 BLOCKED item requires Kendrick's manual action by 07/24/2026.
