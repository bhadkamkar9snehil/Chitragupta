---
type: table
title: "XBatch_Recipe_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Recipe_Mst_Tbl

Table in XStudio_Xbatch. Rows: 7.

## Written by

- XBatch_Remove_Unused_Records_Usp

## Read by

- XBatch_MR_Update_Batch_Status_Usp
- XBatch_RM_Rolling_Plan_Approval_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_WO_Create_Batch_AI_Usp
- XBatch_WO_Create_Batch_Usp
- XBatch_WO_Get_Process_Cell_Usp

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
- MaterialID varchar(36)
- ProcessCellID varchar(-1)
- Version varchar(100)
- Status varchar(100)
- Position varchar(100)
- ProcessTime int
