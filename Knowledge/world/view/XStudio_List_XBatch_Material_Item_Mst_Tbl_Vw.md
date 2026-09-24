---
type: view
title: "XStudio_List_XBatch_Material_Item_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Material_Item_Mst_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`
- LotNumber: same values as key `HeatNo`

## Reads

- XBatch_Material_Grade_Mst_Tbl
- XBatch_Material_Item_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Storage_Rack_Mst_Tbl
- XStudio_Equipment_Mst_Vw

## Columns

- Edit varchar(246)
- ID varchar(36)
- ParentID varchar(36)
- ItemType varchar(100)
- ItemName varchar(100)
- LotNumber varchar(100)
- ReceivedDate datetime
- LocationType varchar(100)
- LocationName varchar(500)
- LocationID varchar(36)
- Sublot varchar(-1)
- Quantity decimal
- UOM varchar(100)
- Grade varchar(100)
- Price decimal
- Vendor varchar(100)
- PONumber varchar(100)
- GRNNumber varchar(100)
- InvoiceNumber varchar(100)
- Expired bit
- ExpiryDate date
- Delete varchar(100)
- UOMID varchar(36)
- GradeID varchar(36)
