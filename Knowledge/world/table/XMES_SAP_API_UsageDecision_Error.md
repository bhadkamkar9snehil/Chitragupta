---
type: table
title: "XMES_SAP_API_UsageDecision_Error"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_API_UsageDecision_Error

Table in XStudio_Xbatch. Rows: 335.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`
- InspectionLot: same values as key `InspectionLot`

## Written by

- XMES_SAP_Usage_Decision_API_Error_Usp

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
- Status varchar(50)
- EntryDateTime datetime
- IsProcessed bit
- ReportDate date
- ParentID varchar(36)
- InspectionLot varchar(100)
- HeatNo varchar(100)
- Body varchar(-1)
- Name varchar(100)
- ErrorMessage varchar(-1)
- TransactionID varchar(100)
- SuccessMessage varchar(-1)
- RecordID varchar(100)
