---
type: view
title: "XBatch_Delay_Analysis_Vw"
built: "2026-09-24T11:36:36"
---

# XBatch_Delay_Analysis_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- Agency_Wise_Delay
- DelayAgency_Master
- DelayTypeMST
- Equipment
- Equipment_Wise_Delay
- ShiftDelayEntry

## Columns

- HeatNo int
- DelayType varchar(100)
- AgencyName varchar(100)
- Equipment varchar(100)
- TotalDelayStartTime nvarchar(8000)
- TotalDelayEndTime nvarchar(8000)
- TotalDelayReason varchar(-1)
- TotalDelayInMinutes decimal
- AgencyDelayDuration decimal
- AgencyRemark varchar(-1)
- EquipmentDuration decimal
- EquipmentRemark varchar(-1)
