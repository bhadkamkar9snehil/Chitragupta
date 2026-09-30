---
type: procedure
title: "XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Customer_Mst_Tbl: CustomerCode, Name
- XBatch_Sales_Order_Mst_Tbl: Area, ItemID, Name, ParentID, Quantity, SalesOrderNumber, Status, UnitID
- XBatch_Work_Order_Mst_Tbl: BilletsRemaining, CampaignId, CustomerName, Equipment, Grade, ItemID, Length, ManufacturingOrderCategory, ManufacturingOrderType, MaterialName, MaxBundles, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, MinBundles, MinQtyToRoll, Name, NoOfPiecesInBundles, ProductionPlant, ProgressTonnage, Quantity, ReleasedDate, SalesOrder, SalesOrderName, Size, Source, Status, StorageLocation, TotalBillets, UnitID
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_Production_Campaign_Tracking: ReleasedDate, Status

## Reads

- XBatch_Customer_Mst_Tbl: ID, IsDeleted
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: IsDeleted
- XMES_Campaign_Plan_Mst: AllFilesUpload, BilletDischarged, BilletDischargedWeight, BilletsCobble, BilletsHotout, BilletsRemaining, BilletsRolled, CampaignEndDate, CampaignId, CampaignstartDate, EndDate, Grade, ID, Length, Material, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, Productname, ProgressPercentage, ProgressTonnage, RemaningTonnage, Size, StartDate, TotalBillets, TotalPieces, TotalQtyWt, WRMExcelUpload, Working
- XMES_Production_Campaign_Tracking: CampaignId, IsDeleted
- XMES_RM_Campaign_Plan_Trn: CampaignId, Customer, Grade, IsDeleted, Length, MaterialNo, MaxNoOfBundles, MaxQtytoRollMT, MinNoOfBundles, MinQtytoRollMT, NumberOfPiecesInBundles, SONumber

## Writes (named in its SQL text)

- XMES_Campaign_Plan_Mst

## What its own log shows

324 log rows, 2026-05-30 10:46 to 2026-08-21 15:52.

Steps:
- 1 Entered
- 2 Insert sonumber from rm campaign plan into table variable Start
- 3 Insert sonumber from rm campaign plan into table variable End
- 4 Insert customer code and name from rm campaign plan into customer master Start
- 5 Insert customer code and name from rm campaign plan into customer master End
- 6 Insert sales order data from rm campaign plan transaction into Sales Order master Start
- 7 Insert sales order data from rm campaign plan transaction into Sales Order master End
- 8 Insert Bundle data from rm campaign plan transaction into table variable for RB and BR material Start
- 9 Insert Bundle data from rm campaign plan transaction into table variable for RB and BR material End
- 10 Insert salesorder data from rm campaign plan transaction into table variable when material except RB and BR and sales order are there Start
- 11 Insert salesorder data from rm campaign plan transaction into table variable when material except RB and BR and sales order are there End
- 12 Insert Bundle data from rm campaign plan transaction into table variable when material except RB and BR and sales order are not there Start
- 13 Insert Bundle data from rm campaign plan transaction into table variable when material except RB and BR and sales order are not there End
- 14 Insert work order data from table varialbe into work order master Start
- 15 Insert work order data from table varialbe into work order master End
- 16 Update released status in Product campaign tracking Start
- 17 Update released status in Product campaign tracking End
- 18 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='49796991-BC00-4368-8182-B39E4E6BD4A6', @p_RecordId='Released', @p_StatusAttributeName='E75E0F96-273C-4C95-B650-D24E5B3DB6E6', @p_Status='Status'`
