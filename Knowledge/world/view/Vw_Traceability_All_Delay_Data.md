---
type: view
title: "Vw_Traceability_All_Delay_Data"
built: "2026-09-24T11:36:36"
---

# Vw_Traceability_All_Delay_Data

View in XStudio_Xbatch. Rows: unknown.

## Reads

- XBatch_Tracability_AgencyDelay_Details_Vw
- XBatch_Tracability_EquipmentDelay_Details_Vw
- XBatch_Tracability_TotalDelay_Details_Vw

## Columns

- HeatNo int
- DelayType varchar(100)
- DelayStartTime nvarchar(8000)
- DelayEndTime nvarchar(8000)
- DelayMinutes int
- AgencyName varchar(100)
- Equipment varchar(100)
