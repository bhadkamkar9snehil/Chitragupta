---
type: view
title: "XStudio_List_MES_SAP_Production_Trn_Tbl_Reversal_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_MES_SAP_Production_Trn_Tbl_Reversal_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`
- Material: same values as key `Material`
- Saptransactionid: same values as key `SAPTransactionID`

## Reads

- CCM_Per_Heat
- MES_SAP_Production_Trn_Tbl
- XMES_SAP_API_GoodsMovement_Error

## Columns

- WorkOrderNumber varchar(100)
- HeatNo int
- Action varchar(50)
- ID varchar(36)
- SAPPostingStatus varchar(50)
- Batch varchar(100)
- Name varchar(100)
- Cutlength decimal
- Material varchar(100)
- WeightTon decimal
- Count int
- InspectionLot varchar(100)
- EntryDateTime datetime
- ProductionPosting varchar(1313)
- MaterialDocument bigint
- Plant varchar(100)
- ReportDate date
- StorageLocation varchar(100)
- ProductionPostingReversal varchar(586)
- Grade varchar(100)
- IsProcessed bit
- MaterialType varchar(100)
- PostingDate datetime
- BatchCharacteristics varchar(-1)
- TransactionsDetails varchar(-1)
- RepostingProduction varchar(-1)
- GoodsMovementType int
- SuccessMessage varchar(100)
- ErrorMessage varchar(-1)
- EntryUnit varchar(100)
- Edit varchar(265)
- ErrorMessageLink varchar(-1)
- MaterialDocumentYear int
- InventoryTransactionType varchar(100)
- DocumentDate datetime
- CreationDate date
- CreationTime time
- CreatedByUser varchar(100)
- MaterialDocumentHeaderText varchar(100)
- ReferenceDocument varchar(100)
- ControlPostingforExternamWMS varchar(100)
- VersionForPrintingSlip int
- ManualPrintLsTriggered varchar(100)
- GoodsMovementCode varchar(100)
- MaterialDocumentItem varchar(100)
- Delete varchar(100)
- Saptransactionid varchar(36)
- CreatedOn datetime
- CCMRecordID varchar(36)
- IsReversal bit
