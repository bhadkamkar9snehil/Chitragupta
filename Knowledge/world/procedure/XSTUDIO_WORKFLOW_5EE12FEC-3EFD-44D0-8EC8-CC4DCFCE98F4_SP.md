---
type: procedure
title: "XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- ShiftDelayEntry: AreaName, DelayEndTime, DelayReason, DelayStartTime, DelayType, OperatorName, RMProduct, RMSection, ShiftManager
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- RM_Delays: EndTime, ID, StartTime, Status
- ShiftDelayEntry_Transaction_Operator: IsDeleted, ModifiedOn, Operator, Product, ReportDate, Section, Shift, ShiftManager

## Writes (named in its SQL text)

- RM_Delays

## What its own log shows

8,795 log rows, 2026-05-25 12:59 to 2026-08-29 10:26.

Steps:
- 1 Entered
- 2 Get Product, Section, Operator and Shift Manager from Shift Delay Entry Trasaction Operator Start
- 3 Get Product, Section, Operator and Shift Manager from Shift Delay Entry Trasaction Operator End
- 4Insert Shift Delay Entry for RM delay Start
- 5Insert Shift Delay Entry for RM delay End

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Completed', @p_StatusAttributeName='FF97D8A7-25D3-4C63-801A-153D70B03377', @p_Status='WorkFlowStatus'`
