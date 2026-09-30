---
type: view
title: "XStudio_XMes_Campaign_Plan_Tracking_RowTemplate_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_XMes_Campaign_Plan_Tracking_RowTemplate_Vw

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
- ID varchar(36)
- BatchSchedule varchar(-1)
- SAPWorkOrderNumber varchar(100)
- Length decimal
- Action varchar(50)
- CrossSectionmm varchar(100)
- ProductionPosting varchar(-1)
- CustomerName varchar(100)
- Campaign varchar(100)
- Equipment varchar(-1)
- TotalQuantity decimal
- ItemID varchar(36)
- ParentID varchar(36)
- ProgressTonnage decimal
- RemainingTonnage decimal
- ProgressPercentage decimal
- CreationDate datetime
- ProgressDurationinDays decimal
- Details varchar(-1)
- UnitID varchar(36)
- MfgOrderActualReleaseDate varchar(100)
- ProductionUnit varchar(100)
- ReleasedDate datetime
- Description varchar(1000)
- SalesOrder varchar(100)
- SerialNumber int
- ColourCode varchar(50)
- WorkOrderMoreDetails varchar(-1)
- StatusColourCode varchar(50)
- Status varchar(50)
- Delete varchar(100)
- ItemColourCode varchar(50)
- ItemName varchar(100)
- ListPageName varchar(200)
- CampaignId varchar(100)
- MinimumQuantity decimal
- Campaign_Status varchar(50)
- Unit varchar(100)
- MinimumBundles decimal
- MaxiumBundles decimal
- TotalPieces int
- TotalBillets int
- BilletsRolled int
- BilletsHotout int
- BilletsCobble int
- BilletDischarged int
- BilletsRemaining int
- BilletDischargedWeight decimal
- BundlesProduce int
- BundlesRemaining int
