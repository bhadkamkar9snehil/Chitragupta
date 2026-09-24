---
type: table
title: "Agency_Wise_Delay"
built: "2026-09-24T11:36:36"
---

# Agency_Wise_Delay

Table in XStudio_Xbatch. Rows: 138,596.

## Written by

- SMS_DelayRemainingDuration_U_Usp
- ShiftDelayEntry_Update_usp
- Xstudio_Agency_Wise_Delay_USP

## Read by

- SMS_AgencyWiseDelayDuration_Validation_Usp
- SMS_DelayRemainingDuration_U_Usp
- SMS_EquipmentWiseDelayDuration_Validation_Usp
- SP_SMS_Producation_Summary
- Xstudio_Agency_Wise_Delay_USP

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Agency varchar(36)
- Duration decimal
- Remark varchar(-1)
- RemainingDuration decimal
- Durationmmss varchar(100)
- DurationInSecond int
