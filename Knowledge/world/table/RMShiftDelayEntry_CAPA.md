---
type: table
title: "RMShiftDelayEntry_CAPA"
built: "2026-09-24T11:36:36"
---

# RMShiftDelayEntry_CAPA

Table in XStudio_Xbatch. Rows: 30.

## Written by

- sp_Generate_CAPA_No

## Read by

- SP_Get_CAPANO_SMS_RM
- sp_Generate_CAPA_No

## Columns

- ID varchar(36)
- Stepstorestartmill varchar(-1)
- DelayTransactionid varchar(36)
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
- Reason1 varchar(-1)
- Reason2 varchar(-1)
- Reason3 varchar(-1)
- Reason4 varchar(-1)
- Reason5 varchar(-1)
- CorrectiveAction varchar(-1)
- ProposedAction varchar(-1)
- Responsibility varchar(36)
- TargetDate date
- File varchar(8000)
- CAPANO varchar(100)
- Area varchar(100)
- AgencyTransactionid varchar(36)
- Agency varchar(36)
- OpenDate datetime
- DateofBD date
- Equipment varchar(36)
- SubEquipment varchar(36)
- Status varchar(50)
- Close varchar(100)
- CAPACloseDate date
- FromTime datetime
- ToTime datetime
- TotalTime decimal
- AgencyBeforeCAPA varchar(36)
- AgencyAfterCAPA varchar(36)
- TypeofBD varchar(36)
- SequenceofBD varchar(-1)
- ContainmentAction varchar(-1)
- ImplementDate datetime
- Photos varchar(8000)
- ListofDocument varchar(8000)
- Review varchar(-1)
- ReviewResponsibility varchar(36)
- ReviewClosedBy varchar(36)
- ReviewDepartment varchar(100)
- ReviewTelephone int
- VerifiedBy varchar(36)
- CloseDate datetime
- NotificationNumber int
- FunctionalLocation varchar(100)
- Component varchar(100)
- Cause varchar(-1)
- EntryDateTime datetime
- Remark varchar(100)
- DealyReason varchar(-1)
- ReportDate date
- IsProcessed bit
