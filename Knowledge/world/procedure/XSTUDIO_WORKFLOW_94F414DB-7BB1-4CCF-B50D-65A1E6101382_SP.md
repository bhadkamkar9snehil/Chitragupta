---
type: procedure
title: "XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, CalcBilletsWeight1, HeatReportDate, ModifiedOn, Noof140mmbillets, NoofBillets1, RemainingPostedBilletCount, RemainingPostedBilletWeightTon, ReportDate, SAPWorkflowStatus, SetWeightTon, TotalBilletsCount, TotalProduction
- Heat_Chemistry_Quality_Data: Grade, ModifiedOn, Section
- Life_Tracking_Status: ConsumedLifePercentage, CurrentLife, HeatID, LastUpdatedTime, ModifiedOn
- Life_Tracking_Transaction_tbl: AlertPercentage, ConsumePercentage, CurrentLife, EntryDateTime, HeatID, Life, LifeType
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Billet_Cross_Section: CreatedOn, CrossSection1, IsDeleted, MaterialSpecificWeight
- BilletsCastCount: ActualBilletsCountbyOperator, EndTime, HeatID, ID, StartTime, Status
- CCM_Per_Heat: CrossSection, Grade, HeatID, IsDeleted, WorkOrder
- EAF_PER_HEAT: HeatID, HeatReportDate, IsDeleted, ReportDate
- Heat_Chemistry_Quality_Data: HeatNo, IsDeleted
- Life_Tracking: IsDeleted, MaximumLife, Name
- Life_Tracking_Status: AlertPercentage, IsDeleted, Life, LifeType

## Writes (named in its SQL text)

- BilletsCastCount

## Calls

- Quality_Spectro_IsLatestSample_Update_Usp
- XBatch_SMS_Heat_Tracking_Daily_Production_Data
- XMES_BackCalculation_GLS_Usp
- XMES_I_Billets_Tracking_Usp
- Xstudio_Historian_CCM_SMS_Block_usp

## What its own log shows

25,872 log rows, 2026-05-22 15:51 to 2026-07-08 19:30.

Steps:
- 1 Entered
- 2 Update Current Life, HeatID, ConsumedLifePercentage and LastUpdatedTime in Life Tracking Status Start
- 3 Update Current Life, HeatID, ConsumedLifePercentage and LastUpdatedTime in Life Tracking Status End
- 4 Insert Life tracking info for Mould Tube Life Strand Start
- 5 Insert Life tracking info for Mould Tube Life Strand End
- 6 Procedure Historian CCM SMS Block Start
- 7 Procedure Historian CCM SMS Block End
- 8 Procedure Quality Spectro Is Latest Sample Update Start
- 9 Procedure Quality Spectro Is Latest Sample Update End
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603107.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603108.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603109.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603110.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603111.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603112.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603113.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603114.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603115.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603116.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603117.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603118.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603119.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603120.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603121.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603122.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603123.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603124.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603125.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603126.0000 Start
- 10 Get Grade and Crosssection from CCM PER HEAT of HeatID 1603127.0000 Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Completed', @p_StatusAttributeName='FFEACBAF-7CA6-4CCD-9DED-2457EFB50767', @p_Status='WorkFlowStatus'`
