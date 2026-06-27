# MRAS Daily Queue — 2026-06-27 (Saturday)

**Run date:** 2026-06-27  
**Inbox window:** newer_than:1d (from:rfi@research.gsa.gov)  
**Emails pulled from Gmail:** 3  
**Breakdown:** 2 new RFIs, 1 reminder  
**Unique after dedup:** 3  
**Triage result:** PASS=0 | MAYBE=0 | DECLINE=3 | SKIP_CLOSED=0  
**Auto-submitted this run:** 0  
**Rejected by Qualtrics:** 0  
**Blocked — needs human:** 0  

---

## PASS — 0 items

No opportunities in SpatialGIS's capability footprint among the 3 items processed.

---

## MAYBE — 0 items

---

## DECLINE — 3 items

| # | Subject | Slug | Due | Type | Triage | Decline Reason |
|---|---------|------|-----|------|--------|----------------|
| 1 | USAF - ACC - A5/8/9 Information Technology, LAN and Security Support | `usaf-acc-a5-8-9-information-technology-lan-and-security-support` | 07/14/2026 | NEW | DECLINE | Client-level IT support for Air Combat Command: hardware management, break-fix (remove/replace components/peripherals), OS install/configure, end-user service desk, user account management, security incident reporting. Primary NAICS is equipment maintenance/repair (811212) — not held by SpatialGIS. No GIS or professional IT services deliverables. Survey: `SV_b2ev16y1Pw4RvGC`. |
| 2 | USDA - FSIS Homegrown AI | `usda-fsis-homegrown-ai` | 07/06/2026 | NEW | DECLINE | USDA Food Safety and Inspection Service seeks SaaS Enterprise AI Platform + professional services for regulatory document analysis, inspection decision support, predictive risk modeling, and RAG/fine-tuning. Requires a SaaS product vendor with food safety domain expertise — SpatialGIS has no SaaS AI platform product and no named teaming partner for this capability. Guardrail: FedRAMP/SaaS product required solo (block). Domain mismatch. Survey: `SV_bK7nYMbRaUKPqVE`. ⚠️ *Teaming note — see below.* |
| 3 | Reminder: OSW - DCMA - Online Legal Research Subscription | `osw-dcma-online-legal-research-subscription` | 07/01/2026 | REMINDER | DECLINED 2026-06-23 | Web-accessible legal research subscription database. Legal research service — outside SpatialGIS's scope entirely. Consistent DECLINE across multiple reminders. |

---

## New RFI Detail Notes

### 1. USAF - ACC - A5/8/9 IT, LAN and Security Support (`SV_b2ev16y1Pw4RvGC`)
**Agency:** U.S. Air Force, Air Combat Command (ACC), A5/8/9 directorate  
**Due:** 07/14/2026  
**Scope:** Client-level IT support functions. Specific deliverables include:
- Manage hardware and software components
- Configuration, management, troubleshooting
- Remove and replace components and peripherals to restore operations
- Install and configure OS and applications
- End-user service for operation, restoration, configuration
- Report security incidents and execute corrective procedures
- Manage client user accounts

**Analysis:** This is a desktop/helpdesk support and break-fix IT role, not professional IT services or GIS. The hardware removal/replacement work maps to NAICS 811212 (equipment maintenance), which SpatialGIS does not hold. No geospatial content. The "LAN and Security" component is network administration, not cybersecurity consulting.  
**Decision: DECLINE — No capability alignment.**

---

### 2. USDA - FSIS Homegrown AI (`SV_bK7nYMbRaUKPqVE`)
**Agency:** USDA Food Safety and Inspection Service (FSIS)  
**Due:** 07/06/2026  
**Scope:** SaaS Enterprise AI Platform + professional services for:
- Agency document ingestion, search, analysis
- Automated regulatory workflows
- Institutional knowledge capture
- Regulatory Q&A
- Inspection decision support
- Document analysis
- Predictive risk modeling
- Model fine-tuning and RAG

**Analysis:** The requirement is for a SaaS AI platform vendor with food safety inspection domain expertise. SpatialGIS holds NAICS 541511/541512 covering custom software and systems design, which are relevant to AI platform development. However:
- No SaaS AI product in SpatialGIS portfolio
- Food safety / inspection domain requires specialized subject matter expertise SpatialGIS lacks
- "Predictive risk modeling" could theoretically leverage spatial analytics but is not framed geospatially
- A response would require a teaming partner with an enterprise AI/SaaS product

**Guardrail triggered:** FedRAMP/SaaS product required solo → BLOCK per standing rules.  
**Decision: DECLINE — SaaS AI platform required; no partner named.**

> ⚠️ **Teaming opportunity flag for Kendrick:** If SpatialGIS has or can identify a teaming partner with an enterprise AI SaaS platform (e.g., Microsoft Azure AI, Palantir AIP, or a smaller AI-native firm), this could become viable as a subcontractor/prime arrangement before 07/06/2026. SpatialGIS's GIS + data analytics capabilities could complement an AI platform company's core product. Worth a quick scan of existing relationships.

---

## Cumulative Prior Submissions

| Slug | Status | Fill Report |
|------|--------|-------------|
| army-real-property-remediation-support-services | SUBMITTED | fill-report.json |
| doj-fbi-dssu-program-support | SUBMITTED-CONFIRMED (POC 2026-06-15) | fill-report.json |
| doj-atf-hrpd-modernized-case-management-system | SUBMITTED-CONFIRMED (POC 2026-06-25) | fill-report.json |
| doi-blm-national-travel-management-planning-tmp-bpa | SUBMITTED-CONFIRMED | fill-report.json |
| usace-usace-professional-support-services | SUBMITTED-CONFIRMED (POC 2026-06-25) | fill-report.json |
| usace-mpbi-data-analytics-support | SUBMITTED | fill-report.json |
| navy-information-technology-governance-and-mission-support-itgms | SUBMITTED | fill-report.json |
| usmc-mcsc-wargaming-capability-software-integration-services | SUBMITTED-CONFIRMED | fill-report.json |
| hhs-cdc-technical-support-for-vehss | SUBMITTED | fill-report.json |
| navy-navsea-contract-support-services | SUBMITTED-CONFIRMED | fill-report.json |
| dhs-uscg-program-management-and-analysis | SUBMITTED-CONFIRMED (POC 2026-06-19) | fill-report.json |
| usmc-infads-professional-services-contract | SUBMITTED | fill-report.json |
| doi-secure-ai-assistant-for-final-agency-decisions-fad | SUBMITTED-CONFIRMED (POC 2026-06-19) | fill-report.json |
| usaf-usafa-donor-funds-management-it-ecosystem | SUBMITTED | fill-report.json |
| usaf-daf-damage-assessment-management-office-damo | SUBMITTED-CONFIRMED (POC 2026-06-19) | fill-report.json |
| va-va-ams-data-governance-standardization | SUBMITTED-CONFIRMED (POC 2026-06-25) | fill-report.json |
| usaf-fire-emergency-information-management | SUBMITTED-CONFIRMED (POC 2026-06-15) | fill-report.json |
| fcc-engineering-and-architecture-services-bpa | SUBMITTED-CONFIRMED (Response 2026-06-24) ⚠️ no fill report | — |

**Total confirmed/submitted:** 18 (unchanged from 2026-06-26)

---

## Open Item (carried from 2026-06-26)

**FCC Engineering and Architecture Services BPA:** Response confirmation received 2026-06-24 but no fill report in `working/mras-runs/`. If submitted manually by Kendrick, recommend creating stub fill report at `working/mras-runs/fcc-engineering-and-architecture-services-bpa-fill-report.json`.

---

## Action Items for Kendrick

1. **USDA FSIS Homegrown AI teaming scan (optional, due 07/06/2026):** If SpatialGIS has a relationship with an enterprise AI platform company (RAG/SaaS), this opportunity could be pursued as a teaming arrangement before the 9-day deadline. No action if no partner available.
2. **FCC BPA fill report stub** (carried forward): Create `working/mras-runs/fcc-engineering-and-architecture-services-bpa-fill-report.json` if submitted manually.

---

## Summary

Quiet Saturday run — 3 items (2 new, 1 reminder), all DECLINE. The USAF ACC IT support role is a hardware break-fix/helpdesk position outside SpatialGIS's capability footprint. The USDA FSIS Homegrown AI opportunity requires a SaaS AI platform product SpatialGIS does not have — flagged as a teaming opportunity if a partner can be identified by 07/06/2026. OSW-DCMA legal research subscription is a consistent DECLINE. Portfolio of 18 prior submissions unchanged.
