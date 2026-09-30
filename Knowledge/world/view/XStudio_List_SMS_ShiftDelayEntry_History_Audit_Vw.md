---
type: view
title: "XStudio_List_SMS_ShiftDelayEntry_History_Audit_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_SMS_ShiftDelayEntry_History_Audit_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- DelayAgency_Master
- DelaySubType_Master
- DelayTypeMST
- Equipment
- ShiftDelayEntry_Audit
- SubEquipment

## Columns

- AddReason varchar(-1)
- DateyyyyMMdd varchar(100)
- HeatNo int
- Grade varchar(100)
- DateTime nvarchar(8000)
- ID varchar(36)
- AreaName varchar(-1)
- DelayStartTime nvarchar(8000)
- DelayAgency varchar(100)
- Details varchar(-1)
- Equipment varchar(100)
- DelayEndTime nvarchar(8000)
- SubEquipment varchar(100)
- OtherAgencyName varchar(100)
- DelayAgencyid varchar(36)
- DelayDurationmmss varchar(100)
- DelaySubtype varchar(100)
- DelayInMinutes decimal
- DelayInSecond int
- DelaySubtypeid varchar(36)
- DelayType varchar(100)
- Reason varchar(-1)
- EquipmentName varchar(-1)
- Operator varchar(200)
- SubEquipmentName varchar(36)
- OperatorName varchar(36)
- ShiftManager varchar(200)
- ShiftManagerid varchar(36)
- RemainingDuration decimal
- ModifiedOn datetime
- ModifiedBy varchar(100)
- HostAddress varchar(100)
