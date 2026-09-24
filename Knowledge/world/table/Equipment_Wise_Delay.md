---
type: table
title: "Equipment_Wise_Delay"
built: "2026-09-24T11:36:36"
---

# Equipment_Wise_Delay

Table in XStudio_Xbatch. Rows: 9.

## Read by

- SMS_DelayRemainingDuration_U_Usp
- SMS_EquipmentWiseDelayDuration_Validation_Usp

## Columns

- ID varchar(36)
- EquipmentName varchar(-1)
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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- DelayAgency varchar(36)
- Duration decimal
- Remark varchar(-1)
- SubEquipmentName varchar(-1)
- Durationmmss varchar(100)
- DurationInSecond int
