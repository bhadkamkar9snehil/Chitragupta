---
type: view
title: "XStudio_List_XBatch_YMS_CurrentStatus_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_YMS_CurrentStatus_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- LotNumber: same values as key `HeatNo`
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

- ItemType varchar(100)
- Edit varchar(249)
- ItemCode varchar(100)
- ID varchar(36)
- ItemName varchar(100)
- LotNumber varchar(100)
- SublotNumber varchar(100)
- Quantity decimal
- UOM varchar(100)
- MaterialGrade varchar(100)
- Split varchar(-1)
- Transfer varchar(-1)
- Reclassify varchar(-1)
- FromLocation varchar(100)
- ToLocation varchar(100)
- Grade varchar(100)
- OperationID varchar(36)
- ParentID varchar(36)
- Description varchar(1000)
- AvailableQuantityPrice decimal
- Price decimal
- ReceivedDate datetime
- Vendor varchar(100)
- UOMID varchar(36)
- PONumber varchar(100)
- Details varchar(-1)
- GRNNumber varchar(100)
- Delete varchar(100)
- InvoiceNumber varchar(100)
- Expired bit
- ExpiryDate date
- WorkOrderNumber varchar(100)
- BatchNumber varchar(100)
- dd varchar(220)
- BatchOperation varchar(100)
- ItemSource varchar(50)
