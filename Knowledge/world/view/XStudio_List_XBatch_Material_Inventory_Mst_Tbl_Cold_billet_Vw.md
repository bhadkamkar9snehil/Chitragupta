---
type: view
title: "XStudio_List_XBatch_Material_Inventory_Mst_Tbl_Cold_billet_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Material_Inventory_Mst_Tbl_Cold_billet_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- LotNumber: same values as key `HeatNo`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- Grade_Master
- XBatch_Batch_Mst_Tbl
- XBatch_Batch_Operation_Mst_Tbl
- XBatch_Batch_Unit_Procedure_Mst_Tbl
- XBatch_Material_Grade_Mst_Tbl
- XBatch_Material_Inventory_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl
- XStudio_Equipment_Mst_Vw

## Columns

- Edit varchar(249)
- ReceivedDate datetime
- PlantName varchar(36)
- StorageLocation varchar(36)
- ID varchar(36)
- ItemType varchar(100)
- ItemCode varchar(100)
- ItemName varchar(100)
- MaterialGrade varchar(100)
- SublotNumber varchar(100)
- LotNumber varchar(100)
- QuantityinCount int
- Quantity decimal
- StackLocation varchar(100)
- LocationType varchar(100)
- Split varchar(-1)
- GradeID varchar(100)
- UOM varchar(100)
- Transfer varchar(-1)
- LocationName varchar(500)
- Reclassify varchar(-1)
- OperationID varchar(36)
- Grade varchar(50)
- ParentID varchar(36)
- AvailableQuantityPrice decimal
- Price decimal
- Vendor varchar(100)
- BilletTransfer varchar(-1)
- Description varchar(1000)
- Delete varchar(100)
- ItemSource varchar(50)
- PONumber varchar(100)
- GRNNumber varchar(100)
- ModifiedOn datetime
- UOMID varchar(36)
- InvoiceNumber varchar(100)
- Details varchar(-1)
- WorkOrderNumber varchar(100)
- BatchNumber varchar(100)
- BatchOperation varchar(100)
- Expired bit
- ExpiryDate date
- MaterialGradeColorCode varchar(50)
- IsPlantToPlantTransfer bit
- MaterialType varchar(100)
