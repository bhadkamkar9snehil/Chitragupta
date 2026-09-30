---
type: table
title: "Power_Consumption_LogSheet"
built: "2026-09-24T11:36:36"
---

# Power_Consumption_LogSheet

Table in XStudio_Xbatch. Rows: 245.

## Written by

- XBatch_Electricity_Meter_Consumption_Usp
- Xstudio_Power_Consumption_LogSheet_USP

## Read by

- XMES_Power_Consumption_report_Usp
- XMES_U_Power_consumption_Report_Usp
- Xstudio_Day_Consumptions_Usp
- Xstudio_Power_Consumption_LogSheet_USP

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Transformer132kv1 decimal
- Transformer132kv2 decimal
- Transformer33kv1 decimal
- Transformer33kv2 decimal
- EAF decimal
- LRF decimal
- Transformer24MVA decimal
- Transformer15MVA decimal
- RollingMill decimal
- WRM decimal
- OxygenPlant4A decimal
- NGConsumptionSm3 decimal
- Transformer63MVALosseskWH decimal
- Transformer125MVALosseskWH decimal
- NGActualReading decimal
- Shift varchar(100)
- RMNGConsumption decimal
