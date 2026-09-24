---
type: table
title: "XStudio_Shift_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XStudio_Shift_Mst_Tbl

Table in XStudio_Xbatch. Rows: 1.

## Read by

- XStudio_Historian_Shift_SMS_Production_Usp
- Xstudio_Shift_CCM_Usp
- Xstudio_Shift_EAF_Usp
- Xstudio_Shift_LRF_Usp

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
- NoOfShift int
- SrNo int
