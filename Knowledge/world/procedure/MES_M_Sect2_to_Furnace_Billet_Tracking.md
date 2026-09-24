---
type: procedure
title: "MES_M_Sect2_to_Furnace_Billet_Tracking"
built: "2026-09-24T11:36:36"
---

# MES_M_Sect2_to_Furnace_Billet_Tracking

Parameters: @systemid varchar, @userid varchar, @RecordId varchar, @status varchar.

## Writes

- BilletsPosition_InFurnace: Position1, Position10, Position11, Position12, Position13, Position14, Position15, Position16, Position17, Position18, Position19, Position2, Position20, Position21, Position22, Position23, Position24, Position25, Position26, Position27, Position28, Position29, Position3, Position30, Position31, Position32, Position33, Position34, Position35, Position36, Position37, Position38, Position39, Position4, Position40, Position41, Position42, Position43, Position44, Position45, Position46, Position47, Position48, Position49, Position5, Position50, Position51, Position52, Position53, Position54, Position55, Position56, Position57, Position58, Position59, Position6, Position60, Position61, Position62, Position63, Position64, Position65, Position7, Position8, Position9
- Billets_InFurnace_Tracking_Trn: BilletNo, BilletPosition, EntryDateTime, Grade, HeatNo, Source
- RM_Operator_HeatSelection: BilletoutofFurnace
- XMES_Billet_Strand_tracking: BIlletNo, EndProduct, ParentID
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn
- XMES_Live_Charging_SECT2: FurnaceOutTime, OutTime, Status
- XMES_RM_Furnace_Billet_Trn_Tbl: BilletNo, EndTime, HeatNo, ParentID, Starttime, zone1ResidenceTime, zone2ResidenceTime, zone3ResidenceTime, zone4ResidenceTime, zone5ResidenceTime, zone6ResidenceTime, zone7ResidenceTime, zone8ResidenceTime
- XMES_RM_Heated_Billet_trn_tbl: BilletNo, HeatNO, ParentID, ProductType, Workorderid

## Reads

- BilletsPosition_InFurnace: IsDeleted, Position1, Position16, Position24, Position32, Position40, Position48, Position56, Position64, Position65, Position8
- Product_Master: ID, IsDeleted
- RM_Operator_HeatSelection: Grade, ID, IsDeleted, workorder
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted
- XBatch_Work_Order_Mst_Tbl: CampaignId, ID, IsDeleted
- XMES_Billet_Tracking_Trn_Tbl: BilletNo, HeatNo, IsDeleted, Materialid, StatePosition
- XMES_Campaign_Plan_Mst: ID, IsDeleted, Productname
- XMES_Live_Billet_Charging_Bed: BilletNo, ID, IsDeleted, ParentID
- XMES_Live_Charging_SECT1: ID, IsDeleted, ParentID
- XMES_Live_Charging_SECT2: BilletNo, ID, IsDeleted, ParentID, Weighment
- XMES_RM_Furnace_Billet_Trn_Tbl: IsDeleted
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber

## Writes (named in its SQL text)

- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst

## Calls

- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- XBatch_Campaign_Plan_Modified_Status_Usp
- XBatch_Update_Furnace_Billet_Tracking_Status
