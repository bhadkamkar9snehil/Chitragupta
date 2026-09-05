---
type: "Routing Guide"
title: "Hermes L2 Task Router"
description: "Human-readable mirror of Knowledge/manifest.json for routing one claimed L2 ticket to a bounded evidence set."
status: current
verified: "2026-09-05"
tags:
  - hermes
  - routing
  - xstudio
  - xmes
---

# Hermes L2 Task Router

Route first. Do not load the whole schema/catalog for every ticket and do not guess objects from memory.

Machine-readable mirror: `Knowledge/manifest.json`.

## Always load

```text
mental-model.md
execution-model.md
```

These define the current lifecycle and the read-only worker boundary. Then choose the narrowest route below.

## Core routing

| Ticket pattern | Route | Skill | Load first | Live evidence leads |
|---|---|---|---|---|
| Ticket workflow, requester, category, priority, assignment, response/close | `helpdesk_ticket` | `xstudio-l2-ticket-workflow` | `helpdesk-workflow-binding.md` | `Complaint_Mst_Tbl`, complaint/priority masters |
| SAP production/consumption/by-product posting failed, pending, duplicate, no material document | `sap_posting` | `xstudio-sap-api-investigation` | `xbatch-investigation-surfaces.md` SAP section, `view_catalog.md` | `XStudio_List_SAP_Posting_Tbl_Vw`, SAP production/consumption views, posting tables |
| API failure, transaction ID, response error, “did the API call happen?” | `api_transaction` | `xstudio-sap-api-investigation` | API transaction section, `view_catalog.md` | API error views, allowlisted `XMES_Get_API_Transaction_Summary`, API error log |
| Work order missing/wrong state/cancelled/campaign/order creation | `work_order` | `xstudio-quality-delay-workorder` | work-order section, `view_catalog.md` | work-order views, `XBatch_Work_Order_Mst_Tbl`, creation/SP definitions |
| Heat/EAF/LRF/CCM/timing/alloy/power/yield/heat attribution | `heat_execution` | `xstudio-sohar-heat-execution` | `sohar-sms-event-workflows.md`, production/tracking section, `view_catalog.md` | comprehensive heat/process-time views, EAF/LRF/CCM tables |
| Billet yard/furnace/location/transfer/genealogy/count/weight | `billet_inventory` | `xstudio-sohar-heat-execution` | billet section, Billets Cast Count section, `view_catalog.md` | billet inventory, transfer-history and genealogy views |
| Chemistry/spectro/result/UD/RR/deviation | `quality` | `xstudio-quality-delay-workorder` | quality section, `view_catalog.md` | chemistry/spectro/deviation views, quality/SAP rows |
| Delay/OEE/downtime/equipment/agency/shift performance | `performance` | `xstudio-quality-delay-workorder` | delay/OEE section, `view_catalog.md` | `XBatch_Delay_Analysis_Vw`, delay/master tables |
| Hermes runtime/audit/Kanban/memory/orchestration | `hermes_runtime` | `xstudio-l2-ticket-workflow` | `hermes-runtime-database-design.md`, `hermes-sp-catalog.md` | Hermes response/action/trace tables |
| Unknown/cross-domain symptom | `discover` | `xstudio-sql-write-discipline` | `xbatch-investigation-surfaces.md`, `view_catalog.md` | typed schema/object discovery |

## Strong identifiers beat vague classification

```text
Saptransactionid / TransactionID -> api_transaction or sap_posting
HeatNo / HeatID                  -> heat_execution
InspectionLot                    -> quality
WorkOrder / WorkOrderNo          -> work_order
ManufacturingOrder               -> work_order
BilletNo / SubLotNo              -> billet_inventory
EquipmentID in delay context     -> performance
```

A route is a starting point, not a prison. Cross-domain evidence may justify switching routes after the first live reads.

## `Common` / uncategorized tickets

When `AreaID` is `Common` and no useful problem category exists, start with `discover` rather than spending the investigation budget debating a speculative domain label. Use ticket text/identifiers plus typed discovery to narrow the surface, then move to a specific route if evidence supports it.

## Typed discovery rule

Use `xstudio_l2`; do not hand-build database transport.

When an object is unknown:

```text
suggest_tables(ticket text)
-> find_objects(term)
-> get_definition(real object)
-> validate_identifiers(table/columns)
-> select/query bounded live evidence
```

For API transaction summary, `read_procedure` is allowed only for the explicit reviewed read-only procedure contract exposed by the tool. Do not call arbitrary procedures.

## View-first rule

Prefer a verified comprehensive view when it already contains the required relationship. Fall back to base tables only when the view lacks the necessary evidence or when the ticket is specifically about how that view is derived.

`view_catalog.md` contains the view inventory. Treat automatically categorized/lite entries as routing leads until their definitions/data are verified for the current ticket.

## Mutation boundary

A route may reveal that a production/configuration change is required. That does not give the L2 worker a write path.

Apply `xstudio-sql-write-discipline` as a boundary rule:

```text
known required action, worker cannot execute -> NEEDS_HUMAN_ACTION
unresolved/beyond L2                     -> L3_ESCALATION
```

Never fall back to terminal/Python/pyodbc/sqlcmd/raw write SQL.

## Ticket workflow route

For `helpdesk_ticket`, workflow values come only from `deploy/helpdesk_workflow_binding.json` / live workflow discovery. The model does not invent status values and does not publish the ticket.

Current bound values are documented in `helpdesk-workflow-binding.md`.

## Runtime procedure routing

The deterministic harness owns the Hermes SQL runtime. For architecture/reference work, the important stored procedures include:

| Need | Procedure |
|---|---|
| Discover live Helpdesk workflow | `Hermes_L2_Discover_Helpdesk_Workflow_Usp` |
| Candidate tickets | `Hermes_L2_Get_Candidate_Tickets_Usp` |
| Atomic claim | `Hermes_L2_Claim_Ticket_Usp` |
| Ticket/prior-run context | `Hermes_L2_Get_Ticket_Context_Usp` |
| SQL object discovery | `Hermes_L2_Find_SQL_Objects_Usp` |
| SQL object definition | `Hermes_L2_Get_SQL_Object_Definition_Usp` |
| Audited publication | `Hermes_L2_Publish_Response_Usp` and its workflow helpers |

Workers consume the corresponding safe `xstudio_l2` operations; they do not invoke raw runtime commands themselves.

## Adding or changing a route

1. Update this file.
2. Update `Knowledge/manifest.json` with the same canonical route name, skill, and document set.
3. Keep the route bounded; do not turn every ticket into “load everything.”
4. Run `python3 Model_Bench/validate_knowledge_manifest.py` and the retrieval tests locally.
