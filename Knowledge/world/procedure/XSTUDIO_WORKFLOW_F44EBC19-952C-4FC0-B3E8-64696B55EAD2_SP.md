---
type: procedure
title: "XSTUDIO_WORKFLOW_F44EBC19-952C-4FC0-B3E8-64696B55EAD2_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_F44EBC19-952C-4FC0-B3E8-64696B55EAD2_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Electricity_Meter_Reading_Upload: AllFIleUpload, FIleUpload132KVIC1, FIleUpload132KVIC2, FIleUpload15MVA, FIleUpload24MVA, FIleUpload33KVIC1, FIleUpload33KVIC2, FIleUploadEAF, FIleUploadLRF, FIleUploadROLLINGMILL, ID, Reportdate

## Writes (named in its SQL text)

- Electricity_Meter_Reading_Upload

## Calls

- XStudio_Schedule_TSQL_Task_Usp

## What its own log shows

496 log rows, 2026-05-28 02:20 to 2026-09-02 07:10.

Steps:
- 1 Entered
- 2 Procedure of Schedule TSQL Task for Electricity Meter Reading Upload Python script Start
- 3 Procedure of Schedule TSQL Task for Electricity Meter Reading Upload Python script End
- 4 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_F44EBC19-952C-4FC0-B3E8-64696B55EAD2_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='F3334E28-CABA-4154-903B-3B1355F07CF8', @p_RecordId='Entered', @p_StatusAttributeName='B6BD5843-0051-4406-B2C6-EBCADD54C04A', @p_Status='Status'`
