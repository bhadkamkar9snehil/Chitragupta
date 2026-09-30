---
type: procedure
title: "XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- LRF_SMS_Data: LRFGrade
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- EAF_PER_HEAT: CreatedOn, HeatID, HeatReportDate, IsDeleted, LiquidMetalWeight, SteelGrade
- LRF_Per_Heat: Aluminium, ArcingTime, ArgonConsumption, AutoAlloyAdditionAluminium, AutoAlloyAdditionCarbon, AutoAlloyAdditionDolo, AutoAlloyAdditionFeSi, AutoAlloyAdditionFlourSpar, AutoAlloyAdditionLime, AutoAlloyAdditionSiMn, Avg_CalcLiquidMetalWeight, Avg_LiquidMetalWeight, CalcLiquidMetalWeight, Carbon, Dolo, ElectrodeConsumption1Kg, ElectrodeConsumption2Kg, ElectrodeConsumption3Kg, EndTime, FeSi, FlourSpar, Grade, HeatID, HeatReportDate, ID, KWHPerTon, LRFTemperature, Lime, LiquidMetalWeight, ManualAlloyAdditionAluminium, ManualAlloyAdditionCarbon, ManualAlloyAdditionDolo, ManualAlloyAdditionFeSi, ManualAlloyAdditionFlourSpar, ManualAlloyAdditionLime, ManualAlloyAdditionSiMn, NitrogenGasConsumption, PowerMWH, PowerOFFTime, PowerONTime, PurgingFlowLPM, ReportDate, SiMn, SiMnn, StartTime, Status, TapStart, Temperature, TemperatureLifting, TotalElectrodeConsumptionKg, TreatmentStart, TreatmentStop, WorkOrder
- XBatch_Work_Order_Mst_Tbl: Equipment, ID, IsDeleted, Status

## Writes (named in its SQL text)

- LRF_Per_Heat

## Calls

- SMS_Data_list_View
- XBatch_I_Material_Consume_NoBOM_USP

## What its own log shows

19,190 log rows, 2026-05-21 11:32 to 2026-07-08 17:10.

Steps:
- 1 Entered
- 2 Get LRF Running Workorder id Start
- 3 Get LRF Running Workorder id 4ED9C313-2B33-4EE4-803C-E59E66C8F111 End
- 3 Get LRF Running Workorder id 8E47732C-5EA3-4773-BAE0-4F6BBB93BF82 End
- 3 Get LRF Running Workorder id D1C1E4CC-0618-46BC-AB29-1690A3352EE8 End
- 3 Get LRF Running Workorder id End
- 3 Get LRF Running Workorder id FF56F036-19A6-4808-8F29-E500C8D878AE End
- 4 Get get latest data of heat from EAF Start
- 5 Get get heatID 1603733, LiquidMetalWeight 76.1655, LotNo LS_1603733, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603734, LiquidMetalWeight 75.2702, LotNo LS_1603734, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603735, LiquidMetalWeight 75.3391, LotNo LS_1603735, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603736, LiquidMetalWeight 75.3391, LotNo LS_1603736, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603737, LiquidMetalWeight 75.3391, LotNo LS_1603737, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603738, LiquidMetalWeight 75.6146, LotNo LS_1603738, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603739, LiquidMetalWeight 76.5787, LotNo LS_1603739, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603740, LiquidMetalWeight 78.1626, LotNo LS_1603740, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603741, LiquidMetalWeight 75.2014, LotNo LS_1603741, Grade B500BLMNHC and Heatreportdate 2026-06-24 from EAF End
- 5 Get get heatID 1603742, LiquidMetalWeight 78.7135, LotNo LS_1603742, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603743, LiquidMetalWeight 75.4080, LotNo LS_1603743, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603744, LiquidMetalWeight 78.2315, LotNo LS_1603744, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603745, LiquidMetalWeight 76.9230, LotNo LS_1603745, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603746, LiquidMetalWeight 76.9919, LotNo LS_1603746, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603747, LiquidMetalWeight 77.6117, LotNo LS_1603747, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603748, LiquidMetalWeight 76.5787, LotNo LS_1603748, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603749, LiquidMetalWeight 76.7164, LotNo LS_1603749, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603750, LiquidMetalWeight 76.0966, LotNo LS_1603750, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603751, LiquidMetalWeight 77.6806, LotNo LS_1603751, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603752, LiquidMetalWeight 76.0278, LotNo LS_1603752, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603753, LiquidMetalWeight 76.0966, LotNo LS_1603753, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End
- 5 Get get heatID 1603754, LiquidMetalWeight 75.8900, LotNo LS_1603754, Grade B500BLMNHC and Heatreportdate 2026-06-25 from EAF End

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_69C53936-AFB3-44F8-874A-FE2336FB0279_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFE494A0-EB9F-4F9D-9FEC-645BC14DF3B8', @p_Status='WorkFlowStatus'`
