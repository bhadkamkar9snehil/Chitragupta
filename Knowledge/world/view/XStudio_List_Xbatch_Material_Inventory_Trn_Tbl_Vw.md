---
type: view
title: "XStudio_List_Xbatch_Material_Inventory_Trn_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_Xbatch_Material_Inventory_Trn_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- LotNumber: same values as key `HeatNo`

## Reads

- Grade_Master
- Plant_Name_MST
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- Xbatch_Material_Inventory_Trn_Tbl

## Columns

- Edit varchar(249)
- PlantCode varchar(36)
- StorageLocationCode varchar(36)
- PlantName varchar(100)
- ID varchar(36)
- ItemType varchar(100)
- ItemCode varchar(100)
- ItemName varchar(100)
- LotNumber varchar(100)
- Quantity decimal
- UOM varchar(100)
- QuantityinCount int
- MaterialGrade varchar(100)
- PostingMaterialType varchar(100)
- MaterialGradeColorCode varchar(50)
- ModifiedOn datetime
- ParentID varchar(36)
- Delete varchar(100)
- UOMID varchar(36)
- StorageLocation varchar(36)
- isExternal bit
