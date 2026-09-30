---
type: table
title: "XMES_Work_Order_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_Work_Order_Trn_Tbl

Table in XStudio_Xbatch. Rows: 20.

## Written by

- XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP

## Read by

- XMES_RM_Production_Summary_Usp
- XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP

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
- WorkOrder varchar(36)
- CampaignID varchar(36)
