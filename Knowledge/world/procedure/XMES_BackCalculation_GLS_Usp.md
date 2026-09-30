---
type: procedure
title: "XMES_BackCalculation_GLS_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_BackCalculation_GLS_Usp

Parameters: @HeatNo int.

## Writes

- CCM_Per_Heat: ActualLiquidMetalWeight
- EAF_PER_HEAT: CalcLiquidMetalWeight, EndTime, EquipmentID, HeatID, LiquidMetalWeight, SAPWorkflowStatus, Source, StartTime, Status, Statusworkflow
- LRF_Per_Heat: CalcLiquidMetalWeight, EndTime, EquipmentID, Grade, HeatID, HeatReportDate, LiquidMetalWeight, ReportDate, SAPWorkflowStatus, Source, StartTime, Status, WorkFlowStatus, WorkOrder
- MES_SAP_Consumption_Trn_Tbl: QuantityInEntryUnit
- MES_SAP_Production_Trn_Tbl: QuantityInEntryUnit
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Per_Heat: ActualBilletWeightTon, CreatedOn, EndCutMeter, Grade, HeatID, IsDeleted, LaunderLossTon, OtherLossesTon, SetWeightTon, TotalProduction, TundishlossTon, WorkOrder
- EAF_PER_HEAT: HeatReportDate, IsDeleted, SteelGrade
- LRF_Per_Heat: IsDeleted
- MES_SAP_Consumption_Trn_Tbl: Batch, PostingMaterialType, SAPPostingStatus
- MES_SAP_Production_Trn_Tbl: Batch, PostingMaterialType, SAPPostingStatus
- SMS_Plant_Process_EventTime: ActualHeatID, EndTime, IsDeleted, StartTime, Status
- XBatch_Formula_Dtl_Tbl: IsDeleted, MaterialID, ParentID, Quantity
- XBatch_Formula_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: Equipment, ID, IsDeleted, ItemID, Status

## Calls

- XBatch_I_Material_Consume_NoBOM_USP

## What its own log shows

120,227 log rows, 2026-05-23 12:33 to 2026-07-19 18:16.
Error steps: 21 Error; 31 Error

Steps:
- 1 Entered
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507915 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507916 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507917 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507918 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507919 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507920 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507921 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507922 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507923 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507924 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507925 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507926 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507927 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507928 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507929 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507930 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1507931 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600018 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600019 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600020 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600021 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600022 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600023 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600024 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600025 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600026 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600027 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600028 Start
- 2 Get Work Order ID from CCM PER HEAT for heat no 1600029 Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_BackCalculation_GLS_Usp @HeatNo='1604014'`
