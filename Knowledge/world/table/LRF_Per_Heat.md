---
type: table
title: "LRF_Per_Heat"
built: "2026-09-24T11:36:36"
---

# LRF_Per_Heat

Table in XStudio_Xbatch. Rows: 7,857.

## Identifiers it holds

- HeatID: same values as key `HeatNo`

## Written by

- XBatch_Add_Default_Heat_start_end_Usp
- XBatch_Add_Heat_start_end_Usp
- XMES_BackCalculation_GLS_Usp
- XMES_BackCalculation_Validation_GLS_Usp
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_I_SAP_GLS_Production_Trn
- XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP (text)
- XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP (text)
- XSTUDIO_WORKFLOW_8DA0CF0E-F9EA-4024-AB36-0C296DE94F61_SP (text)
- Xstudio_LRF_Per_Heat_USP

## Read by

- Per_Heat_LadleNo_Conformation_usp
- SMS_Data_list_View
- SP_GET_AREAWISE_TAG_TREND
- SP_ReCalculate_LRF_SMS_Block_USP
- XBatch_Add_Default_Heat_start_end_Usp
- XBatch_Add_Heat_start_end_Usp
- XBatch_Recalculate_Summary_LRF_Usp
- XMES_AUTO_WO_AND_SO_CALCULATION
- XMES_AUTO_WO_AND_SO_CALCULATION_old
- XMES_BackCalculation_GLS_Usp
- XMES_BackCalculation_Validation_GLS_Usp
- XMES_Dashboard_LRF_Live_USP
- XMES_I_SAP_Billet_Production_Trn
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_I_SAP_GLS_Production_Trn
- XMES_Missing_Heat_Entry_USP
- XMES_Recalculate_heat_Usp
- XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP
- XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP
- XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP
- XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP
- XSTUDIO_WORKFLOW_8DA0CF0E-F9EA-4024-AB36-0C296DE94F61_SP
- Xbatch_SMS_WorkOrder_Wise_Consumption_Usp
- Xstudio_Day_LRF_Usp
- Xstudio_LRF_Per_Heat_USP
- Xstudio_Shift_LRF_Usp

## Rows created by events

- LRF_SMS:LRF_Per_HeatData

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
- EquipmentID varchar(36)
- StartTime datetime
- EndTime datetime
- Status varchar(100)
- PowerONTime decimal
- PowerOFFTime decimal
- ArcingTime decimal
- ArgonConsumption decimal
- PowerMWH decimal
- HeatID int
- EntryDateTime datetime
- ReportDate varchar(100)
- IsProcessed bit
- TapStart datetime
- TreatmentStart datetime
- KWHPerTon decimal
- TreatmentStop datetime
- ProcessTime decimal
- CokeandNutcokepertonofsteel decimal
- Argonpertonofsteel decimal
- LiquidMetalWeight decimal
- WorkFlowStatus varchar(50)
- Lime decimal
- SiMnn decimal
- SiMn decimal
- FeSi decimal
- Dolo decimal
- Grade varchar(100)
- Avg_LiquidMetalWeight decimal
- PurgingFlowLPM decimal
- HeatReportDate date
- WorkOrder varchar(100)
- CalcLiquidMetalWeight decimal
- SAPWorkflowStatus varchar(50)
- GLSDelta decimal
- Avg_CalcLiquidMetalWeight decimal
- ManualAlloyAdditionLime decimal
- ManualAlloyAdditionDolo decimal
- ManualAlloyAdditionFeSi decimal
- ManualAlloyAdditionSiMn decimal
- AutoAlloyAdditionLime decimal
- AutoAlloyAdditionDolo decimal
- AutoAlloyAdditionFeSi decimal
- AutoAlloyAdditionSiMn decimal
- Carbon decimal
- ManualAlloyAdditionCarbon decimal
- AutoAlloyAdditionCarbon decimal
- FlourSpar decimal
- ManualAlloyAdditionFlourSpar decimal
- AutoAlloyAdditionFlourSpar decimal
- Aluminium decimal
- ManualAlloyAdditionAluminium decimal
- AutoAlloyAdditionAluminium decimal
- NitrogenGasConsumption decimal
- ElectrodeConsumption1Kg decimal
- ElectrodeConsumption2Kg decimal
- ElectrodeConsumption3Kg decimal
- Temperature decimal
- TemperatureLifting decimal
- TotalElectrodeConsumptionKg decimal
- LRFTemperature decimal
