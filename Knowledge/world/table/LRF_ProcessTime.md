---
type: table
title: "LRF_ProcessTime"
built: "2026-09-24T11:36:36"
---

# LRF_ProcessTime

Table in XStudio_Xbatch. Rows: 40,881.

## Identifiers it holds

- LRFHeatID: same values as key `HeatNo`

## Written by

- Xstudio_LRF_ProcessTime_USP

## Read by

- SMS_GET_LRF_HeatIDList
- XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP
- XSTUDIO_WORKFLOW_DFEC0CB6-0A1F-4222-9A06-A25774049AC8_SP
- Xstudio_LRF_ProcessTime_USP

## Rows created by events

- LRF_SMS:LRF_ProcessTime

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
- LRFHeatID int
