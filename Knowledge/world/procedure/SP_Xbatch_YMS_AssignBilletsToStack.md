---
type: procedure
title: "SP_Xbatch_YMS_AssignBilletsToStack"
built: "2026-09-24T11:36:36"
---

# SP_Xbatch_YMS_AssignBilletsToStack

Parameters: @GradeNo varchar, @StackID varchar, @UserID varchar, @HeatNo varchar.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: InwardBy, InwardDate, LocationID, MovementType
- XBatch_Storage_Area_Mst_Tbl: GradeType

## Reads

- XBatch_Material_Inventory_Mst_Tbl: IsDeleted, LotNumber, MaterialGrade, SublotNumber
- XBatch_Storage_Area_Mst_Tbl: ID
- XBatch_Storage_Rack_Mst_Tbl: Capacity, ID, IsDeleted, Number, ParentID
