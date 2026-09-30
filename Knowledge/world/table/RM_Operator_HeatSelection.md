---
type: table
title: "RM_Operator_HeatSelection"
built: "2026-09-24T11:36:36"
---

# RM_Operator_HeatSelection

Table in XStudio_Xbatch. Rows: 73.

## Identifiers it holds

- Batch: same values as key `HeatNo`
- Heatno: same values as key `HeatNo`

## Written by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_I_Charging_Bed_From_STEC1
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- XMES_I_Billet_ChargingBed_Usp
- Xstudio_RM_Operator_HeatSelection_USP

## Read by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- BilletsPosition_InFurnace_Usp
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- XBatch_Campaign_Plan_Modified_Status_Usp
- XBatch_GetRemaningHeat_Usp
- XMES_Get_Billet_Count_USP
- XMES_I_Billet_ChargingBed_Usp
- XMES_I_SAP_Batch_Consumption_Trn_Usp
- XMES_heat_selection_usp
- XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP
- Xmes_Billet_Finished_Good_Production_usp
- Xstudio_RM_Operator_HeatSelection_USP

## Columns

- ID varchar(36)
- Heatno varchar(36)
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
- BilletQty int
- Grade varchar(100)
- BilletLength varchar(100)
- Remainingbilletincharging int
- Srno int
- CampaignId varchar(36)
- workorder varchar(36)
- length decimal
- BedNo varchar(36)
- Status varchar(100)
- ReleaseDate datetime
- TotalBillet int
- BilletOnChargingBed int
- Released varchar(50)
- Batch varchar(100)
- BilletMaterialType varchar(100)
- BatchWeight decimal
- BilletsFuranaceStatus varchar(100)
- BilletoutofFurnace int
- BilletOnFurnace int
- IsExternalBillet bit
