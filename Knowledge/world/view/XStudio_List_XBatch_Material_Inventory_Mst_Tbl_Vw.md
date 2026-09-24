---
type: view
title: "XStudio_List_XBatch_Material_Inventory_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Material_Inventory_Mst_Tbl_Vw

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

- ReceivedDate datetime
- Edit varchar(249)
- PlantName varchar(36)
- StorageLocation varchar(36)
- ItemType varchar(100)
- ItemCode varchar(100)
- ID varchar(36)
- ItemName varchar(100)
- LotNumber varchar(100)
- SublotNumber varchar(100)
- Quantity decimal
- AddDetails varchar(-1)
- UOM varchar(100)
- MaterialGrade varchar(100)
- StackLocation varchar(100)
- Grade varchar(50)
- LocationType varchar(100)
- Split varchar(-1)
- GradeID varchar(100)
- LocationName varchar(500)
- Transfer varchar(-1)
- Reclassify varchar(-1)
- Description varchar(1000)
- AvailableQuantityPrice decimal
- Price decimal
- Vendor varchar(100)
- OperationID varchar(36)
- ItemSource varchar(50)
- ParentID varchar(36)
- ModifiedOn datetime
- IsPlantToPlantTransfer bit
- PostingMaterialType varchar(100)
- Delete varchar(100)
- PONumber varchar(100)
- GRNNumber varchar(100)
- UOMID varchar(36)
- InvoiceNumber varchar(100)
- Details varchar(-1)
- WorkOrderNumber varchar(100)
- BatchNumber varchar(100)
- BatchOperation varchar(100)
- Expired bit
- ExpiryDate date
- MaterialGradeColorCode varchar(50)
