---
type: procedure
title: "XSTUDIO_WORKFLOW_C67D7329-8634-4DCC-94B2-B2B950981934_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_C67D7329-8634-4DCC-94B2-B2B950981934_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XBatch_Sales_Order_Mst_Tbl: ActualCompletionDate, ActualStartDate, ApprovedBy, ApprovedDate, Area, ColourCode, Grade, ID, ItemID, ParentID, PlannedCompletionDate, PlannedStartDate, ProgressTonnage, Quantity, ReleasedDate, Remarks, RequiredCompletionDate, SalesOrderItem, SalesOrderNumber, UnitID

## Writes (named in its SQL text)

- XBatch_Sales_Order_Mst_Tbl
