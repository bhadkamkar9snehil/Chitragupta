---
type: view
title: "XStudio_XMes_Campaign_Plan_Tracking_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_XMes_Campaign_Plan_Tracking_Vw

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

- Edit varchar(261)
- WorkOrderNumber varchar(100)
- MESWorkorder varchar(100)
- Grade varchar(100)
- WorkOrderType varchar(100)
- Length decimal
- CrossSectionmm varchar(100)
- ID varchar(36)
- BatchSchedule varchar(-1)
- Campaign varchar(100)
- TotalQuantity decimal
- SAPWorkOrderNumber varchar(100)
- ProgressTonnage decimal
- RemainingTonnage decimal
- ProgressPercentage decimal
- Action varchar(50)
- CreationDate datetime
- ProductionPosting varchar(-1)
- ReleasedDate datetime
- CustomerName varchar(100)
- SalesOrder varchar(100)
- Status varchar(50)
- ItemName varchar(100)
- Equipment varchar(-1)
- MinimumQuantity decimal
- ItemID varchar(36)
- ParentID varchar(36)
- Unit varchar(100)
- MinimumBundles decimal
- MaxiumBundles decimal
- TotalPieces int
- ProgressDurationinDays decimal
- Details varchar(-1)
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- ProductionUnit varchar(100)
- Description varchar(1000)
- SerialNumber int
- ColourCode varchar(50)
- WorkOrderMoreDetails varchar(-1)
- StatusColourCode varchar(50)
- Delete varchar(100)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
- CampaignId varchar(100)
- Campaign_Status varchar(50)
