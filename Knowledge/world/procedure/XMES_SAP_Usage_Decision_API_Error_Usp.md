---
type: procedure
title: "XMES_SAP_Usage_Decision_API_Error_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_Usage_Decision_API_Error_Usp

Parameters: @RecordID varchar, @TransactionID varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_API_UsageDecision_Error: Body, CreatedBy, CreatedOn, EntryDateTime, ErrorMessage, HeatNo, InspectionLot, ModifiedBy, ModifiedOn, RecordID, Source, Status, TransactionID

## Reads

- MES_SAP_UsageDecision_Trn_Tbl: CreatedOn, HeatNo, ID, InspectionLot, IsDeleted, MaterialType, ModifiedBy, SAPTransactionID

## What its own log shows

132 log rows, 2026-03-21 09:44 to 2026-07-05 12:30.
Error steps: Store Errors In Usage Decision Posting Error Table Process End; Store Errors In Usage Decision Posting Error Table Process Start

Steps:
- Completed
- Entered
- Store Errors In Usage Decision Posting Error Table Process End
- Store Errors In Usage Decision Posting Error Table Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_Usage_Decision_API_Error_Usp @RecordID='F93D0911-96B0-433A-B7F0-1E0B2156C8BB', @TransactionID='1ad42725-7acc-41b0-9557-cf0d6ea078fd'`
