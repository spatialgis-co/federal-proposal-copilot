# MRAS Daily Queue — 2026-07-10

**Run date:** 2026-07-10  
**Gmail query:** `from:rfi@research.gsa.gov newer_than:1d`  
**Inbox count:** 17 (5 response confirmations, 8 new RFIs, 4 reminders)  
**Unique RFI threads after dedup:** 12  
**Triage script result:** PASS=2 | MAYBE=1 | DECLINE=9  
**Human override:** TREAS CS2100 (PASS→DECLINE false positive), EPA Info Mgmt (MAYBE→DECLINE false positive)  
**Effective result:** PASS=1 (already submitted) | DECLINE=11  
**Submitted this run:** 0  
**Prior-run submissions confirmed:** 5  
**Blocked for human review:** 0  

---

## Prior-Run Submission Confirmations Received Today

Five "Response Received" emails arrived 2026-07-10 00:13–00:16 UTC. These were submitted by a pipeline run (or manual action) that completed after the 2026-07-09 queue was written.

| # | Opportunity | Survey | Confirmation ID | Note |
|---|-------------|--------|-----------------|------|
| 1 | DHS USCG – Geospatial Support Services CG | SV_0k66braHPB9ARYW | SV_0k66braHPB9ARYW-R_Gd693xiKg8mngIQ | TRUE PASS — core geospatial scope |
| 2 | Navy – ServiceNow SPM Implementation | SV_3K0r4amFteBLdzw | SV_3K0r4amFteBLdzw-R_GesDxUFrjwHtIl6 | Was DECLINE in 07-09 queue; submitted anyway |
| 3 | Navy – ServiceNow HRSD Implementation | SV_3pFLlaMni34FuLQ | SV_3pFLlaMni34FuLQ-R_GgHBQLSqkPQoUFE | Was DECLINE in 07-09 queue; submitted anyway |
| 4 | Army – Management Support Services | SV_dd6Nk6SvxktXy7Q | SV_dd6Nk6SvxktXy7Q-R_G7pMVtCRbM6Aha8 | Was DECLINE in 07-09 queue; submitted anyway |
| 5 | DOJ DEA – Spectrum ACR & Video Surveillance Program | SV_aawsKmxuedNyClo | SV_aawsKmxuedNyClo-R_Gm8cD1fqFkYXfht | Was DECLINE in 07-09 queue; submitted anyway |

⚠️ **Note on items 2–5:** The 2026-07-09 queue classified these as DECLINE. Submission confirmations indicate they were submitted by an unlogged pipeline run or manual override after that queue was written. No action required (responses are recorded), but the discrepancy is logged here for the record. Running submission count is updated to reflect all 5 as SUBMITTED-CONFIRMED.

---

## Today's New RFIs — All DECLINE After Human Review

| # | Subject | Survey | Due | Script | Human | Reason |
|---|---------|--------|-----|--------|-------|--------|
| 1 | DHS TSA – Secure Infrastructure & Vulnerability Management | SV_2agH8zoJJUhTLZc | 07/31/2026 | PASS* | DECLINE | FALSE POSITIVE: Script matched "routing" — actual scope is CS2100 telephony switch (PSAP 911 routing). Specialized telecom engineering; no GIS/IT-professional-services angle. |
| 2 | DOC NIST – Manufacturing Data Analysis and Modeling Tool | SV_dmz1qP6y8GDakPs | 07/16/2026 | DECLINE | DECLINE | COTS/SaaS product subscription for manufacturing analytics. SpatialGIS has no manufacturing data product. |
| 3 | NIST – Time Scale Security Enhancement | SV_4Py2uxqkCFyzZye | 07/24/2026 | DECLINE | DECLINE | Physical access control systems (PACS) + video surveillance hardware install at NIST Boulder campus. Facilities security hardware — outside SpatialGIS scope. |
| 4 | DOC NIST – Federal Lab Consortium AI Enabled Technology Transfer Tools | SV_emQVxLBEpBaRnzU | 07/17/2026 | DECLINE | DECLINE | ML/AI SaaS tool subscription for patent search and tech transfer. No GIS; SpatialGIS has no such product. |
| 5 | USDA – Laboratory Support | SV_a3l5LoocjFjyGpM | 07/14/2026 | DECLINE | DECLINE | Staffing for 1 laboratory scientist + 2 laboratory technicians (physical/biological lab). Non-IT staffing — decline keyword category. |
| 6 | TREAS – NETCOM – CS2100 PRI Provisioning & PSAP Routing Config | SV_0v6jTKLgV3iRXuu | 07/29/2026 | PASS* | DECLINE | FALSE POSITIVE: Script matched "routing" in "PSAP routing." Actual scope is CS2100 telephony switch PRI circuit integration + 911 call routing config. Specialized telecom engineering. |
| 7 | EPA – Information Management Program Support Services | SV_1AAyN7TUQGwMdSu | 07/24/2026 | MAYBE* | DECLINE | FALSE POSITIVE: Script matched "program support." Actual scope requires Nuxeo ECM development + ICR policy writing + NARA records management. None in SpatialGIS capability profile. |
| 8 | DHS USCG – Geospatial Support Services CG | SV_0k66braHPB9ARYW | — | PASS | SUBMITTED-CONFIRMED | TRUE PASS — "geospatial" match confirmed in subject. Already submitted by prior pipeline run at 2026-07-10T00:16:09Z. |

*Script produced 2 PASS + 1 MAYBE — human review overrides 2 to DECLINE (telecom false positives) and 1 to DECLINE (records management false positive). DHS USCG PASS stands but is already submitted.

---

## Reminders — All DECLINE / No Change

| Subject | Slug | Prior Decision | Due |
|---------|------|----------------|-----|
| USACE – Professional Support Services | usace-professional-support-services | DECLINE (ongoing) | 07/22/2026 |
| HHS – CHIP Support and Expand Health Policy Data and Analytic | hhs-chip-support-and-expand-health-policy-data-and-analytic | DECLINE (07-07) | Unknown |
| HHS NIH – Laboratory Information Management System (LIMS) | hhs-nih-laboratory-information-management-system-lims | DECLINE (07-01) | Unknown |
| Army – CMAOD Admin Services Support | army-cmaod-admin-services-support | DECLINE (ongoing) | Unknown |

No change in any reminder classification. USACE Professional Support Services reminder is for a different RFI (SV_7UR3Bl0IblluFHo) from the earlier `usace-usace-professional-support-services` submission — no action required on the reminder.

---

## Cumulative Submission Inventory (29 total, all SUBMITTED-CONFIRMED)

Prior inventory was 24 as of 2026-07-09 queue. Today adds 5 confirmed from the overnight pipeline run:

| # | Opportunity | Survey | Confirmed |
|---|-------------|--------|-----------|
| 25 | DHS USCG – Geospatial Support Services CG | SV_0k66braHPB9ARYW | 2026-07-10 00:16 UTC |
| 26 | Navy – ServiceNow SPM Implementation | SV_3K0r4amFteBLdzw | 2026-07-10 00:15 UTC |
| 27 | Navy – ServiceNow HRSD Implementation | SV_3pFLlaMni34FuLQ | 2026-07-10 00:14 UTC |
| 28 | Army – Management Support Services | SV_dd6Nk6SvxktXy7Q | 2026-07-10 00:13 UTC |
| 29 | DOJ DEA – Spectrum ACR & Video Surveillance Program | SV_aawsKmxuedNyClo | 2026-07-10 00:13 UTC |

For full prior inventory (1–24), see `working/mras-inbox/daily-queue-2026-07-09.md`.

---

## Summary

No new opportunities passed triage today. 12 RFI threads processed (8 new, 4 reminders) — all DECLINE after human review.

The triage script produced 2 PASS and 1 MAYBE, all of which were overridden:
- **TREAS CS2100** (PASS via "routing"): telecom switch engineering, not GIS network analysis
- **EPA Info Mgmt** (MAYBE via "program support"): Nuxeo/NARA records management, not IT professional services
- **DHS USCG Geospatial** (PASS via "geospatial"): true match, already submitted by prior run

5 prior submissions confirmed via response receipts today, bringing running total to **29 SUBMITTED-CONFIRMED**.

No carry-forward items or open BLOCKED items.

**No action required.**
