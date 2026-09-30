---
type: view
title: "XStudio_List_XMES_RM_Production_Data_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XMES_RM_Production_Data_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`
- HeatNo: same values as key `HeatNo`

## Reads

- Product_Master
- XBatch_Material_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst
- XMES_RM_Production_Data

## Columns

- Edit varchar(241)
- EntryDateTime datetime
- ID varchar(36)
- Duplicate varchar(-1)
- WorkOrder varchar(100)
- SAPWorkorderNo varchar(100)
- ReportDate date
- IsProcessed bit
- EndProduct varchar(100)
- HeatNo varchar(100)
- BilletBatchNo varchar(100)
- BilletNo varchar(100)
- FGBatchNo varchar(100)
- TagPrinting varchar(-1)
- BundleWeightTon decimal
- WorkOrderid varchar(-1)
- Delete varchar(100)
- NoofPieces int
- SectionLengthmm varchar(100)
- EndProductName varchar(-1)
- Product varchar(100)
- Details varchar(-1)
