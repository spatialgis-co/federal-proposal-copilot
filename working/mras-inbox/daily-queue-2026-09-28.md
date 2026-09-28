# MRAS Daily Queue — 2026-09-28

**Run date:** 2026-09-28  
**Emails pulled:** 2  
**After dedup:** 2 unique  
**PASS:** 0 | **MAYBE:** 0 | **DECLINE:** 2 | **Submitted:** 0 | **Blocked:** 0

---

## DECLINE — Human Review Recommended

### 1. GSA ASD — Hermes
- **Thread ID:** 1a0e4f6b4c2cdc3d
- **Subject:** GSA ASD - Hermes - MRAS
- **Agency:** GSA (Assisted Acquisition Service / ASD — Hermes)
- **Due:** 2026-10-09
- **Survey URL:** `https://feedback.gsa.gov/jfe/form/SV_bOxhwGzyqlglWmO`
- **Triage:** DECLINE — No GIS/geospatial keyword match
- **Requirement summary:** IT Operations and Maintenance (O&M) and Development, Modernization, and Enhancement (DME) services for the Conexus and Network Hosting Center (NHC) systems, which support telecommunications purchases from GSA's Enterprise Infrastructure Solutions (EIS) contract. ~500 users across Federal, Tribal, and non-governmental agencies.
- **Fit assessment:** The requirement is for general IT O&M/DME on a specific telecom management system — no geospatial or spatial analytics component stated. SpatialGIS holds NAICS 541511/541512 which would technically fit, but the work is telecom-infrastructure management, not GIS services.
- **Recommendation:** Likely out of scope. Review survey form before final call — if the Qualtrics questions are broadly IT professional services (not telecom-specific), SpatialGIS could respond under IT services SIN 54151S. Due 10/09; human review by 10/07.

---

### 2. DOS — Website Support Services
- **Thread ID:** 1a0e3d88dbaf156a
- **Subject:** DOS - Website Support Services - MRAS
- **Agency:** Department of State (DT/CST)
- **Due:** 2026-10-08
- **Survey URL:** `https://feedback.gsa.gov/jfe/form/SV_bQOVRnI3wC4DBye`
- **Triage:** DECLINE — No GIS/geospatial keyword match
- **Requirement summary:** Full-range website support services for State Dept DT/CST environment: Tier III/IV support, cloud services for external-facing sites, alignment with DT/CST Enterprise Architecture and modernization. Place of performance: SA-17, 600 19th St NW, Washington DC and contractor sites within 30-mile radius.
- **Fit assessment:** General website O&M and cloud services. "Cloud services" is a capability MAYBE keyword. No GIS component stated. This is Tier III/IV web infrastructure management — outside SpatialGIS's core geospatial lane. Could potentially respond if survey questions are IT professional services generalist, but the near-Washington DC place of performance and Tier III/IV specialization likely require dedicated web/cloud vendor relationships.
- **Recommendation:** Borderline MAYBE — the cloud services angle is a soft match. Review survey form; if the questions allow a generalist IT services vendor without Tier III/IV proprietary system knowledge, reconsider. Due 10/08; human review by 10/06.

---

## Notes

- Both opportunities were classified DECLINE by `mras_triage_classify.py` (no PASS keyword match in email body text). The script operates on brief email text only, not the full Qualtrics survey. Both *could* be MAYBE based on general IT keyword overlap; human should review the survey forms linked above before final decision.
- No Qualtrics surveys were fetched (PASS-only step).
- No capability statements drafted.
- OK_TO_SUBMIT status: unchanged (true — blanket authorization in effect).
