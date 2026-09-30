---
type: view
title: "XStudio_List_SMS_Plant_Process_EventTime_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_SMS_Plant_Process_EventTime_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- Status: same values as key `StateName-2`

## Reads

- SMS_Plant_Process_EventTime

## Read by

- XMES_SMS_Dashboard_Delay_USP

## Columns

- Edit varchar(241)
- Delete varchar(100)
- ID varchar(36)
- HeatNo int
- ReportDate date
- StartTime datetime
- EndTime datetime
- EquipmentID varchar(36)
- Status varchar(100)
- IsProcessed bit
- DurationMMSS varchar(100)
- DurationinMinutes decimal
- StateSequence int
- Details varchar(-1)
