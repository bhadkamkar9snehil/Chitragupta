---
type: table
title: "XMES_Live_Billet_Charging_Bed"
built: "2026-09-24T11:36:36"
---

# XMES_Live_Billet_Charging_Bed

Table in XStudio_Xbatch. Rows: 1,641.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`

## Written by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_I_Charging_Bed
- MES_I_Charging_Bed_From_STEC1
- MES_M_Billet_to_Sect1
- MES_M_Billet_to_Sect1_Billet_Tracking
- MES_M_Sect1_to_Charge
- MES_M_Sect1_to_Sect2
- MES_M_Sect1_to_Sect2_Billet_Tracking
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- XMES_I_Billet_ChargingBed_Usp
- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP
- XSTUDIO_WORKFLOW_2A11DAF4-C40A-4397-BA57-4247CA39CBC4_SP
- XSTUDIO_WORKFLOW_542D4605-78A7-4E93-A1D3-7A1CC45078AD_SP
- Xmes_Billet_Finished_Good_Production_usp
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18
- Xmes_Billet_Tracking_Sap_Posted_Usp
- Xstudio_XMES_Live_Billet_Charging_Bed_USP

## Read by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Billet_to_Sect1
- MES_M_Billet_to_Sect1_Billet_Tracking
- MES_M_Sect1_to_Charge
- MES_M_Sect1_to_Sect2
- MES_M_Sect1_to_Sect2_Billet_Tracking
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- XBatch_Campaign_Plan_Modified_Status_Usp
- XBatch_GetRemaningHeat_Usp
- XMES_Get_Billet_Count_USP
- XMES_I_Billet_ChargingBed_Usp
- XMES_RemaingBillets_In_Inventory_Usp
- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP
- XSTUDIO_WORKFLOW_2A11DAF4-C40A-4397-BA57-4247CA39CBC4_SP
- XSTUDIO_WORKFLOW_542D4605-78A7-4E93-A1D3-7A1CC45078AD_SP
- Xmes_Billet_Finished_Good_Production_usp
- Xmes_Billet_Tracking_Move_to_Stand_1
- Xmes_Billet_Tracking_Move_to_Stand_18
- Xmes_Billet_Tracking_Sap_Posted_Usp
- Xstudio_XMES_Live_Billet_Charging_Bed_USP

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
- InTIme datetime
- OutTime datetime
- IsProcessed bit
- BedNo varchar(100)
- Status varchar(100)
- BatchNo varchar(100)
- SequenceNo int
- BilletTrackingStatus varchar(50)
- BilletAreaWiseTracking varchar(100)
- BilletLength varchar(100)
- RolledBilletStage varchar(100)
