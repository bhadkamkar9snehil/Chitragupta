# XStudio_Xbatch.dbo.CCM_Per_Heat

**table_kind:** production_data

### What this table is for

- **Curated domain match (heat_execution):** Heat missing, wrong EAF/LRF/CCM state, per-heat value wrong, timing, alloy, power, yield, or attribution question.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** billet, billets, cast, ccm, confirmed, core, count, data, entities, event, flow, from, furnace, heat, insert, map, per, procedure, production, routing, same, sohar, stored, system, tracking, xbatch, xlsx, xstudio (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference std, flow, billet, min, pressure, strand, inlet, outlet, temp, weight, billets, noof.

**Primary Key:** ID  
**Row Count:** 6,862  
**Date Range (ModifiedOn):** 2025-08-21T21:44:03.7530000 to 2026-08-12T08:44:30.5170000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EquipmentID | varchar | YES | 36 | — |
| ReportDate | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| HeatID | int | YES | 10,0 | — |
| ArmNo | decimal | YES | 18,4 | — |
| ArmConsumption | decimal | YES | 18,4 | — |
| TotalBilletsCount | decimal | YES | 18,4 | — |
| Strand1CastingSpeed | decimal | YES | 18,4 | — |
| Strand2CastingSpeed | decimal | YES | 18,4 | — |
| Strand3CastingSpeed | decimal | YES | 18,4 | — |
| Strand5CastingSpeed | decimal | YES | 18,4 | — |
| Strand4CastingSpeed | decimal | YES | 18,4 | — |
| Strand6CastingSpeed | decimal | YES | 18,4 | — |
| Strand1BilletCounter | int | YES | 10,0 | — |
| Strand2BilletCounter | int | YES | 10,0 | — |
| Strand3BilletCounter | int | YES | 10,0 | — |
| Strand4BilletCounter | int | YES | 10,0 | — |
| Strand5BilletCounter | int | YES | 10,0 | — |
| Strand6BilletCounter | int | YES | 10,0 | — |
| STD1OSCSpeed | decimal | YES | 18,4 | — |
| STD2OSCSpeed | decimal | YES | 18,4 | — |
| STD3OSCSpeed | decimal | YES | 18,4 | — |
| STD4OSCSpeed | decimal | YES | 18,4 | — |
| STD5OSCSpeed | decimal | YES | 18,4 | — |
| STD6OSCSpeed | decimal | YES | 18,4 | — |
| TotalProduction | decimal | YES | 18,4 | — |
| MonthlyTarget | decimal | YES | 18,4 | — |
| MTDPlannedProduction | decimal | YES | 18,4 | — |
| TodayPlannedProduction | decimal | YES | 18,4 | — |
| WorkflowStatus | varchar | YES | 50 | — |
| DeltaTSTD1 | decimal | YES | 18,4 | — |
| DeltaTSTD2 | decimal | YES | 18,4 | — |
| DeltaTSTD3 | decimal | YES | 18,4 | — |
| DeltaTSTD4 | decimal | YES | 18,4 | — |
| DeltaTSTD5 | decimal | YES | 18,4 | — |
| DeltaTSTD6 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD1 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD2 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD3 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD4 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD5 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD6 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD1 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD2 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD3 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD4 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD5 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD6 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD1 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD2 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD3 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD4 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD5 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD6 | decimal | YES | 18,4 | — |
| InletPressureSTD1 | decimal | YES | 18,4 | — |
| InletPressureSTD2 | decimal | YES | 18,4 | — |
| InletPressureSTD3 | decimal | YES | 18,4 | — |
| InletPressureSTD6 | decimal | YES | 18,4 | — |
| InletPressureSTD4 | decimal | YES | 18,4 | — |
| InletPressureSTD5 | decimal | YES | 18,4 | — |
| InletTempT1STD1 | decimal | YES | 18,4 | — |
| InletTempT1STD2 | decimal | YES | 18,4 | — |
| InletTempT1STD3 | decimal | YES | 18,4 | — |
| InletTempT1STD4 | decimal | YES | 18,4 | — |
| InletTempT1STD5 | decimal | YES | 18,4 | — |
| InletTempT1STD6 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD1 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD2 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD3 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD4 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD5 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD6 | decimal | YES | 18,4 | — |
| OutletPressureSTD1 | decimal | YES | 18,4 | — |
| OutletPressureSTD2 | decimal | YES | 18,4 | — |
| OutletPressureSTD3 | decimal | YES | 18,4 | — |
| OutletPressureSTD4 | decimal | YES | 18,4 | — |
| OutletPressureSTD5 | decimal | YES | 18,4 | — |
| OutletPressureSTD6 | decimal | YES | 18,4 | — |
| OutletTempT2STD1 | decimal | YES | 18,4 | — |
| OutletTempT2STD2 | decimal | YES | 18,4 | — |
| OutletTempT2STD3 | decimal | YES | 18,4 | — |
| OutletTempT2STD4 | decimal | YES | 18,4 | — |
| OutletTempT2STD5 | decimal | YES | 18,4 | — |
| OutletTempT2STD6 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD1 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD2 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD3 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD4 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD5 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD6 | decimal | YES | 18,4 | — |
| CrossSection | int | YES | 10,0 | — |
| CastingStartTime | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| LadleSequence | int | YES | 10,0 | — |
| TPH | decimal | YES | 18,4 | — |
| Strand1WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand2WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand3WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand4WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand5WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand6WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand1StraightnerPressure | decimal | YES | 18,4 | — |
| Strand2StraightnerPressure | decimal | YES | 18,4 | — |
| Strand3StraightnerPressure | decimal | YES | 18,4 | — |
| Strand4StraightnerPressure | decimal | YES | 18,4 | — |
| Strand5StraightnerPressure | decimal | YES | 18,4 | — |
| Strand6StraightnerPressure | decimal | YES | 18,4 | — |
| HeatReportDate | date | YES | — | — |
| WorkOrder | varchar | YES | -1 | — |
| ShortBilletCount | int | YES | 10,0 | — |
| HotBilletCount | int | YES | 10,0 | — |
| ColdBilletCount | int | YES | 10,0 | — |
| ScaleLossTon | decimal | YES | 18,3 | — |
| EndCutMeter | decimal | YES | 18,3 | — |
| TundishlossTon | decimal | YES | 18,3 | — |
| LaunderLossTon | decimal | YES | 18,3 | — |
| OtherLossesTon | decimal | YES | 18,3 | — |
| ActualBilletWeightTon | decimal | YES | 18,3 | — |
| CutLength | int | YES | 10,0 | — |
| Noof6mbilletsmeter | int | YES | 10,0 | — |
| Noof130mmbillets | int | YES | 10,0 | — |
| Noof140mmbillets | int | YES | 10,0 | — |
| Noof103MtrBillets | int | YES | 10,0 | — |
| Noof117MtrBillet | int | YES | 10,0 | — |
| SetWeightTon | decimal | YES | 18,4 | — |
| SAPWorkflowStatus | varchar | YES | 50 | — |
| TotalPostedBilletCount | int | YES | 10,0 | — |
| TotalPostedBilletWeightTon | decimal | YES | 18,3 | — |
| RemainingPostedBilletWeightTon | decimal | YES | 18,3 | — |
| RemainingPostedBilletCount | int | YES | 10,0 | — |
| ActualBilletCount | int | YES | 10,0 | — |
| SalesOrder | varchar | YES | 36 | — |
| RemainingDeclaredBilletWeightTon | decimal | YES | 18,3 | — |
| RemainingDeclaredBilletCount | int | YES | 10,0 | — |
| Material | varchar | YES | 100 | — |
| BilletType1 | varchar | YES | 100 | — |
| BilletType2 | varchar | YES | 100 | — |
| BilletType3 | varchar | YES | 100 | — |
| BilletType4 | varchar | YES | 100 | — |
| NoofBillets1 | int | YES | 10,0 | — |
| NoofBillets2 | int | YES | 10,0 | — |
| NoofBillets3 | int | YES | 10,0 | — |
| NoofBillets4 | int | YES | 10,0 | — |
| CutLenght1 | decimal | YES | 18,4 | — |
| CutLenght2 | decimal | YES | 18,4 | — |
| CutLenght3 | decimal | YES | 18,4 | — |
| CutLenght4 | decimal | YES | 18,4 | — |
| CalcBilletsWeight1 | decimal | YES | 18,4 | ('0.00') |
| CalcBilletsWeight2 | decimal | YES | 18,4 | ('0.00') |
| CalcBilletsWeight3 | decimal | YES | 18,4 | ('0.00') |
| CalcBilletsWeight4 | decimal | YES | 18,4 | ('0.00') |
| PostToSAP1 | bit | YES | — | ('1') |
| PostToSAP2 | bit | YES | — | ('1') |
| PostToSAP3 | bit | YES | — | ('1') |
| PostToSAP4 | bit | YES | — | ('1') |
| Customer | varchar | YES | 100 | — |
| LadleSequenceText | varchar | YES | 100 | — |
| ProductionPlant | varchar | YES | 36 | — |
| SAPPostingDate | date | YES | — | — |
| CastingStartTimeHHmm | varchar | YES | 100 | — |
| ActualLiquidMetalWeight | decimal | YES | 18,2 | — |
| CasterYield | decimal | YES | 18,2 | — |
| CapturedTPH | decimal | YES | 18,2 | — |
| CastingDuration | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| SuperHeat | decimal | YES | 18,4 | — |
| NoofStrands | decimal | YES | 18,4 | — |
| OldCapturedBilletCount | int | YES | 10,0 | — |
| OldCapturedBilletWeightTon | decimal | YES | 18,4 | — |
| TundishTemperature | decimal | YES | 18,2 | — |
| YearlyTarget | decimal | YES | 18,0 | — |
| WeeklyTarget | decimal | YES | 18,2 | — |
| TodayAchievedpercentage | decimal | YES | 18,2 | — |
| YesterdayAchievedpercentage | decimal | YES | 18,2 | — |
| WeeklyAchievedpercentage | decimal | YES | 18,2 | — |
| MTDAchievedpercentage | decimal | YES | 18,2 | — |
| WeeklyAchievedProduction | decimal | YES | 18,2 | — |
| AskingRate | decimal | YES | 18,2 | — |
| RunningRate | decimal | YES | 18,2 | — |
| Month | varchar | YES | 100 | — |
| Year | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3318E504-8133-4C01-8FB1-1C1D08778346 | NULL | NULL | NULL | NULL | 2025-08-21T21:35:37.0800000 | 2025-08-21T21:44:03.7530000 | False | False | NULL |
| A1B605AF-9B9A-43D2-A5A2-1AD7DD4D7C87 | NULL | NULL | NULL | NULL | 2025-08-21T21:45:04.5270000 | 2025-08-21T22:44:19.5230000 | False | False | NULL |
| 9F17E168-27B5-4AF2-A20E-547D74CA4B84 | NULL | NULL | NULL | NULL | 2025-08-21T22:45:21.3770000 | 2025-08-21T23:42:05.6370000 | False | False | NULL |
| 5481E89B-26D9-4E92-8F8D-67608D96B60C | NULL | NULL | NULL | NULL | 2025-08-21T23:43:07.4930000 | 2025-08-22T00:44:29.5770000 | False | False | NULL |
| 4068D38B-9D1E-4C47-A4EC-2E2DF00F54C1 | NULL | NULL | NULL | NULL | 2025-08-22T00:45:31.3970000 | 2025-08-22T01:44:22.6500000 | False | False | NULL |
| 1D6C8CF9-54A8-40FE-9F42-F38C4D00A330 | NULL | NULL | NULL | NULL | 2025-08-22T01:45:23.5230000 | 2025-08-22T02:43:47.4900000 | False | False | NULL |
| F3D0E6EB-16B2-4B52-BE8A-F4539B4538F5 | NULL | NULL | NULL | NULL | 2025-08-22T02:44:49.3330000 | 2025-08-22T03:44:14.5970000 | False | False | NULL |
| 3DB8DC81-540D-4F06-9B1E-D6D47BF8B82A | NULL | NULL | NULL | NULL | 2025-08-22T03:45:16.4570000 | 2025-08-22T04:42:00.7200000 | False | False | NULL |
| 2B770074-7467-48DE-AAA7-78CBE02444B5 | NULL | NULL | NULL | NULL | 2025-08-22T04:43:03.6130000 | 2025-08-22T05:38:51.5170000 | False | False | NULL |
| 6E3F3DC6-90CD-463F-94CA-C13805882102 | NULL | NULL | NULL | NULL | 2025-08-22T05:39:53.3600000 | 2025-08-22T06:37:48.3600000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33F0CD83-BA60-4B6B-8A6E-4FF0C42BB1CB | NULL | NULL | NULL |  | 2026-08-12T08:44:29.6100000 | 2026-08-12T08:44:30.5170000 | False | False | NULL |
| 4BD90B03-C59A-4EB4-999A-90A3AC0BE6AB | NULL | NULL | NULL | 4BD90B03-C59A-4EB4-999A-90A3AC0BE6AB | 2026-07-08T17:57:22.9330000 | 2026-07-08T23:43:08.1900000 | False | False | NULL |
| 35C35E7B-AFD8-4E42-AA9A-BB2CDFEE482B | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T16:55:48.6470000 | 2026-07-08T23:41:50.1530000 | False | False | NULL |
| 49E98248-9471-43E4-BA0F-07B41D63A505 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:55:21.7370000 | 2026-07-08T18:00:22.4730000 | False | False | NULL |
| 4561D3C0-2334-47AF-8105-FA9F9F6B06A2 | NULL | NULL | NULL |  | 2026-07-08T14:47:13.7730000 | 2026-07-08T16:48:42.2200000 | False | False | NULL |
| B6739BB1-4095-4FC4-B3FF-AB258C46A3BF | NULL | NULL | NULL |  | 2026-07-08T13:46:44.8400000 | 2026-07-08T15:38:53.3600000 | False | False | NULL |
| ADABB939-4E1F-4427-B0B3-A13A74D7ED95 | NULL | NULL | NULL |  | 2026-07-08T12:46:38.6970000 | 2026-07-08T15:38:25.1530000 | False | False | NULL |
| 00ACFF55-52D2-4D80-A205-54928F57EFBB | NULL | NULL | NULL |  | 2026-07-08T11:43:46.9170000 | 2026-07-08T15:37:59.4600000 | False | False | NULL |
| 0F6DEBEA-A460-40B0-B388-1877BBD23F04 | NULL | NULL | NULL |  | 2026-07-08T10:43:47.8530000 | 2026-07-08T12:24:43.0400000 | False | False | NULL |
| 9F3E92F2-E622-4D77-908A-5A0AF7A9410C | NULL | NULL | NULL |  | 2026-07-08T09:42:11.7830000 | 2026-07-08T11:40:06.3200000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Data.CastingTimeHHMMSS` -> `XStudio_XBatch.CCM_Per_Heat.CastingStartTime` (Many to One)
- `XStudio_XBatch.CCM_Per_Heat.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.CCM_Per_Heat.SalesOrder` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Per_Heat.SuperHeat` -> `XStudio_XBatch.CCM_Section_Strands.SuperHeat` (Many to One)
- `XStudio_XBatch.CCM_Per_Heat.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_SAP_Production_Trn_Tbl.HeatNo` -> `XStudio_XBatch.CCM_Per_Heat.HeatID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.Sequence` -> `XStudio_XBatch.CCM_Per_Heat.LadleSequence` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.StartTime` -> `XStudio_XBatch.CCM_Per_Heat.StartTime` (Many to One)
