---
type: procedure
title: "XBatch_Create_Batch_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Create_Batch_Usp

Parameters: @BatchID varchar.

## Writes

- XBatch_Batch_BOM_Mst_Tbl: CreatedOn, ItemID, OperationID, ParentID, PhaseGroupID, PhaseID, Quantity, SourceType, UOMID, UnitProcedureID
- XBatch_Batch_Operation_Mst_Tbl: CreatedOn, EquipmentTypeID, ID, ModifiedOn, Name, OriginalID, OutputMaterialID, OutputMaterialQuantity, ParentID, Position, SrNo
- XBatch_Batch_Phase_Group_Mst_Tbl: CreatedOn, ID, Name, OriginalID, ParentID, Position, SrNo
- XBatch_Batch_Phase_Mst_Tbl: CapabilityID, CreatedOn, ID, MaterialID, Name, OriginalID, ParentID, Position, Quantity, SrNo, TemplateID, Type
- XBatch_Batch_Phase_Parameter_Mst_Tbl: CreatedOn, Description, ID, Name, OriginalID, ParentID, Value
- XBatch_Batch_Unit_Procedure_Mst_Tbl: CreatedOn, ID, ModifiedOn, Name, OriginalID, ParentID, Position, SrNo

## Reads

- XBatch_Batch_Mst_Tbl: ID, ParentID, Quantity
- XBatch_Material_Mst_Tbl: ID, UnitID
- XBatch_Recipe_Operation_Mst_Tbl: EquipmentTypeID, ID, IsDeleted, Name, OutputMaterialID, OutputMaterialQuantity, ParentID, Position, SrNo
- XBatch_Recipe_Phase_Group_Mst_Tbl: ID, IsDeleted, Name, ParentID, Position, SrNo
- XBatch_Recipe_Phase_Mst_Tbl: CapabilityID, ID, IsDeleted, MaterialID, Name, ParentID, Position, Quantity, SrNo, TemplateID, Type
- XBatch_Recipe_Phase_Parameter_Mst_Tbl: Description, ID, IsDeleted, Name, ParentID, Value
- XBatch_Recipe_Unit_Procedure_Mst_Tbl: ID, IsDeleted, Name, ParentID, Position, SrNo
