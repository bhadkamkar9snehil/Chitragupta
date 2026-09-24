---
type: procedure
title: "XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Production_Campaign_Tracking: CampaignId, CancelledDate, Status

## Reads

- XMES_Campaign_Plan_Mst: AllFilesUpload, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, EntryDateTime, Grade, ID, IsProcessed, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressPercentage, ProgressTonnage, RemaningTonnage, ReportDate, Size, StartDate, TotalPieces, TotalQtyWt, WRMExcelUpload, Working
- XMES_Production_Campaign_Tracking: IsDeleted

## Writes (named in its SQL text)

- XMES_Campaign_Plan_Mst

## What its own log shows

54 log rows, 2026-07-15 11:11 to 2026-08-21 09:41.

Steps:
- 1 Entered
- 2 Delete logically Campaign Plan record Start
- 3 Delete logically Campaign Plan record End
- 4 Update status cancelled in Production Campaign tracking Start
- 5 Update status cancelled in Production Campaign tracking End
- 6 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='4EA2C448-9996-458A-8181-AE5DB2C71CEB', @p_RecordId='Cancelled', @p_StatusAttributeName='7BA3E8D6-E60C-4535-807A-5054633BE6C0', @p_Status='Status'`
