---
type: procedure
title: "DelayEntry_EBTFilling_USP"
built: "2026-09-24T11:36:36"
---

# DelayEntry_EBTFilling_USP

Parameters: @HeatNo int.

## Writes

- ShiftDelayEntry: AreaName, DelayAgency, DelayEndTime, DelayStartTime, DelaySubtypeid, DelayType, HeatNo, ID, Source
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- EAF_PER_HEAT: HeatID, PowerOffTimeTotalSeconds
- SMS_Delay_Trn_Tbl: EndTime, HeatNo, StartTime, Status
- ShiftDelayEntry: DelayInMinutes, IsDeleted
- XMES_SMS_Event_Process_Tracker_Mst: DurationInMinutes, IsDeleted, Name, Type

## What its own log shows

15,110 log rows, 2026-05-25 11:32 to 2026-07-08 18:04.

Steps:
- 1 Entered
- 2 Get Duration in Minute from SMS Event Process Tracker of delay type for EBT Filling Start
- 3 Get Duration in Minute from SMS Event Process Tracker of delay type for EBT Filling End
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603166 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603167 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603168 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603169 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603170 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603171 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603172 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603173 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603174 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603175 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603176 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603177 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603178 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603179 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603180 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603181 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603182 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603183 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603184 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603185 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603186 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603187 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603188 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603189 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603190 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603191 Start
- 4 Get Delay in Minute from SMS Delay trn of Bucket Charging and Tapping Delay of heatno 1603192 Start

Example call: `EXEC XStudio_Xbatch.dbo.DelayEntry_EBTFilling_USP @HeatNo='1604015'`
