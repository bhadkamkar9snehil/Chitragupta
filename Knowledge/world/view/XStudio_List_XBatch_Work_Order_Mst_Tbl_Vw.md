---
type: view
title: "XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw

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
- WorkOrderNumber varchar(100)
- WorkOrderType varchar(100)
- ID varchar(36)
- CreationDate datetime
- BatchSchedule varchar(-1)
- SAPWorkOrderNumber varchar(100)
- ReleasedDate datetime
- SalesOrder varchar(100)
- Action varchar(50)
- ProductionPosting varchar(-1)
- Status varchar(50)
- ItemName varchar(100)
- CustomerName varchar(100)
- ItemID varchar(36)
- Equipment varchar(-1)
- ParentID varchar(36)
- TotalQuantity decimal
- Unit varchar(100)
- ProgressTonnage decimal
- RemainingTonnage decimal
- Details varchar(-1)
- ProgressPercentage decimal
- ProgressDurationinDays decimal
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- ProductionUnit varchar(100)
- Description varchar(1000)
- SerialNumber int
- WorkOrderMoreDetails varchar(-1)
- ColourCode varchar(50)
- Delete varchar(100)
- StatusColourCode varchar(50)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
