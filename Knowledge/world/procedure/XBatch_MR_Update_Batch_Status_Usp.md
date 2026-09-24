---
type: procedure
title: "XBatch_MR_Update_Batch_Status_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_MR_Update_Batch_Status_Usp

Parameters: @BatchID varchar, @Status varchar.

## Writes

- XBatch_Batch_Mst_Tbl: ActualEndTime, ActualStartTime, EndTime, StartTime, StatusID
- XBatch_Process_Cell_Mst_Tbl: CurrentBatchID, NextAvailableTime

## Reads

- XBatch_Batch_Mst_Tbl: EndTime, ID, IsDeleted, ParentID, ProcessCellID
- XBatch_Process_Cell_Mst_Tbl: ID
- XBatch_Recipe_Mst_Tbl: ID, ProcessTime
- XBatch_Status_Mst_Tbl: ID, IsDeleted, Name
