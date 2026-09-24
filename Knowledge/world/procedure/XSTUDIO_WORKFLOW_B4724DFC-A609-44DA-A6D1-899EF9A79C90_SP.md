---
type: procedure
title: "XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- CCM_Per_Heat: HeatReportDate, ModifiedOn, ReportDate, Source
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- BilletsCastCount: ActualBilletsCountbyOperator, EndTime, HeatID, ID, StartTime, Status
- CCM_Per_Heat: CreatedOn, CrossSection, Grade, HeatID, StartTime, TotalBilletsCount
- EAF_PER_HEAT: HeatID, HeatReportDate, IsDeleted, ReportDate

## Writes (named in its SQL text)

- BilletsCastCount

## Calls

- Quality_Spectro_IsLatestSample_Update_Usp

## What its own log shows

9,249 log rows, 2026-05-22 15:05 to 2026-07-08 19:15.

Steps:
- 1 Entered
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 00:00:16.567 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 05:27:30.547 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 06:31:56.580 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 07:39:04.593 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 08:37:07.620 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 09:24:33.453 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 10:19:24.313 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 11:12:25.420 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 12:02:12.467 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 12:55:10.317 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 13:49:18.467 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 14:43:17.347 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 15:40:32.313 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 16:33:01.367 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 17:34:00.493 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 18:32:04.283 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 19:24:48.500 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 20:17:29.423 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 21:13:26.270 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 22:06:20.300 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jul-2026 22:57:20.307 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 05:35:17.320 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 06:44:08.023 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 07:36:58.517 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 08:29:58.470 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 09:30:11.260 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 10:21:21.487 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 11:20:11.430 Start
- 2 Get Latest heat id from CCM PER HEAT for starttime 01-Jun-2026 12:15:57.053 Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_B4724DFC-A609-44DA-A6D1-899EF9A79C90_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFEACBAF-7CA6-4CCD-9DED-2457EFB50767', @p_Status='WorkFlowStatus'`
