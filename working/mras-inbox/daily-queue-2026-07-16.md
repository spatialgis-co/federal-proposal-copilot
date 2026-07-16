# MRAS Daily Queue — 2026-07-16

**Run date:** 2026-07-16  
**Inbox window:** newer_than:1d from rfi@research.gsa.gov  
**Totals:** 6 emails received | 0 PASS | 0 submitted | 0 blocked | 5 DECLINE | 1 RESPONSE-CONFIRMED (no fill-report on file)

---

## ⚠️ ANOMALY — DOJ BOP FSA Time Credit Calculation Model (already submitted, no fill-report)

**Thread:** 19f660185b502392  
**Type:** Response Received confirmation (not a new RFI)  
**Status:** SUBMITTED-CONFIRMED via Qualtrics  
**Response ID:** R_GD58fahuUpwcHS8 | **Survey ID:** SV_cTpBr6pqrdM0Z2m

**Finding:** A response confirmation email arrived showing SpatialGIS successfully submitted this MRAS. The response recorded: SIN 54151S, NAICS 541511, small business + SDB (d), Yes/Yes/Yes technical questions, capability statement uploaded. However, there is **no corresponding fill-report** in `working/mras-runs/doj-bop-fsa-time-credit-calculation-model-fill-report.json`. The submission appears to have been completed by a prior pipeline run that did not write a local fill-report, or was submitted manually.

**Action needed:** None — submission is confirmed. No re-submission. Kendrick should note the missing fill-report for record-keeping. The prior daily triages had classified this as DECLINE based on keyword mismatch; that classification was incorrect — the pipeline or a manual run caught it separately.

---

## DECLINE Items

### 1. OSW - WHS - Security Support Services — NEW RFI

**Thread:** 19f66cd84e47b29b  
**Date received:** 2026-07-15T17:22:50Z  
**Responses due:** 07/24/2026  
**Slug:** osw-whs-security-support-services  
**Triage:** DECLINE  

**Full requirement (from email body):**  
WHS SESD seeks a TOP SECRET cleared contractor to provide 6 full-time, TS/SCI-cleared Security Analysts (1 Senior, 5 Mid) under a 3-year Firm-Fixed-Price contract (1-year base starting Sept 10, 2026, plus two 1-year options) to manage security operations, policy, and compliance across the NCR.

**Decline rationale:** Physical/administrative security analyst staffing requirement. Requires TS/SCI-cleared Security Analysts (6 FTE). This is a personnel-based security operations and policy role — not IT, not GIS, not software development, not cybersecurity services. SpatialGIS has no capability match and no cleared security analysts on staff to fulfill 6 FTE. Hard DECLINE — no override warranted.

---

### 2. Reminder: DOC NIST - Federal Lab Consortium AI Enabled Technology Transfer Tools

**Thread:** 19f653c96870005c  
**Date received:** 2026-07-15T10:04:55Z  
**Slug:** doc-nist-federal-lab-consortium-ai-enabled-technology-transfer-tools  
**Triage:** DECLINE  

**Decline rationale:** National lab technology transfer tooling with AI focus. No GIS/geospatial component identifiable from subject or snippet. "AI-enabled technology transfer" at NIST typically involves commercialization support, IP management, or lab-to-industry pathways — not SpatialGIS capabilities. No prior submission on file. Reminder received; original RFI likely issued ~1 week prior. Conservative DECLINE upheld — no IT or GIS keyword match.

---

### 3. Reminder: OSW - DHA - Instrument Tracking System Subscription

**Thread:** 19f653ade58607c7  
**Date received:** 2026-07-15T10:02:42Z  
**Slug:** osw-dha-instrument-tracking-system-subscription  
**Triage:** DECLINE (previously DECLINE on 2026-07-15 for original RFI)  

**Decline rationale:** Defense Health Agency medical instrument tracking COTS subscription. Healthcare IT / medical device inventory domain. Not GIS, not SpatialGIS IT services. Previously triaged as DECLINE. Reminder confirms no change.

---

### 4. Reminder: NIST - Time Scale Security Enhancement

**Thread:** 19f65396a51399b9  
**Date received:** 2026-07-15T10:01:22Z  
**Slug:** nist-time-scale-security-enhancement  
**Triage:** DECLINE  

**Decline rationale:** NIST timekeeping/synchronization security (NTP/PTP protocol security, precision timing). Highly specialized physics/standards domain. No overlap with SpatialGIS capabilities in GIS, geospatial, IT services, or cybersecurity. DECLINE.

---

### 5. Reminder: DOC NIST - Manufacturing Data Analysis and Modeling Tool

**Thread:** 19f6539683af6e5d  
**Date received:** 2026-07-15T10:01:22Z  
**Slug:** doc-nist-manufacturing-data-analysis-and-modeling-tool  
**Triage:** DECLINE  

**Decline rationale:** Manufacturing-domain data analysis and modeling tool — NIST manufacturing research support. While "data analysis" appears in SpatialGIS MAYBE keywords, the manufacturing-specific context places this outside SpatialGIS core capabilities. No GIS/geospatial component. DECLINE.

---

## Summary

| # | Opportunity | Status | Due Date |
|---|-------------|--------|----------|
| 1 | DOJ BOP - FSA Time Credit Calculation Model | SUBMITTED-CONFIRMED (prior run, fill-report missing) | 07/27/2026 |
| 2 | OSW - WHS - Security Support Services | DECLINE (security analyst staffing, TS/SCI, not SpatialGIS work) | 07/24/2026 |
| 3 | DOC NIST - Federal Lab Consortium AI Tech Transfer | DECLINE (reminder, no GIS match) | unknown |
| 4 | OSW - DHA - Instrument Tracking System Subscription | DECLINE (reminder, previously declined) | unknown |
| 5 | NIST - Time Scale Security Enhancement | DECLINE (reminder, specialized timing/physics domain) | unknown |
| 6 | DOC NIST - Manufacturing Data Analysis and Modeling Tool | DECLINE (reminder, manufacturing domain, no GIS) | unknown |

**No submissions made this run.** No blocking conditions triggered (no PASS items reached the submission guardrails).
