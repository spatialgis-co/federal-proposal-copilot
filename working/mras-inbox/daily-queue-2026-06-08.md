# MRAS Daily Queue — 2026-06-08

**Run date:** 2026-06-08  
**Pulled from:** `from:rfi@research.gsa.gov newer_than:1d`  
**Total threads (last 24 h):** 0  
**Submitted today:** 0  
**Rejected by Qualtrics:** 0  
**Blocked (needs user):** 0 new (1 carried forward — see below)  
**Declined:** 0  

> **Infrastructure note (persistent):** Outbound network access to `feedback.gsa.gov` is blocked by the cloud execution environment's network policy. `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics survey URLs from this environment. Survey discovery and form submission must be performed from a local machine or an environment with unrestricted outbound access. This constraint is unresolved since 2026-06-06.

> **Triage bug fix — CONFIRMED APPLIED:** `scripts/mras_triage_classify.py` now uses `re.search(r"\b" + re.escape(kw.lower()) + r"\b", text_lower)` for all keyword matches, eliminating the NGA/GIS/GPS substring false-positive that produced the DOJ FBI DSSU misclassification on 2026-06-06.

---

## TODAY'S NEW OPPORTUNITIES

**None.** Gmail search `from:rfi@research.gsa.gov newer_than:1d` returned zero threads on 2026-06-08.

---

## CARRIED FORWARD — STILL OPEN

### DOJ FBI — Data Sharing Services Unit Program Support ⚠️ URGENT — 7 days remaining
| Field | Value |
|---|---|
| Thread | `19e98be6121d7a05` |
| Slug | `doj-fbi-dssu-program-support` |
| Agency | DOJ / FBI CJIS Division |
| Survey URL | `https://feedback.gsa.gov/jfe/form/SV_1EQyWZDkPl92FdY?Q_DL=n6WiNY1VbBzf601_1EQyWZDkPl92FdY_CGC_LNxOS2OB5k2VesP&Q_CHL=email` |
| Due Date | **2026-06-15** — **7 days remaining** |
| First logged | 2026-06-06 (daily-queue-2026-06-06.md) |
| Status | **BLOCKED-NEEDS-USER** — carried forward unchanged |
| Capability statement | Not drafted |

**Block reason summary** (full detail in `daily-queue-2026-06-06.md`):

1. **Network blocked.** `feedback.gsa.gov` is unreachable from this environment — QID data (required NAICS, SINs, capability sub-questions) cannot be fetched automatically.
2. **CJIS clearance unconfirmed.** FBI CJIS Security Policy requires background screening for all personnel with system access. SpatialGIS clearance status not documented in `my-company/`.
3. **Triage false positive (historical).** "PASS" was originally triggered by `"NGA"` matching as a substring of "e**nga**gement" — this bug is now fixed in the triage classifier. The actual requirement (data analytics, business consulting, content management, systems integration) has no geospatial/NGA content.
4. **Capability fit uncertain.** Without QID sub-questions, substantively true Y/N capability answers cannot be drafted. General IT consulting is a MAYBE, not a PASS.

**Required action before 2026-06-15 (7 days):**
1. Open the survey URL above in your browser.
2. Confirm required NAICS (QID10) and SINs (QID8) — 54151S is the only MAS SIN SpatialGIS holds.
3. Confirm CJIS background screening eligibility.
4. Review capability sub-questions and decide go/no-go.
5. If go: save QID definitions to `working/mras-surveys/doj-fbi-dssu-program-support/qid-definitions.json`, draft `working/mras-answers/doj-fbi-dssu-program-support.json`, and run the pipeline from a local machine.

---

## ACTION ITEMS FOR KENDRICK

1. **URGENT (deadline 2026-06-15 — 7 days):** Review the DOJ FBI DSSU survey manually (link above). See block reasons above and full detail in `daily-queue-2026-06-06.md`. Decision deadline: by **2026-06-12** (3 days before close) to leave time for local pipeline run.

2. **Environment fix:** To enable automated survey discovery and submission, configure outbound access to `*.gsa.gov` in the cloud environment's network policy (see [remote execution environment docs](https://code.claude.com/docs/en/claude-code-on-the-web)), or run the MRAS pipeline locally.
