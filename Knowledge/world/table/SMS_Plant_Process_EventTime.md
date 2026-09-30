---
type: table
title: "SMS_Plant_Process_EventTime"
built: "2026-09-24T11:36:36"
---

# SMS_Plant_Process_EventTime

Table in XStudio_Xbatch. Rows: 107,569.

## Identifiers it holds

- ActualHeatID: same values as key `HeatNo`
- Status: same values as key `StateName-2`

## Written by

- XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP
- Xstudio_SMS_Plant_Process_EventTime_USP

## Read by

- XBatch_Get_Entry_for_ShiftDelay_Usp
- XMES_BackCalculation_GLS_Usp
- XMES_Missing_Heat_Entry_USP
- XMES_SMS_Dashboard_Delay_USP
- XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP
- XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP
- Xstudio_SMS_Plant_Process_EventTime_USP

## Rows created by events

- EAF_SMS:SMS_Plant_Process_Time

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- EquipmentID varchar(36)
- ReportDate date
- IsProcessed bit
- StartTime datetime
- EndTime datetime
- Status varchar(100)
- HeatID decimal
- ActualHeatID int
- Duration decimal
- WorkflowStatus varchar(50)
- StateSequence int
- DurationMMSS varchar(100)
- DurationinSeconds int
