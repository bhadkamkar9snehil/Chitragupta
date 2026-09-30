---
type: procedure
title: "XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Campaign_Plan_Mst: ModifiedOn, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Production_Campaign_Tracking: ModifiedOn, OnholdDate, ProductionStartDate, Status

## Reads

- XMES_Campaign_Plan_Mst: AllFilesUpload, BilletDischarged, BilletDischargedWeight, BilletsCobble, BilletsHotout, BilletsRemaining, BilletsRolled, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, Grade, ID, IsDeleted, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressTonnage, RemaningTonnage, Size, StartDate, TotalBillets, TotalPieces, TotalQtyWt, WRMExcelUpload, Working
- XMES_Production_Campaign_Tracking: CampaignId, IsDeleted

## Calls

- XMES_RM_Tag_Printing_I_TRN

## What its own log shows

264 log rows, 2026-06-24 12:51 to 2026-08-24 16:05.

Steps:
- 1 Entered
- 2 Update OnHold Status in Camapign plan when status is running Start
- 2 Update running status in Production Campaign tracking Start
- 3 Update OnHold Status in Camapign plan when status is running End
- 3 Update running status in Production Campaign tracking End
- 4 Completed
- 4 Update running status in Production Campaign tracking Start
- 5 Update running status in Production Campaign tracking End
- 6 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='49796991-BC00-4368-8182-B39E4E6BD4A6', @p_RecordId='Running', @p_StatusAttributeName='E75E0F96-273C-4C95-B650-D24E5B3DB6E6', @p_Status='Status'`
