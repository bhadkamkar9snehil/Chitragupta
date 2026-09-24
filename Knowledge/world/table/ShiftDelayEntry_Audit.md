---
type: table
title: "ShiftDelayEntry_Audit"
built: "2026-09-24T11:36:36"
---

# ShiftDelayEntry_Audit

Table in XStudio_Xbatch. Rows: 0.

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
- DelayStartTime datetime
- DelayInMinutes decimal
- ParentID varchar(36)
- DelayEndTime datetime
- DelayReason varchar(-1)
- DelayType varchar(36)
- DelayAgency varchar(36)
- AgencyOther varchar(100)
- HeatNo int
- EquipmentName varchar(-1)
- SubEquipmentName varchar(36)
- ReportDate varchar(100)
- AreaName varchar(-1)
- ShiftManager varchar(36)
- OperatorName varchar(36)
- RMProduct varchar(100)
- DelaySubtypeid varchar(36)
- DelayInSecond int
- Grade varchar(100)
- RMSection varchar(100)
- Shift varchar(100)
- Cobble int
- Hotout int
- Refractory int
- Mechanical int
- Electrical int
- Operation int
- OtherDelay int
- RemainingDuration decimal
- DelayDuration varchar(100)
