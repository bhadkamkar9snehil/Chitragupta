---
type: view
title: "XStudio_List_XBatch_Executed_Work_Order_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Executed_Work_Order_Mst_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- XBatch_Material_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Sales_Order_Mst_Tbl
- XBatch_Status_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl

## Columns

- Edit varchar(238)
- SalesOrder varchar(100)
- WorkOrderNumber varchar(100)
- ID varchar(36)
- WorkOrderType varchar(100)
- CreationDate datetime
- ReleasedDate datetime
- BatchSchedule varchar(-1)
- SAPWorkOrderNumber varchar(100)
- Action varchar(50)
- Status varchar(50)
- ItemName varchar(100)
- ProductionPosting varchar(-1)
- CustomerName varchar(100)
- Equipment varchar(-1)
- ItemID varchar(36)
- ParentID varchar(36)
- TotalQuantity decimal
- Unit varchar(100)
- ProgressTonnage decimal
- RemainingTonnage decimal
- ProgressPercentage decimal
- ProgressDurationinDays decimal
- Details varchar(-1)
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- ProductionUnit varchar(100)
- PlannedStartDate datetime
- PlannedCompletionDate datetime
- ActualCompletionDate datetime
- Description varchar(1000)
- SerialNumber int
- ColourCode varchar(50)
- StatusColourCode varchar(50)
- Delete varchar(100)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
- WorkOrderMoreDetails varchar(-1)
- ProductionPlant int
