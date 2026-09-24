---
type: procedure
title: "XBatch_Get_Entry_for_ShiftDelay_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Entry_for_ShiftDelay_Usp

Parameters: @heatNo int.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- SMS_Plant_Process_EventTime: CreatedOn, DurationinSeconds, EndTime, HeatID, IsDeleted, StartTime, Status
- XMES_SMS_Event_Process_Tracker_Mst: DurationInSeconds, IsDeleted, Name, Type

## What its own log shows

5,060 log rows, 2026-05-25 10:35 to 2026-07-08 18:04.

Steps:
- 1 Entered
- 2 Set query for power off delay to Execute Procedure Shift Delay Entry Update Start
- 2 Set query for power on delay to Execute Procedure Shift Delay Entry Update Start
- 3 Set query for power off delay to Execute Procedure Shift Delay Entry Update End
- 3 Set query for power on delay to Execute Procedure Shift Delay Entry Update End
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603165.0000,@StartTime = '25-May-2026 10:31:03.467',@Endtime = '25-May-2026 10:33:34.467' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603166.0000,@StartTime = '25-May-2026 11:27:25.707',@Endtime = '25-May-2026 11:29:57.707' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603167.0000,@StartTime = '25-May-2026 12:22:38.360',@Endtime = '25-May-2026 12:25:42.360' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603168.0000,@StartTime = '25-May-2026 13:18:05.870',@Endtime = '25-May-2026 13:20:46.870' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603169.0000,@StartTime = '25-May-2026 14:13:24.353',@Endtime = '25-May-2026 14:14:58.353' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603170.0000,@StartTime = '25-May-2026 14:37:23.620',@Endtime = '25-May-2026 14:51:04.090' , @status = 'Power OFF Delay' ;
EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603170.0000,@StartTime = '25-May-2026 15:05:29.540',@Endtime = '25-May-2026 15:09:09.250' , @status = 'Power OFF Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603171.0000,@StartTime = '25-May-2026 16:49:37.537',@Endtime = '25-May-2026 16:53:42.537' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603172.0000,@StartTime = '25-May-2026 17:46:00.197',@Endtime = '25-May-2026 17:48:53.197' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603173.0000,@StartTime = '25-May-2026 18:41:12.427',@Endtime = '25-May-2026 18:41:36.427' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603174.0000,@StartTime = '25-May-2026 19:34:58.550',@Endtime = '25-May-2026 19:35:19.550' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603175.0000,@StartTime = '25-May-2026 20:29:51.340',@Endtime = '25-May-2026 20:30:35.340' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603176.0000,@StartTime = '25-May-2026 21:24:03.303',@Endtime = '25-May-2026 21:24:24.303' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603178.0000,@StartTime = '26-May-2026 03:49:26.447',@Endtime = '26-May-2026 04:02:21.447' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603179.0000,@StartTime = '26-May-2026 04:55:12.593',@Endtime = '26-May-2026 04:59:35.593' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603180.0000,@StartTime = '26-May-2026 05:52:40.537',@Endtime = '26-May-2026 05:54:38.537' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603181.0000,@StartTime = '26-May-2026 06:47:26.140',@Endtime = '26-May-2026 06:47:37.140' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603182.0000,@StartTime = '26-May-2026 07:42:03.517',@Endtime = '26-May-2026 07:44:46.517' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603184.0000,@StartTime = '26-May-2026 09:29:43.477',@Endtime = '26-May-2026 09:30:18.477' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603185.0000,@StartTime = '26-May-2026 10:24:49.557',@Endtime = '26-May-2026 10:25:02.557' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603186.0000,@StartTime = '26-May-2026 11:17:19.467',@Endtime = '26-May-2026 11:20:08.467' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603187.0000,@StartTime = '26-May-2026 12:12:40.570',@Endtime = '26-May-2026 12:14:42.570' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603191.0000,@StartTime = '26-May-2026 16:53:16.160',@Endtime = '26-May-2026 16:57:13.160' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603192.0000,@StartTime = '26-May-2026 17:49:16.397',@Endtime = '26-May-2026 17:50:56.397' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603193.0000,@StartTime = '26-May-2026 18:43:23.487',@Endtime = '26-May-2026 18:44:48.487' , @status = 'Power ON Delay' ) Start
- 4 Execute query : (EXEC [XStudio_Xbatch].[dbo].[ShiftDelayEntry_Update_usp] @HeatNo = 1603194.0000,@StartTime = '26-May-2026 19:26:24.210',@Endtime = '26-May-2026 19:26:41.530' , @status = 'Power OFF Delay' ) Start

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_Get_Entry_for_ShiftDelay_Usp @heatNo='1604015'`
