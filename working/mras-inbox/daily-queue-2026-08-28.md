# MRAS Daily Queue — 2026-08-28

**Run time:** 2026-08-28 (automated)
**Inbox search:** `from:rfi@research.gsa.gov newer_than:1d`
**Threads received:** 32
**New RFIs (unsubmitted):** 2
**New RFIs (already submitted via prior run):** 4
**Response confirmations:** 17
**Reminders:** 8
**Other:** 1

**Triage summary (after dedup → 23 unique):** PASS=0 | MAYBE=0 | DECLINE=23 | SKIP_CLOSED=0
**Submissions today:** 0
**Blocked today:** 0

---

## New RFIs — 2 Unsubmitted (Both DECLINE)

### 1. USAF — MEDXS Clinical IT Support Services

| Field | Value |
|-------|-------|
| Thread ID | `1a04585c071a019b` |
| Date received | 2026-08-27T23:19:47Z |
| Slug | `usaf-medxs-clinical-it-support-services` |
| Agency | USAF / Air Force Medical Service |
| Survey ID | SV_2tR7iU55c9MvUCG |
| Survey URL | https://feedback.gsa.gov/jfe/form/SV_2tR7iU55c9MvUCG |
| Due Date | **2026-09-02** |
| Triage | **DECLINE** |

**Requirement description:**
> The Air Force seeks market capability for MEDXS Clinical IT Support under GSA SIN 54151HEAL (Health IT), 54151S, and 54151HACS. Key focus is clinical/medical systems integration, onboarding key personnel, and executing a seamless, low-risk transition-in within a strict 60-calendar-day timeline on an FFP basis.

**Triage rationale:**

| Factor | Assessment |
|--------|------------|
| Core scope | Clinical/medical IT systems integration for the Air Force Medical Service — electronic health records, clinical workflows, patient-facing systems |
| Required SINs | **54151HEAL** (SBA Health IT SIN) + **54151HACS** (SBA High-Value Asset Cybersecurity SIN) + 54151S — SpatialGIS holds **only 54151S** |
| Guardrail block | `never_claim_heal_sin: true` + `never_claim_hacs_sin: true` — cannot claim either required SIN |
| NAICS match | Healthcare IT maps to NAICS 541511/541512, but clinical focus places it in 621999/519xxx territory — not SpatialGIS's SAM-registered portfolio in spirit or substance |
| GIS/IT nexus | None — no geospatial, spatial, or data analytics keywords; entirely clinical/medical domain |
| Keyword match | "clinical" matches hard-decline keyword list ("clinical", "healthcare IT") |
| Capability fit | SpatialGIS has no documented clinical systems integration, EHR/EMR, or healthcare IT experience |

**Decision: DECLINE.** Hard guardrail blocks apply (54151HEAL and 54151HACS not held). Even setting SIN constraints aside, clinical medical IT systems integration is outside SpatialGIS's core GIS/geospatial professional services portfolio. No capability statement prepared.

---

### 2. Army — Support Services for Government Owned Audio/Visual

| Field | Value |
|-------|-------|
| Thread ID | `1a04540228b734a2` |
| Date received | 2026-08-27T22:03:45Z |
| Slug | `army-support-services-for-government-owned-audio-visual` |
| Agency | U.S. Army / Operations Garrison HQ |
| Survey ID | SV_5vYxXR0yC4Q6OfI |
| Survey URL | https://feedback.gsa.gov/jfe/form/SV_5vYxXR0yC4Q6OfI |
| Due Date | **2026-09-04** |
| Triage | **DECLINE** |

**Requirement description:**
> The purpose of this requirement is to obtain contractor support services for Government-owned audio/visual (A/V), video teleconferencing (VTC), and unified communications (UC) systems located within the Operations Garrison Headquarters (HQ). The required outcome is sustained operational availability.

**Triage rationale:**

| Factor | Assessment |
|--------|------------|
| Core scope | Hardware maintenance and field operations support for A/V equipment (projectors, displays, screens), VTC codecs, and UC infrastructure at a Garrison HQ |
| NAICS match | A/V maintenance maps to 811212 (computer/office machine repair and maintenance) or 334310 (audio/video manufacturing/services) — SpatialGIS holds none of these |
| SIN match | 54151S could nominally apply but A/V hardware maintenance is a stretch; evaluators likely expect an integrator with Crestron/Cisco VTC credentials |
| GIS/IT nexus | None — "unified communications" is the closest IT keyword but the work is physical A/V hardware O&M, not IT professional services |
| Keyword match | No PASS or MAYBE keywords triggered; default conservative DECLINE applies |
| Capability fit | SpatialGIS has no documented A/V integration, VTC maintenance, or UC infrastructure experience |

**Decision: DECLINE.** A/V equipment and VTC maintenance is outside SpatialGIS's GIS and IT professional services portfolio. No geospatial or spatial analytics nexus. No capability statement prepared.

---

## Previously Submitted Items (Response Confirmations Received Today)

The following 4 RFIs appeared as new invites in today's inbox but have already-confirmed response receipts from a batch submission at 21:xx UTC on 2026-08-27. No action required.

| Subject | Received | Submitted | Confirmation ID |
|---------|----------|-----------|----------------|
| DOI - OSMRE - Inspection and Enforcement (INE) System Modernizat | 2026-08-27T19:02Z | 2026-08-27T21:21Z | SV_d0aFSGkXECHCrwW-R_GOGvv7XmYfOAZav |
| HHS OIG - Health and Clinical Services Support | 2026-08-27T18:03Z | 2026-08-27T21:49Z | SV_3WQz7mRjKMTu7cy-R_GQME14uDX3xknQx |
| DOJ - ATAK Server Support/Maintenance/Troubleshooting | 2026-08-27T16:07Z | 2026-08-27T21:49Z | SV_9nlqdtswn0xTaCO-R_GeCVvj39gLjop8y |
| VA - Laurel Bridge Compass Software License | 2026-08-27T13:07Z | 2026-08-27T21:47Z | SV_6A0ouQAKyBa9iFU-R_GBHtovABPse62K5 |

**Note on DOJ ATAK:** ATAK (Android Team Awareness Kit) is a mapping/geospatial situational awareness platform, and there may be an indirect GIS nexus to SpatialGIS's services. The prior batch run submitted a response — the submission result should be reviewed to confirm a substantive capability statement was provided. If the submission was a minimal/boilerplate response, Kendrick should consider whether a stronger tailored response is warranted for a future ATAK-related requirement.

---

## Batch Submissions from Prior Run (17 Response Confirmations)

All confirmed submitted 2026-08-27 at ~21:17–21:49Z via prior automated batch run. No re-submission required.

| Subject | Confirmation ID |
|---------|----------------|
| Response Received: Army - HR Career Recruiting Portal | SV_86d61L8t8jgqVuK-R_GQVucqYOhzE3uTy |
| Response Received: USAF - Enterprise Cloud Operation & Modernization | SV_6X05sYX2otwFyRM-R_GDqdTUX2G0RbHPW |
| Response Received: USAF - Platform One Engineering and Operations Services | SV_2ccpXwX313YMDe6-R_G9l7Fy86MrwBUpX |
| Response Received: DOL - Physical Access Control and Surveillance System | SV_9HPWlTDob01bm7A-R_G1rKU1mwikb2Zxf |
| Response Received: VA - Privacy Act Request Fulfillment Services | SV_0VAL7ajLISXUTl4-R_GI4R2OGqtIy0IeT |
| Response Received: DOC - OpenAI ChatGPT Enterprise Licenses | SV_afxGgm4DfSuUb3w-R_GwovjPzkMoNOfUG |
| Response Received: NRC - Collaborative Learning Environment | SV_5mMTI6idL24aj9Y-R_GpyvSqOjAeJdXJW |
| Response Received: FCC - Microsoft ELA recompete | SV_b2ULPPKL6nJw4aW-R_GOi1c89rXnFoOjf |
| Response Received: HHS NIH - Strategic Advisory and Expert Engr Support | SV_cxaVicqrILgRCBw-R_GdELKLbJAdASPQC |
| Response Received: DOL - Private Carrier and Self-Insurer Compliance Experts | SV_d0S8BAap1IC5hc2-R_GMSSSLUjXK1ADqd |
| Response Received: DOC - ServiceNow Nuvolo Developer | SV_emI5e99lK5QIkJM-R_GdZgMAxzugGPkg4 |
| Response Received: DOC - Claude for Government Licenses | SV_78mviSWmnGUFz5I-R_GRCUpluc4F7n1ct |
| Response Received: Navy - USFF - TACAMO Mission Support | SV_0BqF9YPyllGQXxs-R_GRGQF2bVZtB9B7P |
| Response Received: VA - Laurel Bridge Compass Software License | SV_6A0ouQAKyBa9iFU-R_GBHtovABPse62K5 |
| Response Received: DOJ - ATAK Server Support/Maintenance/Troubleshooting | SV_9nlqdtswn0xTaCO-R_GeCVvj39gLjop8y |
| Response Received: HHS OIG - Health and Clinical Services Support | SV_3WQz7mRjKMTu7cy-R_GQME14uDX3xknQx |
| Response Received: DOI - OSMRE - Inspection and Enforcement (INE) System Modernizat | SV_d0aFSGkXECHCrwW-R_GOGvv7XmYfOAZav |

---

## Reminders (Prior RFIs — Previously Processed)

| Subject | Date | Prior Slug | Action |
|---------|------|-----------|--------|
| Reminder: DOL - Private Carrier and Self-Insurer Compliance Experts | 2026-08-27 | dol-private-carrier-and-self-insurer-compliance-experts | Already submitted (confirmed same batch) |
| Reminder: DHS - Information Technology Refresh Program (ITRP) | 2026-08-27 | dhs-information-technology-refresh-program-itrp | Prior DECLINE — no action |
| Reminder: HHS NIH - Strategic Advisory and Expert Engr Support for NIH | 2026-08-27 | hhs-nih-strategic-advisory-and-expert-engr-support-for-nih | Already submitted (confirmed same batch) |
| Reminder: HHS IHS - 30 Years of TIPCAP | 2026-08-27 | hhs-ihs-30-years-of-tipcap | Prior DECLINE — no action |
| Reminder: Army - HR Career Recruiting Portal | 2026-08-27 | army-hr-career-recruiting-portal | Already submitted (confirmed same batch) |
| Reminder: Navy - USFF - TACAMO Mission Support | 2026-08-27 | navy-usff-tacamo-mission-support | Submitted (batch); prior pipeline DECLINED — batch overrode |
| Reminder: USAF - Platform One Engineering and Operations Services | 2026-08-27 | usaf-platform-one-engineering-and-operations-services | Already submitted (confirmed same batch) |
| Reminder: DOC NIST - Installation of New Zayo Dark Fiber Tail | 2026-08-27 | doc-nist-installation-of-new-zayo-dark-fiber-tail | Prior DECLINE — no action |

---

## Items for Human Review

**No BLOCKED items requiring immediate action.**

**Advisory — Navy USFF TACAMO Submission:** The pipeline DECLINED this RFI (2026-08-27) due to no GIS/IT nexus and NAICS mismatch. However, the batch run at ~21:xx UTC on 2026-08-27 submitted a response (confirmation SV_0BqF9YPyllGQXxs-R_GRGQF2bVZtB9B7P). Kendrick should verify the submission was coherent and determine whether this represents an intentional override of the pipeline's DECLINE recommendation. If the submission was incomplete or generic, monitor for a re-RFI opportunity.

**Advisory — DOJ ATAK Submission:** ATAK (Android Team Awareness Kit) is a geospatial mapping platform — there is a legitimate GIS nexus here. The pipeline would likely have classified this as MAYBE or PASS had it not been submitted by the prior batch. The submission result should be reviewed to confirm the response highlighted SpatialGIS's geospatial/mapping capabilities rather than generic IT services language.

**Advisory — Batch submission hygiene:** 17 confirmations from a batch run outside the standard daily triage pipeline arrived today. The batch run does not produce fill reports or capability statements tracked by `working/mras-runs/`. Suggest Kendrick verify those submissions had substantive capability content (not just contact info and SIN selection).

---

## Open Opportunities Within Due Window (For Reference)

| Opportunity | Due Date | Status |
|-------------|----------|--------|
| USAF - MEDXS Clinical IT Support Services | 2026-09-02 | DECLINED — guardrail (HEAL/HACS SINs not held) |
| Army - Support Services for Government Owned Audio/Visual | 2026-09-04 | DECLINED — outside capability |
| DOI OSMRE INE System Modernization | 2026-09-xx | SUBMITTED-CONFIRMED (batch) |
| HHS OIG Health and Clinical Services Support | 2026-09-xx | SUBMITTED-CONFIRMED (batch) |
| DOJ ATAK Server Support | 2026-09-xx | SUBMITTED-CONFIRMED (batch) |
| VA Laurel Bridge Compass Software License | 2026-09-xx | SUBMITTED-CONFIRMED (batch) |

---

**Pipeline summary:** 0 new autonomous submissions today. 0 guardrail blocks triggered (items auto-declined before submission gate). 2 new RFIs triaged as DECLINE. 17 prior batch submissions confirmed via response emails.

---

*Generated by automated MRAS daily triage — 2026-08-28*
