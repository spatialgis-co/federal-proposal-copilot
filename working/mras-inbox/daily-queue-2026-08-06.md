# MRAS Daily Queue — 2026-08-06

**Run timestamp:** 2026-08-06 (automated)  
**Gmail threads fetched (last 24h):** 8  
**Thread types:** 1 new RFI invitation, 2 response confirmations, 5 reminders  
**Triage results:** PASS=0 | MAYBE=0 new | DECLINE=1 new  
**Submitted this run:** 0 (automated) | **Confirmed Kendrick manual:** 2  
**Rejected:** 0 | **Blocked:** 0

---

## Confirmed Manual Submissions (Kendrick — logged for ledger)

Two response confirmation emails arrived today confirming Kendrick submitted these opportunities via browser. No fill-report files existed for either; they are noted here for the activity record. These did NOT go through the automated pipeline.

### 1. USAF AAS — Financial and IT Support Services Recompete
| Field | Value |
|-------|-------|
| Survey ID | SV_bpYyzvMt82YbbfM |
| Response ID | R_GEWFX1oi5oprjZt |
| Confirmation Thread | 19fd326611d96e36 |
| Date Submitted | 2026-08-05 ~18:18 UTC |
| Reminder Thread | 19fd15e3f2cb7932 (same day) |
| RFI Due Date | 2026-08-11 |
| GSA COR | Alex Budai (alex.budai@gsa.gov, 951-704-4440) |
| Slug | `usaf-aas-financial-it-support-services-recompete` |

**Submitted response summary:** MAS 47QTCA24D00DS · SIN 541611 · NAICS 541611 · Small Business · SDB(d) · Would bid: Yes · Subcontracting: 15–30% · Lead time: 30 days. Capability statement uploaded (File F_1gH0d4ZOVds8SFf). Optional feedback cited USAF delivery history (USAFA, DAMO, ACC A5/8/9, Fire & Emergency, TACOS, ANG CDAO) and DoD financial management past performance (USTRANSCOM EADE, USACE PSS, Army CIO/G6).

> **Note:** Response used SIN 541611 (Management Consulting). SpatialGIS's MAS holds SIN 54151S (IT Professional Services). If this advances to RFQ, Kendrick should verify 541611 is accessible under MAS 47QTCA24D00DS before proposing, or pivot the vehicle claim.

---

### 2. USDA APHIS — Program Support and Manuals Program Services
| Field | Value |
|-------|-------|
| Survey ID | SV_8BUUHt3ADUYTD5c |
| Response ID | R_GJ59RIHNg5aVVth |
| Confirmation Thread | 19fd327528044961 |
| Date Submitted | 2026-08-05 ~18:19 UTC |
| Reminder Thread | 19fd15f81cd4d078 (same day) |
| RFI Due Date | 2026-08-10 |
| Slug | `usda-aphis-program-support-and-manuals-program-services` |

**Requirement synopsis:** Information Services and Manuals Unit (ISMU) — program support for the ACIR (Agricultural Commodity Import Requirements) Database and PPQ (Plant Protection & Quarantine) Manuals. Scope: respond to email inquiries via two mailboxes; create user guides and SOPs. Remote/virtual performance.

> **Note:** Automated pipeline would classify this DECLINE (no GIS keywords, "program support" for an agricultural database is admin-focused). Kendrick chose to respond. If this advances to RFQ, a teaming partner with agricultural domain knowledge would strengthen the proposal.

---

## New RFI — DECLINE

### Army — MCASP Recompete
| Field | Value |
|-------|-------|
| Thread ID | 19fd2b2cb25c48cc |
| Survey ID / URL | SV_a66t6xKqEnaEuMe |
| Date received | 2026-08-05T16:12:33Z |
| Due Date | **2026-08-18** |
| Slug | `army-mcasp-recompete` |
| Triage result | **DECLINE** |

**Requirement:** Acquire instructors and IT personnel to support program and instruction for operational mission command systems for the Mission Command Arts and Sciences Program (MCASP).

**Decline rationale:**
1. **Instructors as primary function** — the dominant workforce need is subject-matter experts who can teach Army doctrine and mission command systems. SpatialGIS does not provide instruction/training staff for Army leadership programs.
2. **MCASP is an Army leadership/doctrine program** — the Mission Command Arts and Sciences Program trains officers and NCOs on command philosophy and associated C2 systems. This is a specialized teaching function, not GIS or geospatial professional services.
3. **No GIS/geospatial keyword match** — "operational mission command systems" could theoretically include map-enabled tools (e.g., CPOF), but the RFI framing is instructor-and-IT-support staffing, not geospatial capability development.
4. **NAICS mismatch** — likely 611430 (Professional/Management Development Training) or 541512 narrow staffing; SpatialGIS's primary NAICS (541370, 541511, 541512, 541519) do not anchor on instructor-for-hire services.

**No capability statement drafted. No survey attempted.**

---

## Reminders — Previously Processed (No New Action)

| Thread | Opportunity | Prior Triage | Due | Status |
|--------|-------------|--------------|-----|--------|
| 19fd1614d6df46d5 | OMB EOP - V&V Process Improvement | MAYBE (08-01) | 08/19/2026 | Still open — held for human review |
| 19fd160cc04f8f41 | HHS CMS - Medicare Advantage (MARx) | DECLINE (07-31) | **08/06/2026 — TODAY** | Closing today; previously declined. No action. |
| 19fd15f878711aeb | GSA OGP - Phishing Resistant Authenticators | DECLINE (07-30, 07-31) | 08/12/2026 | Previously declined. No action. |
| 19fd15f81cd4d078 | USDA APHIS - Program Support & Manuals | Confirmed submitted | 08/10/2026 | Response received today (Kendrick). |
| 19fd15e3f2cb7932 | USAF AAS - Financial IT Support Recompete | Confirmed submitted | 08/11/2026 | Response received today (Kendrick). |

---

## Open MAYBEs From Prior Runs (Human Review Available)

| Slug | Agency | Due | Note |
|------|--------|-----|------|
| omb-eop-verification-validation-process-improvement | OMB/OFPP | 08/19/2026 | SAM.gov data V&V — no GIS fit; false-positive "reporting" keyword. Recommended: no response. |
| doe-operation-program-support-services-opss | DOE/NNSA | 08/18/2026 | Broad admin BPA — no GIS fit. Recommended: no response. |
| hhs-acf-child-welfare-technology-solutions-and-services | HHS/ACF | 08/13/2026 | Child welfare technology — no direct GIS fit. Recommended: no response. |
| usace-cenwd-collaborative-partnering | USACE NW Division | 08/10/2026 | Partnering/program support — no GIS fit. Recommended: no response. |
| doe-cyber-security-information-support-services | DOE/CBO | 08/10/2026 | Broad cyber/IT support — no clear GIS angle. Recommended: no response. |

---

## Pipeline Status

- **Proxy block:** `feedback.gsa.gov:443` remains unreachable from this automated environment (ongoing since 07/23). All PASS items continue to require manual browser submission.
- **Total submitted to date:** 29 automated (mras-runs/) + 2 Kendrick manual today (USAF AAS Financial + USDA APHIS) = **~31 total**.
- **OK_TO_SUBMIT:** Remains true (blanket authorization; no reset per protocol).
- **Proxy resolution path:** Update network policy to allow outbound HTTPS to `feedback.gsa.gov:443` from the automated run environment to restore autonomous submission capability.
