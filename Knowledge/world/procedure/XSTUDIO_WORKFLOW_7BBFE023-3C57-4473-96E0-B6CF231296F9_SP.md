---
type: procedure
title: "XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Production_Campaign_Tracking: ProductionEndDate, Status

## Reads

- XMES_Campaign_Plan_Mst: AllFilesUpload, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, EntryDateTime, Grade, ID, IsProcessed, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressPercentage, ProgressTonnage, RemaningTonnage, ReportDate, Size, StartDate, TotalPieces, TotalQtyWt, WRMExcelUpload, Working
- XMES_Production_Campaign_Tracking: CampaignId, IsDeleted

## Writes (named in its SQL text)

- XMES_Campaign_Plan_Mst

## What its own log shows

8 log rows, 2026-07-28 09:12 to 2026-08-14 15:01.

Steps:
- 1 Entered
- 2 Update Completed status in Production Campaign Tracking Start
- 3 Update Completed status in Production Campaign Tracking End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='49796991-BC00-4368-8182-B39E4E6BD4A6', @p_RecordId='Completed', @p_StatusAttributeName='0965F8E3-E3DB-44B8-8732-61F562CCFBC0', @p_Status='Status'`
