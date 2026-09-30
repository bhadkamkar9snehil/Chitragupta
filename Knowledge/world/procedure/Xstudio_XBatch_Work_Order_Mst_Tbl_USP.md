---
type: procedure
title: "Xstudio_XBatch_Work_Order_Mst_Tbl_USP"
built: "2026-09-24T11:36:36"
---

# Xstudio_XBatch_Work_Order_Mst_Tbl_USP

Parameters: @ID varchar, @Mode varchar.

## Writes

- XBatch_Work_Order_Mst_Tbl: MaterialName, ProgressPercentage, RemainingTonnage, SalesOrderName, Source

## Reads

- XBatch_Material_Mst_Tbl: ID, Name
- XBatch_Sales_Order_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: ID, ItemID, ProgressTonnage, Quantity, SalesOrder
