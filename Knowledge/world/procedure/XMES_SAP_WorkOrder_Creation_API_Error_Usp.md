---
type: procedure
title: "XMES_SAP_WorkOrder_Creation_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_WorkOrder_Creation_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar.

## Writes

- XMES_SAP_API_WorkOrderCreation_Error: Body, CreatedBy, CreatedOn, CustomerName, EntryDateTime, ErrorMessage, ItemName, ModifiedBy, ModifiedOn, RecordID, Source, Status, TotalQuantity, TransactionID, WorkOrderType

## Reads

- XBatch_Work_Order_Mst_Tbl: CreatedOn, CustomerName, ID, IsDeleted, ManufacturingOrderType, MaterialName, ModifiedBy, Quantity
