---
type: view
title: "XStudio_List_ShiftDelayEntry_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_ShiftDelayEntry_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- DelayAgency_Master
- DelaySubType_Master
- DelayTypeMST
- Equipment
- ShiftDelayEntry
- SubEquipment

## Read by

- XMES_SMS_Dashboard_Delay_USP

## Columns

- HeatNo int
- AddReason varchar(-1)
- Grade varchar(100)
- DateyyyyMMdd varchar(100)
- DateTime datetime
- DelayStartTime datetime
- ID varchar(36)
- Delete varchar(100)
- DelayEndTime datetime
- DelayDurationmmss varchar(100)
- DelayInSecond int
- SplitDelay varchar(-1)
- OtherAgencyName varchar(100)
- Merge varchar(50)
- DelayType varchar(100)
- DelaySubtype varchar(100)
- DelayInMinutes decimal
- DelayAgency varchar(100)
- Equipment varchar(100)
- SubEquipment varchar(100)
- Reason varchar(-1)
- ShortDescription varchar(100)
- CAPA varchar(-1)
- Operator varchar(200)
- Agency varchar(-1)
- AssignEquipment varchar(-1)
- ShiftManager varchar(200)
- AreaName varchar(-1)
- OperatorName varchar(36)
- ShiftManagerid varchar(36)
- Details varchar(-1)
- RemainingDuration decimal
- Heatid int
- DelayTypeid varchar(36)
- DelaySubtypeid varchar(36)
- DelayAgencyid varchar(36)
- Equipmentid varchar(-1)
- Issplit bit
- SubEquipmentid varchar(36)
- DelayType_DelayType varchar(100)
- DelayAgency_Name varchar(100)
- Status varchar(50)
