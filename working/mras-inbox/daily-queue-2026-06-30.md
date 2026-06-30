# MRAS Daily Queue — 2026-06-30

**Run date:** 2026-06-30  
**Gmail query:** `from:rfi@research.gsa.gov newer_than:1d`  
**Inbox count:** 9  
**Unique after dedup:** 9 (POC confirmation slugs differ from fill-report slugs)  
**PASS / MAYBE / DECLINE / SKIP_CLOSED:** 0 / 0 / 8 / 1  
**Submitted:** 0  
**Rejected:** 0  
**Blocked:** 0  

---

## Summary

9 threads pulled from Gmail. 3 are post-submission POC confirmation emails for already-completed RFIs (USMC Wargaming, Navy NAVSEA, DOI BLM TMP BPA — all SUBMITTED-CONFIRMED). Of the 6 new/reminder RFI emails: 1 is past due (DHS HSIN, due 06/29), 1 is a hard DECLINE by keyword (USAF Weapons Integration SME — weapons/LVC/SAM/RTO), and 4 have no capability keyword match (conservative decline). No auto-submissions triggered.

One item flagged for optional human review: **USDA FSIS Homegrown AI** — Enterprise AI Platform SaaS + professional services, due 07/06/2026. Triage DECLINE by keyword gap (no GIS/geospatial match), but NAICS 541511/512/519 overlap and professional services scope make it a plausible MAYBE if Kendrick wants to respond.

---

## POC Confirmation Emails (3) — No Action Required

| Thread ID | Subject | Related Submission |
|---|---|---|
| 19f15f0467493cae | POC Information: USMC - Wargaming Capability Software Integration Services | usmc-mcsc-wargaming-capability-software-integration-services (SUBMITTED-CONFIRMED) |
| 19f15ed81cce5ee9 | POC Information: Navy - NAVSEA - Contract Support Services | navy-navsea-contract-support-services (SUBMITTED-CONFIRMED) |
| 19f15e36bc1dbf2e | POC Information: DOI - BLM - National Travel Management Planning (TMP) BPA | doi-blm-national-travel-management-planning-tmp-bpa (SUBMITTED-CONFIRMED) |

GSA is providing agency/POC contact information following our prior submissions. No survey URL; no action needed.

---

## SKIP_CLOSED (1)

### DHS - HSIN Stakeholder Engagement
- **Slug:** `dhs-hsin-stakeholder-engagement`
- **Survey:** SV_dpqnpRhjTCpA1nw
- **Due:** 2026-06-29 ← **PAST DUE** (yesterday)
- **Agency:** DHS
- **Description:** Support to the Homeland Security Information Network (HSIN) program — stakeholder relationships, training delivery, engagement coordination, requirements management.
- **Triage:** SKIP_CLOSED — due date passed before this run.

---

## DECLINE — Hard-Decline Keyword (1)

### USAF - 56 RMO Weapons Integration SME
- **Slug:** `usaf-56-rmo-weapons-integration-sme`
- **Survey:** SV_3EPHvGNThoHcyRU
- **Due:** 2026-06-30 (today)
- **Agency:** USAF 56th Range Management Office, Luke AFB
- **Description:** Weapons Integration SME providing SAM-1 director, LVC computer operator, and/or Range Training Officer (RTO) on-site at Luke AFB within the LMOC.
- **Triage:** DECLINE — matched hard-decline keywords: `weapons integration`, `LVC` (live virtual constructive), `range training officer`. Outside SpatialGIS scope by policy.

---

## DECLINE — No Capability Keyword Match (4)

### TREAS - IRS - Hyper-Converged Infrastructure
- **Slug:** `treas-irs-hyper-converged-infrastructure`
- **Survey:** SV_eyZ8WKu0S7jWeqy
- **Due:** 2026-07-10
- **Agency:** Treasury IRS
- **Description:** Procure enterprise-scale software-defined HCI platform (Nutanix/VMware vSAN type): hardware, software, licensing, O&M, migration services, embedded support engineering, enterprise lifecycle management.
- **Triage:** DECLINE — hardware product procurement (HCI appliances); no GIS/IT-services keyword match. SpatialGIS sells professional services, not HCI platforms.

### HHS CDC - Comprehensive Cost Avoidance
- **Slug:** `hhs-cdc-comprehensive-cost-avoidance`
- **Survey:** SV_3DcAmkZcECusIjs
- **Due:** 2026-06-30 (today — closes tonight)
- **Agency:** HHS CDC / WTC Health Program
- **Description:** Health insurance verification solution to identify/reverify OHI policies for WTC Health Program Survivors via automated data matches against an insurance database.
- **Triage:** DECLINE — healthcare insurance data matching; no GIS/geospatial or general IT keyword match. Healthcare IT domain, outside SpatialGIS lane.

### DHS - Card Upgrade Refresh Equipment (CURE)
- **Slug:** `dhs-card-upgrade-refresh-equipment-cure`
- **Survey:** SV_77e3qKYFTd4eDj0
- **Due:** 2026-07-06
- **Agency:** DHS USCIS
- **Description:** Card personalization systems to produce USCIS secure identification cards (PRC and EAD). Secure document production hardware/operations.
- **Triage:** DECLINE — smart card / secure document production hardware. No SpatialGIS capability alignment.

### USDA - FSIS Homegrown AI  ⚑ OPTIONAL HUMAN REVIEW
- **Slug:** `usda-fsis-homegrown-ai`
- **Survey:** SV_bK7nYMbRaUKPqVE
- **Due:** 2026-07-06
- **Agency:** USDA Food Safety and Inspection Service
- **Description:** SaaS Enterprise AI Platform + professional services: ingest/search/analyze agency documents and operational data, automate regulatory workflows, capture institutional knowledge. Supports regulatory Q&A, inspection decision support, document analysis, predictive risk modeling via RAG and model fine-tuning.
- **Triage:** DECLINE (no GIS/geospatial keyword; "AI platform" / "RAG" / "SaaS" not in keyword list).
- **Human review flag:** NAICS 541511/541512/541519 overlap. "Professional services to design, implement, and operationalize" an enterprise AI platform is within SpatialGIS's IT consulting scope. If Kendrick wants to respond, this needs a teaming partner with an AI Platform SaaS product (or can SpatialGIS implement using commercial LLM APIs + open-source stack?). Due 07/06 — 6 days. Run `/mras-discover` manually if proceeding.

---

## Prior Submission Inventory (17 total, all SUBMITTED-CONFIRMED)

| Slug | Status |
|---|---|
| army-real-property-remediation-support-services | SUBMITTED-CONFIRMED |
| dhs-uscg-program-management-and-analysis | SUBMITTED-CONFIRMED |
| doi-blm-national-travel-management-planning-tmp-bpa | SUBMITTED-CONFIRMED |
| doi-secure-ai-assistant-for-final-agency-decisions-fad | SUBMITTED-CONFIRMED |
| doj-atf-hrpd-modernized-case-management-system | SUBMITTED-CONFIRMED |
| doj-fbi-dssu-program-support | SUBMITTED-CONFIRMED |
| hhs-cdc-technical-support-for-vehss | SUBMITTED-CONFIRMED |
| navy-information-technology-governance-and-mission-support-itgms | SUBMITTED-CONFIRMED |
| navy-navsea-contract-support-services | SUBMITTED-CONFIRMED |
| usace-mpbi-data-analytics-support | SUBMITTED-CONFIRMED |
| usace-usace-professional-support-services | SUBMITTED-CONFIRMED |
| usaf-daf-damage-assessment-management-office-damo | SUBMITTED-CONFIRMED |
| usaf-fire-emergency-information-management | SUBMITTED-CONFIRMED |
| usaf-usafa-donor-funds-management-it-ecosystem | SUBMITTED-CONFIRMED |
| usmc-infads-professional-services-contract | SUBMITTED-CONFIRMED |
| usmc-mcsc-wargaming-capability-software-integration-services | SUBMITTED-CONFIRMED |
| va-va-ams-data-governance-standardization | SUBMITTED-CONFIRMED |
