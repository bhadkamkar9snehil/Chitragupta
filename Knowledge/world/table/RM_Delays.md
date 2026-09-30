---
type: table
title: "RM_Delays"
built: "2026-09-24T11:36:36"
---

# RM_Delays

Table in XStudio_Xbatch. Rows: 50,526.

## Written by

- XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP (text)

## Read by

- XMES_Cummulative_RMDelay_Entry_USP
- XSTUDIO_WORKFLOW_5EE12FEC-3EFD-44D0-8EC8-CC4DCFCE98F4_SP

## Rows created by events

- RM_Reheating_Furnace:RM Delay

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
- EquipmentID varchar(36)
- ReportDate date
- IsProcessed bit
- StartTime datetime
- EndTime datetime
- Status varchar(100)
- WorkFlowStatus varchar(50)
