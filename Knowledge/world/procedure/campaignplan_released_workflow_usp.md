---
type: procedure
title: "campaignplan_released_workflow_usp"
built: "2026-09-24T11:36:36"
---

# campaignplan_released_workflow_usp


## Writes

- XBatch_Sales_Order_Mst_Tbl: ItemID, Name, ParentID, PlannedCompletionDate, PlannedStartDate, Quantity, SalesOrderNumber, Status, UnitID
- XBatch_Work_Order_Mst_Tbl: CampaignId, CustomerName, Equipment, Grade, ItemID, Length, ManufacturingOrderCategory, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, ProductionPlant, Quantity, SalesOrder, SalesOrderName, Size, Status, StorageLocation, UnitID
- XMES_Production_Campaign_Tracking: ReleasedDate, Status

## Reads

- XBatch_Customer_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: IsDeleted
- XMES_Campaign_Plan_Mst: CampaignId, EndDate, ID, IsDeleted, Size, StartDate
- XMES_Production_Campaign_Tracking: CampaignId, IsDeleted
- XMES_RM_Campaign_Plan_Trn: CampaignId, Customer, IsDeleted, Length, MaterialNo, MaxQtytoRollMT, SONumber
