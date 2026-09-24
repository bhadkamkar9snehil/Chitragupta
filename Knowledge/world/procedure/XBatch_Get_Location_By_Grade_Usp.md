---
type: procedure
title: "XBatch_Get_Location_By_Grade_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Location_By_Grade_Usp

Parameters: @Type varchar, @GradeNo varchar.

## Reads

- XBatch_Material_Inventory_Mst_Tbl: IsDeleted, LocationID, MaterialGrade, MovementType
- XBatch_Storage_Area_Mst_Tbl: GradeType, ID, IsDeleted, Name, ParentID
- XBatch_Storage_Rack_Mst_Tbl: Capacity, ID, IsDeleted, ParentID
