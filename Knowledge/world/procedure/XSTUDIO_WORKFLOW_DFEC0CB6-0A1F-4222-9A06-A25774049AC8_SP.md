---
type: procedure
title: "XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_ProcessTime: CCMHeatNo, CreatedOn, EndTime, ID, StartTime, Status
- LRF_ProcessTime: CreatedOn, LRFHeatID, StartTime, Status

## Writes (named in its SQL text)

- CCM_ProcessTime

## What its own log shows

11,840 log rows, 2026-06-01 17:38 to 2026-08-12 11:12.

Steps:
- 1 Entered
- 2 Get Latest CCM Heat no of CCM Process time Start
- 2 Get Latest LRF heat ID of LRF Process Time when LRF roof open status got Start
- 3 Get Latest CCM Heat no of CCM Process time End
- 3 Get Latest LRF heat ID of LRF Process Time when LRF roof open status got End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFF5188E-84B2-452E-87C9-D43DC1368F5B', @p_Status='WorkFlowStatus'`
