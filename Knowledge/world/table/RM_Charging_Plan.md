---
type: table
title: "RM_Charging_Plan"
built: "2026-09-24T11:36:36"
---

# RM_Charging_Plan

Table in XStudio_Xbatch. Rows: 16.

## Identifiers it holds

- BilletNo: same values as key `SublotNumber`

## Written by

- XBatch_RM_Billet_Assign_Usp

## Read by

- XBatch_RM_Billet_Assign_Usp

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- HeatNo varchar(100)
- BilletNo varchar(100)
- PO varchar(100)
- Size varchar(100)
- CurrentLocation varchar(100)
- SequenceNo int
- RollingID varchar(100)
- RollingDate date
- MaterialId varchar(100)
- RHFTime datetime
- MillTime datetime
- YardTime datetime
