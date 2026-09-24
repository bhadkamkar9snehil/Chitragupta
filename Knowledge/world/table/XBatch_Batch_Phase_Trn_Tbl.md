---
type: table
title: "XBatch_Batch_Phase_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Batch_Phase_Trn_Tbl

Table in XStudio_Xbatch. Rows: 0.

## Written by

- XBatch_Remove_Unused_Records_Usp

## Read by

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
- Type varchar(100)
- CapabilityID varchar(36)
- MaterialID varchar(36)
- SrNo int
- StartTime datetime
- EndTime datetime
- StatusID varchar(36)
