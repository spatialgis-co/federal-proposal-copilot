# MRAS Daily Queue — 2026-08-01

**Threads received:** 12 (7 new, 5 reminders)  
**Triage results:** PASS=0 | MAYBE=4 | DECLINE=8 | SKIP_CLOSED=0  
**Submitted:** 0 | Rejected: 0 | Blocked: 0

---

## No PASS Items Today

No opportunities reached the PASS bucket. No capability statements drafted, no automated submissions attempted.

---

## MAYBE — Needs Human Review

All 4 MAYBE items are keyword false-positives on generic terms ("reporting", "program support", "technical support", "AWS"). None have a genuine GIS/geospatial/IT-services fit for SpatialGIS. Documented here for awareness.

---

### MAYBE-1 — OMB EOP - Verification & Validation Process Improvement
- **Slug:** `omb-eop-verification-validation-process-improvement`
- **Agency:** OMB / Office of Federal Procurement Policy (OFPP)
- **Due:** 08/19/2026
- **Survey ID:** SV_dnCSNNVXk3XPusu
- **Triage keyword:** "reporting"
- **Actual requirement:** Technical solution to address V&V for Federal Procurement Data System (SAM.gov) reporting — data quality/validation for federal acquisition data.
- **SpatialGIS fit:** None. This is procurement data validation, not geospatial or SpatialGIS's IT services portfolio. "Reporting" keyword match is false-positive.
- **Recommended action:** No response. If Kendrick sees a fit (e.g., data validation capability), manual browser submission possible at https://feedback.gsa.gov/jfe/form/SV_dnCSNNVXk3XPusu by 08/19.

---

### MAYBE-2 — DOE - Operation Program Support Services (OPSS)
- **Slug:** `doe-operation-program-support-services-opss`
- **Agency:** DOE / National Nuclear Security Administration (NNSA)
- **Due:** 08/18/2026
- **Survey ID:** SV_cAuX8bt3iBsn9xs
- **Triage keyword:** "program support", "technical support"
- **Actual requirement:** Decentralized BPA for NNSA covering administrative, management, acquisition, program analysis, human capital management, and technical support services — broad program support contract.
- **SpatialGIS fit:** None. Primary scope is administrative and management support, not IT/GIS. "Technical support" keyword match is false-positive for a broad admin BPA.
- **Recommended action:** No response.

---

### MAYBE-3 — ED - Presidential Scholars Program Support Services
- **Slug:** `ed-presidential-scholars-program-support-services`
- **Agency:** Department of Education
- **Due:** 08/05/2026 (**Wednesday — 4 days away**)
- **Survey ID:** SV_1SMkXmjq5JOAknA
- **Triage keyword:** "program support"
- **Actual requirement:** Technical and logistical support for identifying and recognizing ~161 Presidential Scholars from 6,000 eligible students — event planning and program administration.
- **SpatialGIS fit:** None. This is program/event logistics, not IT or GIS. "Program support" match is false-positive.
- **Recommended action:** No response.

---

### MAYBE-4 — GSA - CALM Recompete 2 *(REMINDER — due in 3 days)*
- **Slug:** `gsa-calm-recompete-2`
- **Agency:** GSA (Contracting & Acquisition Lifecycle Management)
- **Due:** 08/04/2026 (**Monday — 3 days away**)
- **Survey ID:** SV_4N460bmDFtELsRU
- **Email type:** REMINDER (follow-on to RFI1823959)
- **Triage keyword:** "AWS"
- **Actual requirement:** Software licensing and Help Desk support for PRISM (acquisition system), Bizagi (BPM), AWS, and stackArmor — specific product licenses for GSA's contracting systems.
- **SpatialGIS fit:** None. SpatialGIS does not hold PRISM, Bizagi, or stackArmor product licenses and doesn't provide help desk for these specific GSA acquisition tools. "AWS" match is false-positive (SpatialGIS uses AWS but doesn't resell/support for these specific products).
- **Recommended action:** No response.

---

## DECLINE Summary (8 items)

| Slug | Agency | Due | Reason |
|------|--------|-----|--------|
| hhs-acf-child-welfare-technology-solutions-and-services | HHS / ACF | 08/13 | No keyword match — child welfare case mgmt, not GIS |
| usace-cenwd-collaborative-partnering | USACE CENWD | 08/10 | No keyword match — stakeholder/governance consulting |
| doe-cyber-security-information-support-services | DOE | 08/10 | No keyword match — IT support, no GIS component |
| doc-noaa-education-scholarship-support-services | DOC / NOAA | 08/07 | Hard-decline: "financial management" + event planning |
| army-adn-mcn-fiber-install | Army | 08/07 | No keyword match — fiber optic cable installation |
| treas-irs-remote-desktop-support-app-software-licensing | TREAS / IRS | 08/05 | Hard-decline: "treasury" + software product licensing |
| hhs-npdb-customer-service-program-operations | HHS | 08/05 | No keyword match — call center / web content |
| gsa-ocas-oracle-primavera-p6-software-licenses | GSA OCAS | 08/04 | No keyword match — Oracle Primavera P6 product licensing |

---

## Prior Open Items

- **treas-irs-qualified-opportunity-zones-reporting** (QOZ, due 07/28/2026) — **NOW EXPIRED.** This MAYBE item from the 07/25–07/26 queues was not acted on. Deadline has passed.

---

## Pipeline Status

- **Proxy block:** `feedback.gsa.gov:443` remains unreachable from this automated environment (ongoing since 07/23). All PASS items requiring `mras_discover.py` or `mras_submitter.py` will require manual browser submission until the network policy is updated.
- **Prior submitted count:** 24 opportunities submitted to date (see `working/mras-runs/`).
- **OK_TO_SUBMIT:** Remains true (blanket authorization; no reset per protocol).
