---
type: procedure
title: "XBatch_I_Material_Inventory_Transfer_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Material_Inventory_Transfer_USP

Parameters: @Name varchar, @LotNumber varchar, @SublotNumber varchar, @Grade varchar, @Quantity decimal, @ToLocationType varchar, @ToLocation varchar, @FromLocationType varchar, @FromLocation varchar, @UserID varchar.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: CreatedBy, CreatedOn, Description, ExpiryDate, GRNNumber, GradeID, ID, InvoiceNumber, IsExpired, ItemSource, LocationID, LocationType, LotNumber, ModifiedOn, PONumber, ParentID, Price, Quantity, ReceivedDate, Source, SublotNumber, UOMID, Vendor

## Reads

- XBatch_Material_Inventory_Mst_Tbl: Description, ExpiryDate, GRNNumber, GradeID, ID, InvoiceNumber, IsDeleted, IsExpired, LotNumber, PONumber, ParentID, Price, SublotNumber, UOMID, Vendor
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name
- XStudio_Equipment_Mst_Vw: EquipmentName, ID
