---
type: table
title: "CCM_ProcessTime"
built: "2026-09-24T11:36:36"
---

# CCM_ProcessTime

Table in XStudio_Xbatch. Rows: 25,705.

## Identifiers it holds

- CCMHeatNo: same values as key `HeatNo`

## Written by

- XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP (text)

## Read by

- SMS_GET_CCM_HeatIDList
- XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP

## Rows created by events

- CCM:CCM_ProcessTime

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
- CCMHeatNo int
- WorkFlowStatus varchar(50)
