---
type: procedure
title: "SP_XBatch_YMS_TransferIntoHistory"
built: "2026-09-24T11:36:36"
---

# SP_XBatch_YMS_TransferIntoHistory

Parameters: @GradeNo varchar, @StackID varchar, @UserID varchar, @HeatNo varchar.

## Writes

- XBatch_Billets_Transfer_History_Tbl: ActionBy, BilletNo, CurrentStatus, ID, InventoryID, LayerID, LocationAssignedDate, MaterialGrade, ParentID, RecievedBy, RecievedDate, StackID, SubLotNo

## Reads

- XBatch_Material_Inventory_Mst_Tbl: ID, IsDeleted, LocationID, LotNumber, MaterialGrade, ParentID, SublotNumber
- XBatch_Storage_Area_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name
