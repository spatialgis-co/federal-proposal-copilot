# MRAS Daily Queue — 2026-07-14

**Run date:** 2026-07-14  
**Gmail query:** `from:rfi@research.gsa.gov newer_than:1d`  
**Result:** 9 threads (2 new, 7 reminders) — 0 submitted, 0 rejected, 1 blocked for human review

---

## Summary

| Metric | Count |
|--------|-------|
| New threads received | 9 |
| After dedup | 9 |
| PASS (triage script) | 1 |
| MAYBE (triage script) | 1 |
| DECLINE (triage script) | 7 |
| SUBMITTED-CONFIRMED (this run) | 0 |
| REJECTED-BY-QUALTRICS (this run) | 0 |
| BLOCKED-NEEDS-USER (this run) | 1 |
| Running total SUBMITTED-CONFIRMED | 29 |

---

## BLOCKED — Requires Human Review

### TREAS - NETCOM - CS2100 PRI Provisioning & PSAP Routing Config
- **Agency:** Treasury / NETCOM
- **Due:** 07/29/2026
- **Thread ID:** 19f5aedcb89516b8
- **Triage script result:** PASS (keyword: "routing")
- **Guardrail decision:** BLOCKED — **False positive.** "Routing" in the email body refers to PSAP emergency call routing (telecom), not GIS network/route analysis. Requirement is for "specialized telecommunications engineering services to program and configure a CS2100 telephony switch… integrate two (2) Primary Rate Interface (PRI) circuits and configure Public Safety Answering Point (PSAP) emergency routing to ensure local 911 calls are successfully delivered to the designated call center." SpatialGIS has no CS2100 switch programming, PRI circuit integration, or PSAP telecom expertise. Submitting would require unsupported claims.
- **Recommended action:** Decline. Consider adding "PRI provisioning", "PSAP routing", "CS2100", "telephony switch" to `capability_keywords_decline` in `scripts/mras_answers.json` to prevent future false positives.

---

## MAYBE — Logged for Human Review (No Prep)

### EPA - Information Management Program Support Services
- **Agency:** EPA
- **Due:** 07/24/2026
- **Thread ID:** 19f5aeecd7cc1fba
- **Triage script result:** MAYBE (keyword: "program support")
- **Body summary:** "Prior experience in Nuxeo software development. Experience with program/policy development for Information Collection Requests (ICR). Experience working with NARA while supporting another Federal Agency and their Records. Prior experience in writing Agency policies based on laws and regulation."
- **Assessment:** Domain mismatch — Nuxeo ECM platform, NARA records management, and ICR regulatory policy are outside SpatialGIS's core competency. SpatialGIS has no documented Nuxeo experience and no NARA/ICR policy background. Response would require unsupported claims.
- **Recommended action:** Decline. No prep warranted.

---

## DECLINE — 7 Items

| Slug | Agency | Type | Due | Reason |
|------|--------|------|-----|--------|
| usaf-87-fss-military-personnel-flight-customer-service | USAF | NEW | 07/27/2026 | RhyBus customer service portal deployment for Military Personnel Flight — no GIS connection; software deployment for HR/personnel service platform |
| doj-bop-fsa-time-credit-calculation-model | DOJ BOP | NEW | 07/27/2026 | First Step Act time credits calculation model — corrections/legal domain; independent oversight and QA for a DOJ-specific legal compliance model; no GIS connection |
| usda-laboratory-support | USDA | REMINDER | — | Laboratory support services; no GIS/IT relevance in subject or prior triage |
| army-nhng-military-readiness-support-services | Army | REMINDER | — | NHNG (New Hampshire National Guard) military readiness support — non-GIS military HR/operations support |
| doc-nist-manufacturing-data-analysis-and-modeling-tool | DOC NIST | REMINDER | — | NIST manufacturing data analysis and modeling — specialized manufacturing domain; prior triage confirmed decline |
| usaf-jblm-premise-wiring-bldg-12 | USAF | REMINDER | — | Building 12 premise wiring — facilities/construction cabling; not IT or GIS |
| doj-dea-spectrum-acr-video-surveillance-program | DOJ DEA | REMINDER | — | Spectrum ACR (automatic call recording) and video surveillance — telecom/physical security systems; no GIS connection |

---

## Notes

- The triage keyword classifier produced one false positive (TREAS NETCOM, matched "routing"). The "routing" keyword in `capability_keywords_pass` is intended for GIS network/route analysis but matched telecom PSAP call routing. Consider tightening the keyword or adding telecom counter-keywords to the decline list.
- No new submissions this run. Running total remains 29 SUBMITTED-CONFIRMED.
- EPA Information Management item closes 07/24/2026 — human review needed by 07/23/2026 if SpatialGIS wants to reconsider.
