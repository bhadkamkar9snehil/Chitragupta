---
type: table
title: "ChargingBedToFurnance"
built: "2026-09-24T11:36:36"
---

# ChargingBedToFurnance

Table in XStudio_Xbatch. Rows: 66,871.

## Written by

- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP (text)
- XSTUDIO_WORKFLOW_41BFE3D8-412D-46A9-BA44-9F2C2E7779A2_SP (text)

## Read by

- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP
- XSTUDIO_WORKFLOW_41BFE3D8-412D-46A9-BA44-9F2C2E7779A2_SP
- Xstudio_Historian_RM_Billet_Weight_Block_usp

## Rows created by events

- RM_Reheating_Furnace:ChargingBedToFurnance

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
- WorkflowStatus varchar(50)
- BilletWeightTon decimal
