---
type: procedure
title: "ShiftDelayEntry_Update_usp"
built: "2026-09-24T11:36:36"
---

# ShiftDelayEntry_Update_usp

Parameters: @StartTime datetime, @EndTime datetime, @Status varchar, @HeatNo int.

## Writes

- Agency_Wise_Delay: Agency, ParentID
- ShiftDelayEntry: AreaName, DelayAgency, DelayEndTime, DelayReason, DelayStartTime, DelaySubtypeid, DelayType, HeatNo, ID, Source
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- DelayAgency_Master: AreaName, ID, IsDeleted
- ShiftDelayEntry: IsDeleted

## What its own log shows

15,704 log rows, 2026-05-25 10:35 to 2026-08-10 09:48.

Steps:
- 1 Entered
- 2 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Bucket Charging Start
- 2 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Power OFF Delay Start
- 2 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Power ON Delay Start
- 2 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Tapping Delay Start
- 3 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Bucket Charging End
- 3 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Power OFF Delay End
- 3 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Power ON Delay End
- 3 Set Delay Subtype ID, Delay Type ID, Reason and Agency When Status is Tapping Delay End
- 4 Insert Shift Delay Entry table Start
- 5 Insert Shift Delay Entry table End
- 6 Insert Agency wsie delay table From Delay Agency master for SMS area Start
- 7 Insert Agency wsie delay table From Delay Agency master for SMS area End
- 8 Completed

Example call: `EXEC XStudio_Xbatch.dbo.ShiftDelayEntry_Update_usp @StartTime='31-May-2026 23:23:23.790', @EndTime='01-Jun-2026 01:16:51.697', @Status='Tapping Delay', @HeatNo='1603293'`
