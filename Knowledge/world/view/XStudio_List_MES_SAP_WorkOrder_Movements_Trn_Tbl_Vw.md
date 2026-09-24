---
type: view
title: "XStudio_List_MES_SAP_WorkOrder_Movements_Trn_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_MES_SAP_WorkOrder_Movements_Trn_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- MES_SAP_WorkOrder_Movements_Trn_Tbl
- XBatch_Work_Order_Mst_Tbl

## Columns

- Edit varchar(253)
- ID varchar(36)
- Name varchar(100)
- EntryDateTime datetime
- WorkOrderNumber varchar(100)
- Material varchar(100)
- Batch varchar(100)
- MaterialDocument varchar(100)
- Count int
- QuantityTon decimal
- MovementType int
- DebitCreditindication varchar(100)
- IsProcessed bit
- StorageLocation int
- Item int
- Delete varchar(100)
- PostingDate date
- Details varchar(-1)
- ParentID varchar(36)
