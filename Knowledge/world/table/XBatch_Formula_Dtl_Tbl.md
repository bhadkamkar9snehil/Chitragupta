---
type: table
title: "XBatch_Formula_Dtl_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Formula_Dtl_Tbl

Table in XStudio_Xbatch. Rows: 6.

## Written by

- XBatch_I_Formula_Details_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Formula_Details_USP

## Read by

- XBatch_Generate_Recipe_Phase_Parameter_By_Equipment_Type_Usp
- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XBatch_RM_Rolling_Plan_Approval_Usp
- XBatch_Recipe_Operation_Quantity_Save_Usp
- XBatch_Recipe_Validate_BOM_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Formula_Details_USP
- XMES_BackCalculation_GLS_Usp
- XMES_BackCalculation_Validation_GLS_Usp

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
- MaterialID varchar(36)
- UnitID varchar(36)
- Quantity decimal
- QuantityType varchar(100)
- Description varchar(-1)
- IsEnabled bit
- MinQuantity decimal
- MaxQuantity decimal
