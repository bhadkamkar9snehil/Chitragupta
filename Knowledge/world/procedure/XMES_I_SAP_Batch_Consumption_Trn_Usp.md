---
type: procedure
title: "XMES_I_SAP_Batch_Consumption_Trn_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_SAP_Batch_Consumption_Trn_Usp

Parameters: @ID varchar, @BatchWt decimal.

## Writes

- MES_SAP_Consumption_Trn_Tbl: Batch, EntryUnit, GoodsMovementType, Grade, HeatNo, ManufacturingOrder, Material, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation

## Reads

- MES_SAP_Production_Trn_Tbl: Batch, ManufacturingOrder, Material
- RM_Operator_HeatSelection: Batch, BilletMaterialType, BilletQty, Grade, Heatno, ID
