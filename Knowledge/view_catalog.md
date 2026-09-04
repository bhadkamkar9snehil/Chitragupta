---
type: "View Catalog"
title: "XStudio SQL View Catalog"
description: "Categorized, tagged index of documented XStudio_Xbatch/XStudio_Helpdesk SQL views, with confirmed relationships and pre-built, verified queries -- so investigation can find and correlate views instead of reconstructing joins by hand."
status: draft
verified: "2026-09-03 (updated)"
tags:
  - hermes
  - views
  - xstudio
  - xbatch
---

# XStudio SQL View Catalog

**Machine-readable mirror:** `Knowledge/view_catalog.json` carries this same data as structured
JSON (category, tags, key_column, relates_to, verified_queries) for script/model lookup. This
file is the human-readable walkthrough; keep both in sync.

**Coverage: all 666 real `XStudio_Xbatch` views are now in the catalog (2026-09-03) -- 27 as
full hand-curated entries, 639 as lite auto-indexed entries.** Helpdesk (294 views) is out of
scope per user direction.

## Two tiers -- know which one you're reading

- **Full entries** (`"tier"` absent, or check for `verified_queries`): sample rows were actually
  read, category/relationships/queries are human-verified against live data. Trust these.
- **Lite entries** (`"tier": "lite"`): generated in bulk by `Model_Bench/bulk_index_views.py`
  straight from `schema_allowlist.json` -- category is a name-keyword guess, key_column is a
  guess from common ID column names present, **no sample rows were read, nothing is verified**.
  Good for "does a view like this exist / what columns does it have" triage; confirm with
  `export_view_samples.py` before trusting a lite entry's category or writing a query against it
  for a real ticket. `297` views landed in `uncategorized` -- the keyword rules didn't match
  their names, not evidence they're unimportant.

Promote a lite entry to full the same way any view gets documented: run
`export_view_samples.py`, read the real sample rows, then hand-write the category/tags/
relates_to/verified_queries in `view_catalog.json` (this replaces the lite entry in place). All 960 view names+columns are
already in `Knowledge/schema_allowlist.json` (so none get wrongly flagged as hallucinated), but
only these 19 have full column docs + live sample rows + a catalog entry. Extend this file every
time `Model_Bench/export_view_samples.py` documents a new view.

**Naming note:** views named `XStudio_List_*_Vw` are platform-generated grid/LV-binding views
(one per Entity List View config), not hand-authored reporting views like the `Tracability_*_Vw`
family. Their columns often mix real business fields with UI-only ones (`Edit`/`Delete`/`Action`/
`Details` -- JSON blobs for grid action buttons); the catalog entries below already strip those
out of the verified queries, but be aware of them if you read a `view_docs/` file directly.

**Full column list + 5 live sample rows for every view below:** `Knowledge/view_docs/<database>.<view>.md`

## How to use this catalog

1. Find your ticket's category below (or check `task-router.md` first -- it routes to the right
   category).
2. Read the "what it has" line -- most L2 questions are answered by ONE view here without
   touching base tables.
3. Check "relates to" before joining views by hand -- several of these are themselves pre-joined
   merges of other views in this catalog (e.g. `XBatch_Delay_Analysis_Vw`), so a manual join you're
   about to write may already exist.
4. Use a verified query as a starting template, not gospel -- they were checked against the live
   column list on 2026-09-03; re-verify if a view's columns have since changed.

## Category: heat_execution

Per-heat EAF/LRF/CCM state, timing, alloy addition, and yield data. All keyed by heat number
(column is `HeatNo` on some views, `HeatID` on others -- same value, different column name,
confirmed by cross-referencing sample data).

| View | Key col | What it has |
|---|---|---|
| `XBatch_Tracability_Heat_Details_Vw` | HeatNo | **Start here.** One row per heat: charge/liquid weight, EAF+LRF alloy additions, power/tap timing, scrap mix, billet production. Widest single view. |
| `Vw_XBatch_Tracability_SMS_Process_Time` | HeatID | Event/state timeline per heat (real datetime). Use when the question is about WHEN a state happened. |
| `XBatch_Tracability_Process_Details_Vw` | HeatID | Same state timeline, but date-only text timestamps -- prefer the SMS_Process_Time view above unless matching a specific downstream shape. |
| `Vw_EAF_Per_Heat_Report_Data` | HeatID | EAF-side per-channel (CH1-CH4) scrap/CDRI detail, more granular than Heat_Details_Vw's aggregate columns. |
| `Vw_CCM_Per_Heat_Report_Data` | HeatID | Casting-side per-strand mould water flow/pressure telemetry, billet count, shift. |

**Vendor doc cross-reference:** `Knowledge/vendor_docs_extracted/EAF Per Heat Event Doc.md`,
`CCM Per Heat Event Doc.md`, `LRF Per Heat Event Doc.md`, `SMS Plant Process Time Doc.md` carry
the real Attribute -> Tag Name mappings and per-state configuration these views are generated
from -- check them when a view column's meaning isn't obvious from its name alone.

## Category: performance_delay

Delay/downtime attribution per heat. All keyed by `HeatNo`.

| View | What it has |
|---|---|
| `XBatch_Tracability_AgencyDelay_Details_Vw` | Delay events by responsible agency (Electrical/Operation/etc). |
| `XBatch_Tracability_EquipmentDelay_Details_Vw` | Same, adds Equipment column (often blank -- not a bug). |
| `XBatch_Tracability_TotalDelay_Details_Vw` | The only one with real start/end timestamps + free-text reason. |
| `XBatch_Delay_Analysis_Vw` | **Confirmed pre-joined merge of all three above** -- use this instead of hand-joining them for any question needing timing + agency + equipment together. |

**Confirmed relationship (not guessed):** `XBatch_Delay_Analysis_Vw`'s column list is literally
the union of the other three views' distinguishing columns (`TotalDelay*` + `Agency*` +
`Equipment*` all on one row) -- verified by comparing the four `view_docs/` column lists directly.

## Category: sap_posting

SAP posting/API integration status and failures. All confirmed real `XStudio_List_*_Vw`
(platform-generated) views -- see the naming note above.

| View | Key col | What it has |
|---|---|---|
| `XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw` | HeatNo | Production-scoped posting rows with `SAPPostingStatus` -- **not confirmed pre-filtered to failures despite the name**, filter the status column explicitly. |
| `XStudio_List_XMES_SAP_API_GoodsMovement_Error_Vw` | TransactionID | API-call-level log: request Body, ErrorMessage, Status. Confirmed live: `ErrorMessage` can be populated on a `Status='Completed'` row -- check Status, not ErrorMessage-presence, to judge success/failure. |
| `XStudio_List_SAP_Posting_Tbl_Vw` | HeatNo / BatchNoorBilletNo | Cross-domain posting log (heat AND billet level), `SAPStatus`/`SAPDocumentNo`. |
| `XStudio_List_XMES_SAP_API_Batch_Creation_Error_Vw` | TransactionID | Batch-creation API call log, same shape family as GoodsMovement. |
| `XStudio_List_XMES_SAP_API_WorkOrderCreation_Error_Vw` | TransactionID | Work-order-creation API call log -- confirms whether SAP work order creation was ever attempted. |
| `XStudio_List_XMES_SAP_API_UsageDecision_Error_Vw` | HeatNo / InspectionLot | Usage-decision (quality release) API log -- the quality<->SAP bridge. |
| `XStudio_List_XMES_SAP_API_Inventory_Error_Vw` | TransactionID | Plant/storage-location-level inventory sync API log (narrower than GoodsMovement). |
| `XStudio_List_MES_SAP_Consumption_Trn_Tbl_Vw` | HeatNo | Raw-material consumption posting -- the input-side counterpart to the production-posting views. |

## Category: billet_inventory

Billet location, yard/furnace movement, and CCM strand genealogy. All keyed by `BilletNo`.

| View | What it has |
|---|---|
| `XStudio_List_Billet_Inventory_Vw` | Current snapshot: location, quantity, allocated/available flags. |
| `XStudio_List_Billets_In_Yard_Vw` | Yard-specific movement events (narrower than the inventory snapshot). |
| `XStudio_List_XBatch_Billets_Transfer_History_Tbl_Vw` | **Full chronological in/out audit trail** -- use this for "how did billet X get here / who moved it". |
| `XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw` | Heat->strand->sequence genealogy at casting time. Confirmed `BilletNo` format: `<HeatNo>_<Strand>_<Sequence>`. |

## Category: quality

Chemistry/spectrometer sample and result data. All keyed by `HeatNo`.

| View | What it has |
|---|---|
| `XStudio_List_Heat_Chemistry_Quality_Data_Vw` | Wide per-heat row: element composition (C, Mn, Si, S, P, Cr, Mo, V, Al, Sn, +more). |
| `XStudio_List_Quality_Spectro_Result_Vw` | One row per element per sample, with `MinLimit`/`MaxLimit` -- use for pass/fail spec checks. |
| `XStudio_List_Quality_Deviation_Master_Vw` | Master spec-limit configuration by Product/Size/ParameterName -- the reference data per-sample results are checked against. |

## Category: work_order

| View | What it has |
|---|---|
| `XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw` | Work order master + SAP linkage + production progress in one row. |
| `XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw` | Platform-maintained filtered list of cancelled/aborted orders -- use directly instead of filtering the main view by Status. |
| `XStudio_XMes_Campaign_Plan_work_order_Vw` | Work orders grouped by production campaign; adds a third WO identifier (`MESWorkOrderNumber`) alongside `WorkOrderNumber`/`SAPWorkOrderNumber` -- confirm which one a ticket actually cites, they are not interchangeable. |

## Out of scope

**Helpdesk views (294 real views in `XStudio_Helpdesk`) are explicitly out of scope for this
catalog per user direction (2026-09-03)** -- indexing effort stays on `XStudio_Xbatch`/MES views
only. One real finding surfaced before this was descoped, worth keeping in mind if Helpdesk work
ever resumes: `XStudio_List_Ticket_Mst_Tbl_Vw` is confirmed broken (references a table in a
database, `XStudio_CMSI`, that isn't reachable from `XStudio_Helpdesk` -- any SELECT against it
fails outright).

## Categories not yet populated

`api_transaction` (beyond the goods-movement/batch-creation/work-order-creation/usage-decision/
inventory views already catalogued under sap_posting) still has unsurveyed candidates --
`XMES_SAP_API_Batch_Characteristics_Error_Vw`, `XMES_SAP_API_GoodsMovement_ByProduct_Error_Vw`,
`XMES_SAP_API_GoodsMovement_Consumption_Error_Vw`, `XMES_SAP_API_GoodsMovement_Production_Error_Vw`,
`XMES_SAP_API_GoodsMovement_Reversal_Error_Vw`, `XMES_SAP_API_PlantToPlantTransfer_Error_Vw`,
`XMES_SAP_API_ResultRecording_Error_Vw` -- same generated-list-view API-error-log shape as the
ones already documented, next batch to run through `export_view_samples.py`.

## Adding a new view to this catalog

1. `python Model_Bench/export_view_samples.py --server 10.2.6.204 --database <db> <ViewName>` (writes `Knowledge/view_docs/<db>.<ViewName>.md`).
2. Add an entry to `Knowledge/view_catalog.json` under `views` -- category, tags, key_column,
   what_it_has, relates_to (only real, checked relationships -- don't guess), and 1-2 verified
   queries actually run or column-checked against the live sample.
3. Add a row to the matching category table above (or a new category section).
4. If this fills a gap noted in `task-router.md`'s `Live SQL leads` column, update that row too.
