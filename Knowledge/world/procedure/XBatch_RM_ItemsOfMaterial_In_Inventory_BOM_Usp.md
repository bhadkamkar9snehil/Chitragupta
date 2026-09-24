---
type: procedure
title: "XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp

Parameters: @ID varchar, @IsGroupofSubLot bit.

## Reads

- Billet_Inventory: GradeID, IsAllocated, IsDeleted, LotNumber, MaterialID, Quantity, SublotNumber, UOMID
- RM_Rolling_Plan: ID, IsDeleted, MaterialID
- RM_Sales_Order: ID, IsDeleted, MaterialID
- XBatch_Formula_Dtl_Tbl: IsDeleted, MaterialID, ParentID
- XBatch_Formula_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Inventory_Mst_Tbl: GradeID, IsDeleted, LotNumber, ParentID, Quantity, SublotNumber, UOMID
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name, Number
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
