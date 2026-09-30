---
type: procedure
title: "XMES_U_SAP_Billet_Production_Trn_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_U_SAP_Billet_Production_Trn_Usp

Parameters: @ProductionID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- Xbatch_Material_Inventory_Trn_Tbl: CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- CCM_Per_Heat: HeatID, IsDeleted, WorkOrder
- MES_SAP_Production_Trn_Tbl: Batch, BilletNo, CreatedBy, Cutlength, HeatNo, ID, IsDeleted, Plant, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, StorageLocation
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, WorkOrderNumber

## Writes (named in its SQL text)

- MES_SAP_Production_Trn_Tbl
