---
type: procedure
title: "XMES_BackCalculation_Validation_GLS_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_BackCalculation_Validation_GLS_Usp

Parameters: @HeatNo int.

## Writes

- EAF_PER_HEAT: CalcLiquidMetalWeight
- LRF_Per_Heat: CalcLiquidMetalWeight

## Reads

- CCM_Per_Heat: ActualBilletWeightTon, CreatedOn, EndCutMeter, Grade, HeatID, IsDeleted, LaunderLossTon, OtherLossesTon, SetWeightTon, TotalProduction, TundishlossTon, WorkOrder
- EAF_PER_HEAT: HeatID
- LRF_Per_Heat: HeatID
- XBatch_Formula_Dtl_Tbl: IsDeleted, MaterialID, ParentID, Quantity
- XBatch_Formula_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID
