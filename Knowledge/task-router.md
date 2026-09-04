---
type: "Routing Guide"
title: "Hermes L2 Task Router"
description: "Routes an unresolved Helpdesk ticket to the bounded set of Knowledge/ documents and live SQL surfaces worth loading first -- so the investigator never has to read the entire schema/SP catalog or guess which file has the answer."
status: draft
verified: "2026-09-02"
tags:
  - hermes
  - routing
  - xstudio
  - xmes
---

# Hermes L2 Task Router

Route first. Do not load the entire schema dump or all 388+ XBatch stored procedures into
the model for every ticket, and do not guess which `Knowledge/` file has the answer --
match the ticket against the table below.

**Machine-readable mirror:** `Knowledge/manifest.json` carries this same routing table as
structured data (file, route, keywords, ticket patterns) for any future script-based lookup;
this document is the human-readable source of truth, keep both in sync when adding a route.

**View catalog (2026-09-03):** `Knowledge/view_catalog.md` (+ `view_catalog.json` for
script/model lookup) categorizes documented SQL views by domain with confirmed relationships and
pre-built, verified queries. Check it before hand-writing a join across `heat_execution` or
`performance` tables/views -- several of the widest views (e.g. `XBatch_Tracability_Heat_Details_Vw`,
`XBatch_Delay_Analysis_Vw`) already do the join for you. **All 666 real `XStudio_Xbatch` views
are now catalogued, but most are `"tier": "lite"` (auto-indexed, category/key_column are
unverified guesses, no sample rows read) -- only entries without a `tier` field (or with
`verified_queries`) are human-verified. Read the tier field before trusting a category or query.**
**Durable Hermes Skills (2026-09-02):** the procedure and domain discipline this router
routes *to* now also exist as five local Hermes Skills (`skills/xstudio/*/SKILL.md` in each
bot profile) — `xstudio-l2-ticket-workflow`, `xstudio-sap-api-investigation`,
`xstudio-sohar-heat-execution`, `xstudio-quality-delay-workorder`,
`xstudio-sql-write-discipline`. Each carries its own trigger-optimized `description` for
organic discovery independent of this file. This table's `Load` column is the knowledge-file
side of the same routing; the `Skill` column below is the procedure/discipline side — both
point at the same route.

All file paths below are relative to `Knowledge/` and flat (no subfolders) -- this bundle
does not use a `platform/`/`start/`/`machine/` directory layout despite what older drafts of
this document said.

## Always load

```text
mental-model.md
execution-model.md
```

Then select the narrowest route below and load only its matched documents.

## Core routing

| Ticket pattern | Route | Skill | Load | Live SQL leads |
|---|---|---|---|---|
| Ticket workflow, requester, category, priority, assignment, response/close, "how does the ticket lifecycle work" | `helpdesk_ticket` | `xstudio-l2-ticket-workflow` | `helpdesk-workflow-binding.md` | `XStudio_Helpdesk.dbo.Complaint_Mst_Tbl`, Helpdesk masters (`ComplaintType_Mst_Tbl`, `priority_mst`), live workflow objects/SPs |
| SAP production/consumption/by-product posting failed, pending, duplicate, no material document, "stuck in SAP" | `sap_posting` | `xstudio-sap-api-investigation` | `xbatch-investigation-surfaces.md` (SAP posting / integration section), `sql-write-model.md`, **`view_catalog.md` sap_posting category** | **Check `XStudio_List_SAP_Posting_Tbl_Vw` (cross-domain, heat+billet level), `XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw`, and `XStudio_List_MES_SAP_Consumption_Trn_Tbl_Vw` (raw-material input side) first. CONFIRMED via real view definition: `SAPPostingFail_Vw` is NOT filtered to failures (only WHERE IsDeleted=0) -- its `ErrorMessage` comes from a LEFT JOIN, so NULL means either genuine success OR not-yet-attempted, filter `SAPPostingStatus` explicitly.** Fall back to `SAP_Posting_Tbl`, `MES_SAP_Production_Trn_Tbl`, `MES_SAP_Consumption_Trn_Tbl`, `XMES_SAP_*_API_Error_Usp` family. |
| API failed / response error / transaction ID mentioned / "did the API call even happen" | `api_transaction` | `xstudio-sap-api-investigation` | `xbatch-investigation-surfaces.md` (API transaction summary section), **`view_catalog.md` sap_posting category** | **5 API-error-log views now catalogued by call type: `XMES_SAP_API_GoodsMovement_Error_Vw`, `_Batch_Creation_Error_Vw`, `_WorkOrderCreation_Error_Vw`, `_UsageDecision_Error_Vw` (quality<->SAP bridge), `_Inventory_Error_Vw` (plant/storage-location sync). Check `Status` not ErrorMessage-presence (confirmed live: ErrorMessage can be populated on a Completed row).** Fall back to `XMES_Get_API_Transaction_Summary`, `XStudio_API_Error_Log_Mst_Tbl`, `XMES_API_Transaction_Summary_Fact_Tbl` for API types not yet catalogued (ByProduct/Consumption/Production/Reversal GoodsMovement, PlantToPlantTransfer, ResultRecording, Batch_Characteristics -- still on the survey backlog). |
| Work order missing/wrong state/order creation issue | `work_order` | `xstudio-quality-delay-workorder` | `xbatch-investigation-surfaces.md` (work order execution section), `sql-write-model.md`, **`view_catalog.md` work_order category** | **Check `XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw` first -- SAP linkage + status + production progress in one row. For cancelled/aborted orders specifically, use `XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw` (platform-maintained filtered list) directly. For campaign-grouped orders, `XStudio_XMes_Campaign_Plan_work_order_Vw` -- note it exposes a third WO identifier (`MESWorkOrderNumber`), confirm which one the ticket cites.** Fall back to `XBatch_Work_Order_Mst_Tbl`, `XMES_WorkOrders_Creation`, `MES_SAP_WO_Trn_Tbl`, `XMES_SAP_WorkOrder_Creation_API_Error_Usp`. |
| Heat missing, wrong EAF/LRF/CCM state, per-heat value looks wrong, heat attributed to the wrong ID, lot-number confusion, SMS Plant Process Time timing/state question, alloy addition values (Lime/Dolo/SiMn/FeSi/Carbon), power/timing/yield per heat | `heat_execution` | `xstudio-sohar-heat-execution` | **`sohar-sms-event-workflows.md` (primary -- has the actual event/state-machine and workflow-SP logic)**, `xbatch-investigation-surfaces.md` (production/tracking section) | **Check `XBatch_Tracability_Heat_Details_Vw` and `Vw_XBatch_Tracability_SMS_Process_Time` FIRST (real, comprehensive views -- confirmed live 2026-09-03, 666 views exist in XStudio_Xbatch and were never previously routed to). `XBatch_Tracability_Heat_Details_Vw` alone has HeatNo, all EAF/LRF alloy additions, power/timing/yield, and billet production in one row -- covers most per-heat questions without touching base tables at all.** Fall back to `EAF_PER_HEAT`, `LRF_Per_Heat`, `CCM_Per_Heat`, `SMS_Plant_Process_EventTime` only if the view doesn't have what's needed. |
| Billet missing/wrong location/furnace/yard/transfer, billet count or weight looks wrong | `billet_inventory` | `xstudio-sohar-heat-execution` | `xbatch-investigation-surfaces.md` (billet/yard/inventory section), `sohar-sms-event-workflows.md` (Billets Cast Count section -- has the actual weight-calculation formula), `sql-write-model.md`, **`view_catalog.md` billet_inventory category** | **Check `XStudio_List_Billet_Inventory_Vw` for current location/availability, `XStudio_List_XBatch_Billets_Transfer_History_Tbl_Vw` for the full movement audit trail, and `XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw` for heat/strand/sequence genealogy (confirmed BilletNo format `<HeatNo>_<Strand>_<Sequence>`) FIRST.** Fall back to `Billet_Inventory`, `BilletsCastCount`, `Billet_Cross_Section` base tables only if the views don't have what's needed. |
| Chemistry/sample/result recording/UD/RR issue | `quality` | `xstudio-quality-delay-workorder` | `xbatch-investigation-surfaces.md` (quality section), **`view_catalog.md` quality category** | **Check `XStudio_List_Heat_Chemistry_Quality_Data_Vw` (wide per-heat composition), `XStudio_List_Quality_Spectro_Result_Vw` (per-element, with MinLimit/MaxLimit for spec pass/fail), and `XStudio_List_Quality_Deviation_Master_Vw` (master spec-limit config by Product/Size/Parameter) FIRST. For a UD not posting to SAP, also check `XStudio_List_XMES_SAP_API_UsageDecision_Error_Vw` (sap_posting category).** Fall back to `Heat_Chemistry_Quality_Data`, `Quality_Spectro_File`/`_Sample`/`_Result`, `MES_SAP_UsageDecision_Trn_Tbl`, `MES_SAP_RR_Trn_Tbl` base tables. |
| Delay/OEE/performance/downtime issue | `performance` | `xstudio-quality-delay-workorder` | `xbatch-investigation-surfaces.md` (delay/OEE section), **`view_catalog.md` performance_delay category** | **Check `XBatch_Delay_Analysis_Vw` FIRST -- confirmed pre-joined merge of `XBatch_Tracability_TotalDelay_Details_Vw` + `AgencyDelay` + `EquipmentDelay`, one row per delay event with timing + agency + equipment.** Fall back to `Delay_Trn_Tbl`, `ShiftDelayEntry`, `DelayTypeMST`/`DelayCategory_Master`/`DelayAgency_Master`, `Xstudio_Agency_Wise_Delay_USP` only if the view doesn't cover it. |
| Question about which Hermes-runtime table/SP does what, or how the L2 audit trail itself works | `hermes_runtime` | `xstudio-l2-ticket-workflow` | `hermes-runtime-database-design.md`, `hermes-sp-catalog.md` | `Hermes_L2_Response_Trn_Tbl`, `Hermes_L2_SQL_Action_Trn_Tbl`, the 20 `Hermes_L2_*_Usp` procedures |
| Unknown/cross-domain symptom | `discover` | `xstudio-sql-write-discipline` | `xbatch-investigation-surfaces.md` (as a general starting map), `sql-write-model.md` (discovery queries) | `sys.tables`, `sys.columns`, `sys.procedures`, `sys.parameters`, `sys.sql_modules` |

**About to write SQL for any route above?** Also apply `xstudio-sql-write-discipline` -- it
is cross-cutting, not tied to one route.

**Fast path for `AreaID: "Common"` / `ProblemCategory: null` tickets: go straight to
`discover`, do not deliberate about which specific domain fits first.** A real
2026-09-03 incident had an investigator burn its entire time budget (twice, on
retry) reasoning about whether a "Common"-area ticket was heat_execution vs.
quality vs. something else, before ever making a single tool call -- it never got
past domain classification. "Common"/null `ProblemCategory` is itself the signal
that this ticket is `discover`, not a puzzle to solve before picking a route. Start
`discover`'s SQL-discovery queries (or a plain read against
`Complaint_Mst_Tbl`/whatever entity the free text actually names) immediately;
switch to a more specific route only if the evidence you find points there.

## Routing by identifier

When the ticket contains a strong identifier, prefer it over natural-language classification:

```text
Saptransactionid / TransactionID  -> api_transaction or sap_posting
HeatNo / HeatID                   -> heat_execution, then branch as evidence dictates
InspectionLot                     -> quality
WorkOrder / ManufacturingOrder    -> work_order
BilletNo / SubLotNo               -> billet_inventory
EquipmentID (delay context)       -> performance
```

`ExtractedEntitiesJson` on the ticket row (populated once an L1 chatbot exists, usually still
NULL as of 2026-09-02) is a shortcut to these same identifiers -- check it before parsing free
text.

## Cross-domain routing

Do not force one ticket into one domain when the evidence crosses systems.

Example:

```text
"Billet not available in rolling mill"

Start: billet_inventory
Then follow evidence:
billet created?
-> transfer history?
-> SAP inventory/GR?
-> furnace/rolling state?
```

Example (a real case this router was extended for, 2026-09-02 -- see
`sohar-sms-event-workflows.md`):

```text
"SMS Plant Process Time shows Heat 1604015's event attributed to ActualHeatID 1604014"

Start: heat_execution -> sohar-sms-event-workflows.md
This is NOT necessarily a bug: the SMS Plant Process Time workflow action deliberately
computes @ActualHeatID = @HeatID - 1 for states 11+. Confirm the decrement is the explanation
before treating it as a data-integrity defect.
```

The route selects the starting document set; it does not constrain the later investigation.

## Unknown object rule

When a required table/SP is not in the explainer:

```sql
-- procedure name discovery
SELECT s.name AS SchemaName, p.name AS ProcedureName
FROM sys.procedures p
JOIN sys.schemas s ON s.schema_id = p.schema_id
WHERE p.name LIKE '%<term>%'
ORDER BY p.name;

-- definition discovery
SELECT OBJECT_SCHEMA_NAME(m.object_id) AS SchemaName,
       OBJECT_NAME(m.object_id) AS ObjectName
FROM sys.sql_modules m
WHERE m.definition LIKE '%<table-or-column>%';

-- inspect signature
SELECT OBJECT_NAME(object_id) AS ProcedureName,
       parameter_id, name, TYPE_NAME(user_type_id) AS DataType,
       max_length, is_output
FROM sys.parameters
WHERE object_id = OBJECT_ID('dbo.<ProcedureName>')
ORDER BY parameter_id;
```

Do not guess an SP because its name looks plausible.

## Hermes runtime procedure routing

| Need | Stored procedure |
|---|---|
| Discover actual Helpdesk statuses/workflow SQL | `Hermes_L2_Discover_Helpdesk_Workflow_Usp` |
| Poll unresolved L2 work | `Hermes_L2_Get_Candidate_Tickets_Usp` |
| Claim one ticket | `Hermes_L2_Claim_Ticket_Usp` |
| Load ticket + prior Hermes context | `Hermes_L2_Get_Ticket_Context_Usp` |
| Search current SQL surface | `Hermes_L2_Find_SQL_Objects_Usp` |
| Inspect current table/SP/view/trigger | `Hermes_L2_Get_SQL_Object_Definition_Usp` |
| Execute current SQL/SP/write | `Hermes_L2_Execute_SQL_Usp` |
| Ask user | `Hermes_L2_Ask_Question_Usp` |
| Resolve/close via existing status | `Hermes_L2_Resolve_Ticket_Usp` |
| Escalate to human L3 | `Hermes_L2_Escalate_L3_Usp` (also snapshots into `Hermes_L3_Escalation_Trn_Tbl`) |
| Human L3 work queue / status update (not investigator-side; for the L3 UI or an agent acting on their behalf) | `Hermes_L3_Get_Open_Escalations_Usp` / `Hermes_L3_Update_Escalation_Status_Usp` |

## Non-ticket reference

`70_local_inference_setup.md` isn't ticket-domain knowledge -- it's the
desktop GPU/model-provider setup (LM Studio vs Ollama settings, per-model
benchmarks, why Ollama isn't production-deployed yet). Read it before
touching model provider config, not for ticket investigation.

## Adding a new knowledge document

When a new `Knowledge/*.md` file is added:

1. Add a row here (or extend an existing route's `Load` column).
2. Add a matching entry to `Knowledge/manifest.json`.
3. **Do not also hand-edit `SOUL.md`** -- both bot profiles read this router, not a hardcoded
   file list, specifically so new knowledge scales without touching the bot's own instructions.
