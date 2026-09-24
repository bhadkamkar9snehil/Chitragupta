---
type: table
title: "XBatch_Material_Type_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Type_Mst_Tbl

Table in XStudio_Xbatch. Rows: 7.

## Read by

- XBatch_GetRemaningHeat_Usp
- XBatch_I_Material_USP
- XBatch_SAP_Material_Prod_Cons_Usp
- XBatch_U_Material_USP
- XMES_Get_Billet_Count_USP
- XMES_RemaingBillets_In_Inventory_Usp

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
- Description varchar(-1)
- Color varchar(10)
- Icon varchar(8000)
- CanProduced bit
- CanConsumed bit
- CanSold bit
- CanObsolete bit
