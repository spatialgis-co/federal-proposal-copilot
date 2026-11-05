# MRAS Daily Queue — 2026-11-05

**Run timestamp:** 2026-11-05T00:00:00Z  
**Gmail query:** `from:rfi@research.gsa.gov newer_than:1d`  
**Result:** 6 threads found

## Summary

| Metric | Count |
|--------|-------|
| Emails retrieved | 6 |
| After dedup | 6 |
| PASS | 1 |
| MAYBE | 1 |
| DECLINE | 4 |
| Submitted | 0 |
| Blocked (technical) | 1 |
| Blocked (guardrail) | 0 |

---

## PASS — BLOCKED-TECHNICAL (Capability Statement Ready for Manual Submission)

### DOI USGS — AI Assisted Comprehensive Condition Assessments

| Field | Value |
|---|---|
| **Agency** | DOI / U.S. Geological Survey (USGS) |
| **Slug** | `doi-usgs-ai-assisted-comprehensive-condition-assessments` |
| **Thread ID** | 1a1a8d88d7ee3d25 |
| **Survey** | SV_0cRPQFdEtsEOTJQ |
| **Survey URL** | https://feedback.gsa.gov/jfe/form/SV_0cRPQFdEtsEOTJQ |
| **Due Date** | **2026-11-13** (8 days from now) |
| **Triage** | **PASS** — keyword match: `LiDAR` |
| **NAICS** | 541370 (Surveying and Mapping) — SpatialGIS primary NAICS |
| **SIN** | 54151S (IT Professional Services) |
| **Guardrail check** | PASS — no violations |
| **Block reason** | BLOCKED-TECHNICAL: `feedback.gsa.gov` blocked by agent proxy; discover + submit require manual browser session |
| **Capability Statement** | `working/mras-capabilities/doi-usgs-ai-assisted-comprehensive-condition-assessments-capability.md` |
| **Capability Statement (docx)** | `final/docx/mras/doi-usgs-ai-assisted-comprehensive-condition-assessments-capability.docx` |
| **Answers file** | `working/mras-answers/doi-usgs-ai-assisted-comprehensive-condition-assessments.json` |
| **Submission status** | **BLOCKED-TECHNICAL — manual submission required** |

**Requirement summary:** USGS needs condition assessments of real property assets using drones, LiDAR, thermal imaging, and cameras with AI-analyzed results — in lieu of traditional labor-intensive manual inspections.

**Fit assessment:** Direct alignment. SpatialGIS's core capabilities — UAS operations, LiDAR collection and processing, thermal imaging analysis, AI-assisted feature extraction, GIS-integrated reporting — match every technical element in the requirement description. NAICS 541370 is the primary code. No guardrail flags.

**Key flags reviewed:**
- ✅ NAICS 541370 held — primary NAICS for SpatialGIS
- ✅ SIN 54151S held — GSA MAS 47QTCA24D00DS
- ✅ No CMMC L2 Certified requirement detected in email body
- ✅ No FedRAMP-authorized product requirement detected
- ✅ No teaming partner required for core scope
- ⚠️ Capability statement Sections 5 (Past Performance) and 6 (Key Personnel) need population from company records before submission

**Action required from Kendrick:**
1. Open `final/docx/mras/doi-usgs-ai-assisted-comprehensive-condition-assessments-capability.docx`
2. Fill in Sections 5 and 6 with actual past performance and key personnel
3. Navigate to: https://feedback.gsa.gov/jfe/form/SV_0cRPQFdEtsEOTJQ
4. Use personal link in email: https://feedback.gsa.gov/jfe/form/SV_0cRPQFdEtsEOTJQ?Q_DL=gZMGLLVGMwdeufa_0cRPQFdEtsEOTJQ_CGC_F3fhTYeq3ZVEJFK&Q_CHL=email
5. Submit before **2026-11-13**

---

## MAYBE (Human review — no auto-submit)

### USAF — Agile Platform for Expeditionary C2 (APEX)

| Field | Value |
|---|---|
| **Agency** | USAF / Air Force PAE C3BM |
| **Slug** | `usaf-agile-platform-for-expeditionary-c2-apex` |
| **Survey** | SV_bDGTQqDbZOeR9bw |
| **Due Date** | 2026-11-30 (25 days) |
| **Triage** | MAYBE — keyword: `software development` |
| **Status** | No prep; for human review |

**Scope:** Rapid, secure, continuous software development for a portfolio of C2 (command and control) applications for Air Force Mission Planning. Full software lifecycle — custom software engineering, design, continuous code development.

**Assessment:** Software engineering for military C2 mission planning applications. No explicit GIS/geospatial component in the email description. SpatialGIS holds software development capabilities (NAICS 541511/541512) but C2 mission planning software is a specialized domain. If SpatialGIS has relevant past performance on defense software/C2 systems (or a teaming partner with such credentials), this could be viable. RECOMMEND: Kendrick review — if no C2 software past performance, decline; if teaming option exists, respond by 11/30.

---

## DECLINE

### DOT — Design Integration Risk Assessment Framework (USMMA Campus Modernization)

| Field | Value |
|---|---|
| **Slug** | `dot-design-integration-risk-assessment-framework` |
| **Survey** | SV_4YGKWgwOMMHmwSi |
| **Due Date** | 2026-11-17 |
| **Triage** | DECLINE |

**Rationale:** Professional consulting services for a Design Integration Management (DIM) Framework supporting the US Merchant Marine Academy campus modernization. This is architecture/facilities consulting with no IT or GIS component. Not in SpatialGIS's capability portfolio.

---

### OSW MDA — ORBIT Sustainment RFI Follow On

| Field | Value |
|---|---|
| **Slug** | `osw-mda-orbit-sustainment-rfi-follow-on` |
| **Survey** | SV_5j18iBcJd6xldkO |
| **Due Date** | 2026-11-10 |
| **Triage** | DECLINE |

**Rationale:** Missile Defense Agency (MDA) staffing methodology RFI for the ORBIT program (eBuy 1838803–1838806). MDA/missile defense systems staffing — SpatialGIS has no missile defense expertise or relevant past performance in this domain.

---

### TREAS IRS — Enterprise Performance Testing Tool Software Support

| Field | Value |
|---|---|
| **Slug** | `treas-irs-entps-performance-testing-tool-software-support` |
| **Survey** | SV_6nhPO6uNOjGnDTM |
| **Due Date** | 2026-11-12 |
| **Triage** | DECLINE |

**Rationale:** Software licenses and support services for IRS performance testing tool (reliability, scalability testing of mission-critical apps). Performance testing tooling is a specialized software product support domain; no GIS relevance.

---

### GSA — Online University Functional Support

| Field | Value |
|---|---|
| **Slug** | `gsa-online-university-functional-support` |
| **Survey** | SV_5cqQmEwYHZPprb8 |
| **Due Date** | 2026-11-13 |
| **Triage** | DECLINE |

**Rationale:** Enterprise workforce learning and development support services (LMS support). No GIS/IT professional services component. SpatialGIS has no past performance in LMS/training operations.

---

## Pipeline Note — Autonomous Submission Status

The agent proxy blocks outbound connections to `feedback.gsa.gov:443`. As a result:
- `mras_discover.py` cannot fetch QID definitions from Qualtrics survey forms
- `mras_submitter.py` cannot post responses to Qualtrics

All prior submissions in `working/mras-runs/` were executed in sessions with open proxy access. Until `feedback.gsa.gov` is unblocked or a browser-based submit path is implemented, all PASS opportunities will be BLOCKED-TECHNICAL and require Kendrick to submit manually via browser.

---

*Generated by MRAS daily triage automation.*  
*Raw data:* `working/mras-inbox/daily-raw-2026-11-05.json`  
*Triage detail:* `working/mras-inbox/daily-triage-2026-11-05.json`
