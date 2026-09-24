---
type: table
title: "XMES_Recalculate_Data"
built: "2026-09-24T11:36:36"
---

# XMES_Recalculate_Data

Table in XStudio_Xbatch. Rows: 12.

## Read by

- XMES_Schedule_SP_to_Refresh_Data_Usp

## Columns

- ID varchar(36)
- CategoryName varchar(100)
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
- ReportDate date
- StoreProcedure varchar(100)
- Description varchar(-1)
