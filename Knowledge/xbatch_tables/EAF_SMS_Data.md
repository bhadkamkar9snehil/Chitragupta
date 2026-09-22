# XStudio_Xbatch.dbo.EAF_SMS_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** electrical consumption, energy, kwh, power consumption (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, power, status, auto, bin, eafconsumption, current, pump, fan, minute, prev, eafbin.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-09-02T10:48:05.5300000 to 2026-09-02T10:48:05.5300000  

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
| CurrentTTT | decimal | YES | 18,4 | — |
| EAFBriquette | decimal | YES | 18,4 | — |
| EAFBundleorLMS | decimal | YES | 18,4 | — |
| EAFConsumptionBin1 | decimal | YES | 18,4 | — |
| EAFConsumptionBin2 | decimal | YES | 18,4 | — |
| EAFConsumptionBin3 | decimal | YES | 18,4 | — |
| EAFConsumptionBin4 | decimal | YES | 18,4 | — |
| EAFConsumptionPrevBin1 | decimal | YES | 18,4 | — |
| EAFConsumptionPrevBin2 | decimal | YES | 18,4 | — |
| EAFConsumptionPrevBin3 | decimal | YES | 18,4 | — |
| EAFConsumptionPrevBin4 | decimal | YES | 18,4 | — |
| EAFCopexScrap | decimal | YES | 18,4 | — |
| EAFEndCuts | decimal | YES | 18,4 | — |
| EAFEnergyMWH | decimal | YES | 18,4 | — |
| EAFHBIDRI | decimal | YES | 18,4 | — |
| EAFHeatID | decimal | YES | 18,4 | — |
| EAFHMS1 | decimal | YES | 18,4 | — |
| EAFHMS1and2 | decimal | YES | 18,4 | — |
| EAFScull | decimal | YES | 18,4 | — |
| EAFShredded | decimal | YES | 18,4 | — |
| EAFSpecificEnergy | decimal | YES | 18,4 | — |
| NGConsumptionToday | decimal | YES | 18,4 | — |
| NGConsumptionYesterday | decimal | YES | 18,4 | — |
| Oxygenconsumptionnm3 | decimal | YES | 18,4 | — |
| PowerOffTime | decimal | YES | 18,4 | — |
| PowerOnTime | decimal | YES | 18,4 | — |
| PrevTTT | decimal | YES | 18,4 | — |
| TotalChargeWeight | decimal | YES | 18,4 | — |
| EAFBIN1Name | varchar | YES | 100 | — |
| EAFBIN2Name | varchar | YES | 100 | — |
| EAFBIN3Name | varchar | YES | 100 | — |
| EAFBIN4Name | varchar | YES | 100 | — |
| TotalChargeMixWeight | decimal | YES | 18,4 | — |
| PowerOnTime_TimeStamp_Auto | datetime | YES | — | — |
| PowerOnTime_Quality_Auto | int | YES | 10,0 | — |
| PowerOnTimeMinuteSecond | decimal | YES | 18,4 | — |
| PowerOffTime_TimeStamp_Auto | datetime | YES | — | — |
| PowerOffTime_Quality_Auto | int | YES | 10,0 | — |
| PowerOnTimeMinuteSecond_TimeStamp_Auto | datetime | YES | — | — |
| PowerOnTimeMinuteSecond_Quality_Auto | int | YES | 10,0 | — |
| SteelGrade | varchar | YES | 100 | — |
| CurrentTTT_TimeStamp_Auto | datetime | YES | — | — |
| CurrentTTT_Quality_Auto | int | YES | 10,0 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| Yield | decimal | YES | 18,4 | — |
| BriquetteCH1 | decimal | YES | 18,4 | — |
| BriquetteCH2 | decimal | YES | 18,4 | — |
| BundleLMSCH1 | decimal | YES | 18,4 | — |
| BundleLMSCH2 | decimal | YES | 18,4 | — |
| CopexScrapCH1 | decimal | YES | 18,4 | — |
| CopexScrapCH2 | decimal | YES | 18,4 | — |
| EndCutsCH1 | decimal | YES | 18,4 | — |
| EndCutsCH2 | decimal | YES | 18,4 | — |
| HBIDRICH1 | decimal | YES | 18,4 | — |
| HBIDRICH2 | decimal | YES | 18,4 | — |
| HMS12CH1 | decimal | YES | 18,4 | — |
| HMS12CH2 | decimal | YES | 18,4 | — |
| HMS1CH1 | decimal | YES | 18,4 | — |
| HMS1CH2 | decimal | YES | 18,4 | — |
| ScullCH1 | decimal | YES | 18,4 | — |
| ScullCH2 | decimal | YES | 18,4 | — |
| ShreeddedCH1 | decimal | YES | 18,4 | — |
| ShreeddedCH2 | decimal | YES | 18,4 | — |
| CurrentTTTSec | decimal | YES | 18,4 | — |
| PreviousTTTSec | decimal | YES | 18,4 | — |
| CurrentTTTMinute | decimal | YES | 18,4 | — |
| PreviousTTTMinute | decimal | YES | 18,4 | — |
| PonMinute | decimal | YES | 18,4 | — |
| POffMinute | decimal | YES | 18,4 | — |
| PonSeconds | decimal | YES | 18,4 | — |
| POffSec | decimal | YES | 18,4 | — |
| Carbonconsumptionkg | decimal | YES | 18,4 | — |
| LiquidusTemperature | varchar | YES | 100 | — |
| EAFPLCStatus | decimal | YES | 18,4 | — |
| ISACPLCStatus | decimal | YES | 18,4 | — |
| MOREPLCStatus | decimal | YES | 18,4 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| ActivePower | decimal | YES | 18,4 | — |
| PrimaryVoltagekV | decimal | YES | 18,4 | — |
| HydraulicPump1Status | decimal | YES | 18,4 | — |
| HydraulicPump2Status | decimal | YES | 18,4 | — |
| HydraulicPump3Status | decimal | YES | 18,4 | — |
| HydraulicPump4Status | decimal | YES | 18,4 | — |
| RecirculationPump1Status | decimal | YES | 18,4 | — |
| RecirculationPump2Status | decimal | YES | 18,4 | — |
| BoosterFanStatus | decimal | YES | 18,4 | — |
| IdFan1Status | decimal | YES | 18,4 | — |
| IdFan2Status | decimal | YES | 18,4 | — |
| IdFan3Status | decimal | YES | 18,4 | — |
| IdFan4Status | decimal | YES | 18,4 | — |
| TransformerTap | decimal | YES | 18,4 | — |
| ReactorTap | decimal | YES | 18,4 | — |
| CurrentCurve | decimal | YES | 18,4 | — |
| EAFLowerPanelHeader | varchar | YES | 100 | — |
| LRFTransformerTap | decimal | YES | 18,4 | — |
| LRFActivePower | decimal | YES | 18,4 | — |
| LRFLowerPanelHeader | varchar | YES | 100 | — |
| FES1StackDust | decimal | YES | 18,4 | — |
| FES2StackDust | decimal | YES | 18,4 | — |
| EAFHERAUSTemp | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 74874E6C-AC68-4D0A-935F-CD3DA069AF95 | NULL | NULL | NULL | NULL | 2025-07-11T11:48:33.9970000 | 2026-09-02T10:48:05.5300000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_SMS_Data.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
