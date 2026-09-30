---
type: table
title: "Delay_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# Delay_Trn_Tbl

Table in XStudio_Xbatch. Rows: 1,931.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`

## Written by

- XSTUDIO_WORKFLOW_7A119B7F-E474-4946-85D9-4D58065DACBF_SP (text)

## Read by

- XSTUDIO_WORKFLOW_7A119B7F-E474-4946-85D9-4D58065DACBF_SP

## Rows created by events

- CCM_SMS:Delays

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
- HeatNo int
- WorkFlowStatus varchar(50)
