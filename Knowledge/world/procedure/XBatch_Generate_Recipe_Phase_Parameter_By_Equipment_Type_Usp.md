---
type: procedure
title: "XBatch_Generate_Recipe_Phase_Parameter_By_Equipment_Type_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Generate_Recipe_Phase_Parameter_By_Equipment_Type_Usp

Parameters: @PhaseID varchar, @EquipmentTypeID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Recipe_Phase_Mst_Tbl: Quantity
- XBatch_Recipe_Phase_Parameter_Mst_Tbl: CreatedOn, Description, ModifiedOn, Name, ParentID

## Reads

- Equipment_Type_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Formula_Dtl_Tbl: MaterialID, Quantity
- XBatch_Formula_Mst_Tbl: ParentID, Quantity
- XBatch_Recipe_Phase_Mst_Tbl: CapabilityID, ID, MaterialID, Type
- XBatch_Recipe_Phase_Parameter_Mst_Tbl: ID, IsDeleted
