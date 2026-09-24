---
type: procedure
title: "XBatch_I_Material_Produce_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Material_Produce_USP

Parameters: @BOMID varchar, @ItemName varchar, @LotNumber varchar, @SublotNumber varchar, @Quantity decimal, @UOMName varchar, @Grade varchar, @UserID varchar.

## Writes

- XBatch_Batch_BOM_Mst_Tbl: ActualQuantity
- XBatch_Material_Inventory_Mst_Tbl: CreatedBy, CreatedOn, Description, ExpiryDate, GRNNumber, GradeID, ID, InvoiceNumber, IsExpired, ItemSource, LocationID, LocationType, LotNumber, OperationID, PONumber, ParentID, Price, Quantity, ReceivedDate, Remark, Source, SublotNumber, UOMID, Vendor
- XBatch_Material_Item_Prod_Trn_Tbl: CreatedBy, CreatedOn, GradeID, ID, LotNumber, ParentID, Quantity, Source, SublotNumber, UOMID

## Reads

- XBatch_Batch_BOM_Mst_Tbl: ID, IsDeleted, OperationID
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
