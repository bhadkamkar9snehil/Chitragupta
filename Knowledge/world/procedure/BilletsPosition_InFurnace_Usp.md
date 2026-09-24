---
type: procedure
title: "BilletsPosition_InFurnace_Usp"
built: "2026-09-24T11:36:36"
---

# BilletsPosition_InFurnace_Usp

Parameters: @StartTime datetime.

## Writes

- Billet_NGConsumption_InFurnace: BilletNo, InTime, OutTime
- BilletsPosition_InFurnace: Position1, Position10, Position11, Position12, Position13, Position14, Position15, Position16, Position17, Position18, Position19, Position2, Position20, Position21, Position22, Position23, Position24, Position25, Position26, Position27, Position28, Position29, Position3, Position30, Position31, Position32, Position33, Position34, Position35, Position36, Position37, Position38, Position39, Position4, Position40, Position41, Position42, Position43, Position44, Position45, Position46, Position47, Position48, Position49, Position5, Position50, Position51, Position52, Position53, Position54, Position55, Position56, Position57, Position58, Position59, Position6, Position60, Position61, Position62, Position63, Position64, Position65, Position7, Position8, Position9
- Billets_InFurnace_Tracking_Trn: BilletNo, BilletPosition, EntryDateTime, Grade, HeatNo
- XBatch_Billets_Transfer_History_Tbl: ActionBy, BilletNo, CurrentStatus, ID, InventoryID, LayerID, LocationAssignedDate, MaterialGrade, ParentID, RecievedBy, RecievedDate, StackID, SubLotNo
- XBatch_Material_Inventory_Mst_Tbl: LocationID, MovementType, OutwardDate, OutwardLocation
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- BilletsPosition_InFurnace: IsDeleted
- RM_Operator_HeatSelection: BilletQty, Heatno
- XBatch_Material_Inventory_Mst_Tbl: ID, IsDeleted, LotNumber, MaterialGrade, ParentID, SublotNumber
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_OutwardLocation_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Area_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name, ParentID

## Calls

- XBatch_RM_BilletWiseNGConsumption

## What its own log shows

652,171 log rows, 2026-05-30 10:02 to 2026-09-24 11:30.
Error steps: 17 Error; 19 Error; 9 Error

Steps:
- 1 Entered
- 2 Get Heat no, Billet no, material Grade from billet tracking Start
- 2 Get Heat no, Billet no, material Grade from from billet tracking Start
- 3 Get Heat no, Billet no, material Grade from billet tracking End
- 3 Get Heat no, Billet no, material Grade from from billet tracking End
- 4 Get billet no of position 1 from billet position in furnace Start
- 5 Get billet no of position 1 from billet position in furnace End
- 6 Get Lot no and grade of previous billet no from material inventory Start
- 6 Set Billet no as earlier set billet no when previous billet is heat change gap or null Start
- 7 Get Lot no and grade of previous billet no from material inventory End
- 7 Set Billet no as earlier set billet no when previous billet is heat change gap or null End
- 8 Procedure RM Billet wise NG Consumption Start
- 9 Error
- 9 Procedure RM Billet wise NG Consumption End
- 10 Update All Positions in Billets Position in Furnace Start
- 11 Update All Positions in Billets Position in Furnace End
- 12 Insert Billet data in Billets in furnace tracking transaction from billets position in furnace Start
- 13 Insert Billet data in Billets in furnace tracking transaction from billets position in furnace End
- 14 Get Last position from billets in position Start
- 15 Get Last position from billets in position End
- 16 Completed
- 16 Update Outtime in billet ngconsumption in furncae of last position billet no Start
- 16 Update OutwardLocation, Location id in billet ngconsumption in furncae of last position billet no Start
- 17 Error
- 17 Update OutTime in billet ngconsumption in furncae of last position billet no End
- 17 Update OutwardLocation, Location id in billet ngconsumption in furncae of last position billet no End
- 18 Get stack id and Location id from storage area master as per location id of material inventory Start
- 18 Update OutwardLocation, Location id in billet ngconsumption in furncae of last position billet no Start
- 19 Error
- 19 Get stack id and Location id from storage area master as per location id of material inventory End

Example call: `EXEC XStudio_Xbatch.dbo.BilletsPosition_InFurnace_Usp @StartTime='31-May-2026 23:58:51.223'`
