---
type: table
title: "Storage_Location_MST"
built: "2026-09-24T11:36:36"
---

# Storage_Location_MST

Table in XStudio_Xbatch. Rows: 605.

## Read by

- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_SAP_I_EndProduct_Production_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP

## Columns

- ID varchar(36)
- Plant varchar(36)
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
- StorageLocation varchar(100)
- Description varchar(100)
