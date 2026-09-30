---
type: procedure
title: "XMES_U_Inventory_Master_byTrn_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_U_Inventory_Master_byTrn_Usp

Parameters: @EntryDateTime datetime.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: CreatedOn, LotNumber, MaterialGrade, ModifiedOn, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID
- Xbatch_Material_Inventory_Trn_Tbl: Ismodified, ModifiedOn, Source

## Reads

- XBatch_Material_Inventory_Mst_Tbl: IsDeleted
- Xbatch_Material_Inventory_Trn_Tbl: CreatedOn, IsDeleted, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, StorageLocation, UOMID
