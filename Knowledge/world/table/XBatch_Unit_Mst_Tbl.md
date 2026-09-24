---
type: table
title: "XBatch_Unit_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Unit_Mst_Tbl

Table in XStudio_Xbatch. Rows: 1.

## Written by

- XBatch_Remove_Unused_Records_Usp
- XBatch_Reset_System_Usp

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
- Description varchar(-1)
- IsEnabled bit
- Status varchar(100)
- CurrentBatchID varchar(36)
- CurrentUnitProcedureID varchar(36)
