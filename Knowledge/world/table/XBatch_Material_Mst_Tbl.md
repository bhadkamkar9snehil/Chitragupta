---
type: table
title: "XBatch_Material_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Mst_Tbl

Table in XStudio_Xbatch. Rows: 213.

## Identifiers it holds

- Grade: same values as key `Grade`
- Number: same values as key `Material`

## Written by

- XBatch_I_Material_USP
- XBatch_Remove_Unused_Records_Usp
- XBatch_U_Material_USP

## Read by

- Billet_Furnace_Movement
- BilletsPosition_InFurnace_Usp
- HeatChargeMixConsumption
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand
- SAP_Posting_Data_ByHeat_Usp
- SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
- XBatch_Create_Batch_Usp
- XBatch_GetRemaningHeat_Usp
- XBatch_I_Formula_Details_USP
- XBatch_I_Formula_USP
- XBatch_I_Material_Consume_NoBOM_USP
- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Inventory_Transfer_USP
- XBatch_I_Material_Inventory_USP
- XBatch_I_Material_Produce_NoBOM_USP
- XBatch_I_Material_Produce_USP
- XBatch_I_WO_USP
- XBatch_RM_Billet_Assign_Usp
- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XBatch_RM_Rolling_Plan_Approval_Usp
- XBatch_RM_SAP_Inventory_Billet_Usp
- XBatch_Remove_Unused_Records_Usp
- XBatch_SAP_Material_Prod_Cons_Usp
- XBatch_U_Formula_Details_USP
- XBatch_U_Formula_USP
- XBatch_U_Material_USP
- XBatch_U_WO_USP
- XBatch_WO_Create_Batch_AI_Usp
- XMES_BackCalculation_GLS_Usp
- XMES_BackCalculation_Validation_GLS_Usp
- XMES_CCM_BILLET_MASTER_CREATE_USP
- XMES_Get_Billet_Count_USP
- XMES_I_Billets_Tracking_Usp
- XMES_I_ByProduct_Trn_Usp
- XMES_I_PlantToPlantTransfer_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_I_SAP_GLS_Production_Trn
- XMES_I_SAP_LS_Production_Trn
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_Missing_Heat_Entry_USP
- XMES_Nested_heat_selection_usp
- XMES_RM_Campaign_Plan_WorkOrders_Creation
- XMES_RM_Production_Summary_Usp
- XMES_RM_Raw_Material_Entry_Usp
- XMES_RemaingBillets_In_Inventory_Usp
- XMES_SAP_Create_Process_Order_Usp
- XMES_SAP_I_EndProduct_Production_Usp
- XMES_SAP_I_Inventory_Stock_Data_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_SO_Trn_VW
- XMES_U_SAP_Billet_Production_Trn_Usp
- XMES_WO_Trn_VW
- XMES_WorkOrders_Creation
- XMES_heat_selection_usp
- XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP
- XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP
- XSTUDIO_WORKFLOW_98A73AE1-1D20-4959-B45E-121B93225279_SP
- XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP
- XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xstudio_XBatch_Work_Order_Mst_Tbl_USP
- campaignplan_released_workflow_usp

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
- TypeID varchar(36)
- UnitID varchar(36)
- Number varchar(100)
- StockType varchar(100)
- Quantity decimal
- Description varchar(-1)
- IsEnabled bit
- CanExpire bit
- ExpireDays int
- MinInventoryLevel decimal
- MaxOrderSize decimal
- LotNumberFormat varchar(100)
- SubLotNumberFormat varchar(100)
- ColourCode varchar(50)
- PageID varchar(-1)
- PlantID varchar(36)
- StoragelocationID varchar(36)
- Grade varchar(100)
- RawMaterialName varchar(-1)
- SAPColorCode varchar(100)
- InventorySpecialStockType varchar(100)
