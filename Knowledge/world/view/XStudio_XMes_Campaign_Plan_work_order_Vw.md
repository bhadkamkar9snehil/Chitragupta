---
type: view
title: "XStudio_XMes_Campaign_Plan_work_order_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_XMes_Campaign_Plan_work_order_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- Grade_Master
- XBatch_Material_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Sales_Order_Mst_Tbl
- XBatch_Status_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst

## Columns

- Edit varchar(274)
- WorkOrderNumber varchar(100)
- WorkOrderType varchar(100)
- ID varchar(36)
- BatchSchedule varchar(-1)
- MESWorkOrderNumber varchar(100)
- CampaignNo varchar(100)
- CreatedDate datetime
- ReleasedDate datetime
- Action varchar(50)
- SalesOrder varchar(100)
- ProductionPosting varchar(-1)
- CustomerName varchar(100)
- Status varchar(50)
- Equipment varchar(-1)
- ItemID varchar(36)
- ParentID varchar(36)
- ItemName varchar(100)
- TotalQuantity decimal
- Unit varchar(100)
- CutLengthMtr decimal
- CrossSectionmm varchar(100)
- ProgressDurationinDays decimal
- Details varchar(-1)
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- ProductionUnit varchar(100)
- Description varchar(1000)
- Grade varchar(100)
- ProgressTonnage decimal
- SerialNumber int
- WorkOrderMoreDetails varchar(-1)
- ColourCode varchar(50)
- RemainingTonnage decimal
- Delete varchar(100)
- StatusColourCode varchar(50)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
- ProgressPercentage decimal
- CampaignId varchar(100)
- Campaign_Status varchar(50)
- IsDeleted bit
