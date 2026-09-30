---
type: procedure
title: "XSTUDIO_WORKFLOW_FC44CBFD-6EDD-4543-8305-B6560572182C_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_FC44CBFD-6EDD-4543-8305-B6560572182C_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Billets_Per_Stand_Tracking: BilletNo, EndTime, EquipmentID, ID, IsProcessed, ReportDate, StartTime, Status

## Writes (named in its SQL text)

- Billets_Per_Stand_Tracking

## Calls

- Xstudio_Historian_RM_Mill_Block_usp
