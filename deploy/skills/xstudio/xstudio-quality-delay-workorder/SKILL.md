---
name: xstudio-quality-delay-workorder
description: "Investigate work orders, quality results, or delay/OEE data."
version: 0.1.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, xbatch, work-order, quality, delay, oee]
    related_skills: [xstudio-l2-ticket-workflow, xstudio-sql-write-discipline]
---

# XStudio Work Order / Quality / Delay Investigation Skill

For tickets about work-order creation/state, chemistry/sample/quality
results, usage decisions, repeat results, or delay/OEE/downtime in
`XStudio_Xbatch`. Three related-but-distinct production-support domains
grouped in one skill because each is comparatively shallow individually —
split into separate skills if any one grows a `sohar-sms-event-workflows.md`
-sized body of its own event/workflow internals later.

## When to Use

- **Work order**: missing/wrong state, order-creation issue, campaign
  scheduling.
- **Quality**: chemistry/spectro result missing or wrong, usage decision
  (UD) or repeat result (RR) not posted, deviation.
- **Delay/OEE**: downtime not recorded, wrong report date, agency/equipment
  attribution question.

## Procedure

### Work order

1. Master row: `XBatch_Work_Order_Mst_Tbl`, managed via
   `Xstudio_XBatch_Work_Order_Mst_Tbl_USP` (standard `@ID`/`@Mode` CRUD —
   confirm `@Mode` values live).
2. **"Work order never appeared"** → trace `XMES_WorkOrders_Creation`
   (confirmed live: takes `@CampaignID`/`@StartDate`/`@EndDate`, branches
   per product type from Sales Order data) for the relevant campaign/date
   range, not just the master table.
3. SAP side: `MES_SAP_WO_Trn_Tbl`, `MES_SAP_WorkOrder_Movements_Trn_Tbl`,
   errors via `XMES_SAP_WorkOrder_Creation_API_Error_Usp` — hand off to
   `xstudio-sap-api-investigation` if the root cause is SAP-side.

### Quality

1. **RR** = Repeat Result/Rework Request, **UD** = Usage Decision (SAP QM
   accept/reject/restrict). No dedicated RR/UD-specific error or creation
   procedure was found by name search as of 2026-09-02 — check
   `SAP_Posting_Tbl.PostingType`/`MovementType` for RR/UD-tagged rows, or
   re-search live rather than trusting this gap is permanent.
2. **Chemistry chain**: `Quality_Spectro_File` → `_Sample` → `_Result` —
   trace a specific heat through this three-table chain for "chemistry
   result missing."
3. Heat-level: `Chemistry_Deviation_Quality_Data`, `Heat_Chemistry_Quality_Data`.
4. Product-level (match shape to table): `Rebar_Quality_Data`,
   `Rebar_Coil_Quality_Data`, `Round_Bar_Quality_Data`.
5. Reference/config, not transactional: `Quality_Deviation_Master`
   (deviation codes), `MES_Quality_Configurator` (thresholds — relevant
   only for wrong-threshold tickets, not a specific bad result).

### Delay / OEE

1. Central transaction table: `Delay_Trn_Tbl` (`EquipmentID`, `ReportDate`
   columns) — attributed to equipment, not directly to agency/category.
2. Classification lookups: `DelayTypeMST`, `DelayCategory_Master`,
   `DelaySubType_Master`, `DelayAgency_Master`.
3. Rollups (aggregate, not per-event): `Agency_Wise_Delay`,
   `Equipment_Wise_Delay` — managed via `Xstudio_Agency_Wise_Delay_USP`
   (confirmed live: real body recalculates a derived `Durationmmss`
   display column on update, not a pure pass-through).
4. Area-specific shift entry: `ShiftDelayEntry` (+`_Audit`,
   `_Transaction_Operator`), `RMShiftDelayEntry_CAPA`, `SMS_DelayEntry_CAPA`,
   `SMS_Delay_Trn_Tbl`, `RM_Delays` — match the ticket's `AreaID` to the
   right prefix (RM = Rolling Mill, SMS = Steel Melt Shop).

## Pitfalls

- **Several `Temp_*`-prefixed quality tables are scratch/staging** — ignore
  for investigation unless a specific procedure's definition shows it
  deliberately reads one.
- **`Xstudio_Agency_Wise_Delay_USP` carries real business logic**, not
  just CRUD — don't assume a `@Mode`-driven procedure is a dumb wrapper
  without reading it.
- **Multiple `Delay_Trn_Tbl` rows with `ReportDate = NULL` were observed
  live** for at least one equipment ID as of 2026-09-02 — a genuine known
  data-quality gap, not something to assume was already fixed.

## Verification

- [ ] For a work-order ticket, `XMES_WorkOrders_Creation`'s actual branch
      logic for the ticket's product type was checked, not assumed.
- [ ] For a quality ticket, the specific heat was traced through the real
      Spectro File→Sample→Result chain, not just checked for a Result row.
- [ ] For a delay ticket, the equipment/agency classification was resolved
      via the master tables, not guessed from a code.
