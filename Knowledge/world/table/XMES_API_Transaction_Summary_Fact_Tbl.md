---
type: table
title: "XMES_API_Transaction_Summary_Fact_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_API_Transaction_Summary_Fact_Tbl

Table in XStudio_Xbatch. Rows: 44,107.

## Identifiers it holds

- RecordID: same values as key `RecordID`
- TransactionID: same values as key `SAPTransactionID`

## Written by

- XMES_I_API_Transaction_Summary (text)

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
- TransactionID varchar(100)
- APIName varchar(100)
- APIStatus varchar(50)
- APISource varchar(100)
- RequestedDatetime datetime
- ResponseDatetime datetime
- RequestURL varchar(100)
- RequestBody varchar(-1)
- ResponseData varchar(-1)
- ResponseDataInsertion varchar(-1)
- ResponseError varchar(-1)
- RecordID varchar(100)
- EntityID varchar(100)
- LVid varchar(100)
- LVName varchar(100)
- ActionUserName varchar(100)
- ResolvedEntityTable varchar(-1)
