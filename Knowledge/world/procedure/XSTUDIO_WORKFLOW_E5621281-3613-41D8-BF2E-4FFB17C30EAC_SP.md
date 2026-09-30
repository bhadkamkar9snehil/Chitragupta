---
type: procedure
title: "XSTUDIO_WORKFLOW_E5621281-3613-41D8-BF2E-4FFB17C30EAC_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_E5621281-3613-41D8-BF2E-4FFB17C30EAC_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ActualStartDate, ApprovedBy, ApprovedDate, Area, ColourCode, Grade, ID, ItemID, ParentID, PlannedCompletionDate, PlannedStartDate, ProgressTonnage, Quantity, ReleasedDate, Remarks, RequiredCompletionDate, SalesOrderItem, SalesOrderNumber, UnitID

## Writes (named in its SQL text)

- XBatch_Sales_Order_Mst_Tbl
