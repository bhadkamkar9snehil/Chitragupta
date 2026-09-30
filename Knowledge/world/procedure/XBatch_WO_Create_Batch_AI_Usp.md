---
type: procedure
title: "XBatch_WO_Create_Batch_AI_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_WO_Create_Batch_AI_Usp


## Writes

- XBatch_Work_Order_Mst_Tbl: ModifiedOn, Status

## Reads

- XBatch_Material_Mst_Tbl: ID, IsDeleted, UnitID
- XBatch_Recipe_Mst_Tbl: ID, IsDeleted, MaterialID, Position, ProcessCellID, ProcessTime, Version
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, Quantity

## Writes (named in its SQL text)

- XBatch_Process_Cell_Mst_Tbl
