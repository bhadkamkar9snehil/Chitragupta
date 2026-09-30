---
type: procedure
title: "XMES_RM_Campaign_Plan_WorkOrders_Creation"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Campaign_Plan_WorkOrders_Creation

Parameters: @CampaignMasterid varchar.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ItemID, Name, ParentID, PlannedCompletionDate, PlannedStartDate, Quantity, SalesOrderNumber, Status, UnitID
- XBatch_Work_Order_Mst_Tbl: CampaignId, CustomerName, Equipment, Grade, ItemID, ManufacturingOrderCategory, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, ProductionPlant, Quantity, SalesOrder, SalesOrderName, Status, StorageLocation, UnitID

## Reads

- XBatch_Customer_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: IsDeleted
- XMES_Campaign_Plan_Mst: CampaignId, EndDate, ID, IsDeleted, StartDate
- XMES_RM_Campaign_Plan_Trn: CampaignId, Customer, IsDeleted, Length, MaterialNo, MaxQtytoRollMT, SONumber
