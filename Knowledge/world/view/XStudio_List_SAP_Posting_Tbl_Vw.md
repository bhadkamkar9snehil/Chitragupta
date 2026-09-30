---
type: view
title: "XStudio_List_SAP_Posting_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_SAP_Posting_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- SAP_Posting_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Store_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl

## Columns

- Edit varchar(233)
- PlantCode varchar(100)
- IsProcessed bit
- ID varchar(36)
- EntryDateTime datetime
- ReportDate date
- WorkOrderNumber varchar(100)
- HeatNo varchar(100)
- BatchNoorBilletNo varchar(100)
- MaterialCode varchar(100)
- StorageLocation varchar(100)
- Quantity decimal
- UnitofMeasure varchar(100)
- MovementType varchar(100)
- PostingType varchar(100)
- PostingDate datetime
- CreatedOn datetime
- CreatedBy varchar(200)
- ModifiedOn datetime
- Delete varchar(100)
- ModifiedBy varchar(200)
- SAPStatus varchar(100)
- SAPDocumentNo varchar(100)
- Details varchar(-1)
- SAPMessage varchar(100)
- CreatedByid varchar(36)
- SAPPayloadJSON varchar(-1)
- ModifiedByid varchar(36)
- MaterialColourCode varchar(50)
- StorageColourCode varchar(50)
- WorkOrderColourCode varchar(50)
