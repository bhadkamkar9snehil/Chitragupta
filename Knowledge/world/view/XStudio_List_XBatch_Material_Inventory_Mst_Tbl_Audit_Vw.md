---
type: view
title: "XStudio_List_XBatch_Material_Inventory_Mst_Tbl_Audit_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Material_Inventory_Mst_Tbl_Audit_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
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

- Name varchar(100)
- MaterialCode varchar(100)
- ID varchar(36)
- Material varchar(100)
- HeatNo varchar(100)
- BilletNo varchar(100)
- Quantity decimal
- MaterialGrade varchar(100)
- UOM varchar(100)
- Grade varchar(100)
- Split varchar(-1)
- GradeID varchar(36)
- Transfer varchar(-1)
- Reclassify varchar(-1)
- LocationType varchar(100)
- LocationName varchar(500)
- ReceivedDate nvarchar(8000)
- ItemSource varchar(100)
- Description varchar(1000)
- OperationID varchar(36)
- ParentID varchar(36)
- Price decimal
- Vendor varchar(100)
- PONumber varchar(100)
- UOMID varchar(36)
- GRNNumber varchar(100)
- InvoiceNumber varchar(100)
- Details varchar(-1)
- Expired bit
- ExpiryDate nvarchar(8000)
- WorkOrderNumber varchar(100)
- BatchNumber varchar(100)
- BatchOperation varchar(100)
- ModifiedOn datetime
- ModifiedBy varchar(100)
- HostAddress varchar(100)
