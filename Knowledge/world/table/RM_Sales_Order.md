---
type: table
title: "RM_Sales_Order"
built: "2026-09-24T11:36:36"
---

# RM_Sales_Order

Table in XStudio_Xbatch. Rows: 8.

## Written by

- XBatch_RM_Rolling_Process_Usp

## Read by

- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XBatch_RM_Rolling_Process_SPvaildation_Usp
- XBatch_RM_Rolling_Process_Usp

## Columns

- ID varchar(36)
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
- PONumber varchar(100)
- Customer varchar(36)
- Size varchar(100)
- RollingQty int
- OpenQty int
- ReleaseQty int
- OrderDate date
- Status varchar(100)
- MaterialGrade varchar(36)
- MaterialID varchar(36)
- Name varchar(100)
