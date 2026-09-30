---
type: procedure
title: "SP_Xbatch_YMS_U_OutwardLocation"
built: "2026-09-24T11:36:36"
---

# SP_Xbatch_YMS_U_OutwardLocation

Parameters: @ID varchar, @Userid varchar.

## Writes

- XBatch_Billets_Transfer_History_Tbl: ActionBy, BilletNo, CurrentStatus, ID, InventoryID, LayerID, LocationAssignedDate, MaterialGrade, ParentID, RecievedBy, RecievedDate, StackID, SubLotNo
- XBatch_Material_Inventory_Mst_Tbl: LocationID, MovementType, OutwardDate, Outwardby, Quantity

## Reads

- XBatch_Material_Inventory_Mst_Tbl: ID, IsDeleted, LotNumber, MaterialGrade, OutwardLocation, ParentID, SublotNumber
- XBatch_OutwardLocation_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Area_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name, ParentID
