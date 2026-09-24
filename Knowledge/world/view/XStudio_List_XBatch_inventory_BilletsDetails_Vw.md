---
type: view
title: "XStudio_List_XBatch_inventory_BilletsDetails_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_inventory_BilletsDetails_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- XBatch_Batch_Mst_Tbl
- XBatch_Batch_Operation_Mst_Tbl
- XBatch_Batch_Unit_Procedure_Mst_Tbl
- XBatch_Material_Grade_Mst_Tbl
- XBatch_Material_Inventory_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl

## Columns

- Action varchar(50)
- Edit varchar(249)
- MaterialGrade varchar(100)
- MovementType varchar(100)
- ReceivedDate datetime
- Grade varchar(50)
- ID varchar(36)
- ItemType varchar(100)
- ItemCode varchar(100)
- ItemName varchar(100)
- HeatNo varchar(100)
- BilletNo varchar(100)
- Quantity decimal
- Transfer varchar(-1)
- UOM varchar(100)
- ItemSource varchar(50)
- Reclassify varchar(-1)
- FromLocation varchar(100)
- ToLocation varchar(100)
- Graded varchar(100)
- Description varchar(1000)
- AvailableQuantityPrice decimal
- OperationID varchar(36)
- Price decimal
- ParentID varchar(36)
- Vendor varchar(100)
- PONumber varchar(100)
- GRNNumber varchar(100)
- InvoiceNumber varchar(100)
- UOMID varchar(36)
- Expired bit
- ExpiryDate date
- WorkOrderNumber varchar(100)
- BatchNumber varchar(100)
- Details varchar(-1)
- BatchOperation varchar(100)
- Delete varchar(100)
- dd varchar(220)
