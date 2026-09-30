---
type: procedure
title: "XBatch_Check_Material_Availibility_And_Connection_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Check_Material_Availibility_And_Connection_Usp

Parameters: @PhaseID varchar, @MaterialID varchar.

## Reads

- XBatch_Batch_Operation_Mst_Tbl: EquipmentTypeID, ID
- XBatch_Batch_Phase_Group_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Batch_Phase_Mst_Tbl: ID, IsDeleted, ParentID, Quantity
- XBatch_Connection_Mst_Tbl: DestinationEquipmentID, ID, IsDeleted, SourceEquipmentID, Status
- XBatch_Material_Item_Mst_Tbl: IsDeleted, LocationID, LocationType, ParentID
