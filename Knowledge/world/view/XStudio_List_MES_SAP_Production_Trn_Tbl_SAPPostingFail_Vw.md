---
type: view
title: "XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`
- Material: same values as key `Material`

## Reads

- MES_SAP_Production_Trn_Tbl
- XMES_SAP_API_GoodsMovement_Error

## Columns

- CreationDate date
- WorkOrderNumber varchar(100)
- ID varchar(36)
- PostingDate datetime
- Name varchar(100)
- HeatNo int
- EntryDateTime datetime
- CreatedOn datetime
- Edit varchar(244)
- ReportDate date
- IsProcessed bit
- Action varchar(50)
- SAPPostingStatus varchar(50)
- Batch varchar(100)
- Material varchar(100)
- QuantityInEntryUnit decimal
- QuantityInCount int
- InspectionLot varchar(100)
- MaterialDocument bigint
- Plant varchar(100)
- InventoryTransactionType varchar(100)
- StorageLocation varchar(100)
- DocumentDate datetime
- CreationTime time
- CreatedByUser varchar(100)
- Grade varchar(100)
- EntryUnit varchar(100)
- MaterialDocumentHeaderText varchar(100)
- ReferenceDocument varchar(100)
- ControlPostingforExternamWMS varchar(100)
- VersionForPrintingSlip int
- ManualPrintLsTriggered varchar(100)
- PostingMaterialType varchar(100)
- MaterialDocumentItem varchar(100)
- Delete varchar(100)
- Details varchar(-1)
- GoodsMovementType int
- MaterialDocumentYear int
- GoodsMovementCode varchar(100)
- ErrorMessage varchar(-1)
- SAPTransactionID varchar(36)
