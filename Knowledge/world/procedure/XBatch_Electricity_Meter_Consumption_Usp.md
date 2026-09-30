---
type: procedure
title: "XBatch_Electricity_Meter_Consumption_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Electricity_Meter_Consumption_Usp


## Writes

- Electricity_Meter_Reading: Consumption, CreatedBy, FeederName, ModifiedBy, Source, Status
- Power_Consumption_LogSheet: EAF, EntryDateTime, LRF, ModifiedOn, NGConsumptionSm3, OxygenPlant4A, ReportDate, RollingMill, Source, Transformer132kv1, Transformer132kv2, Transformer15MVA, Transformer24MVA, Transformer33kv1, Transformer33kv2, WRM
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Electricity_Meter_Reading: EndDateTime, FeederName, ID, IsDeleted, Position, Value

## Calls

- XMES_Electricity_Bill_Calculator_USP
- XMES_Power_Consumption_report_Usp
- XMES_RM_Raw_Material_Entry_Usp

## What its own log shows

1,830 log rows, 2026-05-29 00:32 to 2026-09-02 07:10.

Steps:
- 1 Entered
- 2 Update Consumption and Calculated status and Feedername in Electricity Meter Reading For Entered Status Start
- 3 Update Consumption and Calculated status and Feedername in Electricity Meter Reading for Entered Status End
- 4 Set Latest Entrydate of Electricity meter Reading Start
- 5 Set Latest Entrydate of Electricity meter Reading End
- 6 Delete record when enddatetime more than 01-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 01-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 01-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 01-Sep-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 02-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 02-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 02-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 03-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 03-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 03-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 04-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 04-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 04-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 05-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 05-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 05-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 06-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 06-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 06-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 07-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 07-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 07-Jun-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 08-Aug-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 08-Jul-2026 00:00:00 Start
- 6 Delete record when enddatetime more than 08-Jun-2026 00:00:00 Start

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_Electricity_Meter_Consumption_Usp`
