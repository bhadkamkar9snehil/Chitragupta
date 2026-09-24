---
type: procedure
title: "Billet_Furnace_Movement_HeatGap"
built: "2026-09-24T11:36:36"
---

# Billet_Furnace_Movement_HeatGap


## Writes

- BilletsPosition_InFurnace: Position1, Position10, Position11, Position12, Position13, Position14, Position15, Position16, Position17, Position18, Position19, Position2, Position20, Position21, Position22, Position23, Position24, Position25, Position26, Position27, Position28, Position29, Position3, Position30, Position31, Position32, Position33, Position34, Position35, Position36, Position37, Position38, Position39, Position4, Position40, Position41, Position42, Position43, Position44, Position45, Position46, Position47, Position48, Position49, Position5, Position50, Position51, Position52, Position53, Position54, Position55, Position56, Position57, Position58, Position59, Position6, Position60, Position61, Position62, Position63, Position64, Position65, Position7, Position8, Position9
- RM_Operator_HeatSelection: BilletoutofFurnace
- XMES_Billet_Strand_tracking: BIlletNo, EndProduct, ParentID
- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn
- XMES_Live_Charging_SECT2: FurnaceOutTime
- XMES_RM_Furnace_Billet_Trn_Tbl: EndTime, zone1ResidenceTime, zone2ResidenceTime, zone3ResidenceTime, zone4ResidenceTime, zone5ResidenceTime, zone6ResidenceTime, zone7ResidenceTime, zone8ResidenceTime
- XMES_RM_Heated_Billet_trn_tbl: BilletNo, HeatNO, ProductType, Workorderid

## Reads

- BilletsPosition_InFurnace: IsDeleted, Position16, Position24, Position32, Position40, Position48, Position56, Position64, Position65, Position8
- Product_Master: ID
- RM_Operator_HeatSelection: ID, workorder
- XBatch_Work_Order_Mst_Tbl: CampaignId, ID
- XMES_Billet_Strand_tracking: ID, IsDeleted
- XMES_Campaign_Plan_Mst: ID, Productname
- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted, ParentID
- XMES_Live_Charging_SECT2: BilletNo
- XMES_RM_Furnace_Billet_Trn_Tbl: BilletNo
