---
type: table
title: "XBatch_Measurement_Unit_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Measurement_Unit_Mst_Tbl

Table in XStudio_Xbatch. Rows: 13.

## Written by

- XBatch_I_Measurement_Unit
- XBatch_I_Measurement_Unit_USP
- XBatch_Remove_Unused_Records_Usp

## Read by

- HeatChargeMixConsumption
- SAP_Posting_Data_ByHeat_Usp
- SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
- XBatch_I_Formula_Details_USP
- XBatch_I_Formula_USP
- XBatch_I_Material_Consume_NoBOM_USP
- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Inventory_USP
- XBatch_I_Material_Produce_NoBOM_USP
- XBatch_I_Material_Produce_USP
- XBatch_I_Material_USP
- XBatch_I_Storage_Area_USP
- XBatch_I_Store_USP
- XBatch_I_WO_USP
- XBatch_MR_Get_Batch_Detail_Usp
- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XBatch_RM_SAP_Inventory_Billet_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Formula_Details_USP
- XBatch_U_Formula_USP
- XBatch_U_Material_USP
- XBatch_U_Storage_Area_USP
- XBatch_U_Store_USP
- XBatch_U_WO_USP
- XBatch_WO_Get_Process_Cell_Usp
- XMES_I_Billets_Tracking_Usp
- XMES_I_ByProduct_Trn_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_RM_Raw_Material_Entry_Usp
- XMES_RemaingBillets_In_Inventory_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_U_SAP_Billet_Production_Trn_Usp
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP

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
- ColourCode varchar(50)
