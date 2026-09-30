---
type: procedure
title: "XMES_SAP_PlantToPlantTransfer_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_PlantToPlantTransfer_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_API_PlantToPlantTransfer_Error: BatchNo, Body, CreatedBy, EntryDateTime, ErrorMessage, ModifiedBy, ModifiedOn, RecordID, Source, Status, TransactionID

## Reads

- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: Batch, ID, IsDeleted, ModifiedBy

## What its own log shows

124 log rows, 2026-04-01 01:07 to 2026-07-01 00:37.
Error steps: Store Errors In Plant to Plant Transfer Posting Error Table Process End; Store Errors In Plant to Plant Transfer Posting Error Table Process Start

Steps:
- Completed
- Entered
- Store Errors In Plant to Plant Transfer Posting Error Table Process End
- Store Errors In Plant to Plant Transfer Posting Error Table Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_API_Error_Usp @RecordID='F9FF106C-05EA-4F82-B552-68AE61E5419F', @TransactionID='8f78a199-ac16-423c-b4f8-dccc13dd3035'`
