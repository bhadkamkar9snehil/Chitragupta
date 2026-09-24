---
type: view
title: "XStudio_List_MES_SAP_Production_RR_Posting_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_MES_SAP_Production_RR_Posting_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`
- Sampleid: same values as key `RecordID`
- Saptransactionid: same values as key `SAPTransactionID`

## Reads

- MES_SAP_Production_Trn_Tbl

## Columns

- SAPPostingStatus varchar(50)
- WorkOrderNumber varchar(100)
- Edit varchar(244)
- ID varchar(36)
- HeatNo int
- Name varchar(100)
- Batch varchar(100)
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Count int
- Material varchar(100)
- WeightTon decimal
- MaterialDocument bigint
- InspectionLot varchar(100)
- Action varchar(50)
- PostingMaterialType varchar(100)
- EntryUnit varchar(100)
- Plant varchar(100)
- StorageLocation varchar(100)
- MaterialDocumentYear int
- GoodsMovementType int
- InventoryTransactionType varchar(100)
- DocumentDate datetime
- PostingDate datetime
- CreationDate date
- Grade varchar(100)
- CreationTime time
- CreatedByUser varchar(100)
- MaterialDocumentHeaderText varchar(100)
- ReferenceDocument varchar(100)
- ControlPostingforExternamWMS varchar(100)
- Delete varchar(100)
- VersionForPrintingSlip int
- Details varchar(-1)
- ManualPrintLsTriggered varchar(100)
- GoodsMovementCode varchar(100)
- MaterialDocumentItem varchar(100)
- ResultRecoding varchar(-1)
- Saptransactionid varchar(36)
- CreatedOn datetime
- Sampleid varchar(36)
