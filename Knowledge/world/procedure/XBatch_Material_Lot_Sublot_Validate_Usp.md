---
type: procedure
title: "XBatch_Material_Lot_Sublot_Validate_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Lot_Sublot_Validate_Usp

Parameters: @ID varchar, @LotNumber varchar, @SubLotNumber varchar, @Source varchar, @AvailableQuantity decimal, @Quantity decimal.

## Reads

- XBatch_Material_Inventory_Mst_Tbl: ID, IsDeleted, LotNumber, SublotNumber
