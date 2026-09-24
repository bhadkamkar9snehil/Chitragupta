---
type: procedure
title: "XMES_SAP_Batch_Creation_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_Batch_Creation_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_API_Batch_Creation_Error: BatchNo, Body, CreatedBy, EntryDateTime, ErrorMessage, ModifiedBy, ModifiedOn, RecordID, Source, Status, TransactionID

## Reads

- XMES_SAP_CreateBatch_Mst_Tbl: Batch, ID, IsDeleted, ModifiedBy

## What its own log shows

488 log rows, 2026-03-25 23:41 to 2026-06-28 12:51.
Error steps: Store Errors In Batch Creation Error Table Process End; Store Errors In Batch Creation Error Table Process Start

Steps:
- Completed
- Entered
- Store Errors In Batch Creation Error Table Process End
- Store Errors In Batch Creation Error Table Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_Batch_Creation_API_Error_Usp @RecordID='FFCEFBED-9AB9-4ABD-8809-6EBC6FFFAF43', @TransactionID='9181e7c0-4777-4234-a333-944ee2c7e84e'`
