---
type: "Reference"
title: "XBatch Investigation Surfaces"
description: "Curated map of the real SAP integration, historian, production-tracking, work order, quality, delay/OEE, billet/yard, and API-transaction tables/SPs in XStudio_Xbatch worth checking during an L2 investigation -- grounded in live-exported schema/SP text, not name-guessing."
status: draft
verified: "2026-09-02"
---

# XBatch Investigation Surfaces

Grounded in `Reference Documents/XStudio_Xbatch_Schema.md` (563 tables) and
`XStudio_Xbatch_StoredProcedures.md` (388 procedures), both live-exported
2026-09-02. This is a **starting map for `find_sql_objects`/
`get_sql_object_definition`, not a substitute for them** — verify against the
live server before trusting a name/column here; schema drifts.

## Why this exists

Before this file, Hermes's only tool for domain knowledge was
`find_sql_objects` — a blunt keyword search. Searching "billet" returns
column names and default-constraint objects mixed in with real tables, with
no sense of which table families actually matter for a given complaint type.
This file is the missing middle layer: know where to look *before* searching.

## SAP posting / integration errors

**Ticket smell:** "SAP document/material doc missing", "posting stuck",
"not appearing in SAP", any complaint naming SAP.

- **`dbo.SAP_Posting_Tbl`** (84 rows as of 2026-09-02) — the central posting
  record. Keyed by `WorkOrderNo`/`HeatNo`. Check first. Real diagnostic
  columns: `SAP_Status`, `SAP_DocumentNo`, `SAP_Message`, `SAP_PayloadJson`,
  `IsProcessed`, `PostingDate`, `PostingType`, `MovementType`, `MaterialCode`,
  `BatchNo`, `Quantity`. A row with `IsProcessed = 0` or a populated
  `SAP_Message` (error text) and no `SAP_DocumentNo` is the classic "stuck
  posting" signature.
- **`dbo.XMES_SAP_*_API_Error_Usp`** family — one procedure per SAP
  operation, each logging a per-transaction API failure. Confirmed by
  reading the live definition of `XMES_SAP_GoodsMovements_API_Error_Usp`
  (params: `@RecordID varchar(36), @TransactionID varchar(36),
  @APIPostingType varchar(100)`; author comment: "For Posting Sequence").
  Siblings by name: `XMES_SAP_Batch_Characteristics_API_Error_Usp`,
  `XMES_SAP_Batch_Creation_API_Error_Usp`,
  `XMES_SAP_Inventory_API_Error_Usp`. These are the write-side of the error
  log — to *read* what they've recorded, find what table they write to
  first (`get_sql_object_definition`), don't assume.
- **`dbo.XMES_I_SAP_*` family** — insert/entry points into the SAP
  transaction pipeline: `XMES_I_SAP_Billet_Production_Trn`,
  `XMES_I_SAP_GLS_LS_Consumption_Trn_Usp`,
  `XMES_I_SAP_GLS_LS_Production_Trn_Usp`, `XMES_I_SAP_GLS_Production_Trn`,
  `XMES_I_SAP_LS_Production_Trn`. These are candidates for "why didn't this
  get created at all" (as opposed to "created but failed") investigations.
- **`dbo.MES_SAP_*_Trn_Tbl` family** — the downstream transaction tables:
  `MES_SAP_Production_Trn_Tbl`, `MES_SAP_Consumption_Trn_Tbl`,
  `MES_SAP_By_Product_Trn_Tbl`, `MES_SAP_RR_Trn_Tbl`, `MES_SAP_UD_Trn_Tbl`,
  `MES_SAP_UsageDecision_Trn_Tbl`, `MES_SAP_WO_Trn_Tbl`,
  `MES_SAP_WorkOrder_Movements_Trn_Tbl`, `MES_SAP_Inventory_Stock_Tbl` /
  `_Data_Tbl`. Reasonable rule of thumb: `MES_SAP_*_Trn_Tbl` = domain-side
  record of what happened; `SAP_Posting_Tbl` = the actual outbound SAP call
  and its result. A ticket about a mismatch between "what MES shows" and
  "what SAP shows" likely means comparing these two layers.
- **`dbo.SAP_Posting_Data_ByHeat_Usp`** — despite the word "Data" in the
  name, this is **not a read**. It writes pending production/consumption
  rows. Don't call it during investigation without understanding what it
  will insert (per `Knowledge/sql-write-model.md`'s "inspect before you
  trust" rule — this exact procedure is the KB's own worked example of that
  rule).
- **`dbo.XBatch_SAP_Material_Prod_Cons_Usp`**, **`XBatch_RM_SAP_Inventory_Billet_Usp`**
  — named like reporting/rollup procedures for production/consumption and
  billet inventory respectively; verify with `get_sql_object_definition`
  before assuming read vs. write.

## Historian

**Ticket smell:** "trend/chart not showing data", "tag stuck", "meter/sensor
reading flat", anything mentioning a chart or historian value.

- **The actual historian time-series data does NOT live in
  `XStudio_Xbatch`.** It lives in separate per-period databases on the same
  server: `XHS_History_<YYMMDDNN>` (one per backup cycle — dozens exist,
  e.g. `XHS_History_26060909`) and `XHS_Buffer_<range>` (live/recent buffer
  windows, e.g. `XHS_Buffer_26_6_17_15_TO_26_6_17_18`). Confirmed via
  `sys.databases` on 10.2.6.204 — this is not a guess. Do not search
  `XStudio_Xbatch` for tag/channel values; you won't find them there.
- **`dbo.XBatch_Get_Historian_Channels_By_Process_Cell_Usp`**,
  **`XBatch_Get_Historian_Collector_Usp`**,
  **`XBatch_Get_Historian_Tags_By_Type_DataSource_Usp`** — these live in
  `XStudio_Xbatch` and are the *configuration/lookup* layer (which
  tag/channel belongs to which process cell/collector/data source), not the
  time-series values themselves. Use these to resolve a human-facing
  "Meter 3" or tag name to its actual channel/collector identity before
  looking for values in the `XHS_*` databases.
- **`dbo.HistorianBackupLog`** — a backup-job log (168 rows, columns
  `DatabaseName`, `BackupRunDate`, `BackupPath`, `Success`, `Notes`), not
  live data. Useful only for "is the historian backup job itself healthy,"
  not for "why is this tag not updating."
- **`dbo.sp_All_Historian_DB_Full_Backup`** — the backup job itself. Not an
  investigation target under normal circumstances.

## Production / tracking (heat, billet, furnace)

**Ticket smell:** "billet count wrong", "heat stuck at position", "furnace
tracking not updating", CCM/RM area complaints.

**For EAF/LRF/CCM/Billets/SMS-process-time complaints specifically, check
`Knowledge/sohar-sms-event-workflows.md` before this section** — it documents
the real event state conditions and workflow SQL behind `EAF_PER_HEAT`,
`LRF_Per_Heat`, `CCM_Per_Heat`, `BilletsCastCount`, and
`SMS_Plant_Process_EventTime` (sourced from the vendor's own project
handover docs, confirmed against the live schema), which explains *why* a
value is missing/wrong, not just where it lives.

- Log/tracking tables by area, confirmed present: `CCM_LogSheet_Ladle_Details`,
  `EAF_LogSheet_Consumption`, `EAF_LogSheet_Ladle_Addition` (+ `_Audit`),
  `EAF_LogSheet_Ladle_Details`, `EAF_LogSheet_Quantity`,
  `RM_Billet_Charging_And_Discharging_Logsheet` (+ `_Audit`),
  `RM_Furnace_Logbook` (+ `_Block`), `RM_LogBook_For_Stand_Assembly` (+ `_Audit`),
  `RM_TC_Grinding_Logbook` (+ `_Audit`), `Power_Consumption_LogSheet` (+ `_Audit`).
  Area in the ticket (`AreaID`/`HermesAreaName`, e.g. `EAF`, `CCM`, `LRF`,
  `Rolling Mill Stands`) is a strong hint for which log-family to check first.
- **`XMES_BilletPosting_Validation_Usp`** — validation logic around billet
  posting; a natural first stop for "billet count is wrong" tickets. Read
  its live definition before assuming what it validates.

## Work order execution

**Ticket smell:** "work order not created", "WO stuck in SAP", "work order
quantity/material wrong", campaign/rolling-mill scheduling complaints.

- **`dbo.XBatch_Work_Order_Mst_Tbl`** — the master work order record.
  Managed through **`dbo.Xstudio_XBatch_Work_Order_Mst_Tbl_USP`** (standard
  `@ID`/`@Mode` CRUD-style procedure, XStudio's usual generated-CRUD pattern
  — confirm `@Mode` values live before calling).
- **`dbo.XMES_WorkOrders_Creation`** — the actual work-order generation
  logic, confirmed by reading its live definition: takes `@CampaignID`,
  `@StartDate`, `@EndDate`, builds a `@WOTable` from Sales Order data with
  separate branches per product type (its own comments show "BRANCH 1: RB
  (Reinforced Bar) - Grouping by Length" as one branch). A "work order never
  appeared" ticket is a call to trace through this procedure for the
  relevant `@CampaignID`/date range, not just check the master table.
- **`dbo.MES_SAP_WO_Trn_Tbl`**, **`MES_SAP_WorkOrder_Movements_Trn_Tbl`** —
  the SAP-side transaction tables for WO creation/movement, matching the
  `MES_SAP_*_Trn_Tbl` pattern documented in the SAP section above.
- **`dbo.XMES_SAP_WorkOrder_Creation_API_Error_Usp`** — logs API failures
  for WO creation specifically (confirmed live: params `@RecordID`,
  `@TransactionID`; header comment "store API error response for Work Order
  Movement" — note the comment says "Movement" even though the name says
  "Creation," a real naming/comment mismatch worth remembering when
  searching by keyword). Same family as `XMES_SAP_*_API_Error_Usp` in the
  SAP section — same "read what it writes to, don't assume" rule applies.
- **`dbo.XMES_Work_Order_Trn_Tbl`** — a separate transaction table (0 rows
  as of 2026-09-02, plain audit-column schema, no WO-specific columns of its
  own beyond `Source`/`ReportDate`/`IsProcessed`) — currently unused or very
  early in adoption; don't assume it holds meaningful history yet.
- **`dbo.XBatch_Material_Item_Cons_Per_WorkOrder_Tbl`** /
  **`_Prod_Per_WorkOrder_Tbl`** — consumption/production rollups keyed per
  work order; useful for "quantity doesn't match" tickets.
- **`dbo.Xbatch_SMS_WorkOrder_Wise_Consumption_Usp`** — an SMS-area
  (Steel Melt Shop) consumption-by-work-order report/lookup procedure;
  verify read vs. write before use, per the standing rule.

## Quality (RR / UD / spectro / chemistry)

**Ticket smell:** "quality result missing", "usage decision not posted",
"RR not generated", "spectro/chemistry data wrong", grade/deviation
complaints.

- **RR** = Repeat Result / Rework Request context, **UD** = Usage Decision
  (SAP QM concept — the decision to accept/reject/use-with-restriction a
  batch). `dbo.MES_SAP_RR_Trn_Tbl` and `dbo.MES_SAP_UsageDecision_Trn_Tbl`
  (alongside the shorter-named `MES_SAP_UD_Trn_Tbl`) are the transaction
  tables for these — same `MES_SAP_*_Trn_Tbl` family as the WO/production
  tables above, so treat them the same way: domain-side record of a
  quality-decision event, cross-check against `SAP_Posting_Tbl` for whether
  it actually made it to SAP. No dedicated `MES_SAP_RR`/`UD`-specific error
  or creation procedure was found by name search (`grep`'d for `_RR_`/`_UD_`
  patterns, none matched) — check `SAP_Posting_Tbl.PostingType`/
  `MovementType` for RR/UD-tagged rows instead, or search
  `find_sql_objects` live rather than trusting this gap is permanent.
- **`dbo.Quality_Spectro_File`**, **`_Result`**, **`_Sample`** — spectrometer
  (chemical composition) data pipeline: file ingestion → sample → result.
  A "chemistry result missing" ticket likely means tracing a specific heat
  through this three-table chain to find where it stopped.
- **`dbo.Chemistry_Deviation_Quality_Data`**, **`Heat_Chemistry_Quality_Data`**
  — heat-level chemistry results and deviations from target grade
  chemistry.
- **`dbo.Rebar_Quality_Data`**, **`Rebar_Coil_Quality_Data`**,
  **`Round_Bar_Quality_Data`** — finished-product quality records, one
  family per product shape. Match the ticket's product type to the right
  table rather than guessing.
- **`dbo.Quality_Deviation_Master`** — deviation reference/master data (not
  transactional) — useful for resolving a deviation code to its meaning.
- **`dbo.MES_Quality_Configurator`** — quality rule/threshold configuration,
  not transactional data; relevant only if a ticket is about wrong
  pass/fail thresholds rather than a specific result.
- Several `Temp_*`-prefixed tables turned up in the same grep sweep
  (scratch/staging tables) — ignore these for investigation purposes unless
  a specific procedure's definition shows it deliberately reads from one.

## Delay / OEE

**Ticket smell:** "delay not recorded", "OEE/downtime wrong", "shift delay
entry missing or duplicated", equipment/agency-attributed downtime
complaints.

- **`dbo.Delay_Trn_Tbl`** (1,931 rows, spans 2025-09-02 to 2026-01-06) — the
  central delay transaction table. Real columns beyond the standard audit
  set: `EquipmentID`, `ReportDate`. Delay rows are attributed to equipment,
  not directly to an agency/category in this table — those live in the
  companion tables below.
- **`dbo.DelayTypeMST`**, **`DelayCategory_Master`**, **`DelaySubType_Master`**,
  **`DelayAgency_Master`** — reference/lookup tables for delay
  classification (type, category, subtype, responsible agency). Resolve a
  delay's classification here rather than guessing from a code.
- **`dbo.Agency_Wise_Delay`**, **`Equipment_Wise_Delay`** — rollup/summary
  tables, one row per agency or equipment aggregate, not per-event. Managed
  via **`dbo.Xstudio_Agency_Wise_Delay_USP`** (confirmed live: standard
  `@ID`/`@Mode` procedure whose real body recalculates a derived
  `Durationmmss` display column from `Duration` on update — a good example
  of a CRUD procedure that also carries real business logic, not just a
  pass-through).
- **`dbo.ShiftDelayEntry`** (+ `_Audit`, `_Transaction_Operator`),
  **`RMShiftDelayEntry_CAPA`**, **`SMS_DelayEntry_CAPA`**,
  **`SMS_Delay_Trn_Tbl`**, **`RM_Delays`** — area-specific shift-level delay
  entry tables (RM = Rolling Mill, SMS = Steel Melt Shop). Same
  area-name-in-table-name pattern as the production/tracking log tables
  above — match the ticket's `AreaID` to the right prefix.
- Managing procedures worth noting by name (not yet read in full):
  `Xstudio_ShiftDelayEntry_USP`, `ShiftDelayEntry_Update_usp`,
  `ShiftDelayEntry_ManagerOperatorName_Usp`,
  `SMS_AgencyWiseDelayDuration_Validation_Usp`,
  `SMS_EquipmentWiseDelayDuration_Validation_Usp`,
  `SMS_DelayRemainingDuration_U_Usp`, `XMES_Delay_Split_Entry_Usp` /
  `_Validate_Usp` (splitting one delay event into multiple), `MES_U_Delay_Merge`
  (the inverse — merging delay entries), `XBatch_SMS_MES_Delay_Dashboard_SP` /
  `XMES_SMS_Dashboard_Delay_USP` (dashboard/reporting reads). Read the
  specific one relevant to a ticket before trusting its name.

## Billet / yard / inventory

**Ticket smell:** "billet missing from yard", "genealogy/traceability
broken", "inventory count wrong", switchyard status complaints.

- **`dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl`** — traceability record linking
  a billet back to its cast/strand. Real columns beyond standard audit set:
  `CutEventID`, `Status`, `ChargeType`, `StrandSequence`, `IsProcessed` (0
  rows as of 2026-09-02 — likely a newer or low-volume table; confirm
  current row count live before assuming it's empty in production, this
  snapshot may be stale by the time you read it). This is the table to
  check for "which cast did this billet come from" / genealogy-broken
  tickets.
- **`dbo.Billet_Inventory`** (+ `_Audit`, `_View`, `_View_Audit`; 142 rows,
  spans 2025-07-04) — yard inventory positions. Real columns:
  `Description`, `ExpiryDate`, `GradeID`. The `_View`/`_View_Audit` variants
  suggest a reporting layer on top of the base table — check which one a
  complaint's UI actually reads from before assuming the base table is the
  source of truth.
- **`dbo.Outdoor_SwitchYard_Status`** — switchyard (electrical, not
  billet-yard) status table — don't confuse with billet yard despite the
  shared "yard" keyword; relevant to power/equipment-availability
  complaints, not material tracking.

## API transaction summary (cross-cutting diagnostic surface)

**Ticket smell:** any integration complaint where the specific domain isn't
obvious yet, or "check if this even reached the system" — a good
first-stop before committing to one of the domain sections above.

- **`dbo.XMES_Get_API_Transaction_Summary`** — confirmed live: single
  parameter `@APIType varchar(300)` (example usage in its own header
  comment: `'UsageDecision'`), reads from
  `XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl`
  (**note: a different database** — the config DB, not `XStudio_Xbatch`
  itself), deduplicates to the latest row per `TransactionID`, and excludes
  `CallerName IN ('API Parameter Mapping', 'API Test')` noise rows. This is
  the single best cross-domain "did this API call happen and what was the
  result" lookup — call it with the relevant `@APIType` (values look like
  SAP operation names, e.g. `UsageDecision`) before diving into a specific
  domain's own error-log procedures.
- **`dbo.XMES_I_API_Transaction_Summary`** — the insert-side counterpart
  (the "I" prefix matches the `XMES_I_SAP_*` insert-family convention in
  the SAP section); not yet read in full — verify before assuming it's a
  pure insert.
- **`dbo.XMES_API_Transaction_Summary_Fact_Tbl`** (30,595 rows, all rows
  timestamped 2026-03-12 17:02:45 — a single bulk-load timestamp, not a
  rolling live feed as of this export) — a fact/rollup table over the same
  transaction data, likely a reporting snapshot rather than the live
  source; prefer `XMES_Get_API_Transaction_Summary` (queries the live
  `XStudio_API_Error_Log_Mst_Tbl`) for current-state investigation, and use
  this fact table only if a ticket is specifically about a historical
  report/dashboard number.

## How to use this file during an investigation

1. Match the ticket's `AreaID`/`ProblemCategory`/keywords against a section
   above to pick a starting table/SP family — don't start from a blank
   `find_sql_objects` search if this file already names a plausible target.
2. Still verify live — `get_sql_object_definition` the specific
   table/procedure before trusting what it does, and re-run
   `find_sql_objects` for anything not covered here. This file is a map to
   the right neighborhood, not a substitute for looking at the actual
   street.
3. If you find a table/SP family that belongs here and isn't listed, that's
   exactly the kind of thing worth adding — extend this file rather than
   re-discovering it cold on the next ticket in the same area.
