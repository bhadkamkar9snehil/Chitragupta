---
type: table
title: "Tag_Configuration"
built: "2026-09-24T11:36:36"
---

# Tag_Configuration

Table in XStudio_Xbatch. Rows: 9.

## Written by

- Tag_Trend

## Read by

- SP_GET_AREAWISE_TAG_TREND
- Tag_Trend

## Columns

- ID varchar(36)
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
- Name varchar(100)
- IsProcessed bit
- Area varchar(36)
- MappedTag varchar(-1)
- ParentID varchar(36)
- HeatID decimal
- Isenable bit
- Srno int
- ReportDate date
