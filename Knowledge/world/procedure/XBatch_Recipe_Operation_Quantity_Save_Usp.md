---
type: procedure
title: "XBatch_Recipe_Operation_Quantity_Save_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Recipe_Operation_Quantity_Save_Usp

Parameters: @OperationID varchar, @OutputMaterialID varchar.

## Writes

- XBatch_Recipe_Operation_Mst_Tbl: OutputMaterialQuantity

## Reads

- XBatch_Formula_Dtl_Tbl: MaterialID, Quantity
- XBatch_Formula_Mst_Tbl: ParentID, Quantity
- XBatch_Recipe_Operation_Mst_Tbl: ID
