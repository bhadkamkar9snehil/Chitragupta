---
type: procedure
title: "XMES_SAP_ResultRecording_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_ResultRecording_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_API_ResultRecording_Error: Body, CreatedBy, EntryDateTime, ErrorMessage, HeatNo, InspectionLot, ModifiedBy, ModifiedOn, RecordID, Source, Status, TransactionID

## Reads

- Heat_Chemistry_Quality_Data: HeatNo, ID, InspectionLot, IsDeleted, ModifiedBy

## What its own log shows

404 log rows, 2026-03-23 00:26 to 2026-07-08 11:17.
Error steps: Store Errors In Result Recording Posting Error Table Process End; Store Errors In Result Recording Posting Error Table Process Start

Steps:
- Completed
- Entered
- Store Errors In Result Recording Posting Error Table Process End
- Store Errors In Result Recording Posting Error Table Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_ResultRecording_API_Error_Usp @RecordID='F554F478-A330-40D7-B039-D1898BA7953B', @TransactionID='d01c631c-3332-4698-9e8b-a62cfbe1784e'`
