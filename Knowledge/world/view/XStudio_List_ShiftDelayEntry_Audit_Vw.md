---
type: view
title: "XStudio_List_ShiftDelayEntry_Audit_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_ShiftDelayEntry_Audit_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- DelayAgency_Master
- DelaySubType_Master
- DelayTypeMST
- Equipment
- ShiftDelayEntry_Audit
- SubEquipment

## Columns

- DateyyyyMMdd varchar(100)
- AddReason varchar(-1)
- HeatNo int
- Grade varchar(100)
- DateTime nvarchar(8000)
- ID varchar(36)
- AreaName varchar(-1)
- DelayStartTime nvarchar(8000)
- DelayAgency varchar(100)
- Equipment varchar(100)
- SubEquipment varchar(100)
- DelayEndTime nvarchar(8000)
- OtherAgencyName varchar(100)
- DelayDurationmmss varchar(100)
- DelayAgencyid varchar(36)
- DelayInMinutes decimal
- DelaySubtype varchar(100)
- DelayInSecond int
- DelayType varchar(100)
- DelaySubtypeid varchar(36)
- Agency varchar(-1)
- AssignEquipment varchar(-1)
- EquipmentName varchar(-1)
- Reason varchar(-1)
- SubEquipmentName varchar(36)
- Operator varchar(200)
- OperatorName varchar(36)
- ShiftManager varchar(200)
- ShiftManagerid varchar(36)
- Details varchar(-1)
- RemainingDuration decimal
- ModifiedOn datetime
- ModifiedBy varchar(100)
- HostAddress varchar(100)
