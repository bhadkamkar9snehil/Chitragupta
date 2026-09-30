---
type: procedure
title: "XMES_SAP_Batch_Characteristics_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_Batch_Characteristics_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_API_Batch_Characteristics_Error: BatchNo, Body, CreatedBy, EntryDateTime, ErrorMessage, ModifiedBy, ModifiedOn, RecordID, Source, Status, TransactionID

## Reads

- XMES_SAP_Batch_Characteristic_Trn_Tbl: BatchNo, ID, IsDeleted, ModifiedBy

## What its own log shows

848 log rows, 2026-03-20 12:25 to 2026-07-05 22:44.
Error steps: Store Errors In Batch Characteristics Error Table Process End; Store Errors In Batch Characteristics Error Table Process Start

Steps:
- Completed
- Entered
- Store Errors In Batch Characteristics Error Table Process End
- Store Errors In Batch Characteristics Error Table Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_Batch_Characteristics_API_Error_Usp @RecordID='FE01CD68-5FC1-4D73-AA35-002ACEE7C2A9', @TransactionID='71ff5314-56d0-41a1-b017-ee15bf34d334'`
