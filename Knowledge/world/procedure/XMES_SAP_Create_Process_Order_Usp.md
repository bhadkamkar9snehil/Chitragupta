---
type: procedure
title: "XMES_SAP_Create_Process_Order_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_Create_Process_Order_Usp

Parameters: @Type varchar.

## Writes

- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, CreatedBy, CreatedOn, EndTime, Equipment, ID, ItemID, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, ProductionPlant, Quantity, ReleasedDate, SalesOrder, SalesOrderItem, Source, StartTime, Status, UnitID

## Reads

- MES_Order_Configurator: Equipment, Itemid, OrderType, Quantity, Unitid
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
