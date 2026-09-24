---
type: procedure
title: "XSTUDIO_WORKFLOW_B74AE750-0673-47A3-8861-D7BBF127C2C7_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_B74AE750-0673-47A3-8861-D7BBF127C2C7_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- BilletsTracking_In_Furnace: EndTime, ID, StartTime, Status

## Writes (named in its SQL text)

- BilletsTracking_In_Furnace

## Calls

- BilletsPosition_InFurnace_Usp

## What its own log shows

41,020 log rows, 2026-05-29 11:25 to 2026-06-11 12:44.

Steps:
- 1 Entered
- 2 Procedure BilletsPosition in Furnace Start
- 3 Procedure BilletsPosition in Furnace End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_B74AE750-0673-47A3-8861-D7BBF127C2C7_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFFB0B29-C1DF-4B88-BDED-9C25AA53D320', @p_Status='WorkFlowStatus'`
