---
type: table
title: "Life_Tracking"
built: "2026-09-24T11:36:36"
---

# Life_Tracking

Table in XStudio_Xbatch. Rows: 25.

## Written by

- Ladle_Life_Count_Each_Heat
- Xstudio_Life_Tracking_USP

## Read by

- Ladle_Life_Count_Each_Heat
- XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP
- Xstudio_Life_Tracking_USP

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
- AlertPercentage int
- Area varchar(36)
- CurrentLife int
- Description varchar(100)
- LifeName varchar(36)
- MaximumLife int
- ConsumeLife decimal
- EnableStatus bit
