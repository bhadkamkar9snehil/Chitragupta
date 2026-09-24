---
type: view
title: "XStudio_List_XBatch_Material_Inventory_Mst_Tbl_U_Audit_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Material_Inventory_Mst_Tbl_U_Audit_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- LotNumber: same values as key `LotNumber`
- SublotNumber: same values as key `SublotNumber`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- XBatch_Batch_Mst_Tbl
- XBatch_Batch_Operation_Mst_Tbl
- XBatch_Batch_Unit_Procedure_Mst_Tbl
- XBatch_Material_Grade_Mst_Tbl
- XBatch_Material_Inventory_Mst_Tbl_Audit
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Storage_Rack_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XStudio_Equipment_Mst_Vw

## Columns

- ItemType varchar(100)
- ItemCode varchar(100)
- ID varchar(36)
- ItemName varchar(100)
- LotNumber varchar(100)
- MaterialGrade varchar(100)
- SublotNumber varchar(100)
- Quantity decimal
- UOM varchar(100)
- Grade varchar(100)
- GradeID varchar(36)
- Split varchar(-1)
- Transfer varchar(-1)
- Reclassify varchar(-1)
- LocationType varchar(100)
- LocationName varchar(500)
- OperationID varchar(36)
- ParentID varchar(36)
- Description varchar(1000)
- Price decimal
- ReceivedDate nvarchar(8000)
- Vendor varchar(100)
- PONumber varchar(100)
- UOMID varchar(36)
- GRNNumber varchar(100)
- Details varchar(-1)
- InvoiceNumber varchar(100)
- Expired bit
- WorkOrderNumber varchar(100)
- ExpiryDate nvarchar(8000)
- BatchNumber varchar(100)
- BatchOperation varchar(100)
- ItemSource varchar(100)
- ModifiedOn datetime
- ModifiedBy varchar(100)
- HostAddress varchar(100)
