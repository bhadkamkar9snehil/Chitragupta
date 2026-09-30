---
type: procedure
title: "XSTUDIO_WORKFLOW_3CD875CC-85C4-4587-848E-DF9361C98F5B_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_3CD875CC-85C4-4587-848E-DF9361C98F5B_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- BilletsTracking_In_Furnace: EndTime, ID, StartTime, Status

## Writes (named in its SQL text)

- BilletsTracking_In_Furnace

## Calls

- XBatch_RM_Mill_Billet_DischargeTemp

## What its own log shows

37,396 log rows, 2026-05-30 10:29 to 2026-06-11 12:44.

Steps:
- 1 Entered
- 2 Procedure RM Mill Billet discharge Temp Start
- 3 Procedure RM Mill Billet discharge Temp End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_3CD875CC-85C4-4587-848E-DF9361C98F5B_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Completed', @p_StatusAttributeName='FFFB0B29-C1DF-4B88-BDED-9C25AA53D320', @p_Status='WorkFlowStatus'`
