---
type: procedure
title: "XMES_SMS_Temperature_Per_Heat_USP"
built: "2026-09-24T11:36:36"
---

# XMES_SMS_Temperature_Per_Heat_USP

Parameters: @HeatID varchar, @StartTime datetime, @EndTime datetime, @Area varchar.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Writes (named in its SQL text)

- EAF_PER_HEAT
- SMS_Temperature_Per_Heat

## What its own log shows

32,082 log rows, 2026-06-24 14:37 to 2026-07-08 18:50.
Error steps: 10 Raise Error When no record in Temp table #HistorianData; 11 Error; 9 Error

Steps:
- 1 Entered
- 2 Set Area Start
- 3 Set Area CCM Start
- 3 Set Area EAF Start
- 3 Set Area LRF Start
- 4 Set Tagname When Area is CCM Start
- 4 Set Tagname When Area is EAF Start
- 4 Set Tagname When Area is LRF Start
- 5 Set Tagname CCM_TUNDISH_TEMPERATURE_PRM When Area is CCM End
- 5 Set Tagname EAF_HERAUS_TEMPERATURE_PRM When Area is EAF End
- 5 Set Tagname LRF_TEMPERATURE_PRM When Area is LRF End
- 6 Create Temp Table #HistorianData Start
- 7 Create Temp Table #HistorianData End
- 8 insert into Temp Table #HistorianData by executing procedure XHS_Retrieve_tag_full_value_fast_NONUTC_usp Start
- 9 Error
- 9 insert into Temp Table #HistorianData by executing procedure XHS_Retrieve_tag_full_value_fast_NONUTC_usp End
- 10 Insert Temparature changes data in SMS Temparature per Heat from Temp table #HistorianData Start
- 10 Raise Error When no record in Temp table #HistorianData
- 10 Select Message When no record of value in range of 1000 to 2000 in Temp table #HistorianData Start
- 11 Error
- 11 Insert Temparature changes data in SMS Temparature per Heat from Temp table #HistorianData End
- 11 Select Message When no record of value in range of 1000 to 2000 in Temp table #HistorianData End
- 12 SELECT Success message Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603294) from Temp table #HistorianData Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603295) from Temp table #HistorianData Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603296) from Temp table #HistorianData Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603297) from Temp table #HistorianData Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603298) from Temp table #HistorianData Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603299) from Temp table #HistorianData Start
- 12 Update EAF Temparature in EAF Per Heat for Heatid (1603300) from Temp table #HistorianData Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SMS_Temperature_Per_Heat_USP @HeatID='1604015', @StartTime='08-Jul-2026 17:08:11.123', @EndTime='08-Jul-2026 18:04:22.053', @Area='EAF'`
