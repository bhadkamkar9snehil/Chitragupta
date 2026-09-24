---
type: table
title: "RM_Rolling_Plan"
built: "2026-09-24T11:36:36"
---

# RM_Rolling_Plan

Table in XStudio_Xbatch. Rows: 13.

## Written by

- XBatch_RM_Billet_Assign_Usp
- XBatch_RM_Rolling_Plan_Approval_Usp
- XBatch_RM_Rolling_Process_Usp

## Read by

- XBatch_RM_Billet_Assign_SPValidation_Usp
- XBatch_RM_Billet_Assign_Usp
- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XBatch_RM_Rolling_Plan_Approval_Usp
- XBatch_RM_Rolling_Process_SPvaildation_Usp
- XBatch_RM_Rolling_Process_Usp
- XBatch_Rolling_ID_Changer

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
- PONumber varchar(100)
- Customer varchar(36)
- Size varchar(100)
- ReleaseRollingQty int
- SequenceNo int
- RollingDate datetime
- Status varchar(100)
- RollingQty int
- RollingID varchar(100)
- AssignedQty decimal
- MaterialGrade varchar(36)
- MaterialID varchar(36)
