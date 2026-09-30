---
type: procedure
title: "XMES_AUTO_WO_AND_SO_CALCULATION_old"
built: "2026-09-24T11:36:36"
---

# XMES_AUTO_WO_AND_SO_CALCULATION_old

Parameters: @Plant varchar, @WorkOrder varchar.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ProgressTonnage
- XBatch_Work_Order_Mst_Tbl: ProgressTonnage, Status

## Reads

- CCM_Per_Heat: ActualBilletWeightTon, TotalProduction, WorkOrder
- EAF_PER_HEAT: CalcLiquidMetalWeight, LiquidMetalWeight, WorkOrder
- LRF_Per_Heat: CalcLiquidMetalWeight, LiquidMetalWeight, WorkOrder
- XBatch_Sales_Order_Mst_Tbl: ID
- XBatch_Work_Order_Mst_Tbl: Equipment, ID, MfgOrderPlannedStartDate, Quantity, RemainingTonnage, SalesOrder
