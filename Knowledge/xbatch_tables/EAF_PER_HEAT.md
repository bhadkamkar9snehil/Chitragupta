# XStudio_Xbatch.dbo.EAF_PER_HEAT

**table_kind:** production_data

### What this table is for

- **Curated domain match (heat_execution):** Heat missing, wrong EAF/LRF/CCM state, per-heat value wrong, timing, alloy, power, yield, or attribution question.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** billet, billets, cast, confirmed, core, count, data, eaf, entities, event, flow, from, furnace, heat, insert, lrf, map, per, procedure, production, routing, same, sohar, stored, system, tracking, xbatch, xlsx, xstudio (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, hms, addition, ladle, manual, power, auto, consumption, avg, end, heat, briquette.

**Primary Key:** ID  
**Row Count:** 7,541  
**Date Range (ModifiedOn):** 2025-08-06T13:38:00.2570000 to 2026-07-17T17:18:20.0100000  

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
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| HeatID | int | YES | 10,0 | — |
| CopexScrapCH1 | decimal | YES | 18,4 | — |
| CopexScrapCH2 | decimal | YES | 18,4 | — |
| BundleLMSCH1 | decimal | YES | 18,4 | — |
| BundleLMSCH2 | decimal | YES | 18,4 | — |
| HMS12CH1 | decimal | YES | 18,4 | — |
| HMS12CH2 | decimal | YES | 18,4 | — |
| HMS1CH1 | decimal | YES | 18,4 | — |
| HMS1CH2 | decimal | YES | 18,4 | — |
| EndCutsCH1 | decimal | YES | 18,4 | — |
| EndCutsCH2 | decimal | YES | 18,4 | — |
| ScullCH1 | decimal | YES | 18,4 | — |
| ScullCH2 | decimal | YES | 18,4 | — |
| BriquetteCH1 | decimal | YES | 18,4 | — |
| BriquetteCH2 | decimal | YES | 18,4 | — |
| HBIDRICH1 | decimal | YES | 18,4 | — |
| HBIDRICH2 | decimal | YES | 18,4 | — |
| ShreeddedCH1 | decimal | YES | 18,4 | — |
| ShreeddedCH2 | decimal | YES | 18,4 | — |
| PowerMWH | decimal | YES | 18,4 | — |
| PowerKWHPerTon | decimal | YES | 18,4 | — |
| OxygenConsumption | decimal | YES | 18,4 | — |
| PowerOnTime | varchar | YES | 100 | — |
| PowerOffTime | varchar | YES | 100 | — |
| HeatTime | varchar | YES | 100 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| Lime | decimal | YES | 18,4 | — |
| DoloLime | decimal | YES | 18,4 | — |
| TrunageofHeat | decimal | YES | 18,4 | — |
| ChargeWeight | decimal | YES | 18,4 | — |
| TaptoTapTime | decimal | YES | 18,4 | — |
| CopexScrap | decimal | YES | 18,4 | — |
| HMS12 | decimal | YES | 18,4 | — |
| HMS1 | decimal | YES | 18,4 | — |
| BundleLMS | decimal | YES | 18,4 | — |
| EndCuts | decimal | YES | 18,4 | — |
| Scull | decimal | YES | 18,4 | — |
| Briquette | decimal | YES | 18,4 | — |
| HeatTimeMinute | decimal | YES | 18,4 | — |
| Shredded | decimal | YES | 18,4 | — |
| ArcingTime | decimal | YES | 18,4 | — |
| Tapping1 | decimal | YES | 18,4 | — |
| Tapping2 | decimal | YES | 18,4 | — |
| HeatTimeSecond | decimal | YES | 18,4 | — |
| PowerOnTimeSecond | decimal | YES | 18,4 | — |
| PowerOnTimeMinute | decimal | YES | 18,4 | — |
| PowerOFFTimeMinute | decimal | YES | 18,4 | — |
| PowerOFFTimeSecond | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| BIN1LimeConsumption | decimal | YES | 18,4 | — |
| BIN2DoloConsumption | decimal | YES | 18,4 | — |
| BIN3Consumption | decimal | YES | 18,4 | — |
| BIN4Consumption | decimal | YES | 18,4 | — |
| ChargeMixWeight | decimal | YES | 18,4 | — |
| HeattimeTotalSeconds | decimal | YES | 18,4 | — |
| PoweronTimeTotalSeconds | decimal | YES | 18,4 | — |
| PowerOffTimeTotalSeconds | decimal | YES | 18,4 | — |
| Statusworkflow | varchar | YES | 50 | — |
| SteelGrade | varchar | YES | 100 | — |
| TotalChargeWeightMT | decimal | YES | 18,4 | — |
| TapTimeMinute | decimal | YES | 18,4 | — |
| TapStart | datetime | YES | — | — |
| HeatStart | datetime | YES | — | — |
| HBIDRI | decimal | YES | 18,4 | — |
| Shreedded | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| YieldPerHeat | decimal | YES | 18,4 | — |
| NGconsumptionpertonofsteel | decimal | YES | 18,4 | — |
| Limepertonofsteel | decimal | YES | 18,4 | — |
| Dololimepertonofsteel | decimal | YES | 18,4 | — |
| PowerPerTonofSteel | decimal | YES | 18,4 | — |
| BIN3Name | varchar | YES | 100 | — |
| BIN4Name | varchar | YES | 100 | — |
| CarbonConsumption | decimal | YES | 18,4 | — |
| LadleAdditionLime | decimal | YES | 18,4 | — |
| LadleAdditionDolo | decimal | YES | 18,4 | — |
| LadleAdditionSiMn | decimal | YES | 18,4 | — |
| LadleAdditionFeSi | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight | decimal | YES | 18,2 | — |
| LadleAdditionSiMnn | decimal | YES | 18,4 | — |
| Avg_PoweronTIme | decimal | YES | 18,4 | — |
| Avg_PoweroffTIme | decimal | YES | 18,4 | — |
| Avg_PowerMW | decimal | YES | 18,4 | — |
| Avg_TTT | decimal | YES | 18,4 | — |
| HeatReportDate | date | YES | — | — |
| WorkOrder | varchar | YES | 100 | — |
| CalcLiquidMetalWeight | decimal | YES | 18,2 | — |
| SAPWorkflowStatus | varchar | YES | 50 | — |
| LSDELTA | decimal | YES | 18,4 | — |
| ManualLadleAdditionLime | decimal | YES | 18,4 | — |
| ManualLadleAdditionDolo | decimal | YES | 18,4 | — |
| ManualLadleAdditionFesi | decimal | YES | 18,4 | — |
| ManualLadleAdditionSimn | decimal | YES | 18,4 | — |
| AutoLadleAdditionLime | decimal | YES | 18,4 | — |
| AutoLadleAdditionDolo | decimal | YES | 18,4 | — |
| AutoLadleAdditionFesi | decimal | YES | 18,4 | — |
| AutoLadleAdditionSiMn | decimal | YES | 18,4 | — |
| TempTips | decimal | YES | 18,4 | — |
| EBTFilter | decimal | YES | 18,4 | — |
| RamMass | decimal | YES | 18,4 | — |
| GunningMass | decimal | YES | 18,4 | — |
| FettlingMass | decimal | YES | 18,4 | — |
| ElectrodeConsumption1Kg | decimal | YES | 18,4 | — |
| ElectrodeConsumption2Kg | decimal | YES | 18,4 | — |
| ElectrodeConsumption3Kg | decimal | YES | 18,4 | — |
| RejectedBilletWeightTon | decimal | YES | 18,4 | — |
| NutCokeKgPerTon | decimal | YES | 18,4 | — |
| TapTemp | decimal | YES | 18,4 | — |
| ThroughputTPH | decimal | YES | 18,4 | — |
| PowerOnCharge | decimal | YES | 18,4 | — |
| CokeInjection | decimal | YES | 18,4 | — |
| TotalElectrodeConsumption | decimal | YES | 18,4 | — |
| CopexScrapAuto | decimal | YES | 18,4 | — |
| CopexScrapManual | decimal | YES | 18,4 | — |
| HMS1Auto | decimal | YES | 18,4 | — |
| HMS1Manual | decimal | YES | 18,4 | — |
| HMS12Auto | decimal | YES | 18,4 | — |
| HMS12Manual | decimal | YES | 18,4 | — |
| EndCutsAuto | decimal | YES | 18,4 | — |
| EndCutsManual | decimal | YES | 18,4 | — |
| BriquetteAuto | decimal | YES | 18,4 | — |
| BriquetteManual | decimal | YES | 18,4 | — |
| BundleLMSAuto | decimal | YES | 18,4 | — |
| BundleLMSManual | decimal | YES | 18,4 | — |
| HBIDRIAuto | decimal | YES | 18,4 | — |
| HBIDRIManual | decimal | YES | 18,4 | — |
| ShreddedAuto | decimal | YES | 18,4 | — |
| ShreddedManual | decimal | YES | 18,4 | — |
| SkullAuto | decimal | YES | 18,4 | — |
| SkullManual | decimal | YES | 18,4 | — |
| HBIConsumption | decimal | YES | 18,4 | — |
| CdriConsumption | decimal | YES | 18,4 | — |
| CopexScrapCH3 | decimal | YES | 18,4 | — |
| CopexScrapCH4 | decimal | YES | 18,4 | — |
| BundleLMSCH3 | decimal | YES | 18,4 | — |
| BundleLMSCH4 | decimal | YES | 18,4 | — |
| HMS12CH3 | decimal | YES | 18,4 | — |
| HMS12CH4 | decimal | YES | 18,4 | — |
| HMS1CH3 | decimal | YES | 18,4 | — |
| HMS1CH4 | decimal | YES | 18,4 | — |
| EndCutsCH3 | decimal | YES | 18,4 | — |
| EndCutsCH4 | decimal | YES | 18,4 | — |
| ScullCH3 | decimal | YES | 18,4 | — |
| ScullCH4 | decimal | YES | 18,4 | — |
| BriquetteCH3 | decimal | YES | 18,4 | — |
| BriquetteCH4 | decimal | YES | 18,4 | — |
| HBIDRICH3 | decimal | YES | 18,4 | — |
| HBIDRICH4 | decimal | YES | 18,4 | — |
| ShreeddedCH3 | decimal | YES | 18,4 | — |
| ShreeddedCH4 | decimal | YES | 18,4 | — |
| HerausTemp | decimal | YES | 18,4 | — |
| HerausManualPPM | decimal | YES | 18,4 | — |
| EAFTemperature | decimal | YES | 18,2 | — |
| E1SprayCoolingFlowAvg | decimal | YES | 18,4 | — |
| E2SprayCoolingFlowAvg | decimal | YES | 18,4 | — |
| E3SprayCoolingFlowAvg | decimal | YES | 18,4 | — |
| E1SprayCollingFlowDurationSec | int | YES | 10,0 | — |
| E2SprayCollingFlowDurationSec | int | YES | 10,0 | — |
| E3SprayCollingFlowDurationSec | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 397C021D-D40D-4034-A3F4-0B43EDA49F59 | NULL | NULL | NULL | NULL | 2025-08-06T13:35:37.2770000 | 2025-08-06T13:38:00.2570000 | False | False | NULL |
| B56265C6-C3F8-447C-80D7-8A7791677435 | NULL | NULL | NULL | NULL | 2025-08-06T14:31:58.6570000 | 2025-08-06T14:34:27.2330000 | False | False | NULL |
| 1AD5CC1A-DA89-4CF8-B136-F1767C7C7D15 | NULL | NULL | NULL | NULL | 2025-08-06T15:28:14.3500000 | 2025-08-06T15:30:47.3530000 | False | False | NULL |
| 00CF84FD-FC4F-4DB1-B526-BD03DA2DD5C1 | NULL | NULL | NULL | NULL | 2025-08-06T16:24:54.2830000 | 2025-08-06T16:27:48.4170000 | False | False | NULL |
| C6525037-A132-488D-B4CB-E74A51C067BE | NULL | NULL | NULL | NULL | 2025-08-06T17:21:37.3000000 | 2025-08-06T17:23:47.2900000 | False | False | NULL |
| 1E1F88C8-2D05-4F14-A7DA-F21A4468470F | NULL | NULL | NULL | NULL | 2025-08-06T18:15:13.4270000 | 2025-08-06T18:17:29.5900000 | False | False | NULL |
| 17DD4EA5-7286-4681-A6D5-5C9B02E46DE3 | NULL | NULL | NULL | NULL | 2025-08-06T19:18:23.5700000 | 2025-08-06T19:20:39.2300000 | False | False | NULL |
| 8EA8885F-CABD-4F75-BC79-7CCD44EFFC08 | NULL | NULL | NULL | NULL | 2025-08-06T20:13:58.2700000 | 2025-08-06T20:15:48.1630000 | False | False | NULL |
| CD794A4A-5688-458F-9B8A-C0F38C767F4F | NULL | NULL | NULL | NULL | 2025-08-06T21:08:41.2030000 | 2025-08-06T21:10:52.3200000 | False | False | NULL |
| F58CA3F7-FA25-423B-9BBA-E1E159355E05 | NULL | NULL | NULL | NULL | 2025-08-06T22:02:59.5900000 | 2025-08-06T22:06:31.5900000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B5B76317-3980-4788-B46C-7386AEC110B5 | NULL | NULL | NULL |  | 2026-07-17T17:18:19.4370000 | 2026-07-17T17:18:20.0100000 | False | False | NULL |
| CE2268C7-9D85-4465-AAAF-6D04426AFEC5 | NULL | NULL | NULL |  | 2026-07-08T17:03:36.3030000 | 2026-07-08T23:43:08.7400000 | False | False | NULL |
| 8CD203DB-A35C-49B4-B7E9-F5C4654806C3 | NULL | NULL | NULL |  | 2026-07-08T16:07:22.3500000 | 2026-07-08T23:41:50.6800000 | False | False | NULL |
| C8A83181-905E-4BFF-9559-2D267B8A3000 | NULL | NULL | NULL |  | 2026-07-08T17:59:18.4130000 | 2026-07-08T18:04:24.4670000 | False | False | NULL |
| FFC9BEB1-33ED-492A-8BF5-423D4177DBA8 | NULL | NULL | NULL |  | 2026-07-08T15:06:57.9700000 | 2026-07-08T18:00:23.1270000 | False | False | NULL |
| 206E9344-067C-45A7-A887-F44068AEBCFC | NULL | NULL | NULL |  | 2026-07-08T14:03:19.9630000 | 2026-07-08T16:48:42.8500000 | False | False | NULL |
| 563AF68D-4F0F-4A23-A93E-A6A1885C5C03 | NULL | NULL | NULL |  | 2026-07-08T13:06:12.2630000 | 2026-07-08T15:38:53.7400000 | False | False | NULL |
| B79A2D1C-069C-41C7-94EC-6FEAE10D9635 | NULL | NULL | NULL |  | 2026-07-08T12:08:23.1570000 | 2026-07-08T15:38:25.7130000 | False | False | NULL |
| E4479F09-779A-472A-8531-106526A360D3 | NULL | NULL | NULL |  | 2026-07-08T10:58:52.1770000 | 2026-07-08T15:38:00.0970000 | False | False | NULL |
| 8F340E1F-3F9A-4663-A5EE-CED47DCDC4A9 | NULL | NULL | NULL |  | 2026-07-08T09:58:35.2770000 | 2026-07-08T12:24:43.7500000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Chemistry_Deviation_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.EAF_LogSheet_Quantity.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.HeatID` (Many to One)
- `XStudio_XBatch.EAF_PER_HEAT.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_PER_HEAT.SteelGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.EAF_PER_HEAT.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Heat_Chemistry_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Rebar_Coil_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Rebar_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Round_Bar_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Tag_Configuration.HeatID` -> `XStudio_XBatch.EAF_PER_HEAT.HeatID` (Many to One)
- `XStudio_XBatch.Wire_Rod_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Wire_Rod_Quality_Data_File_Import.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
