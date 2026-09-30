---
type: table
title: "XMES_State_Position_State_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_State_Position_State_Mst_Tbl

Table in XStudio_Xbatch. Rows: 92.

## Read by

- Billet_Furnace_Movement
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand
- MES_M_Strand_TMT
- MES_M_Strand_WRM
- XBatch_GetRemaningHeat_Usp
- XMES_Get_Billet_Count_USP
- XMES_I_Billet_ChargingBed_Usp
- XMES_I_Billets_Tracking_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_RemaingBillets_In_Inventory_Usp
- XMES_SAP_I_Inventory_Stock_Data_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18

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
- PositionName varchar(100)
- PositionType varchar(100)
- ParentArea varchar(100)
- SequenceNumber int
- IsActive bit
- Description varchar(-1)
