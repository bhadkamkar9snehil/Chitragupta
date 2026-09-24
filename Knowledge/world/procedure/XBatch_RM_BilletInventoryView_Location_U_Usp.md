---
type: procedure
title: "XBatch_RM_BilletInventoryView_Location_U_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_BilletInventoryView_Location_U_Usp

Parameters: @HeatNo varchar, @AssignQty int, @TotalQty int, @Location varchar, @Material varchar, @Grade varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- Billet_Inventory_View: Grade, GradeID, LocationID, LocationName, Status

## Reads

- Billet_Inventory_View: Description, ExpiryDate, GRNNumber, Grade, ID, InvoiceNumber, IsDeleted, IsExpired, LocationName, LocationType, LotNumber, MaterialGrade, OperationID, PONumber, Price, Quantity, ReceivedDate, Remark, Status, SublotNumber, UOMID, Vendor
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Inventory_Mst_Tbl: IsDeleted, LotNumber, SublotNumber
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name
