---
type: procedure
title: "XMES_I_PlantToPlantTransfer_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_PlantToPlantTransfer_Usp

Parameters: @ID varchar, @ToPlant varchar, @ToStorageLocation varchar, @quantityinCount int, @quantityInentryUnit decimal.

## Writes

- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: Batch, CreatedOn, Customer, EntryUnit, GoodsMovementType, HeatNo, IssgOrRcvgBatch, IssgOrRcvgMaterial, IssuingOrReceivingPlant, IssuingOrReceivingStorageLoc, ManufacturingOrder, Material, Plant, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, SalesOrder, SalesOrderItem, Source, StorageLocation, Supplier

## Reads

- CCM_Per_Heat: HeatID, WorkOrder
- XBatch_Material_Inventory_Mst_Tbl: ID, IsDeleted, LotNumber, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, StorageLocation
- XBatch_Material_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: ID, SalesOrder, SalesOrderItem, WorkOrderNumber
