---
type: procedure
title: "XBatch_I_Material_Inventory_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Material_Inventory_USP

Parameters: @Name varchar, @LotNumber varchar, @SublotNumber varchar, @Grade varchar, @Quantity decimal, @UOMName varchar, @LocationType varchar, @Location varchar, @IsExpired bit, @ExpiryDate date, @ReceivedDate datetime, @Vendor varchar, @PONumber varchar, @GRNNumber varchar, @InvoiceNumber varchar, @Price decimal, @Description varchar, @OperationID varchar, @Remark varchar, @UserID varchar.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: CreatedBy, CreatedOn, Description, ExpiryDate, GRNNumber, GradeID, ID, InvoiceNumber, IsExpired, ItemSource, LocationID, LocationType, LotNumber, OperationID, PONumber, ParentID, Price, Quantity, ReceivedDate, Remark, Source, SublotNumber, UOMID, Vendor

## Reads

- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name
- XStudio_Equipment_Mst_Vw: EquipmentName, ID
