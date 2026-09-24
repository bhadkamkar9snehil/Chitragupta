---
type: table
title: "XBatch_Connection_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Connection_Mst_Tbl

Table in XStudio_Xbatch. Rows: 0.

## Written by

- XBatch_Remove_Unused_Records_Usp

## Read by

- XBatch_Check_Material_Availibility_And_Connection_Usp
- XBatch_Remove_Unused_Records_Usp

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
- CollectorName varchar(100)
- ChannelName varchar(100)
- SourceEquipmentID varchar(36)
- DestinationEquipmentID varchar(36)
- SourceEquipmentName varchar(100)
- DestinationEquipmentName varchar(100)
- Status varchar(15)
