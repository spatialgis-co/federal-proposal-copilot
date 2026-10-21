# MRAS Daily Queue — 2026-10-21

**Run summary:** 1 email received | 1 new RFI solicitation | 0 PASS | 1 MAYBE | 0 DECLINE | 0 submitted | 0 blocked | **1 needs human decision**

---

## MAYBE — Needs Human Review

### USAF AETC – Data Science, Metadata Mgmt & Enterprise Learning App Support (ELAS)

| Field | Value |
|---|---|
| **Agency** | USAF / DAF, HQ Air Education Training Command (AETC) — A9, A6, A3G directorates |
| **Opportunity slug** | `usaf-data-science-metadata-mgmt-enterprise-learning-app-spt` |
| **Survey ID** | SV_6hSM8nYJ4KNzz5I |
| **Due Date** | **2026-10-30** (9 days) |
| **Triage result** | MAYBE — matched broad-IT keyword: `software development` |
| **Thread ID** | 1a15a89d43962930 |
| **Email date** | 2026-10-20 18:18 UTC |

**Description:**
Data Science, Metadata Management, and Enterprise Learning Application Support (ELAS) for DAF/AETC. The contractor will operate as part of a Government-led MFT and provide qualified personnel to perform **operations research, data science, AI/ML, enterprise data management, software development, and application sustainment** activities across the Analysis and Assessments Directorate (A9), AETC Data Office (A6), and Learning Services Division (A3G).

**Fit Assessment:**

| Factor | Status |
|---|---|
| Core capability match (GIS/geospatial) | ❌ No GIS/geospatial component in scope |
| Broad IT match | ⚠️ Software development, enterprise data mgmt |
| NAICS fit | ✅ 541511/541512/541519 would cover software dev |
| Data science / AI/ML | ⚠️ SpatialGIS has adjacent capability but this is the core requirement |
| Operations research | ⚠️ Outside SpatialGIS core competency |
| Learning systems / EDRMS / LMS | ⚠️ No established capability — would require teaming |
| Contract vehicle | ✅ GSA MAS 47QTCA24D00DS (SIN 54151S) |
| Due date | ✅ 10/30/2026 — 9 days remaining |

**Why MAYBE, not PASS:** No GIS, geospatial, mapping, or spatial analysis keywords in the RFI. The primary work is data science/AI/ML for Air Force training operations — not SpatialGIS's lead differentiator. However, SpatialGIS holds NAICS 541511/541512 and has legitimate software development and data management experience.

**Human decision needed — options:**

1. **SKIP:** No meaningful fit beyond generic IT; conserve effort for better-fit opportunities. Recommended if no data science / AI/ML-focused teaming partner is available.
2. **PROCEED with teaming:** If Kendrick has a data science / AI/ML partner who can carry the core work, SpatialGIS could contribute geospatial data management and software development components. Would require manual survey completion or running `/mras_discover.py` and drafting a targeted capability statement emphasizing the data management and software development overlap.
3. **PROCEED solo:** Submit a narrow capability statement scoped to the software development and enterprise data management components only, with honest assessment of the AI/ML and operations research requirements.

**To promote to PASS and process:** Run `python3 scripts/mras_discover.py --survey-url 'https://feedback.gsa.gov/jfe/form/SV_6hSM8nYJ4KNzz5I' --opportunity-id usaf-data-science-metadata-mgmt-enterprise-learning-app-spt` after reviewing the full survey questions.

---

## Summary

| Metric | Count |
|---|---|
| New emails from rfi@research.gsa.gov | 1 |
| New RFI solicitations | 1 |
| PASS (processed automatically) | 0 |
| MAYBE (needs human decision) | 1 |
| DECLINE | 0 |
| SKIP_CLOSED (past due) | 0 |
| Capability statements drafted | 0 |
| Submitted (this run) | 0 |
| Blocked for review | 0 |
