---
type: table
title: "Product_Master"
built: "2026-09-24T11:36:36"
---

# Product_Master

Table in XStudio_Xbatch. Rows: 4.

## Read by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- XMES_MaterialProcess_Cursor_usp
- XMES_Nested_heat_selection_usp
- XMES_RM_Production_Summary_Usp
- XMES_RM_Tag_Printing_I_TRN
- XMES_SAP_I_EndProduct_Production_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_heat_selection_usp
- Xmes_Billet_Finished_Good_Production_usp

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
- ShortName varchar(100)
