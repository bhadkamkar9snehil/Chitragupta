---
type: view
title: "XStudio_List_XBatch_inventory_BilletsDetails_CP_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_inventory_BilletsDetails_CP_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- XBatch_Batch_Mst_Tbl
- XBatch_Batch_Operation_Mst_Tbl
- XBatch_Batch_Unit_Procedure_Mst_Tbl
- XBatch_Material_Inventory_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_OutwardLocation_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl

## Columns

- ToLocation varchar(100)
- OutwardLocation varchar(100)
- Action varchar(50)
- OutwardBy varchar(100)
- MaterialGrade varchar(100)
- Edit varchar(249)
- InwardBy varchar(100)
- OutwardDate datetime
- Grade varchar(50)
- InwardDate datetime
- Outward varchar(-1)
- MovementType varchar(100)
- ID varchar(36)
- ItemType varchar(100)
- ItemCode varchar(100)
- ItemName varchar(100)
- HeatNo varchar(100)
- BilletNo varchar(100)
- Transfer varchar(-1)
- Quantity decimal
- UOM varchar(100)
- ReceivedDate datetime
- Description varchar(1000)
- Reclassify varchar(-1)
- AvailableQuantityPrice decimal
- Price decimal
- Vendor varchar(100)
- PONumber varchar(100)
- GRNNumber varchar(100)
- ItemSource varchar(50)
- OperationID varchar(36)
- InvoiceNumber varchar(100)
- Expired bit
- LayerNo int
- ParentID varchar(36)
- ExpiryDate date
- FromLocation varchar(100)
- WorkOrderNumber varchar(100)
- BatchNumber varchar(100)
- BatchOperation varchar(100)
- UOMID varchar(36)
- Details varchar(-1)
- Delete varchar(100)
- dd varchar(220)
- InwardByID varchar(36)
- Outwardbyid varchar(36)
- OutwardLocationID varchar(36)
- LocationID varchar(36)
