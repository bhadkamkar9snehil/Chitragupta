---
type: table
title: "XMES_SAP_API_ResultRecording_Error"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_API_ResultRecording_Error

Table in XStudio_Xbatch. Rows: 147.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`

## Written by

- XMES_SAP_ResultRecording_API_Error_Usp

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
- EntryDateTime datetime
- Body varchar(-1)
- RecordID varchar(100)
- Status varchar(50)
- IsProcessed bit
- HeatNo varchar(100)
- ParentID varchar(36)
- InspectionLot varchar(100)
- ReportDate date
- TransactionID varchar(100)
- ErrorMessage varchar(-1)
- SuccessMessage varchar(-1)
