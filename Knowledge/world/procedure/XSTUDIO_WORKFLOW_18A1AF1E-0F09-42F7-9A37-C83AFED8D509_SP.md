---
type: procedure
title: "XSTUDIO_WORKFLOW_18A1AF1E-0F09-42F7-9A37-C83AFED8D509_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_18A1AF1E-0F09-42F7-9A37-C83AFED8D509_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- BilletsPosition_InFurnace: Position64
- Billets_Per_Stand_Tracking: BilletNo, EndTime, EquipmentID, ID, IsProcessed, ReportDate, StartTime, Status
- RM_Mill_Mst_Tbl: ID, IsDeleted, Name

## Writes (named in its SQL text)

- Billets_Per_Stand_Tracking
