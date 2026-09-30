---
type: table
title: "XMES_Billet_Tracking_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_Billet_Tracking_Trn_Tbl

Table in XStudio_Xbatch. Rows: 180,813.

## Identifiers it holds

- Batch: same values as key `HeatNo`

## Written by

- Billet_Furnace_Movement
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand
- MES_M_Strand_TMT
- MES_M_Strand_WRM
- XMES_CREATE_BILLETNO_USP
- XMES_I_Billets_Tracking_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_SAP_I_Inventory_Stock_Data_Usp
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18

## Read by

- Billet_Furnace_Movement
- MES_I_Charging_Bed
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand
- XBatch_GetRemaningHeat_Usp
- XMES_Get_Billet_Count_USP
- XMES_I_Billet_ChargingBed_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_RemaingBillets_In_Inventory_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- Xmes_Billet_Tracking_Move_to_Stand_1

## Columns

- ID varchar(36)
- Name varchar(36)
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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- HeatNo varchar(100)
- Batch varchar(100)
- BilletNo varchar(100)
- Plant varchar(100)
- StorageLocation varchar(100)
- StatePosition varchar(100)
- ProcessStage varchar(100)
- Materialid varchar(36)
- Qualitygradeid varchar(36)
- BilletWeight decimal
- UOMID varchar(36)
- ManufacturingOrder varchar(100)
- BilletQuantity int
- PostingMaterialType varchar(100)
- CutLength decimal
