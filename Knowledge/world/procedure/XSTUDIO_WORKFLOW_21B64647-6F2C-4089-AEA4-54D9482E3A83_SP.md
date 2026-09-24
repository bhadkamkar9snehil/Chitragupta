---
type: procedure
title: "XSTUDIO_WORKFLOW_21B64647-6F2C-4089-AEA4-54D9482E3A83_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_21B64647-6F2C-4089-AEA4-54D9482E3A83_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Work_Order_Mst_Tbl: ModifiedOn, Status

## Reads

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ActualStartDate, ApprovedBy, ApprovedDate, Area, ColourCode, Grade, ID, ItemID, ParentID, PlannedCompletionDate, PlannedStartDate, ProgressTonnage, Quantity, ReleasedDate, Remarks, RequiredCompletionDate, SalesOrderItem, SalesOrderNumber, UnitID
- XBatch_Work_Order_Mst_Tbl: SalesOrder

## Writes (named in its SQL text)

- XBatch_Sales_Order_Mst_Tbl
