---
type: procedure
title: "XBatch_WO_Create_Batch_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_WO_Create_Batch_Usp

Parameters: @BatchList BatchToGenerate, @UserID varchar, @WorkOrderID varchar.

## Writes

- XBatch_Batch_Mst_Tbl: ApprovedBy, ApprovedOn, BatchMode, BatchNumber, CreatedBy, CreatedOn, EndTime, ID, Name, ParentID, Position, ProcessCellID, Quantity, QuantityUnitID, ScheduledBy, ScheduledOn, Source, StartTime, StatusID, Version, WorkOrderID

## Reads

- XBatch_Recipe_Mst_Tbl: ID, Position, Version
- XBatch_Status_Mst_Tbl: ID, Name

## Calls

- XBatch_Create_Batch_Usp
