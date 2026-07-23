# MRAS Daily Queue — 2026-07-23

**Run date:** 2026-07-23  
**Inbox window:** newer_than:1d from rfi@research.gsa.gov  
**Totals:** 11 emails received | 2 new RFIs | 1 PASS | 1 MAYBE | 9 DECLINE | 0 submitted | 0 blocked-guardrail | **PIPELINE BLOCKED: feedback.gsa.gov is unreachable via session egress proxy**

---

## ⛔ CRITICAL: Qualtrics Proxy Block — All Submission Pipeline Steps Failed

**feedback.gsa.gov:443 is blocked by the session's egress proxy (policy denial, 403).**  
This means `mras_discover.py` and `mras_submitter.py` cannot reach any Qualtrics survey URL. Neither QID discovery nor automated submission is possible in this remote session.

**Manual action required:** Use a local machine or browser to:
1. Open the survey URL for the PASS opportunity (DoD Data Science) — see below
2. Evaluate whether SpatialGIS can honestly answer the capability questions
3. If yes, complete the capability statement and submit manually through the Qualtrics form

The pipeline otherwise ran correctly through triage: raw saved, dedup'd, triage classifications applied. The gap is the final submission steps.

---

## PASS — Requires Human Submission

### DoD - Data Science and Research Support — NEW RFI

**Thread:** 19f8a5051c880e29  
**Date received:** 2026-07-22T14:52:24Z  
**Due:** 08/05/2026 *(13 days from today — actionable)*  
**Survey URL:** https://feedback.gsa.gov/jfe/form/SV_erfihPmq9dRKOuq  
**Survey ID:** SV_erfihPmq9dRKOuq  
**Slug:** dod-data-science-and-research-support  
**Triage:** PASS — keyword match: `geospatial`

**Full requirement (from email body):**  
The Government seeks a commercial off-the-shelf data science and business research solution that provides access to comprehensive, frequently updated business, ownership, financial, supply chain, and **geospatial data**. The solution will support analysis of companies and related entities to identify ownership structures, beneficial ownership, foreign influence, supply chain risks, financial indicators, and other business relationships relevant to mission assurance and risk management.

**Capability analysis:**  
The geospatial data keyword triggered a PASS. However, the core requirement is a **COTS data intelligence platform** (think Dun & Bradstreet Hoovers, Sayari Analytics, or Esri Business Analyst) covering business, ownership, financial, supply chain, AND geospatial data feeds. SpatialGIS provides GIS professional services, not a COTS multi-domain data subscription product. Before responding, Kendrick must confirm:

1. **Can SpatialGIS honestly claim a solution?** If responding, the capability statement must cover geospatial data component only and not overclaim on the business/ownership/financial data domains.
2. **COTS vs. services framing:** If the survey allows professional services (GIS data integration, geospatial analytics) rather than requiring a product license, SpatialGIS may be able to respond honestly.
3. **Check actual Qualtrics questions** at the survey URL — the questions will reveal whether this is strictly product-only or allows services vendors.

**Potential guardrail blocks to verify before submitting:**
- If Q asks "Do you have a COTS platform with business/ownership/financial data" → answer honestly No (BLOCK if that's the only path)
- If the RFI Technical Questions document covers domains outside geospatial → answer honestly, with teaming attribution or No as appropriate

**Status:** BLOCKED-NEEDS-USER — Cannot auto-submit. Survey access blocked at proxy layer. Manual browser submission required after reviewing the actual questions.

---

## MAYBE — Human Review Recommended

### EPA - Information Management Program Support Services — REMINDER

**Thread:** 19f894749bada5e3  
**Date received:** 2026-07-22T10:02:30Z  
**Type:** Reminder (original RFI issued ~1 week prior)  
**Slug:** epa-information-management-program-support-services  
**Triage:** MAYBE — keyword match: `program support`

**Note:** "Information Management" and "Program Support Services" at EPA could be IT/data management services, which may be within SpatialGIS's scope. However:
- It is a reminder, suggesting this was already visible in a prior day's inbox but was not triaged as a new item (likely never seen in daily-unique due to a different thread ID for the original)
- Cannot access the survey to inspect questions (proxy block)
- "Program support services" broadly overlaps with SpatialGIS's IT services, but EPA information management could be records/EDRMS/SharePoint — domains that require teaming

**Status:** LOGGED-FOR-HUMAN-REVIEW — Recommend Kendrick manually check whether this is IT/data management (respond) or records/content management (decline or team). Check the EPA RFI directly using the URL in the reminder email.

---

## DECLINE Items

| # | Subject | Type | Slug | Reason |
|---|---------|------|------|--------|
| 1 | Re: Sources Sought Response — RFI1824769 | admin_reply | (not an RFI) | GSA admin reply thread, no opportunity |
| 2 | Regarding your MRAS Inquiry — RFI1824769 | auto_response | (not an RFI) | GSA auto-acknowledgement, no opportunity |
| 3 | Army - Program Management Support Services (PMSS) | new_rfi | army-program-management-support-services-pmss | Program management/SAFe/acquisition financial/sustainment ops — no GIS or IT match. SpatialGIS lacks SAFe PM credentials, contracting/acquisition financial management, and property management. IT support is a minor secondary element. DECLINE. Due 08/06/2026. |
| 4 | POC Information: DOJ BOP - FSA Time Credit Calculation Model | poc_notification | (prior confirmed submission) | POC notification received — confirms the FSA Time Credit submission previously noted (no fill-report on file per 2026-07-16 queue). No action needed. |
| 5 | Reminder: DOJ ATF - Federated Search Platform | reminder | doj-atf-federated-search-platform | Previously DECLINE 2026-07-22. No change. |
| 6 | Reminder: Navy - SSP - Personnel Reliability Program (PRP) Administration | reminder | navy-ssp-personnel-reliability-program-prp-administration-market-research | Personnel reliability/nuclear surety program administration. Not IT, not GIS. DECLINE. |
| 7 | Reminder: DOI - NPS - Law Enforcement Readiness SaaS | reminder | doi-nps-law-enforcement-readiness-saas | Previously DECLINE 2026-07-22. SaaS platform for law enforcement readiness — not SpatialGIS domain. |
| 8 | Reminder: USAF - Pilot Training Transformation Device Support Services IV | reminder | usaf-pilot-training-transformation-device-support-services-iv | Flight training device support — hardware/simulator maintenance domain. No GIS match. DECLINE. |
| 9 | Reminder: Army - CMAOD Admin Services Support | reminder | army-cmaod-admin-services-support | CMAOD administrative support — program office admin/clerical support. Not IT, not GIS. DECLINE. |

---

## Summary Table

| Opportunity | Status | Due Date | Action |
|-------------|--------|----------|--------|
| DoD - Data Science and Research Support | BLOCKED-NEEDS-USER (proxy block, COTS mismatch TBD) | 08/05/2026 | Kendrick: open survey URL, review questions, submit manually if honest fit |
| EPA - Information Management Program Support Services | LOGGED-FOR-HUMAN-REVIEW (MAYBE, reminder) | Unknown | Kendrick: review EPA RFI to determine if IT/data vs. records domain |
| Army - Program Management Support Services (PMSS) | DECLINE | 08/06/2026 | No action |
| All 6 reminder items + 2 admin emails | DECLINE / NO-ACTION | Various | No action |

**0 submissions made this run. Pipeline blocked at feedback.gsa.gov.** Contact Anthropic support or re-run on a local machine to unlock autonomous Qualtrics submission.
