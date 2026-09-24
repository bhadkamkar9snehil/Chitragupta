---
type: table
title: "XMES_SAP_API_Batch_Characteristics_Error"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_API_Batch_Characteristics_Error

Table in XStudio_Xbatch. Rows: 596.

## Identifiers it holds

- BatchNo: same values as key `HeatNo`
- TransactionID: same values as key `TransactionID`

## Written by

- XMES_SAP_Batch_Characteristics_API_Error_Usp

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
- ReportDate date
- IsProcessed bit
- Name varchar(100)
- ParentID varchar(36)
- RecordID varchar(100)
- ErrorMessage varchar(-1)
- BatchNo varchar(100)
- TransactionID varchar(100)
- Body varchar(-1)
- EntryDateTime datetime
- Status varchar(50)
- SuccessMessage varchar(-1)
