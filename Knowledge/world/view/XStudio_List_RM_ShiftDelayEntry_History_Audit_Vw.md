---
type: view
title: "XStudio_List_RM_ShiftDelayEntry_History_Audit_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_RM_ShiftDelayEntry_History_Audit_Vw

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
- Shift varchar(100)
- Product varchar(100)
- AreaName varchar(-1)
- DateTime nvarchar(8000)
- Section varchar(100)
- ID varchar(36)
- DelayStartTime nvarchar(8000)
- DelayEndTime nvarchar(8000)
- DelayInMinutes decimal
- DelayInSecond int
- Cobble int
- Hotout int
- DelayType varchar(100)
- DelaySubtype varchar(100)
- DelayAgency varchar(100)
- Equipment varchar(100)
- SubEquipment varchar(100)
- Reason varchar(-1)
- Operator varchar(200)
- OtherAgencyName varchar(100)
- ShiftManager varchar(200)
- DelayTypeid varchar(36)
- DelaySubtypeid varchar(36)
- DelayAgencyid varchar(36)
- ShiftManagerid varchar(36)
- OperatorName varchar(36)
- SubEquipmentName varchar(36)
- EquipmentName varchar(-1)
- Details varchar(-1)
- ModifiedOn nvarchar(8000)
- ModifiedByid varchar(36)
- ModifiedBy varchar(200)
- HostAddress varchar(100)
