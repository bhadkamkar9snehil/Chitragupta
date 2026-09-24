---
type: table
title: "XBatch_Material_Inventory_Mst_Tbl_Audit"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Inventory_Mst_Tbl_Audit

Table in XStudio_Xbatch. Rows: 155.

## Identifiers it holds

- LotNumber: same values as key `LotNumber`
- SublotNumber: same values as key `SublotNumber`

## Columns

- ID varchar(36)
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
- LotNumber varchar(100)
- SublotNumber varchar(100)
- Quantity decimal
- UOMID varchar(36)
- LocationType varchar(100)
- LocationID varchar(36)
- LocationName varchar(100)
- IsExpired bit
- ExpiryDate date
- ReceivedDate datetime
- Vendor varchar(100)
- PONumber varchar(100)
- GRNNumber varchar(100)
- InvoiceNumber varchar(100)
- Price decimal
- Description varchar(1000)
- OperationID varchar(36)
- ItemSource varchar(50)
- Remark varchar(1000)
- LotwiseBillet varchar(100)
- SrNo varchar(100)
- MaterialGrade varchar(100)
- AvailableQuantityPrice decimal
- BilletReceivedBy varchar(100)
- StackLocation varchar(100)
- InwardDate datetime
- InwardBy varchar(36)
- MovementType varchar(100)
- OutwardLocation varchar(36)
- Outwardby varchar(36)
- OutwardDate datetime
- GradeID varchar(50)
- outwardremarks varchar(-1)
- Color varchar(100)
- LayerNo varchar(100)
- BilletLength int
