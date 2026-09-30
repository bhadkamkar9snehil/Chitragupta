---
type: view
title: "XBatch_CAPA_Delay_Report_Vw"
built: "2026-09-24T11:36:36"
---

# XBatch_CAPA_Delay_Report_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- CAPA_CorrectiveAction
- CAPA_PreventiveAction
- CAPA_ProblemSolvingTeam
- DelayAgency_Master
- Equipment
- RMShiftDelayEntry_CAPA
- SubEquipment

## Columns

- CAPANO varchar(100)
- Area varchar(100)
- Equipment varchar(100)
- SubEquipment varchar(100)
- OpenDate datetime
- Status varchar(50)
- Component varchar(100)
- FunctionalLocation varchar(100)
- Close varchar(100)
- CAPACloseDate date
- DateofBD date
- NotificationNumber int
- Name varchar(36)
- Dept varchar(100)
- Telephone int
- FromTime datetime
- ToTime datetime
- TotalTime decimal
- AgencyBeforeCAPA varchar(100)
- AgencyAfterCAPA varchar(100)
- TypeofBD varchar(36)
- SequenceofBD varchar(-1)
- ContainmentAction varchar(-1)
- ImplementDate datetime
- Cause varchar(-1)
- Reason1 varchar(-1)
- Reason2 varchar(-1)
- Reason3 varchar(-1)
- Reason4 varchar(-1)
- Reason5 varchar(-1)
- Photos varchar(8000)
- FilePath varchar(-1)
- CorrectiveAction varchar(-1)
- CorrectiveResponsibility varchar(36)
- CorrectiveTargetDate datetime
- CorrectiveStatus varchar(36)
- CorrectiveRemakrs varchar(100)
- PreventiveAction varchar(-1)
- PreventiveResponsibility varchar(36)
- PreventiveTargetDate datetime
- PreventiveStatus varchar(36)
- PreventiveRemarks varchar(100)
- ListofDocument varchar(8000)
- Review varchar(-1)
- ReviewResponsibility varchar(36)
- ReviewDepartment varchar(100)
- ReviewClosedBy varchar(36)
- VerifiedBy varchar(36)
- CloseDate datetime
- ReviewTelephone int
