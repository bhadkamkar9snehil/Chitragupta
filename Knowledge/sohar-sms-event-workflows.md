---
type: "Reference"
title: "SMS (EAF/LRF/CCM) Per-Heat Event & Workflow Internals -- Sohar Steel Oman"
description: "Real event/state-machine/workflow-SP internals for the EAF, LRF, CCM, Billets Cast Count, and SMS Plant Process Time per-heat data flows in XStudio_Xbatch, sourced from the vendor's own project handover documents (SITC of X-Force Historian and Dashboard Development, Sohar Steel Oman). Confirms XStudio_Xbatch on 10.2.6.204 IS the Sohar Steel Oman plant."
status: draft
verified: "2026-09-02"
source: "Vendor handover docs supplied by the user (Sohar_Data.zip), preserved at Reference Documents/Sohar_Vendor_Docs/ (EAF/LRF/CCM/Billets/SMS Plant Process Time Doc.docx + Sohar Entities.xlsx), authored by Mahesh Udar, Document Version 1.0. Not live-queried SQL -- treat as design documentation, verify against the live server before trusting a specific value/GUID for a live investigation."
---

# SMS Per-Heat Event & Workflow Internals (Sohar Steel Oman)

This file is a level below `xbatch-investigation-surfaces.md` — it doesn't just
name tables, it documents **why they get written to and by what logic**: the
X-Force/XStudio Event Framework configuration (tag mapping, state conditions)
and the actual T-SQL inside each workflow's Entered/Completed stored-procedure
actions, for the EAF → LRF → CCM → Billets production chain.

**Why this matters for L2 investigation:** most "why is this heat/billet data
wrong or missing" tickets are really asking "did the event state condition
fire, and did the workflow action run correctly" — a question the plain
schema/SP-name map can't answer. This file can.

## Confirmed: this is the same system as `XStudio_Xbatch` on 10.2.6.204

`EAF_PER_HEAT`, `LRF_Per_Heat`, `CCM_Per_Heat`, `CCM_Data`,
`SMS_Plant_Process_EventTime`, `BilletsCastCount` all exist in the live schema
export (`Reference Documents/XStudio_Xbatch_Schema.md`), confirmed
2026-09-02. Treat every table/procedure name below as a real, live object on
this project's server — but the specific GUIDs, tag names, and SQL text are
from the vendor's design document, not a fresh live pull; re-verify with
`get_sql_object_definition` before relying on exact current behavior for a
ticket, since this document (v1.0, undated handover) may predate schema
drift.

## The production chain, in order

**EAF (melt) → LRF (ladle refining) → CCM (continuous casting) → Billets Cast
Count**, with **SMS Plant Process Time** as a single, longer state chain that
runs in parallel across all three areas to track ladle-car and turret timing
end-to-end. Each area writes its own per-heat "Event" entity when a real-time
tag condition (state) becomes true; workflow actions (Entered / Completed)
then compute and post the derived, cross-referenced values.

**Common patterns across all four flows** (worth knowing before reading any
one section in detail):
- Every state condition is built from live historian tag reads (via named
  `_PRM`/`_STATUS` tags), evaluated as `IIF(<ON-condition>, True,
  IIF(<OFF-condition>, False, Null))` — a nested ternary, not a simple
  boolean, so a tag combination outside both branches leaves the state
  unchanged (Null), not necessarily "off."
- `WorkflowStatus` (or `@p_Status`) drives Entered → Completed; the *Entered*
  action typically resolves identity (which heat/work order this is) and
  posts a **consumption** transaction; the *Completed* action typically
  posts calculated **production** totals and triggers downstream
  calculation procedures.
- Liquid-metal/material postings all go through
  `XBatch_I_Material_Produce_NoBOM_USP` / `XBatch_I_Material_Consume_NoBOM_USP`
  with a generated lot number (`LS_<HeatID>` at EAF/LRF-entered stage,
  `GLS_<HeatID>` at LRF-completed/CCM stage) — a ticket about a missing or
  duplicate lot number is a cue to check which of these two lot-numbering
  points is involved.
- Every flow ends its Completed action by updating the
  `XMES_ActiveLife_Element_Mst_Tbl` / `XMES_Life_Tracker_Register_Mst_Tbl`
  pair for a hardcoded `ParentID` GUID (life-tracking for consumable
  equipment parts — electrodes, mould tubes, etc.) — if a life-tracker
  "didn't update," that's a symptom of the *parent workflow* not completing,
  not a separate life-tracking bug.
- `SMS_Data_list_View` is called from several Entered actions as a generic
  "data list" refresh action — its own definition wasn't in this handover
  set; treat as a UI/report-refresh trigger, not a data source, until
  verified live.

## EAF — Per Heat Data Insert Flow

- **Event entity:** `EAF_PER_HEAT`. **Trigger:** `HeatIDChange` event.
- **State condition:** `IIF(Tapping1=1 AND LivePowerONTime>0, True,
  IIF(Tapping1=0 AND LivePowerONTime=0, False, Null))` — heat capture turns
  on during tapping with power-on time accumulated, off when tapping has
  stopped and power-on time is reset.
- **~40 tag-mapped attributes** covering charge weights per material
  (Copex Scrap, HMS1, HMS1/2, End Cuts, Briquette, Bundle LMS, HBI/DRI,
  Shredded, Scull — each split across up to 4 charge numbers CH1–CH4),
  consumption (lime/dolo/carbon/NG/oxygen), power/energy, and the EAF
  temperature.
- **Entered action:** resolves heat start time from `EAF_ProcessTime`
  (`Status = 'heat start'`), finds the running EAF work order in
  `XBatch_Work_Order_Mst_Tbl`, retrieves steel grade from the historian via
  `XHS_Retrieve_Tag_Full_Value_Usp` for a 1-minute window ~10 minutes before
  heat start, then activates the relevant life-element/life-tracker rows.
- **Completed action:** sums each material's auto+manual charge weights
  across CH1–CH4 from `SMS_EAF_Per_Heat_ChargeMix`, resolves HBI vs. CDRI
  bin consumption (bin 3/4 name-dependent branching — a bin literally named
  `'cdri'` routes to `@CdriConsumption`, anything else to
  `@HBIConsumption`), writes the totals to `EAF_PER_HEAT`, runs
  `HeatChargeMixConsumption`, posts a liquid-metal **production** transaction
  (`LIQUID METAL`, grade `'TBD'`, lot `LS_<HeatID>`) when
  `@LiquidMetal > 0`, pulls automatic ladle-addition quantities from
  `LadleAddition` (lime = Silo3+Silo4, dolomite = Silo8, SiMn =
  Silo5+Silo6, FeSi = Silo7), then runs work-order/sales-order calc, per-heat
  temperature calc, historian attribute calc, and spray-cooling
  flow-duration calc.
- **`EAF_PER_HEAT` LV columns** (from the vendor's own source definition):
  real (non-calculated) columns include `HeatID`, `HeatReportDate`,
  `StartTime`/`EndTime`, all per-material weights, `TotalChargeWeightMT`,
  `SteelGrade`, `PowerOnTimeMinute`/`Second`, `LiquidMetalWeight`,
  `WorkOrder`, `SAPWorkflowStatus`, `TapTemp`, `EAFTemperature`. Notable
  **calculated** columns (`ColumnEquation`, computed at display time, not
  stored): `HeatTime` (mm:ss from minute/second parts), `TapTimeMinute`
  (`DATEDIFF` between StartTime/EndTime), `YieldPerHeat` (liquid metal ÷
  total charge weight × 100), `ThroughputTPH`, `LSDELTA` (calc vs. actual
  liquid metal weight delta — a ticket about "yield/throughput looks wrong"
  is checking a *formula*, not stored data; read the equation before
  assuming the underlying numbers are bad).

## LRF — Per Heat Data Insert Flow

- **Event entity:** `LRF_Per_Heat`. **Trigger:** `LRF_Per_HeatData` event,
  **state:** `LRF Start`, condition simply `ActualPowerOnTime > 0` (not a
  nested IIF, unlike EAF).
- **Entered action:** finds the running LRF work order, pulls the **most
  recently created** `EAF_PER_HEAT` record (heat ID, liquid metal weight,
  lot no, steel grade, report date) — note this is "most recent," not
  matched by a shared key, so a delayed/out-of-order EAF completion could
  make LRF pick up the wrong heat's data; worth checking on a "wrong grade
  copied to LRF" ticket. Updates `LRF_SMS_Data.LRFGrade`, posts a liquid-metal
  **consumption** transaction (lot `LS_<HeatID>`) when applicable, then
  dynamically resolves which SMS "block" table (`XStudio_Block_Entities_Mst_Tbl`
  / `XStudio_Block_Databases_Mst_Tbl`, time-windowed by `@StartTime`) holds
  this heat's live process values and copies power/arcing/argon/energy/alloy
  values from it into `LRF_Per_Heat` via dynamic SQL (`SP_EXECUTESQL`) —
  **the SMS block resolution is itself time-window-dependent**; a wrong or
  missing value here is worth checking against the block table's
  `StartTime`/`EndTime` validity window, not just the tag mapping.
- **Completed action:** reads `'Treatment Start'` timing from
  `LRF_ProcessTime`, runs work-order/sales-order calc, posts a liquid-metal
  **production** transaction (lot prefix now `GLS_<HeatID>`, distinct from
  the `LS_` prefix used in the Entered stage — a ticket about "two different
  lot numbers for the same heat" is expected behavior at this
  Entered-vs-Completed boundary, not a bug), runs the LRF SMS-block historian
  calc, raw-material consumption (`XMES_LRF_I_Raw_Material_Cons_Usp`),
  updates the quality module's latest-spectro-sample flag, does the same
  life-element/life-tracker update as EAF (different hardcoded `ParentID`),
  then calculates per-heat temperature.

## CCM — Per Heat Data Insert Flow

- **Event entity:** `CCM_Per_Heat`. **Trigger:** two **parallel, independent**
  states — `Arm 1 Cast Position` and `Arm 2 Cast Position` — each its own
  nested IIF on that arm's cast-position tag and ladle-weight tag (`>10`
  tons to activate). Both arms share the same workflow action, so **the
  action resolves which arm/heat fired by querying the most recent matching
  event**, not by an arm-specific parameter — a ticket about "wrong arm's
  data got mixed into a heat" is a concurrency/ordering question on this
  shared resolution query, worth checking first.
- **Entered action:** resolves `@HeatID` from the latest
  `SMS_Plant_Process_EventTime` row with status in
  `('CCM Arm 1 Casting Position','CCM Arm 2 Casting Position')`, finds the
  running CCM work order (sales order, grade, material), pulls the most
  recent `LRF_Per_Heat` record for that heat (liquid metal weight, lot no —
  note the LRF-side lot no here is already `GLS_<HeatID>`, generated
  earlier in LRF's own Completed stage, then re-read here), posts a liquid
  metal **consumption** transaction, sets the CCM work order's `StartTime`
  only if not already set, and writes heat number + grade into `CCM_Data`.
- **Completed action:** on the **first ladle of the sequence only**
  (`@LadleSequence = 0`) records casting date/time into `CCM_Data`; updates
  the quality spectro-sample flag; falls back to EAF's `HeatReportDate` if
  still null; does the same life-element/life-tracker update; calculates
  per-heat temperature via `XMES_SMS_Temperature_Per_Heat_USP` for area
  `'CCM'`.

## Billets Cast Count — Data Insert Flow

- **Event entity:** `BilletsCastCount`. **Trigger:** `Cast Billets Count`
  process event, state `Billets Produces Start`, condition simply
  `CCMTotalBilletsCount > 0` (direct boolean, State-On → workflow `Entered`,
  State-Off → `Completed`; not the nested-IIF pattern).
- Only **3 tag-mapped attributes**:
  `CCMTotalBilletsCount`/`CCMHeatNO`/`ActualBilletCountByOperator` — the
  last one is an **operator-declared manual override**, distinct from the
  live-tag-driven `CCMTotalBilletsCount`; the Completed action uses the
  operator-declared value (`@ActualBilletsCountbyOperator`), not the raw tag
  count, for the final weight calculation — a ticket about "billet count
  doesn't match what's on the historian trend" may be comparing the wrong
  one of these two numbers on purpose.
- **Entered action:** resolves the relevant CCM heat from `CCM_PER_HEAT`
  (`Starttime < @StartTime`, most recent), syncs `HeatReportDate`/`ReportDate`
  from `EAF_PER_HEAT` where missing, derives billet item name from
  cross-section (**hardcoded**: `CrossSection = 130` → `Billet_130X130`,
  anything else → `Billet_150X150` — a ticket about a wrong billet item name
  for an unusual cross-section is this exact hardcoded fallback, not a
  config lookup), defaults grade to `'3SP/PS'` when null.
- **Completed action** (the most consequential one in this whole file —
  posts the actual production numbers):
  1. Increments **mould-tube life** (`Life_Tracking_Status` rows named like
     `'Mould Tube Life Strand %'`), logs to `Life_Tracking_Transaction_tbl`.
  2. Runs the CCM SMS-block historian calc, refreshes the spectro-sample
     flag, syncs `Heat_Chemistry_Quality_Data.Grade`/`Section` for the heat.
  3. Re-syncs `CCM_PER_HEAT` report dates from EAF again (same fallback
     pattern repeated).
  4. **Weight calculation — this is the formula that matters for any
     "billet tonnage is wrong" ticket:**
     `TotalBilletWeight = ActualBilletsCountByOperator * 12 * SetWeight`,
     where `SetWeight` comes from `Billet_Cross_Section.MaterialSpecificWeight`
     for the heat's cross-section (most recent, non-deleted row). **The
     literal `12` is hardcoded in this procedure** — billets are evidently
     counted/weighed in sets of 12; if that plant convention ever changes,
     this constant would need updating and is a real drift risk worth
     flagging if a weight ticket doesn't reconcile.
  5. Updates `CCM_Per_Heat` with count/weight/`SAPWorkflowStatus` (defaults
     to `'Entered'` if not already set — first time through this path sets
     the SAP posting cycle in motion).
  6. Runs `XMES_BackCalculation_GLS_Usp`,
     `XBatch_SMS_Heat_Tracking_Daily_Production_Data`, and
     `XMES_I_Billets_Tracking_Usp` — the downstream GLS/daily-production/
     billet-tracking chain. A "billet tracking never updated" ticket is a
     check of whether this Completed action ran at all (state condition
     never fired) versus one of these three downstream calls failing
     partway through.

## SMS Plant Process Time — the cross-area timing chain

**Event entity:** `SMS_Plant_Process_EventTime`, one ordered chain of states
(1–14, 18; 15–17 unused) spanning EAF roof-open through CCM turret control
off. This is the single richest timing/traceability surface in the whole
plant — every ladle-car and turret movement between EAF, LRF, and CCM is a
state transition here.

- **States 1–10 have workflow disabled.** They just read the *live* current
  value of `EAF_HEAT_NUMBER_PRM` at evaluation time — no heat-ID resolution
  needed because the live EAF heat is still the relevant one.
- **From state 11 onward, workflow is enabled**, because by then CCM is
  casting a heat that is *no longer* the live EAF heat — a stored-procedure
  action (below) has to resolve which historical heat this state actually
  belongs to.
- **State chain** (condition summarized; full detail in the source doc if a
  specific transition needs exact tag thresholds):
  1. EAF Roof Open For Fill Bucket Charging — roof open + zero power-on time.
  2. EAF Power On — active power > 10 MW (5s on-delay/10s off-delay debounce).
  3. Ladle Car At EAF — ladle car in position + power-on time > 0.
  4. EAF Tapping — tapping tag = 1 + power-on time > 0.
  5. Ladle Car Move From EAF To LRF — car left EAF, not yet at LRF, tapping
     occurred.
  6. Ladle Car Reach At LRF — car at LRF, roof still open, no arc time yet.
  7. LRF Roof Close — both roof indicators (E1/E3) agree closed.
  8. LRF Arcing — arc time > 0 while roof closed.
  9. LRF Roof Open — both roof indicators agree open (mirror of state 7).
  10. Ladle Move From LRF To CCM (**per arm**, Arm 1 and Arm 2 configured
      separately) — roof open + arc time was > 0 + that arm's instant
      weight still low (<10t, not yet arrived) vs. full (>75t, arrived).
  11. Ladle At CCM Arm N Rest Position (**per arm**, workflow enabled) —
      full ladle (>75t) present, cast-position tag 0→Entered / 1→Completed.
  12. Turret Rotation (**per arm**, workflow enabled) — turret lubrication
      running (rotating) vs. stopped, while that arm's ladle stays full.
  13. CCM Arm N Casting Position (**per arm**, workflow enabled) — cast tag
      = 1 + weight > 50t (actively casting) → Entered; cast tag = 0 + weight
      < 50t (ladle emptying) → Completed.
  14. Billets Production (workflow enabled) — `CCMTotalBillets > 0 AND
      CCMTurretControlOff = 0` (direct boolean, not nested IIF).
  18. CCM Turret Control Off (workflow enabled) — `CCMTurretControlOff = 1`
      (e.g. manual intervention or end of casting sequence).
- **The single workflow action serving states 11+** resolves `@HeatID`
  differently depending on which state fired: for the ladle-transfer/turret
  states (10→13's rest-position/rotation states) it carries the heat ID
  forward from the most recent `'LRF Roof Open'` record with an earlier
  `StartTime`; for the casting/billet-production states (13/14/18) it
  instead carries forward from the most recent `'Ladle At CCM Arm 1/2 Rest
  Position'` record. **Then, critically: `@ActualHeatID = @HeatID - 1` —
  the resolved heat ID is decremented by one before being stored.** The
  vendor's own document flags this as worth double-checking ("confirm this
  offset is intentional") — if a ticket reports an SMS process-time record
  attributed to the wrong (adjacent) heat, **this off-by-one decrement is
  the first thing to check**, not a data-entry error. For the two CCM
  casting-position states specifically, this action also copies
  `LRF_Per_Heat.LiquidMetalWeight` into `CCM_Data.LiquidSteelWeight` for the
  resolved `@ActualHeatID`.

## Event → Workflow → Stored Procedure map (from `Sohar Entities.xlsx`)

Confirmed real workflow names and their generated action-procedure names
(XStudio auto-generates one `XSTUDIO_WORKFLOW_<GUID>_SP` per
workflow+state-transition — these are callable/inspectable directly if a
ticket needs the exact current SQL, since the text in this file is from the
vendor doc, not a fresh pull):

| Event table | Workflow name | Status | Generated SP |
|---|---|---|---|
| `EAF_Per_Heat` | Laddle Popup | Entered | `XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP` |
| `EAF_Per_Heat` | Laddle Popup | Completed | `XSTUDIO_WORKFLOW_CB83D9D0-0256-44F8-BC97-461935B736D8_SP` |
| `LRF_per_heat` | LRF Parameters | Entered | `XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP` |
| `LRF_per_heat` | LRF Parameters | Completed | `XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP` |
| `CCM_per_heat` | CCM Per Heat CCM HeatNo insert | Entered | `XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP` |
| `CCM_per_heat` | CCM Per Heat CCM HeatNo insert | Completed | `XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP` (same SP as Entered) |
| `BilletsCastCount` | CCM_Trigger_Workflow | Entered | `XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP` |
| `BilletsCastCount` | CCM_Trigger_Workflow | Completed | `XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP` |
| `SMS_Plant_Process_EventTime` | Process Time CCM HeatNo insert | Entered | `XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP` |
| `SMS_Delay_Trn_Tbl` | SMS Delay Data | Completed | `XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP` — writes into `ShiftDelayEntry`, per the sheet's own note; not otherwise documented in this handover set. |
| `CCM_ProcessTime` | CCM Process Time HeatNo Insert | Entered | `XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP` — a *separate* table from `SMS_Plant_Process_EventTime`, not otherwise documented in this handover set; don't confuse the two. |

**These GUIDs are exactly what to hand to `get_sql_object_definition` /
`OBJECT_DEFINITION(OBJECT_ID('dbo.XSTUDIO_WORKFLOW_<GUID>_SP'))`** when a
ticket needs the *current* live SQL for one of these actions rather than the
vendor doc's point-in-time text above.

## Entity catalog highlights (from `Sohar Entities.xlsx`, 168 entities)

The workbook's "All Navigations Entity data" sheet is a full plant entity
list with human-written one-line descriptions — useful as a fast
name→purpose lookup when `find_sql_objects` returns a name with no other
context. Selected groupings worth knowing (full list is in the source
workbook if a name isn't below):

- **Explicitly marked "Not used"** — don't waste investigation time here
  unless a ticket specifically claims otherwise: `Agency_Wise_Delay`,
  `CCM_Summary_Shift`, `Equipment_Wise_Delay`, `Grade_Characteristics`
  (+`_Mapping`), `Grade_Test_Mapping`/`_Master`, `MES_WRM`,
  `Particulars_Masters_Trn`, `Size_Nominal_Wt_Value_Master`,
  `Tag_Configuration`, `Wire_Rod_Quality_Data`.
- **Summary/rollup tables** (daywise/shiftwise, not raw transaction data —
  check the underlying per-heat table first for a specific-event ticket,
  use these only for reporting/trend tickets): `CCM_Summary_Day`,
  `EAF_Summary_Day`, `LRF_Summary_Day`/`_Shift`, `Ngconsumption_Summary_Day`,
  `RM_Quality_Data_Day_Summary`, `SMS_Production_Summary`/`_Day`,
  `SMS_Target_Summary_Day`.
- **Life tracking** (equipment-part consumable life, the mechanism the
  EAF/LRF/CCM Completed actions all update): `Life_Tracking_Status`,
  `Life_Tracking_Transaction_tbl`, `LifeName_Mst_Tbl`, and the `XMES_*Life*`
  family already in the entities list (`XMES_ActiveLife_Element_Mst_Tbl`,
  `XMES_Life_Tracker_Register_Mst_Tbl`, `XMES_Element_Life_*`).
- **Electrical/substation** (MRSS = Main Receiving Sub-Station; a separate
  domain from steelmaking, don't confuse with process delays):
  `Electricity_Meter_*` family, `Sub_Station_Check_List`,
  `Transformer_125MVA`/`_15MVA`/`_24MVA`/`_63MVA`/`_6_6kv`/`_LRF`,
  `Transformer_Capacitor_Bank`, `Transformer_BATTERY_BANK_DG_STATUS`,
  `Electrical_A_Shift_Check_List`/`Electrical_Shift_B_Check_List`.
- **Rolling Mill (RM) logbooks and quality** — a large family not yet
  covered by name in `xbatch-investigation-surfaces.md`'s production
  section: `RM_Furnace_Parameter`, `RM_NGConsumption`,
  `RM_Operator_HeatSelection`, `RM_Roll_History_Card`/`_Stock_Card`/
  `_Turning_Job_Card`, `RM_Rolling_Standards`, `RM_Shift_Producation_Report`,
  `RM_Ring_No_MST`, `Billet_NGConsumption_InFurnace`,
  `Billet_Wise_WRMParameters`, `Billets_InFurnace_Tracking_Trn`,
  `BilletsPosition_InFurnace`, `XMES_RM_Furnace_Billet_Trn_Tbl`,
  `XMES_RM_Production_Data`/`_Summary`.
- **Master/reference data** worth resolving codes against rather than
  guessing: `Grade_Master`/`Grade_Type_Master`, `Status_Mst_Tbl`,
  `Product_Master`, `Plant_Name_MST`, `Storage_Location_MST`,
  `Order_Type_MST`, `Billet_Cross_Section` (the `SetWeight` source used in
  the Billets Cast Count Completed action above).

## How to use this file during an investigation

1. If a ticket names EAF/LRF/CCM/billet/SMS-process-time and the plain
   table-map file (`xbatch-investigation-surfaces.md`) doesn't explain a
   *behavior* (why a value is what it is, why it's missing, why it's
   attributed to the wrong heat), come here first — this file documents the
   actual write-time logic, not just where data lands.
2. The GUIDs above are real, callable procedure names — use them directly
   with `get_sql_object_definition` for the current live SQL rather than
   re-deriving from this document's point-in-time text.
3. This is vendor handover documentation, not a live query result. Treat
   specific numeric thresholds, GUIDs, and hardcoded values (the `12` in the
   billet-weight formula, the `@HeatID - 1` offset, the `130`/`150` cross-
   section split) as **hypotheses to verify live**, not settled fact, if a
   ticket's root cause hinges on one of them.
