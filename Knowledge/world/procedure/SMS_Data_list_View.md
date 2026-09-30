---
type: procedure
title: "SMS_Data_list_View"
built: "2026-09-24T11:36:36"
---

# SMS_Data_list_View


## Writes

- SMS_DATA_DASHBOARD: AverageChargeMixWeight, AveragePower, AverageTappingWeight, AverageTaptoTapTime, NoofHeatCast, NoofHeatTap, TodayProduction
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Per_Heat: HeatID, HeatReportDate, IsDeleted
- CCM_Summary_Day: CreatedOn, IsDeleted, ReportDate, TotalProduction
- EAF_PER_HEAT: HeatID, HeatReportDate, HeattimeTotalSeconds, IsDeleted, PowerMWH, TotalChargeWeightMT
- LRF_Per_Heat: HeatReportDate, IsDeleted, LiquidMetalWeight

## What its own log shows

11,292 log rows, 2026-05-21 08:45 to 2026-08-12 08:44.

Steps:
- 1 Entered
- 2 Update no of heat tap, no of heat cast, today prod, avgpow, avgtaptotaptime, avgchargemixwt, avgtappingwt in SMS Data Dashboard start
- 2 Update no of heat tap, no of heat cast, today prod, avgpow, avgtaptotaptime, avgchargemixwt, avgtappingwt start
- 3 Update no of heat tap, no of heat cast, today prod, avgpow, avgtaptotaptime, avgchargemixwt, avgtappingwt End
- 3 Update no of heat tap, no of heat cast, today prod, avgpow, avgtaptotaptime, avgchargemixwt, avgtappingwt in SMS Data Dashboard End
- 4 Completed
- Completed
- Entered
- Update no of heat tap, no of heat cast, today prod, avgpow, avgtaptotaptime, avgchargemixwt, avgtappingwt End
- Update no of heat tap, no of heat cast, today prod, avgpow, avgtaptotaptime, avgchargemixwt, avgtappingwt start

Example call: `EXEC XStudio_Xbatch.dbo.SMS_Data_list_View`
