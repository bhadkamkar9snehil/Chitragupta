---
type: procedure
title: "XBatch_WO_Get_Process_Cell_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_WO_Get_Process_Cell_Usp

Parameters: @WorkOrderID varchar.

## Reads

- XBatch_Batch_Mst_Tbl: ID, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, Name
- XBatch_Process_Cell_Mst_Tbl: Capacity, CurrentBatchID, ID, MaxCapacity, MinCapacity, Name, NextAvailableTime, Status, UnitID
- XBatch_Recipe_Mst_Tbl: ID, MaterialID, ProcessCellID, ProcessTime
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, Status
