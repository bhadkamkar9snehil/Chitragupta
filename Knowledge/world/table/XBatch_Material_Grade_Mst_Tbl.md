---
type: table
title: "XBatch_Material_Grade_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Grade_Mst_Tbl

Table in XStudio_Xbatch. Rows: 5.

## Written by

- XBatch_I_Material_Grade_USP

## Read by

- HeatChargeMixConsumption
- SP_XBatch_YMS_Display_HeatNo_Wise_Total_Billet
- SP_Xbatch_SplitsBillets_From_CCM_To_Inventory
- XBatch_I_Material_Consume_NoBOM_USP
- XBatch_I_Material_Consume_USP
- XBatch_I_Material_Inventory_USP
- XBatch_I_Material_Produce_NoBOM_USP
- XBatch_I_Material_Produce_USP
- XBatch_RM_BilletInventoryView_Location_U_Usp
- XBatch_RM_ItemsOfMaterial_In_Inventory_BOM_Usp
- XBatch_RM_SAP_Inventory_Billet_Usp
- XMES_I_Billets_Tracking_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_SAP_I_Inventory_Stock_Data_Usp
- XSTUDIO_WORKFLOW_24F2F246-218B-40A0-99DB-EC15F3350D4E_SP

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
- Description varchar(1000)
- Color varchar(50)
- IsActive bit
