---
type: procedure
title: "XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_Batch_Characteristic_Trn_Tbl: ModifiedBy, ModifiedOn, NoOfPieces, Pieces, SAPPostingStatus, Source, TonsPerPiece

## Reads

- MES_SAP_Production_Trn_Tbl: Batch, CreatedByUser, CreationDate, CreationTime, CtrlPostForWhseMgmtSyst, DocumentDate, EntryDateTime, EntryUnit, GoodsMovementCode, GoodsMovementType, Grade, HeatNo, ID, InspectionLot, InventoryTransactionType, IsAutoPost, IsProcessed, IsReversal, ManualPrintLsTriggered, ManufacturingOrder, Material, MaterialDocument, MaterialDocumentHeaderText, MaterialDocumentItem, MaterialDocumentYear, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, ReferenceDocument, ReportDate, Sampleid, Saptransactionid, StorageLocation, SuccessMessage, VersionForPrintingSlip
- XMES_SAP_Batch_Characteristic_Trn_Tbl: BatchNo

## Writes (named in its SQL text)

- MES_SAP_Production_Trn_Tbl

## What its own log shows

11,560 log rows, 2026-03-20 00:40 to 2026-07-08 23:43.

Steps:
- Completed
- Entered
- Update Posted state for Batch Characteristic of Cold and Hot Billet Process End
- Update Posted state for Batch Characteristic of Cold and Hot Billet Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_23A94AFA-F5AE-4E7F-A558-84B7DA72D410_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='E21F8C9A-2293-4D0C-BDB3-35B89330ACE1', @p_RecordId='Post', @p_StatusAttributeName='D9032952-5A83-4854-9FE8-9037BD41AC25', @p_Status='SAPPostingStatus'`
