---
type: view
title: "XStudio_List_XBatch_RM_Planned_Work_Order_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_RM_Planned_Work_Order_Mst_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- XBatch_Material_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Sales_Order_Mst_Tbl
- XBatch_Status_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst

## Columns

- Edit varchar(238)
- Status varchar(50)
- Action varchar(50)
- ID varchar(36)
- CampaignNo varchar(100)
- SalesOrder varchar(100)
- WorkOrderNumber varchar(100)
- BatchSchedule varchar(-1)
- CustomerName varchar(100)
- ItemName varchar(100)
- SAPWorkOrderNumber varchar(100)
- TotalQuantity decimal
- Unit varchar(100)
- WorkOrderType varchar(100)
- Length decimal
- CreateProductionOrder varchar(1491)
- CreateProcessOrder varchar(1467)
- CrossSection varchar(100)
- CreationDate datetime
- PlannedStartDate datetime
- PlannedCompletionDate datetime
- ReleasedDate datetime
- Grade varchar(100)
- WorkOrderMoreDetails varchar(-1)
- ItemID varchar(36)
- Equipment varchar(-1)
- Description varchar(1000)
- ParentID varchar(36)
- ProgressTonnage decimal
- RemainingTonnage decimal
- ProgressPercentage decimal
- Details varchar(-1)
- ProgressDurationinDays decimal
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- ProductionUnit varchar(100)
- SerialNumber int
- ColourCode varchar(50)
- Delete varchar(100)
- StatusColourCode varchar(50)
- ItemColourCode varchar(50)
- ProductionPlant int
- SalesOrderItem varchar(100)
- OrderIsCreated varchar(100)
- CampaignId varchar(100)
