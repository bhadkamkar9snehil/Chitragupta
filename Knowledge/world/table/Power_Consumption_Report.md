---
type: table
title: "Power_Consumption_Report"
built: "2026-09-24T11:36:36"
---

# Power_Consumption_Report

Table in XStudio_Xbatch. Rows: 245.

## Written by

- XMES_Power_Consumption_report_Usp
- XMES_U_Power_consumption_Report_Usp

## Read by

- SP_SMS_Producation_Summary
- XMES_Power_Consumption_Report_Per_Ton_Data_Usp
- XMES_U_Power_consumption_Report_Usp

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
- OxygenPlant4A decimal
- SMSTotal decimal
- Transformer132kv2 decimal
- Transformer132kv1 decimal
- Transformer63MVALosses decimal
- Transformer33kv1 decimal
- EntryDateTime datetime
- WRM decimal
- ReportDate date
- RollingMill decimal
- Transformer15MVA decimal
- SMSAuxWithO2 decimal
- ParentID varchar(36)
- Transformer33kv2 decimal
- TotalRollingMill decimal
- LRF decimal
- Transformer125MVALosses decimal
- PlantTotal decimal
- Name varchar(100)
- SMSAuxWithoutO2 decimal
- NGConsumption decimal
- IsProcessed bit
- EAF decimal
- Transformer24MVA decimal
- SMSConsumption decimal
- TotalProduction decimal
- RMNGConsumption decimal
