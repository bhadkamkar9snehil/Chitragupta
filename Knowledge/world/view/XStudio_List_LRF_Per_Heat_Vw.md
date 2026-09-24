---
type: view
title: "XStudio_List_LRF_Per_Heat_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_LRF_Per_Heat_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- HeatID: same values as key `HeatNo`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- Grade_Master
- LRF_Per_Heat
- LRF_SMS_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl

## Read by

- usp_SMS_EAF_LRF_CCM_KPI_PerDate

## Columns

- LiquidMetalWeightTon decimal
- NitrogenGasConsumptionNm3 decimal
- AutoAlloyAdditionLime decimal
- HeatNo int
- Edit varchar(236)
- TapTimeHHMM datetime
- ElectrodeConsumption1Kg decimal
- TreatmentStartTimeHHMM datetime
- SteelGrade varchar(100)
- CalcLiquidMetalWeightTon decimal
- ManualAlloyAdditionLime decimal
- TreatmentStopTimeHHMM datetime
- ElectrodeConsumption2Kg decimal
- LimeInKg decimal
- TotalLimeInKg decimal
- GLSDelta decimal
- LRFTemperature decimal
- ArcingTimeMinutes decimal
- EquipmentName varchar(100)
- ArgonConsumptionNm3 decimal
- WorkOrderNumber varchar(100)
- AutoAlloyAdditionDolo decimal
- ElectrodeConsumption3Kg decimal
- ManualAlloyAdditionDolo decimal
- TemperatureC decimal
- PowerMWh decimal
- PowerONTimeMinutes decimal
- LogbookManualAndAlloyAdditionEntry varchar(-1)
- TemperatureLiftinginC decimal
- TotalDoloInKg decimal
- LogbookManualEntry varchar(-1)
- HeatChemistrydata varchar(-1)
- PurgingFlowLPM decimal
- GradeChange varchar(-1)
- ID varchar(36)
- AutoAlloyAdditionFeSi decimal
- DoloInKg decimal
- ManualAlloyAdditionFeSi decimal
- TotalFeSiInKg decimal
- SAPPosting varchar(50)
- EquipmentID varchar(36)
- StartTime datetime
- AutoAlloyAdditionSiMn decimal
- FeSiInKg decimal
- ManualAlloyAdditionSiMn decimal
- Dateyyyymmdd varchar(100)
- HeatID int
- EndTime datetime
- TotalSiMninKg decimal
- SiMninKg decimal
- PowerOFFTimeMinutes decimal
- SiMnn decimal
- KWHPerTon decimal
- Status varchar(100)
- AutoAlloyAdditionCarbon decimal
- ManualAlloyAdditionCarbon decimal
- Delete varchar(100)
- TotalCarboninKg decimal
- Details varchar(-1)
- CarboninKg decimal
- AutoAlloyAdditionFlourSpar decimal
- ManualAlloyAdditionFlourSpar decimal
- TotalFlourSparinKg decimal
- Grade varchar(100)
- GradeColorCode varchar(50)
- FlourSparinKg decimal
- AutoAlloyAdditionAluminium decimal
- ManualAlloyAdditionAluminium decimal
- WorkOrder varchar(100)
- TotalAluminiuminKg decimal
- AluminiuminKg decimal
