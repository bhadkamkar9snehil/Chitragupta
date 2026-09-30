---
type: procedure
title: "XSTUDIO_WORKFLOW_2AF85FD5-BE15-4380-9504-341EE986C74D_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_2AF85FD5-BE15-4380-9504-341EE986C74D_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Work_Order_Mst_Tbl: ModifiedOn, Status

## Reads

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ActualStartDate, ApprovedBy, ApprovedDate, Area, ColourCode, Grade, ID, ItemID, ParentID, PlannedCompletionDate, PlannedStartDate, ProgressTonnage, Quantity, ReleasedDate, Remarks, RequiredCompletionDate, SalesOrderItem, SalesOrderNumber, UnitID
- XBatch_Work_Order_Mst_Tbl: SalesOrder

## Writes (named in its SQL text)

- XBatch_Sales_Order_Mst_Tbl
