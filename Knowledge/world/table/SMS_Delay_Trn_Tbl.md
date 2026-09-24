---
type: table
title: "SMS_Delay_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# SMS_Delay_Trn_Tbl

Table in XStudio_Xbatch. Rows: 15,428.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP (text)

## Read by

- DelayEntry_EBTFilling_USP
- XSTUDIO_WORKFLOW_A8001D7B-0DFD-4034-B0DE-A73B7218AD49_SP

## Rows created by events

- EAF_SMS:SMS Delay Data

## Columns

- ID varchar(36)
- HeatNo int
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
- WorkflowStatus varchar(50)
