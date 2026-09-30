---
type: procedure
title: "XBatch_Material_Split_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Split_Usp

Parameters: @SourceItemId varchar, @SplitItemId varchar, @SplitQuantity decimal.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: Description, ExpiryDate, GRNNumber, GradeID, InvoiceNumber, IsExpired, ItemSource, LocationID, LocationName, LocationType, PONumber, Price, Quantity, ReceivedDate, Vendor

## Reads

- XBatch_Material_Inventory_Mst_Tbl: ID
