---
type: table
title: "XMES_SAP_API_WorkOrderCreation_Error"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_API_WorkOrderCreation_Error

Table in XStudio_Xbatch. Rows: 20.

## Written by

- XMES_SAP_WorkOrder_Creation_API_Error_Usp

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
- RecordID varchar(100)
- Body varchar(-1)
- ErrorMessage varchar(-1)
- Status varchar(50)
- WorkOrderType varchar(100)
- TotalQuantity decimal
- ItemName varchar(100)
- CustomerName varchar(100)
- SuccessMessage varchar(-1)
