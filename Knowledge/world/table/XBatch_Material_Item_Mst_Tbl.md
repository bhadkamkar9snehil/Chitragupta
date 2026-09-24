---
type: table
title: "XBatch_Material_Item_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Item_Mst_Tbl

Table in XStudio_Xbatch. Rows: 4,347.

## Identifiers it holds

- LotNumber: same values as key `HeatNo`

## Written by

- XBatch_Remove_Unused_Records_Usp

## Read by

- XBatch_Check_Material_Availibility_And_Connection_Usp
- XBatch_Remove_Unused_Records_Usp

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
- Vendor varchar(100)
- LotNumber varchar(100)
- Quantity decimal
- Price decimal
- PONumber varchar(100)
- InvoiceNumber varchar(100)
- ReceivedDate datetime
- LocationType varchar(100)
- LocationID varchar(36)
- LocationName varchar(100)
- ExpiryDate date
- IsExpired bit
- UOMID varchar(36)
- GradeID varchar(36)
- GRNNumber varchar(100)
- Description varchar(1000)
