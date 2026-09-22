# XStudio_Xbatch.dbo.XBatch_MES_Heat_Tracking

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ccmstrand, time, ton, avg, speed, billet, total, consumption, casting, count, cut, oscillation.

**Primary Key:** ID  
**Row Count:** 1,850  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| HeatNo | int | YES | 10,0 | — |
| SteelGrade | varchar | YES | 100 | — |
| EAFHeatStartDateTime | datetime | YES | — | — |
| EAFTapStartDateTime | datetime | YES | — | — |
| EAFTTTTimeMMSS | varchar | YES | 100 | — |
| EAFPowerOnTimeMMSS | varchar | YES | 100 | — |
| EAFPowerOffTimeMMSS | varchar | YES | 100 | — |
| EAFTapTimeMMSS | varchar | YES | 100 | — |
| EAFChargeWeightTon | decimal | YES | 18,4 | — |
| EAFTotalChargeWeightMT | decimal | YES | 18,4 | — |
| EAFLiquidMetalWeightTon | decimal | YES | 18,4 | — |
| EAFLiquidMetalYield | decimal | YES | 18,4 | — |
| EAFNGConsumptionSm3 | decimal | YES | 18,4 | — |
| EAFCarbonConsumptionKg | decimal | YES | 18,4 | — |
| EAFOxygenConsumptionNm3 | decimal | YES | 18,4 | — |
| EAFPowerMWH | decimal | YES | 18,4 | — |
| EAFBin1LimeConsumptionTon | decimal | YES | 18,4 | — |
| EAFBin2DoloConsumptionTon | decimal | YES | 18,4 | — |
| EAFBin3ConsumptionTon | decimal | YES | 18,4 | — |
| EAFBin4ConsumptionTon | decimal | YES | 18,4 | — |
| EAFCopexScrapTon | decimal | YES | 18,4 | — |
| EAFHMS12Ton | decimal | YES | 18,4 | — |
| EAFHMS1Ton | decimal | YES | 18,4 | — |
| EAFEndCutsTon | decimal | YES | 18,4 | — |
| EAFBriquetteTon | decimal | YES | 18,4 | — |
| EAFBundleLMSTon | decimal | YES | 18,4 | — |
| EAFHBIDRITon | decimal | YES | 18,4 | — |
| EAFShreddedTon | decimal | YES | 18,4 | — |
| EAFSkullTon | decimal | YES | 18,4 | — |
| EAFLadleAdditionLimeKg | decimal | YES | 18,4 | — |
| EAFLadleAdditionDoloKg | decimal | YES | 18,4 | — |
| EAFLadleAdditionSiMnnKg | decimal | YES | 18,4 | — |
| EAFLadleAdditionSiMnKg | decimal | YES | 18,4 | — |
| EAFLadleAdditionFeSiKg | decimal | YES | 18,4 | — |
| LRFTreatmentStartTimeHHMMSS | datetime | YES | — | — |
| LRFTreatmentStopTimeHHMMSS | datetime | YES | — | — |
| LRFTreatmentTimeMinutes | varchar | YES | 100 | — |
| LRFArcingTimeMinutes | varchar | YES | 100 | — |
| LRFLiquidMetalWeightTon | decimal | YES | 18,4 | — |
| LRFArgonConsumptionNm3 | decimal | YES | 18,4 | — |
| LRFPowerMWH | decimal | YES | 18,4 | — |
| LRFAdditionLimeKg | decimal | YES | 18,4 | — |
| LRFAdditionDoloKg | decimal | YES | 18,4 | — |
| LRFAdditionFeSiKg | decimal | YES | 18,4 | — |
| LRFAdditionSiMnKg | decimal | YES | 18,4 | — |
| LRFAdditionSiMnnKg | decimal | YES | 18,4 | — |
| CCMLadleBottomOpenTime | datetime | YES | — | — |
| CCMLadleBottomCloseTime | datetime | YES | — | — |
| CCMArmPosition | varchar | YES | 100 | — |
| CCMArmConsumptionTon | decimal | YES | 18,4 | — |
| CCMTotalBilletCount | int | YES | 10,0 | — |
| CCMCrossSectionmm | int | YES | 10,0 | — |
| CCMTotalProductionTon | decimal | YES | 18,4 | — |
| CCMStrand1BilletCount | int | YES | 10,0 | — |
| CCMStrand1CastingSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand1OscillationSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand2BilletCount | int | YES | 10,0 | — |
| CCMStrand3BilletCount | int | YES | 10,0 | — |
| CCMStrand4BilletCount | int | YES | 10,0 | — |
| CCMStrand5BilletCount | int | YES | 10,0 | — |
| CCMStrand6BilletCount | int | YES | 10,0 | — |
| CCMStrand2CastingSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand3CastingSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand4CastingSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand5CastingSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand6CastingSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand2OscillationSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand3OscillationSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand4OscillationSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand5OscillationSpeedAvg | decimal | YES | 18,4 | — |
| CCMStrand6OscillationSpeedAvg | decimal | YES | 18,4 | — |
| EAFWorkOrder | varchar | YES | 100 | — |
| LRFWorkOrder | varchar | YES | 100 | — |
| CCMWorkOrder | varchar | YES | 100 | — |
| Sequence | varchar | YES | 100 | — |
| ShiftManager | varchar | YES | 100 | — |
| Melter | varchar | YES | 100 | — |
| SetupTime | time | YES | — | — |
| TappingDuration | varchar | YES | 100 | — |
| ArcingOFFtime | varchar | YES | 100 | — |
| TPH | decimal | YES | 18,4 | — |
| TapEndTime | time | YES | — | — |
| PowerDrawnAvg | decimal | YES | 18,4 | — |
| Bundlewip | decimal | YES | 18,4 | — |
| BundleTotal | decimal | YES | 18,4 | — |
| RDcut | decimal | YES | 18,4 | — |
| RDcutWip | decimal | YES | 18,4 | — |
| RDcutTotal | decimal | YES | 18,4 | — |
| RMSEndCut | decimal | YES | 18,4 | — |
| RMSEndCutWIP | decimal | YES | 18,4 | — |
| RMSEndCutTotal | decimal | YES | 18,4 | — |
| CopexscrapWIP | decimal | YES | 18,4 | — |
| CopexscrapTotal | decimal | YES | 18,4 | — |
| SkullWIP | decimal | YES | 18,4 | — |
| SkullTotal | decimal | YES | 18,4 | — |
| PDOScrap | decimal | YES | 18,4 | — |
| BriquetteWIP | decimal | YES | 18,4 | — |
| BriquetteTotal | decimal | YES | 18,4 | — |
| PigIron | decimal | YES | 18,4 | — |
| PigIronWIP | decimal | YES | 18,4 | — |
| PigIronTotal | decimal | YES | 18,4 | — |
| DRI | decimal | YES | 18,4 | — |
| DRIWIP | decimal | YES | 18,4 | — |
| DRITotal | decimal | YES | 18,4 | — |
| HBI | decimal | YES | 18,4 | — |
| HBIWIP | decimal | YES | 18,4 | — |
| HBITotal | decimal | YES | 18,4 | — |
| LMProdnasperOprn | decimal | YES | 18,4 | — |
| EnergyKWH | decimal | YES | 18,4 | — |
| AvgPowerDrawn | decimal | YES | 18,4 | — |
| ScrapTotal | decimal | YES | 18,4 | — |
| Totalo2 | decimal | YES | 18,4 | — |
| NaturalGas | decimal | YES | 18,4 | — |
| InjectionCarbon | decimal | YES | 18,4 | — |
| TopCarbonkg | decimal | YES | 18,4 | — |
| Electrodekg | decimal | YES | 18,4 | — |
| Electrode1 | decimal | YES | 18,4 | — |
| Electrode2 | decimal | YES | 18,4 | — |
| Electrode3 | decimal | YES | 18,4 | — |
| FirstTemp | decimal | YES | 18,4 | — |
| Tappingtemp | decimal | YES | 18,4 | — |
| TappingCarbon | decimal | YES | 18,4 | — |
| N2ppm | decimal | YES | 18,4 | — |
| TappingAlingot | decimal | YES | 18,4 | — |
| TappingLime | decimal | YES | 18,4 | — |
| Flourspar | decimal | YES | 18,4 | — |
| TappingHCFeCr | decimal | YES | 18,4 | — |
| LcFeCr | decimal | YES | 18,4 | — |
| HcFeCr | decimal | YES | 18,4 | — |
| LcFeMn | decimal | YES | 18,4 | — |
| Nutcoke | decimal | YES | 18,4 | — |
| Tappingothercarbon | decimal | YES | 18,4 | — |
| Gunningkg | decimal | YES | 18,4 | — |
| LRFElectrodes | decimal | YES | 18,4 | — |
| LFEngineer | varchar | YES | 100 | — |
| LFHoldingTime | varchar | YES | 100 | — |
| MnRecovery | decimal | YES | 18,4 | — |
| SiRecovery | decimal | YES | 18,4 | — |
| CACkg | decimal | YES | 18,4 | — |
| Spar | decimal | YES | 18,4 | — |
| AlIngot | decimal | YES | 18,4 | — |
| LCC | decimal | YES | 18,4 | — |
| HCFeMn | decimal | YES | 18,4 | — |
| LFinTemp | decimal | YES | 18,4 | — |
| TundishT1 | decimal | YES | 18,4 | — |
| TundishT2 | decimal | YES | 18,4 | — |
| TundishT3 | decimal | YES | 18,4 | — |
| AvgTemp | decimal | YES | 18,4 | — |
| Superheat | decimal | YES | 18,4 | — |
| NoofStrands | decimal | YES | 18,4 | — |
| Noof140mmBillets | decimal | YES | 18,4 | — |
| HotChargeBillets | decimal | YES | 18,4 | — |
| Noof130mm12m875mbillets | decimal | YES | 18,4 | — |
| CutLength | decimal | YES | 18,4 | — |
| Billets103mtr | decimal | YES | 18,4 | — |
| Billet117mtr | decimal | YES | 18,4 | — |
| Tonnage12m875m | decimal | YES | 18,4 | — |
| Noof6mbillets | decimal | YES | 18,4 | — |
| Billet6mwt | decimal | YES | 18,4 | — |
| TotalBillet | decimal | YES | 18,4 | — |
| Noof87mbillets | decimal | YES | 18,4 | — |
| Billets87mweight | decimal | YES | 18,4 | — |
| LadleLoss | decimal | YES | 18,4 | — |
| SecWt | decimal | YES | 18,4 | — |
| EndCutShortLength | decimal | YES | 18,4 | — |
| Tundishloss | decimal | YES | 18,4 | — |
| LaunderLoss | decimal | YES | 18,4 | — |
| Scaleloss | decimal | YES | 18,4 | — |
| Others | decimal | YES | 18,4 | — |
| LiquidMetalCalc | decimal | YES | 18,4 | — |
| YieldChargetoBL | decimal | YES | 18,4 | — |
| YieldChargetoLM | decimal | YES | 18,4 | — |
| CasterYield | decimal | YES | 18,4 | — |
| TeemingStart | datetime | YES | — | — |
| TeemingEnd | datetime | YES | — | — |
| CastingTime | datetime | YES | — | — |
| PowerOFFtimechecker | varchar | YES | 100 | — |
| LiftTemp | decimal | YES | 18,4 | — |
| LRFLCFeMn | decimal | YES | 18,4 | — |
| Hour | time | YES | — | — |
| CCMTPH | decimal | YES | 18,4 | — |
| EndCut | decimal | YES | 18,4 | — |
| StartTime | datetime | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01F3E6DC-39EE-46FD-8785-54CAFB2F6346 | NULL | NULL | NULL | NULL | 2026-05-20T13:18:47.5000000 | NULL | False | False | NULL |
| 01C7509C-16FB-4B94-8590-D4EFD87EF7E7 | NULL | NULL | NULL | NULL | 2026-05-24T20:47:22.0230000 | NULL | False | False | NULL |
| 0132C52C-7242-40B2-AFC9-A3A30CA0A94A | NULL | NULL | NULL | NULL | 2026-05-15T05:53:45.3100000 | NULL | False | False | NULL |
| 00F7DC17-34A6-4A69-AE8B-62DB3DDA5561 | NULL | NULL | NULL | NULL | 2026-06-22T13:27:08.4770000 | NULL | False | False | NULL |
| 0090384A-0FDA-4B15-A522-6FCB28259B44 | NULL | NULL | NULL | NULL | 2026-05-12T06:25:44.8830000 | NULL | False | False | NULL |
| 008156F5-A0EF-4761-B64E-D36B3530837B | NULL | NULL | NULL | NULL | 2026-06-23T16:42:14.3030000 | NULL | False | False | NULL |
| 0080F70F-F30F-4903-BE78-D50A4C9456B7 | NULL | NULL | NULL | NULL | 2025-12-16T16:27:38.5370000 | NULL | False | False | NULL |
| 006232EF-176A-4AB8-B40D-B67230E42BB7 | NULL | NULL | NULL | NULL | 2025-12-16T16:27:38.5370000 | NULL | False | False | NULL |
| 0058427D-4026-48DC-8318-ABB3499D948D | NULL | NULL | NULL | NULL | 2026-05-26T15:46:32.6170000 | NULL | False | False | NULL |
| 005706A4-49AF-4749-AE45-870E0FA67B44 | NULL | NULL | NULL | NULL | 2026-06-10T18:01:22.4600000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01F3E6DC-39EE-46FD-8785-54CAFB2F6346 | NULL | NULL | NULL | NULL | 2026-05-20T13:18:47.5000000 | NULL | False | False | NULL |
| 01C7509C-16FB-4B94-8590-D4EFD87EF7E7 | NULL | NULL | NULL | NULL | 2026-05-24T20:47:22.0230000 | NULL | False | False | NULL |
| 0132C52C-7242-40B2-AFC9-A3A30CA0A94A | NULL | NULL | NULL | NULL | 2026-05-15T05:53:45.3100000 | NULL | False | False | NULL |
| 00F7DC17-34A6-4A69-AE8B-62DB3DDA5561 | NULL | NULL | NULL | NULL | 2026-06-22T13:27:08.4770000 | NULL | False | False | NULL |
| 0090384A-0FDA-4B15-A522-6FCB28259B44 | NULL | NULL | NULL | NULL | 2026-05-12T06:25:44.8830000 | NULL | False | False | NULL |
| 008156F5-A0EF-4761-B64E-D36B3530837B | NULL | NULL | NULL | NULL | 2026-06-23T16:42:14.3030000 | NULL | False | False | NULL |
| 0080F70F-F30F-4903-BE78-D50A4C9456B7 | NULL | NULL | NULL | NULL | 2025-12-16T16:27:38.5370000 | NULL | False | False | NULL |
| 006232EF-176A-4AB8-B40D-B67230E42BB7 | NULL | NULL | NULL | NULL | 2025-12-16T16:27:38.5370000 | NULL | False | False | NULL |
| 0058427D-4026-48DC-8318-ABB3499D948D | NULL | NULL | NULL | NULL | 2026-05-26T15:46:32.6170000 | NULL | False | False | NULL |
| 005706A4-49AF-4749-AE45-870E0FA67B44 | NULL | NULL | NULL | NULL | 2026-06-10T18:01:22.4600000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_MES_Heat_Tracking.CCMWorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.EAFWorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.LFEngineer` -> `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.LRFOperator` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.LRFWorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.Melter` -> `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.EAFOperator` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.Sequence` -> `XStudio_XBatch.CCM_Per_Heat.LadleSequence` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.ShiftManager` -> `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.StartTime` -> `XStudio_XBatch.CCM_Per_Heat.StartTime` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.SteelGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
