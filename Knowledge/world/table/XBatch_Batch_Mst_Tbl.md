---
type: table
title: "XBatch_Batch_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Batch_Mst_Tbl

Table in XStudio_Xbatch. Rows: 1.

## Written by

- XBatch_MR_Update_Batch_Component_Status_Usp
- XBatch_MR_Update_Batch_Status_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_WO_Create_Batch_Usp

## Read by

- XBatch_Create_Batch_Usp
- XBatch_Generate_Next_Batch_No_Usp
- XBatch_MR_Update_Batch_Component_Status_Usp
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
- BatchNumber varchar(100)
- BatchMode varchar(100)
- ProcessCellID varchar(-1)
- Quantity decimal
- QuantityUnitID varchar(36)
- StartTime datetime
- EndTime datetime
- StatusID varchar(36)
- Version varchar(100)
- Position varchar(100)
- ApprovedBy varchar(36)
- ApprovedOn datetime
- ScheduledBy varchar(36)
- ScheduledOn datetime
- ActualStartTime datetime
- ActualEndTime datetime
- WorkOrderID varchar(36)
