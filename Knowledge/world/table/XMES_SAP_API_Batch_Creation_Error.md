---
type: table
title: "XMES_SAP_API_Batch_Creation_Error"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_API_Batch_Creation_Error

Table in XStudio_Xbatch. Rows: 249.

## Identifiers it holds

- BatchNo: same values as key `HeatNo`

## Written by

- XMES_SAP_Batch_Creation_API_Error_Usp

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
- ParentID varchar(36)
- Status varchar(50)
- RecordID varchar(100)
- Name varchar(100)
- TransactionID varchar(100)
- ReportDate date
- ErrorMessage varchar(-1)
- IsProcessed bit
- Body varchar(-1)
- EntryDateTime datetime
- BatchNo varchar(100)
- SuccessMessage varchar(-1)
