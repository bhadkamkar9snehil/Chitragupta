---
type: procedure
title: "XBatch_MR_Update_Batch_Component_Status_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_MR_Update_Batch_Component_Status_Usp

Parameters: @PhaseID varchar, @Status varchar.

## Writes

- XBatch_Batch_Mst_Tbl: ModifiedOn, StatusID
- XBatch_Batch_Operation_Mst_Tbl: ModifiedOn, StatusID
- XBatch_Batch_Phase_Group_Mst_Tbl: ModifiedOn, StatusID
- XBatch_Batch_Phase_Mst_Tbl: ModifiedOn, StatusID
- XBatch_Batch_Unit_Procedure_Mst_Tbl: ModifiedOn, StatusID

## Reads

- XBatch_Batch_Mst_Tbl: ID, IsDeleted
- XBatch_Batch_Operation_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Batch_Phase_Group_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Batch_Phase_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Batch_Unit_Procedure_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Status_Mst_Tbl: ID, IsDeleted, Name
