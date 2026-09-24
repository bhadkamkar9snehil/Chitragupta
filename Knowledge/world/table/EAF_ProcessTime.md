---
type: table
title: "EAF_ProcessTime"
built: "2026-09-24T11:36:36"
---

# EAF_ProcessTime

Table in XStudio_Xbatch. Rows: 51,428.

## Written by

- Xstudio_EAF_ProcessTime_USP

## Read by

- SMS_GET_EAF_HeatIDList
- XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP
- Xstudio_EAF_ProcessTime_USP

## Rows created by events

- EAF_SMS:EAF_All_Process_Time

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
- StartTime datetime
- EndTime datetime
- Status varchar(100)
- HeatID decimal
- Duration int
- WorkflowStatus varchar(100)
