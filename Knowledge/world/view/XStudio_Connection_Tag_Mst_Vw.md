---
type: view
title: "XStudio_Connection_Tag_Mst_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_Connection_Tag_Mst_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- XBatch_Connection_Capability_Mst_Tbl
- XBatch_Connection_Mst_Tbl
- XBatch_Connection_Parameter_Mst_Tbl

## Read by

- XBatch_Get_All_Tags_Usp

## Columns

- ConnectionID varchar(36)
- Connection varchar(100)
- Capability varchar(100)
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
- Type varchar(100)
- Mode varchar(100)
- Description varchar(-1)
- IsHistorize bit
- TagName varchar(100)
- DataSourceID varchar(36)
- FunctionType varchar(10)
