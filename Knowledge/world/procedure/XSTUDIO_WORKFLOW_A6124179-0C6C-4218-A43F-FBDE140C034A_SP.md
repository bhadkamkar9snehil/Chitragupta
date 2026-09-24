---
type: procedure
title: "XSTUDIO_WORKFLOW_A6124179-0C6C-4218-A43F-FBDE140C034A_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_A6124179-0C6C-4218-A43F-FBDE140C034A_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_ActiveLife_Element_Mst_Tbl: Source, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XMES_ActiveLife_Element_Mst_Tbl: ElementNameID
- XMES_Element_Life_Type_Mapping_Mst_Tbl: DataCaptureType, ElementType, ParentID
- XMES_Life_Element_Mst_Tbl: ID, IsDeleted, ParentID
- XMES_Life_Tracker_Register_Mst_Tbl: ID, Srno

## Writes (named in its SQL text)

- XMES_Life_Tracker_Register_Mst_Tbl

## What its own log shows

22,790 log rows, 2026-06-01 16:58 to 2026-07-17 17:18.

Steps:
- 1 Entered
- 2 Declare Prod cursor for elementtype in element life type mapping for auto type Start
- 2 Get Element type from element life type mapping of auto type Start
- 3 Declare Prod cursor for elementtype in element life type mapping for auto type End
- 3 Get Element type from element life type mapping of auto type End
- 4 Declare Prod cursor for Id of life element master Start
- 4 Open Prod cursor Start
- 5 Declare Prod cursor for Id of life element master Start
- 5 Open Prod cursor End
- 6 Fetch Element type after open Prod cursor Start
- 6 Open Prod cursor for Id of life element master Start
- 7 Fetch Element type after open Prod cursor End
- 7 Open Prod cursor for Id of life element master End
- 8 Fetch Element ID after open prod cursor Start
- 8 close and deallcoate prod cursor cursor Start
- 9 Fetch Element ID after open prod cursor End
- 9 close and deallcoate prod cursor cursor End
- 10 Completed
- 10 close and deallocate prod cursor Start
- 11 close and deallocate prod cursor End
- 12 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_A6124179-0C6C-4218-A43F-FBDE140C034A_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='CF587DA9-0FDF-494E-8044-7620D00418AE', @p_RecordId='Active', @p_StatusAttributeName='8D0E1442-1B43-4281-AC79-F68EB569AF51', @p_Status='Status'`
