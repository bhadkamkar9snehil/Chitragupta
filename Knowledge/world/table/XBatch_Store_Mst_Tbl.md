---
type: table
title: "XBatch_Store_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Store_Mst_Tbl

Table in XStudio_Xbatch. Rows: 6.

## Written by

- XBatch_I_Store_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Store_USP

## Read by

- SP_YMS_StoarageCapacityDetails_With_TotalHeatNo
- XBatch_I_Storage_Area_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Storage_Area_USP
- XBatch_U_Store_USP

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
- Capacity decimal
- CapacityUnitID varchar(36)
- Description varchar(-1)
- IsEnabled bit
- ColourCode varchar(50)
- SAPStorageLocation varchar(-1)
