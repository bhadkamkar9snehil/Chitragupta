---
type: procedure
title: "XMES_WorkOrders_Creation"
built: "2026-09-24T11:36:36"
---

# XMES_WorkOrders_Creation

Parameters: @CampaignID varchar, @StartDate datetime, @EndDate datetime.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ID, ItemID, Name, ParentID, PlannedCompletionDate, PlannedStartDate, Quantity, SalesOrderNumber, Status, UnitID
- XBatch_Work_Order_Mst_Tbl: CustomerName, Equipment, Grade, ItemID, ManufacturingOrderCategory, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, ProductionPlant, Quantity, SalesOrder, SalesOrderName, Status, StorageLocation, UnitID

## Reads

- XBatch_Customer_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XMES_RM_Campaign_Plan_Trn: CampaignId, Customer, IsDeleted, ItemNo, Length, MaterialNo, MaxQtytoRollMT, SONumber
