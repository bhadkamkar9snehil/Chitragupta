---
type: procedure
title: "XMES_U_Power_consumption_Report_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_U_Power_consumption_Report_Usp

Parameters: @recordid varchar.

## Writes

- Power_Consumption_Report: EAF, LRF, NGConsumption, OxygenPlant4A, PlantTotal, RMNGConsumption, ReportDate, RollingMill, SMSAuxWithO2, SMSAuxWithoutO2, SMSConsumption, SMSTotal, TotalProduction, TotalRollingMill, Transformer125MVALosses, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, Transformer63MVALosses, WRM

## Reads

- CCM_Summary_Day: ActualBilletWeightTon, ReportDate, TotalProduction
- Power_Consumption_LogSheet: EAF, EntryDateTime, ID, IsDeleted, LRF, NGConsumptionSm3, OxygenPlant4A, ReportDate, RollingMill, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, WRM
- Power_Consumption_Report: EntryDateTime
- RM_Consumption_Summary_Day: IsDeleted, NGCons, ReportDate
