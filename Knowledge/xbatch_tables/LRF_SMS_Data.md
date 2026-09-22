# XStudio_Xbatch.dbo.LRF_SMS_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** data, flow, heat, insert, lrf, per (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference silo, name, status, power, pump, hydraclauric, primary, time, voltage, energy, fan, flow.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-09-02T10:48:05.5530000 to 2026-09-02T10:48:05.5530000  

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
| LRFHeatID | decimal | YES | 18,4 | — |
| ArcingTime | decimal | YES | 18,4 | — |
| ArgonFlow | decimal | YES | 18,4 | — |
| SiloName3 | varchar | YES | 100 | — |
| Silo3Kg | decimal | YES | 18,4 | — |
| SiloName4 | varchar | YES | 100 | — |
| Silo4Kg | decimal | YES | 18,4 | — |
| SiloName5 | varchar | YES | 100 | — |
| Silo5Kg | decimal | YES | 18,4 | — |
| SiloName6 | varchar | YES | 100 | — |
| Silo6Kg | decimal | YES | 18,4 | — |
| SiloName7 | varchar | YES | 100 | — |
| Silo7Kg | decimal | YES | 18,4 | — |
| SiloName8 | varchar | YES | 100 | — |
| Silo8Kg | decimal | YES | 18,4 | — |
| LRFActualEnergy | decimal | YES | 18,4 | — |
| EnergyConsumption | decimal | YES | 18,4 | — |
| PowerOffTime | decimal | YES | 18,4 | — |
| LRFLime | decimal | YES | 18,4 | — |
| LRFSiMn | decimal | YES | 18,4 | — |
| LRFFeSi | decimal | YES | 18,4 | — |
| LRFDolo | decimal | YES | 18,4 | — |
| PowerOnTime | decimal | YES | 18,4 | — |
| HeatID | int | YES | 10,0 | — |
| LRFLiquidSteelweight | decimal | YES | 18,4 | — |
| LRFGrade | varchar | YES | 100 | — |
| PrimaryVoltage1 | decimal | YES | 18,4 | — |
| PrimaryVoltage2 | decimal | YES | 18,4 | — |
| PrimaryVoltage3 | decimal | YES | 18,4 | — |
| BoosterFanStatus | decimal | YES | 18,4 | — |
| LRFActivePower | decimal | YES | 18,4 | — |
| PurgingFlow | decimal | YES | 18,4 | — |
| LRFPLCStatus | decimal | YES | 18,4 | — |
| MHSPLCStatus | decimal | YES | 18,4 | — |
| TransformerTap | decimal | YES | 18,4 | — |
| MHSBoosterFanStatus | decimal | YES | 18,4 | — |
| HydraclauricPump1Status | decimal | YES | 18,4 | — |
| HydraclauricPump2Status | decimal | YES | 18,4 | — |
| HydraclauricPump3Status | decimal | YES | 18,4 | — |
| RecirculationPumpStatus | decimal | YES | 18,4 | — |
| TransformerTemperature | decimal | YES | 18,4 | — |
| SpecificPower | decimal | YES | 18,4 | — |
| LRFLowerPanelHeader | varchar | YES | 100 | — |
| LRFTemp | decimal | YES | 18,2 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 27DD4C1E-349C-4BB9-8BBD-32C7ECB23F78 | NULL | NULL | NULL | NULL | 2025-07-22T10:36:31.7730000 | 2026-09-02T10:48:05.5530000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_SMS_Data.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
