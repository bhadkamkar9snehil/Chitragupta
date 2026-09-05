---
name: xstudio-sap-api-investigation
description: "Investigate stuck/failed SAP posting or API transactions."
version: 0.1.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, xbatch, sap, api, integration]
    related_skills: [xstudio-l2-ticket-workflow, xstudio-sql-write-discipline]
---

# XStudio SAP / API Investigation Skill

For tickets about SAP posting stuck/pending/duplicate, missing material
documents, or any "did the API call even happen" question against
`XStudio_Xbatch` on 10.2.6.204. Not for work-order creation itself (see
`xstudio-quality-delay-workorder`) or per-heat process data (see
`xstudio-sohar-heat-execution`).

## When to Use

- Ticket mentions SAP, posting stuck/pending, no document number, goods
  movement, usage decision API, or a transaction ID.
- Don't use for: work-order *creation* logic, per-heat EAF/LRF/CCM values.

## Procedure

1. **Start broad, one call, before anything else:** the `xstudio_l2`
   `read_procedure` operation with
   `procedure = "XMES_Get_API_Transaction_Summary"` and
   `parameters = {"APIType": "<Type>"}` (values look like SAP operation
   names, e.g. `UsageDecision`), against
   `database = "XStudio_Configuration_Xbatch"` — it reads
   `XStudio_API_Error_Log_Mst_Tbl` there (a **different database** than
   `XStudio_Xbatch`), deduplicated to the latest row per `TransactionID`.
   This answers "did it happen and what was the result" faster than
   chasing domain-specific error tables first. This is the only stored
   procedure the typed tool will execute; everything else is read through
   `select`/`query`/`find_objects`.
2. **Then narrow to the posting record:** `SAP_Posting_Tbl`, keyed by
   `WorkOrderNo`/`HeatNo`. A row with `IsProcessed = 0`/NULL, a populated
   `SAP_Message`, and no `SAP_DocumentNo` is the classic stuck signature.
3. **If the summary shows a failure**, find the specific
   `XMES_SAP_*_API_Error_Usp` for that operation (e.g.
   `XMES_SAP_GoodsMovements_API_Error_Usp`) and read what table it writes
   to — don't assume from the name.
4. **Cross-check the domain-side record**, `MES_SAP_*_Trn_Tbl` (e.g.
   `MES_SAP_Production_Trn_Tbl`, `MES_SAP_Consumption_Trn_Tbl`), against
   `SAP_Posting_Tbl` when the ticket is "MES shows X but SAP shows Y."

## Pitfalls

- **`SAP_Posting_Data_ByHeat_Usp` is not a read** despite "Data" in the
  name — it writes pending production/consumption rows. Read its
  definition before calling it during investigation.
- **`XMES_API_Transaction_Summary_Fact_Tbl` is a stale bulk-load snapshot**
  (all rows share one load timestamp as of the last check), not a live
  feed — prefer `XMES_Get_API_Transaction_Summary` for current state; use
  the fact table only for a ticket specifically about a historical
  dashboard number.
- **A comment naming the wrong operation is real** —
  `XMES_SAP_WorkOrder_Creation_API_Error_Usp`'s own header comment says
  "Work Order Movement" even though the procedure name says "Creation."
  Trust the parameters/body, not the comment, when they disagree.

## Verification

- [ ] The specific stuck/failed row was found live (not assumed from this
      file), with its actual `SAP_Status`/`SAP_Message`/`IsProcessed`.
- [ ] If claiming "never called," `XMES_Get_API_Transaction_Summary` was
      actually queried for that `APIType`, not inferred from absence
      elsewhere.
