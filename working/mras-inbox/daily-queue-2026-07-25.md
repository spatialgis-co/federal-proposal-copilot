# MRAS Daily Queue — 2026-07-25

**Threads received:** 5 (2 new RFIs, 3 reminders)  
**Triage results:** PASS=0 | MAYBE=1 | DECLINE=4 | SKIP_CLOSED=0  
**Submitted:** 0 | Rejected: 0 | Blocked: 0

---

## MAYBE — Needs Human Review

### TREAS - IRS - Qualified Opportunity Zones Reporting
- **Slug:** `treas-irs-qualified-opportunity-zones-reporting`
- **Agency:** Treasury / IRS Statistics of Income (SOI) Division
- **Due:** 07/28/2026 (**Monday — 3 days from today**)
- **Survey ID:** SV_cuzzoHIS4z2agRw
- **Fit:** Triage MAYBE on "reporting" keyword. The requirement is for analyzing and reporting on Opportunity Zone investment data under the One Big Beautiful Bill Act (OB3). Qualified Opportunity Zones are geographic designations — SpatialGIS may have relevant spatial analysis/visualization capabilities for OZ program oversight. However, the core ask appears to be tax/financial data analytics, not GIS specifically.
- **Key flags:**
  - Very tight deadline (3 days). If Kendrick wants to respond, must act by Sunday.
  - SOI Division data work — not core GIS but geographic entities are involved.
  - "financial management" hard-decline keyword was NOT triggered (description avoided direct match).
- **Action needed:** Kendrick to decide: respond as GIS/spatial-analytics capability for geographic OZ data, or pass. If respond, must draft and submit manually or approve a capability statement draft by EOD Sunday.
- **Capability statement path:** Not drafted (MAYBE, not PASS)

---

## DECLINE

### TREAS - IRS - Remote Desktop support APP Software licensing
- **Slug:** `treas-irs-remote-desktop-support-app-software-licensing`
- **Agency:** Treasury / IRS
- **Due:** 08/05/2026
- **Survey ID:** SV_a8J3v0iPCklTugS
- **Reason:** Hard-decline keyword `treasury` + scope is commercial remote desktop software licensing (enterprise remote support tool for IRS Service Desk, e.g. BeyondTrust/TeamViewer-class product). SpatialGIS has no product or reseller capability here.

### Reminder: GSA OCAS - FedHub Managed Service Office (MSO) Operations
- **Slug:** `gsa-ocas-fedhub-managed-service-office-mso-operations`
- **Agency:** GSA OCAS
- **Due:** 07/31/2026
- **Survey ID:** SV_9XHGddS8vARgiSW
- **Reason:** No keyword match — conservative decline. FedHub/XMS is an existing HHS document management implementation; requirement is program management and technical support for that specific platform. Not GIS.

### Reminder: HHS CDC - National Technical Assistance Center for Adolescent Health
- **Slug:** `hhs-cdc-national-technical-assistance-center-for-adolescent-health`
- **Agency:** HHS CDC / DASH
- **Due:** 07/27/2026 (tomorrow)
- **Survey ID:** SV_2blRw9S2KPGoHFc
- **Reason:** No keyword match — conservative decline. Public health technical assistance, advisory council operations, and TA/PD framework for adolescent health programs. No IT or GIS fit.

### Reminder: HHS CMS - CRM Enterprise Transformation and System Testing
- **Slug:** `hhs-cms-crm-enterprise-transformation-and-system-testing`
- **Agency:** HHS CMS
- **Due:** 07/29/2026
- **Survey ID:** SV_cZPUR0kCGvOtheC
- **Reason:** No keyword match — conservative decline. CRM application testing and Change Control Board management for CMS Virtual Center Strategy. No GIS fit.

---

## Pipeline Status Note

Proxy block to `feedback.gsa.gov:443` noted in prior runs (07/23, 07/24) — `mras_discover.py` and `mras_submitter.py` cannot reach Qualtrics forms from this environment. No PASS items today so this did not affect the run. If PASS items appear in future runs, manual browser submission will be required until the proxy policy is updated.
