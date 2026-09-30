---
type: table
title: "XMES_SAP_PlantToPlantTransfer_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_PlantToPlantTransfer_Trn_Tbl

Table in XStudio_Xbatch. Rows: 2,091.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- HeatNo: same values as key `HeatNo`
- IssgOrRcvgBatch: same values as key `HeatNo`
- ManufacturingOrder: same values as key `ManufacturingOrder`

## Written by

- XMES_I_PlantToPlantTransfer_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_SAP_Posting_Sequence_Usp

## Read by

- XMES_I_API_Transaction_Summary
- XMES_SAP_GoodsMovements_API_Error_Usp
- XMES_SAP_PlantToPlantTransfer_API_Error_Usp
- XMES_SAP_Posting_Sequence_Usp

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- DocumentDate datetime
- PostingDate datetime
- MaterialDocumentHeaderText varchar(100)
- ReferenceDocument varchar(100)
- Material varchar(100)
- Plant varchar(100)
- StorageLocation varchar(100)
- Batch varchar(100)
- GoodsMovementType varchar(100)
- EntryUnit varchar(100)
- QuantityInEntryUnit varchar(100)
- ManufacturingOrder varchar(100)
- Supplier varchar(100)
- Customer varchar(100)
- SalesOrder varchar(100)
- SalesOrderItem varchar(100)
- IssgOrRcvgMaterial varchar(100)
- IssgOrRcvgBatch varchar(100)
- IssuingOrReceivingPlant varchar(100)
- IssuingOrReceivingStorageLoc varchar(100)
- MaterialDocumentYear varchar(100)
- MaterialDocument varchar(100)
- InventoryTransactionType varchar(100)
- CreationDate datetime
- CreationTime datetime
- CreatedByUser varchar(100)
- VersionForPrintingSlip varchar(100)
- ManualPrintIsTriggered varchar(100)
- CtrlPostgForExtWhseMgmtSyst varchar(100)
- GoodsMovementCode varchar(100)
- SAPPostingStatus varchar(50)
- SAPTransactionID varchar(100)
- QuantityInCount int
- HeatNo int
- PostingMaterialType varchar(100)
