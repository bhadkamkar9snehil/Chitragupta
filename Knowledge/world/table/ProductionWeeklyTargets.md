---
type: table
title: "ProductionWeeklyTargets"
built: "2026-09-24T11:36:36"
---

# ProductionWeeklyTargets

Table in XStudio_Xbatch. Rows: 48.

## Read by

- XStudio_Historian_Day_SMS_Production_Usp
- Xstudio_Day_SMS_Target_Usp

## Columns

- ID varchar(36)
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
- WeekStartTime date
- Month varchar(36)
- Week varchar(36)
- WeekEndTime date
- TargetMT decimal
