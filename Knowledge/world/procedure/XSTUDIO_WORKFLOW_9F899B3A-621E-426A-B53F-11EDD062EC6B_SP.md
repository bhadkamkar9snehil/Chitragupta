---
type: procedure
title: "XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Campaign_Plan_Mst: MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, ModifiedOn
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Production_Campaign_Tracking: CampaignId, Status

## Reads

- XMES_Campaign_Plan_Mst: AllFilesUpload, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, EntryDateTime, Grade, ID, IsDeleted, IsProcessed, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressPercentage, ProgressTonnage, RemaningTonnage, ReportDate, Size, StartDate, TotalPieces, TotalQtyWt, WRMExcelUpload, Working
- XMES_RM_Campaign_Plan_Trn: CampaignId, IsDeleted, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT

## Calls

- XMES_MaterialProcess_Cursor_usp

## What its own log shows

250 log rows, 2026-05-30 10:46 to 2026-08-21 15:50.

Steps:
- 1 Entered
- 2 Get Min Qty, Max Qty, Min No of Bundles and Max no of Bundles Start
- 3 Get Min Qty, Max Qty, Min No of Bundles and Max no of Bundles End
- 4 Update MinQty 10973.3550, MaxQty 10973.0000, Min no of Bundles 5656.0000 and Max no of Bundles 5656.0000 in campaign plan Start
- 4 Update MinQty 1500.0000, MaxQty 1696.0000, Min no of Bundles 773.0000 and Max no of Bundles 873.0000 in campaign plan Start
- 4 Update MinQty 1500.0000, MaxQty 1834.0000, Min no of Bundles 773.0000 and Max no of Bundles 945.0000 in campaign plan Start
- 4 Update MinQty 2200.0000, MaxQty 2200.0000, Min no of Bundles 1104.0000 and Max no of Bundles 1104.0000 in campaign plan Start
- 4 Update MinQty 3000.0000, MaxQty 3392.0000, Min no of Bundles 1546.0000 and Max no of Bundles 1746.0000 in campaign plan Start
- 4 Update MinQty 32920.0650, MaxQty 32919.0000, Min no of Bundles 16968.0000 and Max no of Bundles 16968.0000 in campaign plan Start
- 4 Update MinQty 4500.0000, MaxQty 5088.0000, Min no of Bundles 2319.0000 and Max no of Bundles 2619.0000 in campaign plan Start
- 4 Update MinQty 7062.6470, MaxQty 7216.0000, Min no of Bundles 2031.0000 and Max no of Bundles 2075.0000 in campaign plan Start
- 5 Update MinQty 10973.3550, MaxQty 10973.0000, Min no of Bundles 5656.0000 and Max no of Bundles 5656.0000 in campaign plan End
- 5 Update MinQty 1500.0000, MaxQty 1696.0000, Min no of Bundles 773.0000 and Max no of Bundles 873.0000 in campaign plan End
- 5 Update MinQty 1500.0000, MaxQty 1834.0000, Min no of Bundles 773.0000 and Max no of Bundles 945.0000 in campaign plan End
- 5 Update MinQty 2200.0000, MaxQty 2200.0000, Min no of Bundles 1104.0000 and Max no of Bundles 1104.0000 in campaign plan End
- 5 Update MinQty 3000.0000, MaxQty 3392.0000, Min no of Bundles 1546.0000 and Max no of Bundles 1746.0000 in campaign plan End
- 5 Update MinQty 32920.0650, MaxQty 32919.0000, Min no of Bundles 16968.0000 and Max no of Bundles 16968.0000 in campaign plan End
- 5 Update MinQty 4500.0000, MaxQty 5088.0000, Min no of Bundles 2319.0000 and Max no of Bundles 2619.0000 in campaign plan End
- 5 Update MinQty 7062.6470, MaxQty 7216.0000, Min no of Bundles 2031.0000 and Max no of Bundles 2075.0000 in campaign plan End
- 6 Procedure Material Process Cursor Start
- 7 Procedure Material Process Cursor End
- 8 Add CampaignId and Entered status in Procedure Campaign Tracking Start
- 9 Add CampaignId and Entered status in Procedure Campaign Tracking End
- 10 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='4EA2C448-9996-458A-8181-AE5DB2C71CEB', @p_RecordId='Completed', @p_StatusAttributeName='7BA3E8D6-E60C-4535-807A-5054633BE6C0', @p_Status='UploadStatus'`
