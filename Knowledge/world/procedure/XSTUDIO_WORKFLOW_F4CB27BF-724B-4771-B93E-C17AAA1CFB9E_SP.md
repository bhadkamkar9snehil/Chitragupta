---
type: procedure
title: "XSTUDIO_WORKFLOW_F4CB27BF-724B-4771-B93E-C17AAA1CFB9E_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_F4CB27BF-724B-4771-B93E-C17AAA1CFB9E_SP

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

81 log rows, 2026-06-12 16:18 to 2026-08-21 15:50.

Steps:
- 1 Entered
- 2 Procedure Schedule TSQL Task for Python script Start
- 3 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_F4CB27BF-724B-4771-B93E-C17AAA1CFB9E_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='4EA2C448-9996-458A-8181-AE5DB2C71CEB', @p_RecordId='Entered', @p_StatusAttributeName='7BA3E8D6-E60C-4535-807A-5054633BE6C0', @p_Status='UploadStatus'`
