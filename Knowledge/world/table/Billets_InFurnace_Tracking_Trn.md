---
type: table
title: "Billets_InFurnace_Tracking_Trn"
built: "2026-09-24T11:36:36"
---

# Billets_InFurnace_Tracking_Trn

Table in XStudio_Xbatch. Rows: 1,141,648.

## Written by

- Billet_Furnace_Movement
- BilletsPosition_InFurnace_Usp
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- Xstudio_Billets_InFurnace_Tracking_Trn_USP

## Read by

- XBatch_AllFurnacePosition_Billet_Deatils
- XBatch_RM_BilletWiseNGConsumption
- XMES_RemaingBillets_In_Inventory_Usp
- Xstudio_Billets_InFurnace_Tracking_Trn_USP

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
- EntryDateTime datetime
- ReportDate varchar(100)
- IsProcessed bit
- BilletPosition varchar(100)
- BilletNo varchar(100)
- HeatNo int
- Grade varchar(100)
