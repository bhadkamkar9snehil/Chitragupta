---
type: table
title: "MES_SAP_Consumption_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_Consumption_Trn_Tbl

Table in XStudio_Xbatch. Rows: 7,913.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- BilletNo: same values as key `BilletNo`
- HeatNo: same values as key `HeatNo`

## Written by

- MES_M_Strand
- XMES_BackCalculation_GLS_Usp
- XMES_I_SAP_Batch_Consumption_Trn_Usp
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_SAP_Posting_Sequence_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP
- XSTUDIO_WORKFLOW_9A172601-2557-4597-B6A4-CDE39CA602BB_SP (text)
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18 (text)

## Read by

- MES_M_Strand
- XMES_BackCalculation_GLS_Usp
- XMES_I_API_Transaction_Summary
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_RM_Production_Summary_Usp
- XMES_RM_SAP_Posting_Sequence_Usp
- XMES_SAP_GoodsMovements_API_Error_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_SAP_Posting_Sequence_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP
- XSTUDIO_WORKFLOW_9A172601-2557-4597-B6A4-CDE39CA602BB_SP
- Xmes_Billet_Tracking_Move_to_Stand_1

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
- InventorySpecialStockType varchar(100)
- RawMaterialRecordID varchar(100)
- FurnaceBilletStatus varchar(100)
- Cutlength decimal
- SAPQuantity decimal
- BilletNo varchar(100)
