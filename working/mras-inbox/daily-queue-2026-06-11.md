# MRAS Daily Queue — 2026-06-11

**Run date:** 2026-06-11  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads (last 24 h):** 5  
**After dedup:** 5 unique (0 removed)  
**New RFIs processed:** 0 (all 5 are reminders)  
**Submitted today (auto):** 0  
**Rejected by Qualtrics:** 0  
**Blocked (needs user):** 0 new  
**Declined today:** 5 reminders  

> **Infrastructure note (persistent):** Outbound network access to `feedback.gsa.gov` is blocked by the cloud execution environment's network policy. `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics survey URLs from this environment. All QID discovery and form submission must be performed from a local machine or an environment with unrestricted outbound access.

---

## REMINDERS — DECLINED (5)

### 1. USMC MCSC — Software License and On-Site Support *(repeat)*
| Field | Value |
|---|---|
| Thread | `19eb0fc68b38bf26` |
| Slug | `usmc-mcsc-software-license-and-on-site-support` |
| Agency | U.S. Marine Corps / MCSC |
| Due Date | **2026-06-19** — 8 days remaining |
| First seen | 2026-06-09 (new RFI), DECLINE |
| Status | **DECLINED** — repeat reminder |

**Decline rationale:** Procurement of 3 unspecified software licenses + maintenance/support. No GIS/geospatial content identified. SIN 54151S does not cover generic software resale without a clear product fit.

> **Note for Kendrick:** Due 2026-06-19. If you know which 3 software products MCSC is buying and they include geospatial/ESRI software, manually review the survey. Survey URL from 2026-06-10 queue.

---

### 2. HHS — Program Monitoring and Evaluation Support Services *(repeat)*
| Field | Value |
|---|---|
| Thread | `19eb0fc4336bbfae` |
| Slug | `hhs-program-monitoring-and-evaluation-support-services` |
| Agency | HHS |
| Due Date | **2026-06-17** — 6 days remaining |
| First seen | 2026-06-09 (new RFI), DECLINE |
| Status | **DECLINED** — repeat reminder |

**Decline rationale:** Public health program monitoring and evaluation. No explicit geospatial content. SpatialGIS cannot substantiate program M&E expertise for public health outbreak response.

> **Note for Kendrick:** Due 2026-06-17. If SpatialGIS has health-related geospatial analytics work (disease mapping, spatial epidemiology), manually review the survey before 2026-06-14. Survey URL from 2026-06-10 queue.

---

### 3. DOC NIST — Federal Credit, Portfolio, and Financial Mgmt. *(repeat)*
| Field | Value |
|---|---|
| Thread | `19eb0fbda0a4b348` |
| Slug | `doc-nist-federal-credit-portfolio-and-financial-mgmt` |
| Agency | DOC / NIST |
| Due Date | Unknown (hard-declined on keyword) |
| First seen | 2026-06-06, DECLINE |
| Status | **DECLINED** — hard-decline keyword: `financial management` |

**Decline rationale:** Federal financial management services. Hard-decline keyword match. Outside SpatialGIS's scope.

---

### 4. DHS CBP — Information Technology Refresh Program (ITRP) Support *(NEW)*
| Field | Value |
|---|---|
| Thread | `19eb0fa3b5296244` |
| Slug | `dhs-cbp-information-technology-refresh-program-itrp-sup` |
| Agency | DHS / U.S. Customs and Border Protection |
| Survey ID | `SV_2t8nPOH7txaVaRw` |
| Due Date | **2026-06-18** — 7 days remaining |
| First seen | Today (this run) |
| Status | **DECLINED** — no capability keyword match |

**Requirement:** End-user device lifecycle management and hardware procurement support for CBP's enterprise IT refresh. Scope includes desktops, laptops, non-cellular tablets, peripherals, network devices, and mobile devices — approximately 24,700 devices replaced annually. Services: Program Management, Storefront Capability, Lifecycle Management, Hardware Procurement Assistance, Asset Management, Hardware Prep for Deployment, Infrastructure and Endpoint Management.

**Decline rationale:** Hardware procurement and endpoint management program for ~24,700 consumer-tier devices annually. This is a large-scale IT reseller / logistics / asset management engagement. SpatialGIS is a GIS professional services firm with no hardware procurement, warehousing, device imaging, or large-scale endpoint management infrastructure. No GIS/geospatial angle. Responding would require claiming hardware fulfillment capabilities SpatialGIS does not hold.

---

### 5. DHS CISA — IT Research and Support Services *(NEW)*
| Field | Value |
|---|---|
| Thread | `19eb0f9d23fa1d91` |
| Slug | `dhs-cisa-it-research-and-support-services` |
| Agency | DHS / Cybersecurity and Infrastructure Security Agency |
| Survey ID | `SV_9vRIeIONIz7sgzY` |
| Due Date | **2026-06-12** — **1 day remaining** |
| First seen | Today (this run) |
| Status | **DECLINED** — no capability keyword match |

**Requirement:** Licensed access for 7 users to an existing online IT research database (Gartner/Forrester-type) providing insight into IT products, services, processes, metrics, and roles/functions. Executive-level research and advice on CTO/CIO-level challenges.

**Decline rationale:** Software subscription procurement for a commercial IT research/analyst database (likely Gartner, Forrester, or similar). SpatialGIS is a GIS professional services provider, not a software reseller or IT research database vendor. Cannot offer a Gartner-style research subscription. No GIS relevance. Survey closes tomorrow — no action warranted.

---

## PIPELINE SUMMARY

| Category | Count |
|---|---|
| Total threads pulled | 5 |
| After dedup | 5 |
| All reminders (no new RFIs) | 5 |
| PASS | **0** |
| MAYBE | **0** |
| DECLINE | **5** |
| Submitted today (auto) | **0** |
| Rejected by Qualtrics | **0** |
| Newly BLOCKED-NEEDS-USER | **0** |
| Carried forward BLOCKED | 1 (DOI FAD, due 2026-06-17) |

---

## ACTION ITEMS FOR KENDRICK

1. **URGENT — Decision needed by TODAY (2026-06-11):** DOI FAD AI Assistant (due 2026-06-17). The 2026-06-09 queue flagged this as BLOCKED-NEEDS-USER — requires a named Microsoft Power Platform teaming partner. Decision deadline is today to allow manual pipeline execution before close. Survey URL in the 2026-06-09 and 2026-06-10 queues.

2. **Optional — USMC MCSC Software License (due 2026-06-19):** Second reminder received. If you know the 3 software products and they're geospatial, manually review before 2026-06-16. Survey URL in 2026-06-10 queue.

3. **Optional — HHS Program M&E (due 2026-06-17):** Second reminder received. Manually review if SpatialGIS has public health GIS work to cite. Survey URL in 2026-06-10 queue.

4. **Housekeeping:** Add stub fill-reports (`submitted: true`) to `working/mras-runs/` for any MRAS RFIs Kendrick submitted manually (USAF USAFA Donor Funds, DOJ FBI DSSU, USAF Fire & Emergency) so dedup stops flagging reminders as new candidates.

5. **Environment (persistent):** Configure outbound access to `*.gsa.gov` or run MRAS pipeline locally to enable automated QID discovery and submission.
