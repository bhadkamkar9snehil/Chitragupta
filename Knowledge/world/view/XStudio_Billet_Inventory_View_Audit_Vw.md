---
type: view
title: "XStudio_Billet_Inventory_View_Audit_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_Billet_Inventory_View_Audit_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Grade: same values as key `Grade`

## Reads

- Billet_Inventory_View_Audit
- XBatch_Material_Grade_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Storage_Rack_Mst_Tbl
- XStudio_Equipment_Mst_Vw

## Columns

- MaterialID varchar(36)
- MaterialCode varchar(100)
- MaterialName varchar(100)
- HeatNo varchar(100)
- BilletNo varchar(100)
- Quantity decimal
- UOM varchar(100)
- Grade varchar(100)
- GradeID varchar(36)
- MaterialGrade varchar(100)
- UOMID varchar(36)
- LocationName varchar(500)
- Description varchar(100)
- ExpiryDate nvarchar(8000)
- LocationType varchar(100)
- ReceivedDate nvarchar(8000)
- Crosssection varchar(100)
- GRNNumber varchar(100)
- Height int
- InvoiceNumber varchar(100)
- IsAllocated varchar(100)
- IsAvailable varchar(100)
- IsExpired bit
- ItemSource varchar(100)
- Length int
- Price decimal
- PONumber varchar(100)
- Remark varchar(100)
- TotalQty int
- Vendor varchar(100)
- ID varchar(36)
- Status varchar(100)
- ModifiedOn datetime
- ModifiedBy varchar(100)
- HostAddress varchar(100)
