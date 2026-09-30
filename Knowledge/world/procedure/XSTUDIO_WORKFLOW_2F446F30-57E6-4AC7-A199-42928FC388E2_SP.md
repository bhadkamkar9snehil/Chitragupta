---
type: procedure
title: "XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_ActiveLife_Element_Mst_Tbl: LastUsedBatch, ModifiedBy, ModifiedOn
- XMES_Life_Tracker_Register_Mst_Tbl: ModifiedBy, ModifiedOn, Source, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- EAF_PER_HEAT: AutoLadleAdditionDolo, AutoLadleAdditionFesi, AutoLadleAdditionLime, AutoLadleAdditionSiMn, Avg_LiquidMetalWeight, Avg_PowerMW, Avg_PoweroffTIme, Avg_PoweronTIme, Avg_TTT, BIN1LimeConsumption, BIN2DoloConsumption, BIN3Consumption, BIN3Name, BIN4Consumption, BIN4Name, Briquette, BriquetteAuto, BriquetteCH1, BriquetteCH2, BriquetteCH3, BriquetteCH4, BriquetteManual, BundleLMS, BundleLMSAuto, BundleLMSCH1, BundleLMSCH2, BundleLMSCH3, BundleLMSCH4, BundleLMSManual, CalcLiquidMetalWeight, CarbonConsumption, CdriConsumption, ChargeWeight, CokeInjection, CopexScrap, CopexScrapAuto, CopexScrapCH1, CopexScrapCH2, CopexScrapCH3, CopexScrapCH4, CopexScrapManual, Dololimepertonofsteel, E1SprayCollingFlowDurationSec, E1SprayCoolingFlowAvg, E2SprayCollingFlowDurationSec, E2SprayCoolingFlowAvg, E3SprayCollingFlowDurationSec, E3SprayCoolingFlowAvg, EAFTemperature, EBTFilter, ElectrodeConsumption1Kg, ElectrodeConsumption2Kg, ElectrodeConsumption3Kg, EndCuts, EndCutsAuto, EndCutsCH1, EndCutsCH2, EndCutsCH3, EndCutsCH4, EndCutsManual, EndTime, FettlingMass, GunningMass, HBIConsumption, HBIDRI, HBIDRIAuto, HBIDRICH1, HBIDRICH2, HBIDRICH3, HBIDRICH4, HBIDRIManual, HMS1, HMS12, HMS12Auto, HMS12CH1, HMS12CH2, HMS12CH3, HMS12CH4, HMS12Manual, HMS1Auto, HMS1CH1, HMS1CH2, HMS1CH3, HMS1CH4, HMS1Manual, HeatID, HeatReportDate, HeatStart, HeatTimeMinute, HeatTimeSecond, HerausManualPPM, HerausTemp, ID, LadleAdditionDolo, LadleAdditionFeSi, LadleAdditionLime, LadleAdditionSiMn, LadleAdditionSiMnn, Limepertonofsteel, LiquidMetalWeight, ManualLadleAdditionDolo, ManualLadleAdditionFesi, ManualLadleAdditionLime, ManualLadleAdditionSimn, NGConsumption, NGconsumptionpertonofsteel, NutCokeKgPerTon, OxygenConsumption, PowerMWH, PowerOFFTimeMinute, PowerOFFTimeSecond, PowerOnCharge, PowerOnTimeMinute, PowerOnTimeSecond, PowerPerTonofSteel, RamMass, RejectedBilletWeightTon, Scull, ScullCH1, ScullCH2, ScullCH3, ScullCH4, ShreddedAuto, ShreddedManual, Shreedded, ShreeddedCH1, ShreeddedCH2, ShreeddedCH3, ShreeddedCH4, SkullAuto, SkullManual, StartTime, Status, SteelGrade, TapTemp, Tapping1, Tapping2, TempTips, TotalChargeWeightMT, TotalElectrodeConsumption, WorkOrder
- EAF_ProcessTime: HeatID, IsDeleted, StartTime, Status
- EAF_SMS_Tag_Mapping_Tbl: Attribute, IsDeleted, TagName
- XBatch_Work_Order_Mst_Tbl: Equipment, ID, IsDeleted, Status
- XMES_ActiveLife_Element_Mst_Tbl: ElementNameID, IsDeleted
- XMES_Element_Life_Type_Mapping_Mst_Tbl: DataCaptureType, ElementType, IsDeleted, ParentID
- XMES_Life_Element_Mst_Tbl: ID, IsDeleted, ParentID
- XMES_Life_Tracker_Register_Mst_Tbl: ID

## Writes (named in its SQL text)

- EAF_PER_HEAT

## Calls

- SMS_Data_list_View

## What its own log shows

19,532 log rows, 2026-05-20 09:45 to 2026-07-17 17:18.

Steps:
- 1 Entered
- 2 Get heat latest starttime from EAF Processtime Start
- 3 Get heat latest 01-Jul-2026 04:03:33.787 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 05:00:54.793 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 05:59:14.737 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 06:59:10.747 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 07:53:53.147 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 08:51:44.837 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 09:51:05.863 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 10:46:29.037 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 11:41:45.153 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 12:36:26.860 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 13:31:57.750 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 14:27:26.957 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 15:23:16.740 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 16:19:35.687 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 17:17:41.843 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 18:13:51.717 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 19:05:44.807 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 19:57:46.810 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 20:48:47.087 starttime from EAF Processtime End
- 3 Get heat latest 01-Jul-2026 21:46:12.160 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 04:02:40.873 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 05:11:46.800 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 06:07:27.687 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 07:03:21.897 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 07:57:44.033 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 08:51:54.160 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 09:47:42.880 starttime from EAF Processtime End
- 3 Get heat latest 02-Jul-2026 10:43:10.127 starttime from EAF Processtime End

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFD08E96-6960-46D7-956E-D0D4D41F3321', @p_Status='Statusworkflow'`
