---
type: view
title: "XStudio_List_RM_Operator_HeatSelection_History_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_RM_Operator_HeatSelection_History_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`

## Reads

- RM_Operator_HeatSelection
- XBatch_Material_Inventory_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst

## Columns

- EntryDateTime datetime
- ID varchar(36)
- Edit varchar(245)
- CampaignNumber varchar(100)
- workordernumber varchar(100)
- IsProcessed bit
- ReportDate date
- Grade varchar(100)
- Delete varchar(100)
- Details varchar(-1)
- HeatNo varchar(36)
- BilletQty int
- RemainingBilletIncharging int
- RemainingBillets int
- SerialNumber int
- BilletLength varchar(100)
- CampaignId varchar(36)
- workorder varchar(36)
