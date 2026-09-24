---
type: table
title: "XMES_Live_Charging_SECT2"
built: "2026-09-24T11:36:36"
---

# XMES_Live_Charging_SECT2

Table in XStudio_Xbatch. Rows: 1,599.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`

## Written by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect1_to_Sect2
- MES_M_Sect1_to_Sect2_Billet_Tracking
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP
- Xstudio_XMES_Live_Charging_SECT2_USP

## Read by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect1_to_Sect2
- MES_M_Sect1_to_Sect2_Billet_Tracking
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand_TMT
- MES_M_Strand_WRM
- XBatch_GetRemaningHeat_Usp
- XMES_Get_Billet_Count_USP
- XMES_I_Billet_ChargingBed_Usp
- XMES_RemaingBillets_In_Inventory_Usp
- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP
- Xstudio_Day_Ngconsumption_Usp
- Xstudio_RM_NGConsumption_USP
- Xstudio_XMES_Live_Charging_SECT2_USP

## Columns

- ID varchar(36)
- BilletNo varchar(100)
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
- IsProcessed bit
- InTIme datetime
- OutTime datetime
- Status varchar(100)
- Weighment decimal
- FurnaceOutTime datetime
- TotalResidenceTime int
