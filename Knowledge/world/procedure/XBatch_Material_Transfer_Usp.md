---
type: procedure
title: "XBatch_Material_Transfer_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Transfer_Usp

Parameters: @SourceItemId varchar, @TransfereItemId varchar.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: Description, ExpiryDate, GRNNumber, GradeID, InvoiceNumber, IsExpired, ItemSource, LocationID, LocationName, PONumber, Price, Quantity, ReceivedDate, Vendor

## Reads

- XBatch_Material_Inventory_Mst_Tbl: ID, LocationType, LotNumber, SublotNumber
