# MRAS Daily Queue — 2026-07-05

**Run date:** 2026-07-05  
**Gmail query:** `from:rfi@research.gsa.gov newer_than:1d`  
**Inbox count:** 0 (Independence Day federal holiday — GSA did not send MRAS RFIs on 2026-07-04)  
**Unique after dedup:** 0  
**Triage result:** PASS=0 | MAYBE=0 | DECLINE=0  
**Submitted this run:** 0  
**Blocked for human review:** 0 new (2 carry-forward from 2026-07-03 remain open)

---

## Today's Batch

No new emails received. July 4, 2026 (Independence Day) was a federal holiday; GSA does not send MRAS RFIs on holidays.

---

## Carry-Forward: Open BLOCKED Items — ACTION REQUIRED

### 1. DOJ DEA - EPIC General Watch Modernization ⚠️ URGENT — CLOSES TOMORROW

- **Slug:** `doj-dea-epic-general-watch-modernization`
- **Agency:** DOJ / Drug Enforcement Administration / El Paso Intelligence Center (EPIC)
- **Due:** 2026-07-08 — **TODAY (07/05) IS THE LAST PRACTICAL DAY TO RESPOND**
- **Survey URL:** https://feedback.gsa.gov/jfe/form/SV_8uGEum6wf3K7NIO
- **Status:** BLOCKED-NEEDS-USER
- **Fit assessment:** MAYBE. IT system modernization for a drug intelligence watch center. DEA/EPIC mission involves multi-source data fusion and intelligence analysis that could have a geospatial component, but the email body did not explicitly name GIS, mapping, or data analytics.
- **What Kendrick must do today:**
  1. Open the Qualtrics survey at the URL above.
  2. Check QID10 for required NAICS — if 541511/541512/541519/541370 are listed, SpatialGIS qualifies.
  3. Check QID8 for required SIN — if MAS 54151S is accepted, proceed.
  4. Read the capability questions — if geospatial analysis, data analytics, or IT modernization/UX are explicitly asked, this is PASS.
  5. If PASS: respond by running `mras_discover.py` and drafting the capability statement. Survey closes 07/08; allow at least one day for review before submitting.
  6. If the survey reveals watch-floor application development only (no GIS/analytics): decline.
- **If no action today:** window closes 07/08; any response after that will be rejected by Qualtrics.

---

### 2. OSW - DCSA - Enterprise Asset Management Service (E-AMS)

- **Slug:** `osw-dcsa-enterprise-asset-management-service-e-ams`
- **Agency:** Defense Counterintelligence and Security Agency (DCSA)
- **Due:** 2026-07-15 — 10 days remaining
- **Survey URL:** https://feedback.gsa.gov/jfe/form/SV_en58ME1dyaPqWLY
- **Status:** BLOCKED-NEEDS-USER
- **Fit assessment:** MAYBE. IT asset lifecycle management (software + hardware, needs analysis through disposal). NAICS 541511/541512/541519 plausible. DCSA is a cleared agency — security clearance and CMMC certification tier unknown.
- **What Kendrick must do:**
  1. Open the Qualtrics survey at the URL above.
  2. Check clearance requirement — if Secret/TS/SCI workforce required, SpatialGIS must confirm cleared staff availability.
  3. Check CMMC requirement — if CMMC L2 *Certified* (C3PAO-certified) is required, this is BLOCKED until SpatialGIS holds certification. CMMC L2 *Aligned* (current posture) is acceptable for bid but must not be misrepresented as certified.
  4. Check NAICS/SIN — confirm MAS 54151S is accepted.
  5. If all clear: flip to PASS and run the pipeline (mras_discover.py → capability draft → mras_map_answers → mras_submitter dry-run → submit).
- **Practical deadline for decision:** 2026-07-12 (3 days before close — allows 3 days for draft, review, submit).

---

## Prior Submission Inventory (22 total, all SUBMITTED-CONFIRMED)

| Slug | Status |
|------|--------|
| army-real-property-remediation-support-services | SUBMITTED-CONFIRMED |
| dhs-uscg-program-management-and-analysis | SUBMITTED-CONFIRMED |
| doc-nist-uncrewed-aircraft-system-uas-stakeholder-workshop | SUBMITTED-CONFIRMED |
| doi-blm-national-travel-management-planning-tmp-bpa | SUBMITTED-CONFIRMED |
| doi-secure-ai-assistant-for-final-agency-decisions-fad | SUBMITTED-CONFIRMED |
| doj-atf-hrpd-modernized-case-management-system | SUBMITTED-CONFIRMED |
| doj-fbi-dssu-program-support | SUBMITTED-CONFIRMED |
| hhs-cdc-technical-support-for-vehss | SUBMITTED-CONFIRMED |
| hhs-change-management-support | SUBMITTED-CONFIRMED |
| navy-information-technology-governance-and-mission-support-itgms | SUBMITTED-CONFIRMED |
| navy-navsea-contract-support-services | SUBMITTED-CONFIRMED |
| treas-irs-international-tax-modeling-tool-imit | SUBMITTED-CONFIRMED |
| usace-foia-support | SUBMITTED-CONFIRMED |
| usace-mpbi-data-analytics-support | SUBMITTED-CONFIRMED |
| usace-usace-professional-support-services | SUBMITTED-CONFIRMED |
| usaf-acc-a5-8-9-information-technology-lan-and-security-support | SUBMITTED-CONFIRMED |
| usaf-daf-damage-assessment-management-office-damo | SUBMITTED-CONFIRMED |
| usaf-fire-emergency-information-management | SUBMITTED-CONFIRMED |
| usaf-usafa-donor-funds-management-it-ecosystem | SUBMITTED-CONFIRMED |
| usmc-infads-professional-services-contract | SUBMITTED-CONFIRMED |
| usmc-mcsc-wargaming-capability-software-integration-services | SUBMITTED-CONFIRMED |
| va-va-ams-data-governance-standardization | SUBMITTED-CONFIRMED |

---

## Summary

No new MRAS opportunities today (federal holiday). Pipeline is healthy — 22 submissions on record.

**Immediate action required:** The DEA EPIC watch modernization RFI closes 2026-07-08. Today is the last practical day to review the survey and decide. Open `SV_8uGEum6wf3K7NIO` now and reply to this session with the scope findings so the capability statement can be drafted and submitted before the window closes.
