# MRAS Daily Queue — 2026-07-22

**Run date:** 2026-07-22  
**Inbox window:** newer_than:1d from rfi@research.gsa.gov  
**Totals:** 10 emails received | 3 new RFIs | 0 PASS | 0 submitted | 0 blocked | 3 DECLINE (new RFIs) | 3 DECLINE (reminders) | 4 RESPONSE-CONFIRMED (prior submissions, no local fill-report)

---

## ⚠️ ANOMALY — 4 Response Confirmations (prior submissions, fill-reports missing)

Four confirmation emails arrived today for prior submissions that have no corresponding `working/mras-runs/*-fill-report.json`. This is the same pattern as the DOJ BOP FSA anomaly noted on 2026-07-16. No re-submission needed — responses are confirmed. Kendrick should note the missing fill-reports for record-keeping.

| # | Opportunity | Confirmation ID | Status |
|---|-------------|-----------------|--------|
| 1 | HHS CMS - CRM Enterprise Transformation and System Testing | SV_cZPUR0kCGvOtheC-R_GO6UAgMwsWC4lEi | SUBMITTED-CONFIRMED |
| 2 | DHS USCG - Strategic Services | SV_2mfScn3upmXinDU-R_GYwR2CCsDnWXWIx | SUBMITTED-CONFIRMED |
| 3 | DOJ BOP - Training and Support Services FSA Time Credit Administration | SV_3xAVzI9girTGmxg-R_GDSnPD3VAgsWZG1 | SUBMITTED-CONFIRMED |
| 4 | DOJ OUSA - Professional IT Support Services | SV_0JQQzmimQF4B9TU-R_G418T59VQmJ1bNG | SUBMITTED-CONFIRMED |

---

## New RFI DECLINE Items

### 1. DOJ ATF - Federated Search Platform

**Thread:** 19f86f5e587a7d21  
**Date received:** 2026-07-21T23:14:45Z  
**Responses due:** 07/31/2026  
**Survey URL:** SV_1NtI4oDTgFlcBYW  
**Slug:** doj-atf-federated-search-platform  
**Triage:** DECLINE  

**Requirement summary:**  
ATF requires enterprise-grade decentralized data discovery COTS platform for federated search across disparate internal and external repositories — no data ingestion into a centralized warehouse. Must be fully operational in 90 calendar days.

**Decline rationale:** COTS Federated Search platform product acquisition. ATF is seeking a specific data discovery/search platform product (e.g., Datafabric, Elastic, Alation-class), not GIS or professional IT services. SpatialGIS does not sell or resell federated search platforms and has no relevant COTS product to offer. No keyword match. Hard DECLINE.

---

### 2. DOI - NPS - Law Enforcement Readiness SaaS

**Thread:** 19f864ca8f5fc99e  
**Date received:** 2026-07-21T20:09:49Z  
**Responses due:** 07/31/2026  
**Survey URL:** SV_bwMn92lOdIJnvdI  
**Slug:** doi-nps-law-enforcement-readiness-saas  
**Triage:** DECLINE  

**Requirement summary:**  
FedRAMP Moderate cloud-hosted SaaS to manage NPS law enforcement training records, certifications, medical clearances, background investigations, instructor qualifications, and government-issued property — including implementation, data migration, licensing, and support.

**Decline rationale (two independent grounds):**
1. **FedRAMP guardrail triggered.** Requires a FedRAMP Moderate-authorized SaaS product. SpatialGIS does not hold FedRAMP authorization and does not resell an authorized SaaS product for this domain. Block per `block_if_fedramp_product_required_solo = true`.
2. **Capability mismatch.** Law enforcement HR/readiness management SaaS is outside SpatialGIS core capabilities. No GIS, no geospatial, no IT services match. Hard DECLINE.

---

### 3. HHS CDC - National Technical Assistance Center for Adolescent Health

**Thread:** 19f84dfd44320eb2  
**Date received:** 2026-07-21T13:31:10Z  
**Responses due:** 07/27/2026  
**Survey URL:** SV_2blRw9S2KPGoHFc  
**Slug:** hhs-cdc-national-technical-assistance-center-for-adolescent-health  
**Triage:** DECLINE  

**Requirement summary:**  
CDC Division of Adolescent and School Health (DASH) requires a Technical Assistance and Professional Development (TA/PD) Center supporting CDC-funded adolescent health recipients across four areas: (1) Advisory Council operations; (2) strategic plan for evidence-based TA/PD; (3) TA/PD Center website; (4) monitoring and evaluation. Kickoff within one month of award.

**Decline rationale:** Public health program management and technical assistance — not IT, not GIS, not software development. No SpatialGIS capability applies. "Website development" is a minor sub-element of a predominantly public health program management effort. DECLINE.

---

## Reminder DECLINE Items

### 4. Reminder: DHS TSA - Secure Infrastructure & Vulnerability Management

**Thread:** 19f8420d16dfc72a  
**Date received:** 2026-07-21T10:02:49Z  
**Slug:** dhs-tsa-secure-infrastructure-vulnerability-management  
**Triage:** DECLINE (reminder — original RFI not previously triaged in prior queues)  

**Decline rationale:** TSA secure infrastructure and vulnerability management — network/endpoint security domain, not GIS or professional IT services that SpatialGIS delivers. No capability match. DECLINE.

---

### 5. Reminder: OSW - WHS - Security Support Services

**Thread:** 19f841fb4f978dfa  
**Date received:** 2026-07-21T10:01:27Z  
**Slug:** osw-whs-security-support-services  
**Triage:** DECLINE (previously DECLINE on 2026-07-16 for original + first reminder)  

**Decline rationale:** WHS SESD TS/SCI-cleared Security Analyst staffing requirement. Previously triaged DECLINE. No change.

---

### 6. Reminder: NIST - Time Scale Security Enhancement

**Thread:** 19f841e8eda0f6f3  
**Date received:** 2026-07-21T10:00:07Z  
**Slug:** nist-time-scale-security-enhancement  
**Triage:** DECLINE (previously DECLINE on 2026-07-16)  

**Decline rationale:** NIST timekeeping/synchronization security (NTP/PTP). Specialized physics/standards domain. Previously DECLINE. No change.

---

## Summary Table

| # | Opportunity | Type | Status | Due Date |
|---|-------------|------|--------|----------|
| 1 | HHS CMS - CRM Enterprise Transformation | Response confirmation | SUBMITTED-CONFIRMED (prior run, fill-report missing) | — |
| 2 | DHS USCG - Strategic Services | Response confirmation | SUBMITTED-CONFIRMED (prior run, fill-report missing) | — |
| 3 | DOJ BOP - FSA Time Credit Administration | Response confirmation | SUBMITTED-CONFIRMED (prior run, fill-report missing) | — |
| 4 | DOJ OUSA - Professional IT Support Services | Response confirmation | SUBMITTED-CONFIRMED (prior run, fill-report missing) | — |
| 5 | DOJ ATF - Federated Search Platform | New RFI | DECLINE (COTS search product, no match) | 07/31/2026 |
| 6 | DOI NPS - Law Enforcement Readiness SaaS | New RFI | DECLINE (FedRAMP required + no match) | 07/31/2026 |
| 7 | HHS CDC - National Technical Assistance Center for Adolescent Health | New RFI | DECLINE (public health TA/PD, no IT/GIS match) | 07/27/2026 |
| 8 | DHS TSA - Secure Infrastructure & Vulnerability Mgmt | Reminder | DECLINE (network security, no match) | unknown |
| 9 | OSW - WHS - Security Support Services | Reminder | DECLINE (previously declined, TS/SCI staffing) | 07/24/2026 |
| 10 | NIST - Time Scale Security Enhancement | Reminder | DECLINE (previously declined, physics domain) | unknown |

**No submissions made this run.** No PASS items reached the submission guardrails. Four prior submissions confirmed by response emails received today.
