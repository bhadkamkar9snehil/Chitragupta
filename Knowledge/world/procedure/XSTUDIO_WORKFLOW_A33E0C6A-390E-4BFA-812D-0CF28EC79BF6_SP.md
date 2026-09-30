---
type: procedure
title: "XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Production_Campaign_Tracking: AbortDate, Status

## Reads

- XMES_Campaign_Plan_Mst: AllFilesUpload, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, EntryDateTime, Grade, ID, IsProcessed, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressPercentage, ProgressTonnage, RemaningTonnage, ReportDate, Size, StartDate, TotalPieces, TotalQtyWt, WRMExcelUpload, Working
- XMES_Production_Campaign_Tracking: CampaignId, IsDeleted

## Writes (named in its SQL text)

- XMES_Campaign_Plan_Mst
