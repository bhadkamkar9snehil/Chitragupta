---
type: table
title: "Life_Tracking_Transaction_tbl"
built: "2026-09-24T11:36:36"
---

# Life_Tracking_Transaction_tbl

Table in XStudio_Xbatch. Rows: 66,316.

## Identifiers it holds

- HeatID: same values as key `HeatNo`

## Written by

- SMS_Reset_Life_Tracking_Status
- XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP
- XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP

## Read by

- SMS_Ladle_Life_Tracking_Validation

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- HeatID varchar(100)
- Life varchar(100)
- LifeType varchar(100)
- CurrentLife int
- ConsumePercentage decimal
- AlertPercentage varchar(100)
- Remarks varchar(100)
