---
type: procedure
title: "XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_ActiveLife_Element_Mst_Tbl: LastUsedBatch, ModifiedOn
- XMES_Life_Tracker_Register_Mst_Tbl: ModifiedBy, ModifiedOn, Source, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- EAF_PER_HEAT: HeatID, HeatReportDate, IsDeleted, TapStart
- LRF_Per_Heat: Aluminium, ArcingTime, ArgonConsumption, AutoAlloyAdditionAluminium, AutoAlloyAdditionCarbon, AutoAlloyAdditionDolo, AutoAlloyAdditionFeSi, AutoAlloyAdditionFlourSpar, AutoAlloyAdditionLime, AutoAlloyAdditionSiMn, Avg_CalcLiquidMetalWeight, Avg_LiquidMetalWeight, CalcLiquidMetalWeight, Carbon, Dolo, ElectrodeConsumption1Kg, ElectrodeConsumption2Kg, ElectrodeConsumption3Kg, EndTime, FeSi, FlourSpar, Grade, HeatID, HeatReportDate, ID, IsDeleted, KWHPerTon, LRFTemperature, Lime, LiquidMetalWeight, ManualAlloyAdditionAluminium, ManualAlloyAdditionCarbon, ManualAlloyAdditionDolo, ManualAlloyAdditionFeSi, ManualAlloyAdditionFlourSpar, ManualAlloyAdditionLime, ManualAlloyAdditionSiMn, NitrogenGasConsumption, PowerMWH, PowerOFFTime, PowerONTime, PurgingFlowLPM, ReportDate, SiMn, SiMnn, StartTime, Status, TapStart, Temperature, TemperatureLifting, TotalElectrodeConsumptionKg, TreatmentStart, TreatmentStop, WorkOrder
- LRF_ProcessTime: EndTime, IsDeleted, LRFHeatID, StartTime, Status
- XBatch_Material_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: ID, ItemID
- XMES_ActiveLife_Element_Mst_Tbl: ElementNameID, IsDeleted
- XMES_Element_Life_Type_Mapping_Mst_Tbl: DataCaptureType, ElementType, IsDeleted, ParentID
- XMES_Life_Element_Mst_Tbl: ID, IsDeleted, ParentID
- XMES_Life_Tracker_Register_Mst_Tbl: ID

## Writes (named in its SQL text)

- LRF_Per_Heat

## Calls

- Quality_Spectro_IsLatestSample_Update_Usp
- XBatch_I_Material_Produce_NoBOM_USP
- XMES_AUTO_WO_AND_SO_CALCULATION
- XMES_LRF_I_Raw_Material_Cons_Usp
- XMES_SMS_Temperature_Per_Heat_USP
- Xstudio_Historian_LRF_SMS_Block_usp

## What its own log shows

25,090 log rows, 2026-05-21 14:59 to 2026-07-08 17:43.

Steps:
- 1 Entered
- 2 Get start and end time for treatment start from LRF Processtime Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603734 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603735 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603736 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603737 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603738 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603739 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603740 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603741 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603742 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603743 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603744 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603745 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603746 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603747 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603748 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603749 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603750 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603751 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603752 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603753 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603754 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603755 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603756 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603757 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603758 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603759 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603760 Start
- 2 Get start time and end time for treatment start status from LRF Processtime of heatid 1603761 Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='A6E924D5-B2F0-4A5F-9717-3A63F6190358', @p_RecordId='Completed', @p_StatusAttributeName='FFE494A0-EB9F-4F9D-9FEC-645BC14DF3B8', @p_Status='WorkFlowStatus'`
