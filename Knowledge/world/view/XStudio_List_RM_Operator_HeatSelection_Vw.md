---
type: view
title: "XStudio_List_RM_Operator_HeatSelection_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_RM_Operator_HeatSelection_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- Grade: same values as key `Grade`

## Reads

- RM_Operator_HeatSelection
- XBatch_Material_Inventory_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst
- XMES_Live_Billet_Charging_Bed
- XMES_Live_Charging_SECT1
- XMES_Live_Charging_SECT2

## Columns

- EntryDateTime datetime
- ID varchar(36)
- Edit varchar(245)
- Delete varchar(100)
- ReportDate date
- Grade varchar(100)
- IsProcessed bit
- HeatNo varchar(36)
- Details varchar(-1)
- Batch varchar(100)
- Action varchar(50)
- Release varchar(319)
- RemainingBilletsold int
- BilletLength varchar(100)
- SAPPosting varchar(-1)
- ReleasedStatus varchar(50)
- SerialNumber int
- CampaignId varchar(36)
- BilletData varchar(-1)
- BilletQty int
- Status varchar(100)
- RemainingBillets int
- CampaignNumber varchar(100)
- ReleaseDate datetime
- BilletOnChargingBed int
- BilletOnChargingSect1 int
- BilletOnChargingSect2 int
- BilletInFurnace int
- BilletsFuranaceStatus varchar(100)
- workorderid varchar(36)
- workName varchar(100)
- BatchWeightKG decimal
- BilletsoutofFurnace int
- BilletMaterialType varchar(100)
