---
type: table
title: "MES_SAP_By_Product_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_By_Product_Trn_Tbl

Table in XStudio_Xbatch. Rows: 7,968.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- XMES_I_ByProduct_Trn_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_SAP_Posting_Sequence_Usp

## Read by

- XMES_I_API_Transaction_Summary
- XMES_I_ByProduct_Trn_Usp
- XMES_RM_Production_Summary_Usp
- XMES_SAP_GoodsMovements_API_Error_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_SAP_Posting_Sequence_Usp

## Columns

- ID varchar(36)
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
- Grade varchar(100)
- GoodsMovementCode varchar(100)
- PostingDate datetime
- DocumentDate datetime
- StorageLocation varchar(100)
- InspectionLot int
- CtrlPostForWhseMgmtSyst varchar(100)
- CreatedByUser varchar(100)
- EntryUnit varchar(100)
- ManualPrintLsTriggered varchar(100)
- ReferenceDocument varchar(100)
- InventoryTransactionType varchar(100)
- Material varchar(100)
- VersionForPrintingSlip int
- QuantityInEntryUnit decimal
- MaterialDocumentItem varchar(100)
- QuantityInCount int
- SAPPostingStatus varchar(50)
- CreationDate date
- CreationTime time
- GoodsMovementType int
- Plant varchar(100)
- MaterialDocumentYear int
- MaterialDocumentHeaderText varchar(100)
- ParentID varchar(36)
- HeatNo int
- ReportDate date
- MaterialDocument varchar(100)
- Saptransactionid varchar(36)
- Batch varchar(100)
- EntryDateTime datetime
- ManufacturingOrder varchar(100)
- PostingMaterialType varchar(100)
- IsProcessed bit
- Name varchar(100)
- SuccessMessage varchar(100)
