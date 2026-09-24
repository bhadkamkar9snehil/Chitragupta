---
type: view
title: "XStudio_List_XBatch_CC_Work_Order_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_CC_Work_Order_Mst_Tbl_Vw

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
- Status varchar(50)
- ProgressPercentage decimal
- ID varchar(36)
- Action varchar(50)
- SalesOrder varchar(100)
- BatchSchedule varchar(-1)
- SAPWorkOrderNumber varchar(100)
- WorkOrderNumber varchar(100)
- WorkOrderType varchar(100)
- ItemName varchar(100)
- TotalQuantity decimal
- Unit varchar(100)
- CustomerName varchar(100)
- ProgressTonnage decimal
- ItemID varchar(36)
- RemainingTonnage decimal
- ParentID varchar(36)
- CreationDate datetime
- ReleasedDate datetime
- ProductionPosting varchar(-1)
- DocumentedGoodMovements varchar(-1)
- Details varchar(-1)
- ProgressDurationinDays decimal
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- Equipment varchar(-1)
- PlannedStartDate datetime
- PlannedCompletionDate datetime
- ProductionUnit varchar(100)
- ActualCompletionDate datetime
- Description varchar(1000)
- WorkOrderMoreDetails varchar(-1)
- SerialNumber int
- Plant varchar(100)
- ColourCode varchar(50)
- Delete varchar(100)
- ProductionPlant int
- StatusColourCode varchar(50)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
