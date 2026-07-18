# MRAS Daily Queue — 2026-07-18

**Run summary:** 8 threads received | 0 submitted | 0 blocked | 7 declined | 1 MAYBE (needs user review)  
**Active PASS items: 0** — No new submissions required today.

---

## New RFIs (4)

| Slug | Subject | Due | Triage | Rationale |
|------|---------|-----|--------|-----------|
| `gsa-ocas-fedhub-managed-service-office-mso-operations` | GSA OCAS — FedHub Managed Service Office (MSO) Operations | 07/31/2026 | **DECLINE** | FedHub/XMS is a federal procurement/contract lifecycle management platform. Scope = PMO support for HHS implementation of FedHub/XMS. Acquisition system management — no GIS/spatial component. SpatialGIS has no XMS experience. |
| `dhs-uscg-strategic-services` | DHS USCG — Strategic Services | 07/24/2026 | **DECLINE** | USCG CIO organizational gap analysis + strategic consulting + executive staff support. Management consulting / organizational strategy — no IT or GIS component. SpatialGIS is a technical GIS firm, not a management consultancy. |
| `doj-bop-training-and-support-services-fsa-time-credit-administration` | DOJ BOP — Training and Support Services FSA Time Credit Administration | 07/23/2026 | **DECLINE** | First Step Act (FSA) time credit administration — oversight, validation, software development support, training, QA for BOP corrections IT. Specialized justice/corrections domain. No GIS component. SpatialGIS has no BOP/corrections-system experience. |
| `doj-ousa-professional-it-support-services` | DOJ OUSA — Professional IT Support Services | 07/24/2026 | **MAYBE** | SQL Server 2019 database analytics, report generation for US Attorneys Offices (EOUSA). Touches SpatialGIS IT capabilities (NAICS 541511/541512; data analytics keyword). No GIS component. Email body truncated — full scope unclear. See human review note below. |

---

## Reminders (4) — All DECLINE

| Slug | Subject | Prior Classification | Notes |
|------|---------|---------------------|-------|
| `gsa-aas-calm-recompete` | GSA AAS — CALM Recompete | DECLINE (07/17) | Contract Administration & Lifecycle Management — acquisition support. No action. |
| `hhs-cms-crm-enterprise-transformation-and-system-testing` | HHS CMS — CRM Enterprise Transformation & System Testing | DECLINE (07/17) | CRM platform + healthcare IT. No GIS. No action. |
| `navy-ssp-personnel-reliability-program-prp-administration-market-research` | Navy SSP — Personnel Reliability Program (PRP) Administration | DECLINE (07/17) | Personnel security administration. No action. |
| `usaf-jblm-premise-wiring-bldg-12` | USAF — JBLM Premise Wiring Bldg 12 | DECLINE (first seen today as reminder) | Building premise wiring/cabling infrastructure. Facilities/construction — outside SpatialGIS scope. No action. |

---

## Human Review Items

### MAYBE: DOJ OUSA — Professional IT Support Services
**Slug:** `doj-ousa-professional-it-support-services`  
**Survey URL:** `SV_0JQQzmimQF4B9TU`  
**Due:** 07/24/2026 (6 days remaining)  
**Full scope snippet from email:** "The Contractor shall provide support services to assist Data Integrity and Analysis in developing and generating reports and analyses on the USAOs' data. The data is stored in Microsoft SQL Server 2019 databases and is accessible using SQL, PL/SQL, and T-SQL. In addition, EOUSA utilizes the United S..." (truncated in email)  
**Why MAYBE:** Data integrity, SQL analytics, report generation aligns with SpatialGIS's IT capabilities. EOUSA (Executive Office for US Attorneys) uses case management systems — likely LCMS or similar. No GIS component visible, but if the full survey reveals data management/analytics emphasis and SIN 54151S is acceptable, this could be viable.  
**Recommendation:** Review the full Qualtrics survey to see if scope extends to a case management system that has geospatial or data analytics components. If purely legal case data with no IT infrastructure angle, DECLINE. If approve, note due date is 07/24 — would need to move quickly.

---

## Pipeline Status

- **Submitted today:** 0
- **BLOCKED-NEEDS-USER:** 0
- **REJECTED-BY-QUALTRICS:** 0
- **MAYBE-NEEDS-USER:** 1 (`doj-ousa-professional-it-support-services`, due 07/24)
- **Total submitted to date (all-time):** 24

*Next run: 2026-07-19*
