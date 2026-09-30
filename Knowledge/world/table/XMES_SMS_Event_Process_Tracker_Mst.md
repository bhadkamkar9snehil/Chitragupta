---
type: table
title: "XMES_SMS_Event_Process_Tracker_Mst"
built: "2026-09-24T11:36:36"
---

# XMES_SMS_Event_Process_Tracker_Mst

Table in XStudio_Xbatch. Rows: 19.

## Written by

- Xstudio_XMES_SMS_Event_Process_Tracker_Mst_USP

## Read by

- DelayEntry_EBTFilling_USP
- XBatch_Get_Entry_for_ShiftDelay_Usp
- Xstudio_XMES_SMS_Event_Process_Tracker_Mst_USP

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
- DurationInSeconds int
- DurationInMMSS varchar(100)
- DurationInMinutes decimal
- Remarks varchar(-1)
- Type varchar(100)
- Logic varchar(-1)
