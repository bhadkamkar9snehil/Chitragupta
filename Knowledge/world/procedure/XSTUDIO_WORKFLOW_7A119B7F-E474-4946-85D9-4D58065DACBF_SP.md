---
type: procedure
title: "XSTUDIO_WORKFLOW_7A119B7F-E474-4946-85D9-4D58065DACBF_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_7A119B7F-E474-4946-85D9-4D58065DACBF_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Delay_Trn_Tbl: EndTime, HeatNo, ID, StartTime, Status

## Writes (named in its SQL text)

- Delay_Trn_Tbl

## Calls

- ShiftDelayEntry_Update_usp
- XBatch_Get_Entry_for_ShiftDelay_Usp
