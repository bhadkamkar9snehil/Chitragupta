---
type: procedure
title: "XMES_I_ByProduct_Trn_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_ByProduct_Trn_Usp

Parameters: @heatno int.

## Writes

- MES_SAP_By_Product_Trn_Tbl: EntryUnit, GoodsMovementType, Grade, HeatNo, ManufacturingOrder, Material, Plant, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation
- Xbatch_Material_Inventory_Trn_Tbl: CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- CCM_Per_Heat: EndCutMeter, Grade, HeatID, IsDeleted, LaunderLossTon, ScaleLossTon, SetWeightTon, TundishlossTon, WorkOrder
- MES_SAP_By_Product_Trn_Tbl: CreatedBy, Grade, HeatNo, IsDeleted, Material, Plant, QuantityInEntryUnit, StorageLocation
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name, Number, TypeID
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ProductionPlant, StorageLocation, WorkOrderNumber

## Writes (named in its SQL text)

- XBatch_Material_Inventory_Mst_Tbl
