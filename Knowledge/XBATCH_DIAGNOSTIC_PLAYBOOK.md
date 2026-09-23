---
type: "Playbook"
title: "XBatch Diagnostic Playbook -- where XBatch breaks and where to look"
status: draft
verified: "2026-09-23 (live survey of XStudio_Xbatch, XStudio_Configuration_Xbatch and msdb on 10.2.6.204)"
sources: "live sys.tables/sys.triggers/msdb job history; XMES_Log_Trn_Tbl, XMES_SAP_API_*_Error, response_error, XStudio_API_*_Log samples; Knowledge/sohar-sms-event-workflows.md (vendor handover docs); Knowledge/xbatch-investigation-surfaces.md"
---

# XBatch Diagnostic Playbook

L2 tickets arrive because **XBatch did not do something it should have**: an event did not fire,
a workflow procedure stopped partway, a value was computed wrong, an SAP/API call failed, a feed
stopped updating, or master/config data is wrong. This playbook maps each failure class to the
exact evidence surfaces that prove or disprove it, in the order an L2 engineer would check them.

Every check is read-only. The planned diagnostic procedures (section 4) run each class's checks
in one call so the harness, not a model, gathers the evidence.

## 1. How XBatch works (the machinery that fails)

```
Historian tags (XHS_History_*, XHS_Buffer_* databases)
   │  state conditions evaluated by the X-Force event framework
   ▼
<Area>_SMS_Event_State_Mst_Tbl  (StateCondition, IsActive, StateOn/OffWorkFlow, IsErrorState)
   │  state ON → Entered action, state OFF → Completed action
   ▼
XSTUDIO_WORKFLOW_<GUID>_SP  (generated per workflow + status; see sohar-sms-event-workflows.md)
   │  writes the per-heat event row and calls calculation/posting procedures
   ▼
Per-heat tables: EAF_PER_HEAT → LRF_Per_Heat → CCM_Per_Heat → BilletsCastCount
Timing chain:    SMS_Plant_Process_EventTime (states 1–14, 18)
Genealogy:       XMES_CCM_Billet_Genealogy_Trn_Tbl
   │  material postings via XBatch_I_Material_Produce/Consume_NoBOM_USP (lots LS_<heat>, GLS_<heat>)
   ▼
MES_SAP_*_Trn_Tbl (domain record)  →  SAP_Posting_Tbl (outbound call)  →  SAP via CPI
   │  failures land in
   ▼
XMES_SAP_API_<Op>_Error  +  response_error  +  XStudio_Configuration_Xbatch.XStudio_API_Error_Log_Mst_Tbl
```

Also running:
- **SQL Agent jobs** (msdb): `BilletOneMinutestde` runs `BilletsPosition_InFurnace_Usp` every minute;
  backup jobs `Database Daily Backup`, `Database Backup Weekly`, `Database Transaction Log`.
- **Procedure step logging**: `XMES_Log_Trn_Tbl` (4.8M rows). Instrumented procedures write one row
  per step: `Name` = procedure, `Type` = process, `Status` = `"<n> <step> Start|End"`. A run that
  stops after a `Start` with no matching `End` shows exactly where it failed.
- **Table triggers**: `XStudio_TRG_<table>` on most business tables (audit/sync; enabled).

## 2. Failure classes

| # | Class | Typical ticket wording | First evidence |
|---|---|---|---|
| A | **Event did not fire / record missing** | "heat 1604014 not showing in LRF report", "no CCM data for last heat" | per-heat row exists? `SMS_Plant_Process_EventTime` states for the heat; event state config |
| B | **Record exists, value wrong** | "arcing time too low", "billet tonnage wrong", "grade copied wrong" | the computing workflow's formula + its inputs (SMS block window, "most recent" lookups, HeatID-1 offset, calculated columns) |
| C | **Downstream step did not run** | "billet tracking not updated", "electrode life not updating", "daily production missing" | did the Completed action run (log steps, target-table timestamps)? which downstream proc did not |
| D | **SAP / API integration failed** | "not showing in SAP", "posting stuck", "usage decision not posted" | `SAP_Posting_Tbl` status → per-API error tables → `response_error` → config API error log |
| E | **Feed stopped / not updating** | "values not updating since 6 PM", "screen frozen", "sensor stuck at zero" | last-arrival per feed table vs cadence; job outcomes; log activity per procedure; historian buffer freshness |
| F | **Master/config data wrong** | "wrong billet size", "grade missing", "work order not running" | master tables (Grade_Master, Billet_Cross_Section, XBatch_Work_Order_Mst_Tbl, Status_Mst_Tbl) |
| G | **Report/dashboard number wrong** | "daily carbon consumption doubled", "shift report wrong" | summary table vs its per-heat source for the same period; view definition |
| H | **How-to / clarification** | "which delay code to use" | knowledge base / vendor docs, no data check |
| I | **Change request** | "add an export button" | human (L3), no diagnosis |

## 3. Checks per class (in order)

### A. Event did not fire / record missing
1. Does the per-heat row exist in the expected table (EAF_PER_HEAT / LRF_Per_Heat / CCM_Per_Heat /
   BilletsCastCount) for the heat? If yes, this is class B or C, not A.
2. Which `SMS_Plant_Process_EventTime` states exist for the heat, in order? The last state reached
   shows where the ladle/process chain stopped (e.g. reached "LRF Roof Open" but never
   "Ladle At CCM Arm N Rest Position").
3. Adjacent heats: does the neighbouring heat have the row instead? Known attribution traps:
   - LRF Entered takes the **most recent** EAF_PER_HEAT row, not a keyed match;
   - CCM resolves arm/heat from the **most recent** matching event;
   - SMS process-time states 11+ store `@HeatID - 1` (vendor-flagged off-by-one).
4. Event configuration for the area: state `IsActive`, `IsWorkFlowEnable`, `StateCondition`,
   `IsErrorState` in `<Area>_SMS_Event_State_Mst_Tbl`; action rows in `<Area>_SMS_Event_Action_Mst_Tbl`.
5. If the state never went ON: historian tag values in the `XHS_*` databases for the window
   (condition tags e.g. Tapping1, LivePowerONTime, cast-position/ladle-weight tags).

### B. Record exists, value wrong
1. Read the row and the column's origin: stored vs **calculated at display** (EAF HeatTime,
   TapTimeMinute, YieldPerHeat, ThroughputTPH, LSDELTA are ColumnEquation display values).
2. Recompute from inputs in code:
   - Billet weight = `ActualBilletsCountByOperator × 12 × Billet_Cross_Section.MaterialSpecificWeight`
     (operator count, not the tag count; literal 12);
   - EAF material totals = sum of auto+manual CH1–CH4 from `SMS_EAF_Per_Heat_ChargeMix`;
   - LRF power/arcing/argon copied from the SMS block table valid for `@StartTime`.
3. Check the lookup that feeds it (most-recent-record traps in A.3; SMS block time window;
   hardcoded cross-section 130 → Billet_130X130 else 150X150; grade default '3SP/PS').

### C. Downstream step did not run
1. Did the parent Completed action run? Target-table `ModifiedOn` after the event; `SAPWorkflowStatus`.
2. For instrumented procedures: last `XMES_Log_Trn_Tbl` steps for that procedure around the time —
   last `Start` without `End` = the failing step.
3. Which downstream table was not written: `XMES_ActiveLife_Element_Mst_Tbl` /
   `XMES_Life_Tracker_Register_Mst_Tbl` (life), `XMES_I_Billets_Tracking_Usp` outputs (billet
   tracking), `XBatch_SMS_Heat_Tracking_Daily_Production_Data` (daily production),
   `XMES_BackCalculation_GLS_Usp` (GLS).

### D. SAP / API integration failed
1. `SAP_Posting_Tbl` rows for the heat/work order/batch: `IsProcessed`, `SAP_Status`,
   `SAP_DocumentNo`, `SAP_Message`. Populated message + no document = stuck/failed posting.
2. `MES_SAP_*_Trn_Tbl` (domain record) vs `SAP_Posting_Tbl` (outbound call) for the same key: a
   domain row with no posting row means the posting was never created.
3. Per-API error tables (verified columns: TransactionID, RecordID, Body, ErrorMessage, Status,
   Type, Batch, ManufacturingOrder, Material, MovementType, SuccessMessage):
   `XMES_SAP_API_GoodsMovement_Error`, `_Batch_Characteristics_Error`, `_Batch_Creation_Error`,
   `_UsageDecision_Error`, `_ResultRecording_Error`, `_PlantToPlantTransfer_Error`,
   `_WorkOrderCreation_Error`, `_Inventory_Error`. Match by Batch (`LS_`/`GLS_` + heat), MO, Material.
4. `response_error` (TransactionID → raw CPI response, e.g. "Property Plant is mandatory for
   GoodsMovement", "content of element <Material> is empty").
5. `XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl` (APIName, APIStatus,
   CallerName, TransactionID, Message, StackTrace) and `XStudio_API_Request_Log_Trn_Tbl` /
   `XStudio_API_Timeline_Log_Trn_Tbl` for the request lifecycle.
6. Cross-API summary: `XMES_Get_API_Transaction_Summary @APIType` (already allowlisted).

### E. Feed stopped / not updating
1. Last arrival per feed table vs its normal cadence (per-heat tables: minutes to hours; process
   events; billet position every minute; logs every minute).
2. SQL Agent job last outcome and last run (`msdb.dbo.sysjobhistory`).
3. Last `XMES_Log_Trn_Tbl` activity per instrumented procedure.
4. Historian: newest `XHS_Buffer_*` / `XHS_History_*` database and its latest data.

### F. Master/config data wrong
Resolve the entity's reference rows directly: `Grade_Master`, `Billet_Cross_Section`,
`XBatch_Work_Order_Mst_Tbl` (status, running work order per area), `Status_Mst_Tbl`,
`Product_Master`, `Storage_Location_MST`, `Plant_Name_MST`.

### G. Report/dashboard number wrong
1. Identify the summary table (`EAF_Summary_Day`, `LRF_Summary_Day/_Shift`, `CCM_Summary_Day`,
   `SMS_Production_Summary(_Day)`, `Ngconsumption_Summary_Day`, ...) and its period.
2. Aggregate the per-heat source for the same period in code and compare; a mismatch localises
   to the rollup; a match means the source data itself is the issue (go to B).
3. Note tables the vendor marks **Not used** (e.g. `Agency_Wise_Delay`, `CCM_Summary_Shift`,
   `Equipment_Wise_Delay`) before blaming them.

## 4. Planned diagnostic procedures (read-only, one call per class)

All in XStudio_Helpdesk, reading XBatch/config/msdb cross-database, parameterised, audited through
`Hermes_L2_Execute_SQL_Usp` like every other read.

| Procedure | Input | Returns |
|---|---|---|
| `Hermes_Diag_Heat_Journey_Usp` | @HeatID | one row per stage: process-time states, EAF/LRF/CCM/billet rows, genealogy count, lots LS_/GLS_, SAP postings, API errors for those batches, with timestamps and status (classes A–D in one timeline) |
| `Hermes_Diag_SAP_Trace_Usp` | @HeatID / @WorkOrder / @Batch / @MaterialDocument | domain rows, posting rows, every per-API error, raw responses, config API log for the matched transactions (class D) |
| `Hermes_Diag_Feed_Health_Usp` | @Since | last arrival per feed table vs cadence, job outcomes, log activity per procedure, newest historian database (class E) |
| `Hermes_Diag_Procedure_Run_Usp` | @ProcName, @Since | runs from XMES_Log_Trn_Tbl with last step reached and incomplete runs (class C) |
| `Hermes_Diag_Event_Config_Usp` | @Area | event states, conditions, workflow flags, actions (class A.4) |
| `Hermes_Diag_WorkOrder_Journey_Usp` | @WorkOrder | master row, per-heat usage, consumption/production rollups, SAP WO transactions and errors |

## 5. How the harness uses this

1. Jev classifies the ticket into A–I (choice) and aligns ticket spans to the entity (heat, work
   order, batch, material document) with the entity's diagnostic procedure as the target.
2. The harness runs that class's diagnostic procedure(s) and flattens the result into numbered lines.
3. Jev picks the lines that explain the complaint and judges whether they settle it; code does all
   arithmetic and time comparisons.
4. Settled → templated reply citing the lines; not settled → L3 with the full diagnostic attached;
   class H → knowledge answer; class I → human.

## 6. Current environment facts (live, 2026-09-23)

- **Plant process data is frozen at 2026-07-08** (per-heat, genealogy, SAP API errors); this server
  is a snapshot copy. Only the rolling-mill procedures (`BilletsPosition_InFurnace_Usp`,
  `XBatch_RM_BilletWiseNGConsumption`) are still running and logging.
- **All three backup jobs failed on every run in the last 30 days** (weekly 4/4, daily 31/31,
  transaction log 50/50). This is an operational fault independent of the helpdesk.
- Event error tables (`*_Event_Error_*`, `*_Interlock_Error_*`) and `XStudio_Workflow_Action_Error_Log`
  are empty: event/workflow failures are **not** recorded there, so they must be inferred from missing
  rows, process-time states and step logs.
