---
type: table
title: "XBatch_Status_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Status_Mst_Tbl

Table in XStudio_Xbatch. Rows: 12.

## Read by

- XBatch_MR_Get_Batch_Detail_Usp
- XBatch_MR_Update_Batch_Component_Status_Usp
- XBatch_MR_Update_Batch_Status_Usp
- XBatch_WO_Create_Batch_Usp
- XBatch_WO_Get_Process_Cell_Scheduled_Batch_Usp
- XMES_SO_Trn_VW
- XMES_WO_Trn_VW

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
- Color varchar(50)
