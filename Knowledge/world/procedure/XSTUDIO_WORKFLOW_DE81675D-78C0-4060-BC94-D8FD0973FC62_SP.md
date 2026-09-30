---
type: procedure
title: "XSTUDIO_WORKFLOW_DE81675D-78C0-4060-BC94-D8FD0973FC62_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_DE81675D-78C0-4060-BC94-D8FD0973FC62_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- XMES_Campaign_Plan_Mst: AllFilesUpload, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, EntryDateTime, Grade, ID, IsProcessed, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressPercentage, ProgressTonnage, RemaningTonnage, ReportDate, Size, StartDate, TotalPieces, TotalQtyWt, WRMExcelUpload, Working

## Writes (named in its SQL text)

- XMES_Campaign_Plan_Mst

## Calls

- XStudio_Schedule_TSQL_Task_Usp

## What its own log shows

8 log rows, 2026-05-30 10:45 to 2026-07-28 15:04.

Steps:
- 1 Entered
- 2 Procedure Schedule TSQL Task for Python script Start
- 3 Procedure Schedule TSQL Task for Python script End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_DE81675D-78C0-4060-BC94-D8FD0973FC62_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='19F651E7-FC5E-4A24-8D95-48F5FE661683', @p_RecordId='Enter', @p_StatusAttributeName='ED024396-5600-4FB1-B864-BF20FACD6A50', @p_Status='UploadStatus'`
