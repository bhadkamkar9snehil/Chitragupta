---
type: table
title: "XBatch_Connection_Capability_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Connection_Capability_Mst_Tbl

Table in XStudio_Xbatch. Rows: 0.

## Written by

- XBatch_Create_Connection_Default_Transfer_Capability
- XBatch_Remove_Unused_Records_Usp

## Read by

- XBatch_Create_Connection_Default_Transfer_Capability
- XBatch_Get_Tag_Mapping_Entries_By_Page_Type_Usp
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
- IsStart bit
- IsHold bit
- IsRestart bit
- IsAbort bit
- IsReset bit
- IsReady bit
- IsHeld bit
- IsRun bit
- IsDone bit
- IsInterlock bit
- IsAborted bit
- InterlockValueType varchar(100)
- ErrorCodeTag varchar(100)
- ErrorLookUpTable varchar(100)
- ErrorCodeField varchar(100)
- ErrorDescriptionField varchar(100)
