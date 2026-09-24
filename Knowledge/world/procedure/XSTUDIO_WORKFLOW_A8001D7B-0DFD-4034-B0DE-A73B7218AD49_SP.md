---
type: procedure
title: "XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- SMS_Delay_Trn_Tbl: EndTime, EquipmentID, HeatNo, ID, IsProcessed, ReportDate, StartTime, Status

## Writes (named in its SQL text)

- SMS_Delay_Trn_Tbl

## Calls

- DelayEntry_EBTFilling_USP
- ShiftDelayEntry_Update_usp
- XBatch_Get_Entry_for_ShiftDelay_Usp

## What its own log shows

13,998 log rows, 2026-05-25 11:29 to 2026-08-10 09:48.

Steps:
- 1 Entered
- 2 Completed
- 2 Procedure Shift Delay Entry Update When Status is Tapping Delay Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 1044 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 1046282 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 10841 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 11487 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 11809 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 121 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 122 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 123 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 124 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 125 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 126 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 127 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 128 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 129 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 130 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 131 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 1312 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 132 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 133 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 1333 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 134 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 13465 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 135 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 136 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 138 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 139 Start
- 2 Set Delay Starttime When Status is Bucket Charging and Duration is 140 Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Completed', @p_StatusAttributeName='FFEE44E5-F6E9-40DC-AFD4-B8432308C92C', @p_Status='WorkflowStatus'`
