---
type: procedure
title: "XBatch_Create_Connection_Default_Transfer_Capability"
built: "2026-09-24T11:36:36"
---

# XBatch_Create_Connection_Default_Transfer_Capability

Parameters: @ConnectionID varchar, @UserID varchar.

## Writes

- XBatch_Connection_Capability_Mst_Tbl: CreatedBy, CreatedOn, Description, ID, IsAbort, IsAborted, IsDone, IsHeld, IsHold, IsInterlock, IsReady, IsReset, IsRestart, IsRun, IsStart, Name, ParentID, Source
- XBatch_Connection_Parameter_Mst_Tbl: CreatedBy, CreatedOn, Description, IsHistorize, Mode, Name, ParentID, Source, Type

## Reads

- XBatch_Connection_Capability_Mst_Tbl: IsDeleted
- XBatch_Connection_Parameter_Mst_Tbl: IsDeleted
