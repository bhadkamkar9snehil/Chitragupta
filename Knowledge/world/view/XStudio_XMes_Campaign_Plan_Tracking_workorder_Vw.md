---
type: view
title: "XStudio_XMes_Campaign_Plan_Tracking_workorder_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_XMes_Campaign_Plan_Tracking_workorder_Vw

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

- WorkOrderNumber varchar(100)
- Edit varchar(261)
- Name varchar(100)
- WorkOrderType varchar(100)
- ID varchar(36)
- CreationDate datetime
- BatchSchedule varchar(-1)
- ReleasedDate datetime
- SAPWorkOrderNumber varchar(100)
- SalesOrder varchar(100)
- Campaign_Campaign varchar(100)
- Action varchar(50)
- Status varchar(50)
- ItemName varchar(100)
- MinimumQuantity decimal
- TotalQuantity decimal
- ProductionPosting varchar(-1)
- Unit varchar(100)
- Grade varchar(100)
- CutLengthMtr decimal
- CustomerName varchar(100)
- ItemID varchar(36)
- Equipment varchar(-1)
- CrossSectionmm varchar(100)
- MinimumBundles decimal
- ParentID varchar(36)
- MaximumBundles decimal
- PiecesInBundles int
- Details varchar(-1)
- ProgressDurationinDays decimal
- MfgOrderActualReleaseDate varchar(100)
- UnitID varchar(36)
- ProductionUnit varchar(100)
- Description varchar(1000)
- ProgressTonnage decimal
- SerialNumber int
- ColourCode varchar(50)
- WorkOrderMoreDetails varchar(-1)
- RemainingTonnage decimal
- StatusColourCode varchar(50)
- Delete varchar(100)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
- ProgressPercentage decimal
- CampaignId varchar(100)
- Campaign_Status varchar(50)
- TotalBillets int
- BilletDischarged int
- BilletsCobble int
- BilletsHotout int
- BilletsRolled int
