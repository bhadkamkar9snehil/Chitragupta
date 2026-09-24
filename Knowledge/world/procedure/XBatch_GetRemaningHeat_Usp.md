---
type: procedure
title: "XBatch_GetRemaningHeat_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_GetRemaningHeat_Usp

Parameters: @type bit, @WOID varchar, @IsExt bit.

## Reads

- Grade_Master: GradeName, ID, IsDeleted
- RM_Operator_HeatSelection: Batch, BilletQty, Heatno, IsDeleted, Status
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name, TypeID
- XBatch_Material_Type_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, ItemID
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, HeatNo, IsDeleted, Materialid, PostingMaterialType, StatePosition
- XMES_Billet_VS_GLS_Grade_Mapping: BilletGrade, EndproductGrade, IsDeleted
- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted, Status
- XMES_Live_Charging_SECT1: BilletNo, IsDeleted, Status
- XMES_Live_Charging_SECT2: BilletNo, IsDeleted, Status
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber
