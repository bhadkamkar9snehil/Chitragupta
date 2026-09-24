---
type: table
title: "XBatch_Process_Cell_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Process_Cell_Mst_Tbl

Table in XStudio_Xbatch. Rows: 1.

## Written by

- XBatch_MR_Update_Batch_Status_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_Reset_System_Usp
- XBatch_WO_Create_Batch_AI_Usp (text)

## Read by

- XBatch_Get_Historian_Channels_By_Process_Cell_Usp
- XBatch_MR_Get_Batch_Detail_Usp
- XBatch_MR_Update_Batch_Status_Usp
- XBatch_Remove_Unused_Records_Usp
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
- Capacity decimal
- UnitID varchar(36)
- Description varchar(-1)
- IsEnabled bit
- Status varchar(36)
- CurrentBatchID varchar(36)
- MinCapacity decimal
- MaxCapacity decimal
- CollectorName varchar(100)
- NextAvailableTime datetime
