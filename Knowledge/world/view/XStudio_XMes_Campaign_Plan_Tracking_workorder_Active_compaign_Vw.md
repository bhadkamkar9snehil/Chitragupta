---
type: view
title: "XStudio_XMes_Campaign_Plan_Tracking_workorder_Active_compaign_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_XMes_Campaign_Plan_Tracking_workorder_Active_compaign_Vw

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

- Edit varchar(261)
- CreationDate datetime
- ReleasedDate datetime
- Name varchar(100)
- ItemName varchar(100)
- ID varchar(36)
- WorkOrderNumber varchar(100)
- BatchSchedule varchar(-1)
- WorkOrderType varchar(100)
- SAPWorkOrderNumber varchar(100)
- Status varchar(50)
- Campaign_Campaign varchar(100)
- Action varchar(50)
- MinimumQuantity decimal
- TotalQuantity decimal
- ProductionPosting varchar(-1)
- Unit varchar(100)
- Grade varchar(100)
- ProgressTonnage decimal
- RemainingTonnage decimal
- CustomerName varchar(100)
- ProgressPercentage decimal
- ItemID varchar(36)
- Equipment varchar(-1)
- CutLengthMtr decimal
- SalesOrder varchar(100)
- ParentID varchar(36)
- CrossSectionmm varchar(100)
- Details varchar(-1)
- MinimumBundles decimal
- ProgressDurationinDays decimal
- MfgOrderActualReleaseDate varchar(100)
- UnitID varchar(36)
- MaximumBundles decimal
- ProductionUnit varchar(100)
- Description varchar(1000)
- SerialNumber int
- PiecesInBundles int
- ColourCode varchar(50)
- WorkOrderMoreDetails varchar(-1)
- StatusColourCode varchar(50)
- Delete varchar(100)
- ItemColourCode varchar(50)
- ListPageName varchar(200)
- CampaignId varchar(100)
- Campaign_Status varchar(50)
- TotalBillets int
- BilletDischarged int
- BilletsCobble int
- BilletsHotout int
- BilletsRolled int
