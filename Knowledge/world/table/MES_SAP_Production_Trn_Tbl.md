---
type: table
title: "MES_SAP_Production_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_Production_Trn_Tbl

Table in XStudio_Xbatch. Rows: 11,836.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`
- Sampleid: same values as key `RecordID`
- Saptransactionid: same values as key `SAPTransactionID`

## Written by

- XMES_BackCalculation_GLS_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_I_SAP_GLS_Production_Trn
- XMES_I_SAP_LS_Production_Trn
- XMES_RM_SAP_Posting_Sequence_Usp
- XMES_SAP_I_EndProduct_Production_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_U_SAP_Billet_Production_Trn_Usp (text)
- XSTUDIO_WORKFLOW_0E59C696-ECB5-4E5C-B246-4275C0A324A4_SP (text)
- XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP (text)

## Read by

- XMES_BackCalculation_GLS_Usp
- XMES_I_API_Transaction_Summary
- XMES_I_SAP_Batch_Consumption_Trn_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_RM_SAP_Posting_Sequence_Usp
- XMES_SAP_GoodsMovements_API_Error_Usp
- XMES_SAP_I_Inventory_Stock_Data_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_U_SAP_Billet_Posting_Count_Usp
- XMES_U_SAP_Billet_Production_Trn_Usp
- XSTUDIO_WORKFLOW_0E59C696-ECB5-4E5C-B246-4275C0A324A4_SP
- XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- HeatNo int
- Grade varchar(100)
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Material varchar(100)
- Plant varchar(100)
- StorageLocation varchar(100)
- Batch varchar(100)
- ManufacturingOrder varchar(100)
- QuantityInEntryUnit decimal
- InspectionLot varchar(100)
- MaterialDocument bigint
- InventoryTransactionType varchar(100)
- MaterialDocumentYear int
- DocumentDate datetime
- PostingDate datetime
- CreationDate date
- CreationTime time
- CreatedByUser varchar(100)
- MaterialDocumentHeaderText varchar(100)
- ReferenceDocument varchar(100)
- VersionForPrintingSlip int
- ManualPrintLsTriggered varchar(100)
- CtrlPostForWhseMgmtSyst varchar(100)
- GoodsMovementCode varchar(100)
- MaterialDocumentItem varchar(100)
- Saptransactionid varchar(36)
- GoodsMovementType int
- EntryUnit varchar(100)
- QuantityInCount int
- PostingMaterialType varchar(100)
- SAPPostingStatus varchar(50)
- Sampleid varchar(36)
- IsReversal bit
- SuccessMessage varchar(100)
- IsAutoPost bit
- Cutlength decimal
- BilletNo int
- SectionLength varchar(100)
