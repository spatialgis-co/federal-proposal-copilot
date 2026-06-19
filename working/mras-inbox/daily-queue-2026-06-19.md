# MRAS Daily Queue — 2026-06-19

**Run date:** 2026-06-19  
**Emails pulled:** 9 (from:rfi@research.gsa.gov newer_than:1d)  
**Unique after dedup:** 9 (no duplicates or prior-submitted slugs removed)  
**Triage result:** PASS=0 | MAYBE=1 | DECLINE=8  
**Submitted today:** 0  
**Rejected:** 0  
**Blocked:** 0  
**Needs human review:** 1 (MAYBE)

---

## PASS — 0 items

No opportunities met core capability criteria today.

---

## MAYBE — 1 item (needs human review — not auto-submitted)

### USMC - MCSC - Wargaming Capability Software Integration Services

| Field | Value |
|-------|-------|
| **Agency** | USMC Marine Corps Systems Command (MCSC) |
| **Type** | NEW RFI (not a reminder) |
| **Due date** | 2026-07-07 |
| **Survey URL** | SV_07YYaZbqYgm2jkO |
| **Triage keyword** | "Azure" (broad IT) |
| **Slug** | `usmc-mcsc-wargaming-capability-software-integration-services` |

**Description from email:**  
> The Contractor shall serve as the Prime Systems Integrator responsible for the design, provisioning, deployment, and integration of the simulation software within a Government-designated Azure Cloud environment. Software licenses will be provided as Government Furnished Software (GFS).

**Fit analysis:**  
SpatialGIS holds NAICS 541511/541512/541519, which cover custom software development and computer systems design — both on-contract for this type of work. The scope is Azure cloud provisioning and software integration, not domain-specific simulation expertise per se. Software licenses are GFS (government-furnished), so the contractor role is integration and deployment, not simulation development.

**Why MAYBE and not PASS:**  
No GIS/geospatial keyword in subject or description. The "wargaming" and "simulation" context signals MCSC defense domain — the survey may require defense-specific qualifications, ITAR registration, or specialized wargaming tool experience that SpatialGIS cannot claim. The email body alone is insufficient to assess NAICS fit, required SINs, or domain certifications.

**Why not DECLINE:**  
Azure cloud integration (design, provisioning, deployment) is directly within SpatialGIS's IT professional services capability. Due date is 07/07 — 18 days out. Worth a quick survey discovery pass before declining.

**Recommended action:**  
Run `python3 scripts/mras_discover.py --survey-url 'https://feedback.gsa.gov/jfe/form/SV_07YYaZbqYgm2jkO' --opportunity-id usmc-mcsc-wargaming-capability-software-integration-services` to fetch the full QID structure, NAICS requirement, and any DRD. Then decide: if NAICS is 541511/541512 and no simulation domain cert is required, escalate to PASS and draft. If defense-simulation-specific quals are required that SpatialGIS lacks, confirm DECLINE.

**Status:** MAYBE — awaiting human decision before any prep or submission.

---

## DECLINE — 8 items

### Reminders (no prior PASS decision)

| # | Subject | Slug | Due | Decline Reason |
|---|---------|------|-----|----------------|
| 1 | Reminder: DHS CBP - Apache ActiveMQ Escalation Support Services | `dhs-cbp-apache-activemq-escalation-support-services` | 2026-06-23 | Dedicated toll-free service desk for Apache ActiveMQ middleware — specialized product support not in SpatialGIS's scope; no keyword match |
| 2 | Reminder: NMB - DUO/EID PIV Multi-Factor Authentication Support | `nmb-duo-eid-piv-multi-factor-authentication-support` | 2026-06-22 | Cisco Duo / eID Authenticate license provisioning and Tier III support — MFA product license resale; not SpatialGIS's scope |
| 3 | Reminder: HHS - Okta Licenses | `hhs-okta-licenses` | 2026-06-24 | Okta Cell Add-On license renewal — product resale; not SpatialGIS's scope |
| 4 | Reminder: DOC NIST - Boulder, CO Data Center Co-Location | `doc-nist-boulder-co-data-center-co-location` | 2026-06-26 | Physical data center co-location (HPC, 250kW, liquid cooling); not IT professional services |
| 5 | Reminder: DHS USCG - Boating Safety Public Health Effort | `dhs-uscg-boating-safety-public-health-effort` | 2026-06-23 | Public health epidemiology (NEMSIS, NSSP, ESSENCE), boating safety, non-profit partnerships — no geospatial / GIS component; note: "geographic hotspots" mentioned in Q5 but dominant scope is clinical epidemiology outside SpatialGIS's declared capability |
| 6 | Reminder: DOC NIST - Gaithersburg, MD Data Center Co-Location | `doc-nist-gaithersburg-md-data-center-co-location` | 2026-06-22 | Physical data center co-location (HPC, 250kW, liquid cooling); not IT professional services |
| 7 | Reminder: USAF - Vehicular Portable Scales and Cargo Measuring System | `usaf-vehicular-portable-scales-and-cargo-measuring-system` | 2026-06-23 | Physical hardware procurement (weigh-in-motion scales, cargo measuring system); not IT/GIS |
| 8 | Reminder: USMC - MCSC - Software License and On-Site support | `usmc-mcsc-software-license-and-on-site-support` | 2026-06-19 | Vague ("3 separate software licenses") + closes today; no keyword match; insufficient detail to assess fit |

---

## Summary

One new RFI arrived today — USMC MCSC Wargaming Software Integration (due 07/07/2026) — classified MAYBE. Triage scored it on the "Azure" keyword; actual fit depends on the survey's NAICS requirement and whether the scope calls for defense-simulation domain expertise SpatialGIS does not hold. Discovery is recommended before committing.

All 8 reminders are outside SpatialGIS's core scope (product licenses, physical data center, hardware, specialized middleware support, clinical public health). No submissions made today.

**Cumulative submitted opportunities:** 14 (unchanged from 2026-06-18)
