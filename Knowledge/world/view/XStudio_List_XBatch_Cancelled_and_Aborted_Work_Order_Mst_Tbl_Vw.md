---
type: view
title: "XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw

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
- CreationDate datetime
- ReleasedDate datetime
- ID varchar(36)
- BatchSchedule varchar(-1)
- SalesOrder varchar(100)
- SAPWorkOrderNumber varchar(100)
- WorkOrderNumber varchar(100)
- WorkOrderType varchar(100)
- Action varchar(50)
- Status varchar(50)
- ItemName varchar(100)
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
- MfgOrderActualReleaseDate varchar(100)
- UnitID varchar(36)
- PlannedCompletionDate datetime
- Description varchar(1000)
- ProductionUnit varchar(100)
- SerialNumber int
- ColourCode varchar(50)
- Delete varchar(100)
- StatusColourCode varchar(50)
- ItemColourCode varchar(50)
- WorkOrderMoreDetails varchar(-1)
- ProductionPlant int
