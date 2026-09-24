---
type: procedure
title: "XMES_Power_Consumption_report_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Power_Consumption_report_Usp

Parameters: @EntryDate date.

## Writes

- Power_Consumption_Report: CreatedOn, EAF, EntryDateTime, LRF, ModifiedOn, NGConsumption, OxygenPlant4A, PlantTotal, RMNGConsumption, ReportDate, RollingMill, SMSAuxWithO2, SMSAuxWithoutO2, SMSConsumption, SMSTotal, Source, TotalProduction, TotalRollingMill, Transformer125MVALosses, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, Transformer63MVALosses, WRM
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Summary_Day: ActualBilletWeightTon, ReportDate, TotalProduction
- Power_Consumption_LogSheet: EAF, EntryDateTime, IsDeleted, LRF, NGConsumptionSm3, OxygenPlant4A, ReportDate, RollingMill, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, WRM
- RM_Consumption_Summary_Day: IsDeleted, NGCons, ReportDate

## What its own log shows

906 log rows, 2026-05-29 00:32 to 2026-09-02 07:10.

Steps:
- 1 Entered
- 2 Insert Calculated Consumption data into table variable Start
- 3 Insert Calculated Consumption data into table variable End
- 4 Update Calculated Consumption data from table variable in Power consumption Report Start
- 5 Update Calculated Consumption data from table variable in Power consumption Report End
- 6 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XMES_Power_Consumption_report_Usp @EntryDate='31-May-2026'`
