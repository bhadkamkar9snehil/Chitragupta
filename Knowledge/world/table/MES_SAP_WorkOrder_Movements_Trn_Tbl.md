---
type: table
title: "MES_SAP_WorkOrder_Movements_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_WorkOrder_Movements_Trn_Tbl

Table in XStudio_Xbatch. Rows: 607,884.

## Written by

- XMES_SAP_Posting_Sequence_Usp

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- EntryDateTime datetime
- PostingDate date
- IsProcessed bit
- MaterialDocument varchar(100)
- MovementType int
- Batch varchar(100)
- StorageLocation int
- DebitCreditindication varchar(100)
- Quantity decimal
- NoOfItem int
- QuantityinCount int
