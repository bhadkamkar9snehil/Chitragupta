---
type: procedure
title: "XBatch_RM_Rolling_Plan_Approval_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_Rolling_Plan_Approval_Usp

Parameters: @ID varchar.

## Writes

- RM_Rolling_Plan: Status

## Reads

- RM_Rolling_Plan: ID, IsDeleted, MaterialGrade, MaterialID, RollingDate, RollingID, SequenceNo
- Steel_Grade_Master: ID, IsDeleted, MaterialGrade
- XBatch_Formula_Dtl_Tbl: IsDeleted, ParentID
- XBatch_Formula_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Recipe_Mst_Tbl: IsDeleted, MaterialID
