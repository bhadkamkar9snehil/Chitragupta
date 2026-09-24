---
type: view
title: "XStudio_List_XMES_Billet_Tracking_Trn_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XMES_Billet_Tracking_Trn_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Batch: same values as key `HeatNo`

## Reads

- XBatch_Measurement_Unit_Mst_Tbl
- XMES_Billet_Tracking_Trn_Tbl
- XMES_Process_Stage_Mst_Tbl
- XMES_State_Position_State_Mst_Tbl

## Columns

- Edit varchar(246)
- ID varchar(36)
- Name varchar(36)
- DateTime datetime
- HeatNo varchar(100)
- Batch varchar(100)
- BilletNo varchar(100)
- ReportDate date
- Plant varchar(100)
- IsProcessed bit
- StorageLocation varchar(100)
- StatePosition varchar(100)
- BilletWeight decimal
- ProcessStage varchar(100)
- UOM varchar(100)
- Delete varchar(100)
- PositionName varchar(100)
- Details varchar(-1)
- StageName varchar(100)
- SequenceNumber int
- UOMID varchar(36)
- PostingMaterialType varchar(100)
