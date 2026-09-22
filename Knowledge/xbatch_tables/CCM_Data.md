# XStudio_Xbatch.dbo.CCM_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** area, ccm, chain, confirmed, cross, data, flow, heat, insert, per, plant, process, same, sms, system, time, timing, xbatch, xstudio (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference std, strand, flow, water, zone, casting, billet, weight, pressure, plcstatus, specific, time.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-09-02T10:48:14.9900000 to 2026-09-02T10:48:14.9900000  

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
| CCMHEATID | decimal | YES | 18,4 | — |
| STD1BilletCount | decimal | YES | 18,4 | — |
| STD1CastingSpeed | decimal | YES | 18,4 | — |
| STD1OSCSpeed | decimal | YES | 18,4 | — |
| STD2BilletCount | decimal | YES | 18,4 | — |
| STD2CastingSpeed | decimal | YES | 18,4 | — |
| STD2OSCSpeed | decimal | YES | 18,4 | — |
| STD3BilletCount | decimal | YES | 18,4 | — |
| STD3CastingSpeed | decimal | YES | 18,4 | — |
| STD3OSCSpeed | decimal | YES | 18,4 | — |
| STD4BilletCount | decimal | YES | 18,4 | — |
| STD4CastingSpeed | decimal | YES | 18,4 | — |
| STD4OSCSpeed | decimal | YES | 18,4 | — |
| STD5BilletCount | decimal | YES | 18,4 | — |
| STD5CastingSpeed | decimal | YES | 18,4 | — |
| STD5OSCSpeed | decimal | YES | 18,4 | — |
| STD6BilletCount | decimal | YES | 18,4 | — |
| STD6CastingSpeed | decimal | YES | 18,4 | — |
| STD6OSCSpeed | decimal | YES | 18,4 | — |
| TotalBilletWeight | decimal | YES | 18,4 | — |
| TotalCastTime | decimal | YES | 18,4 | — |
| TotalTPH | decimal | YES | 18,4 | — |
| Zone1WaterFlow | decimal | YES | 18,4 | — |
| Zone2WaterFlow | decimal | YES | 18,4 | — |
| Zone3WaterFlow | decimal | YES | 18,4 | — |
| TundishRemainingWeight | decimal | YES | 18,4 | — |
| STD1CastingLevel | decimal | YES | 18,4 | — |
| STD2CastingLevel | decimal | YES | 18,4 | — |
| STD3CastingLevel | decimal | YES | 18,4 | — |
| STD4CastingLevel | decimal | YES | 18,4 | — |
| STD5CastingLevel | decimal | YES | 18,4 | — |
| STD6CastingLevel | decimal | YES | 18,4 | — |
| TurretCastedWeight | decimal | YES | 18,4 | — |
| TundishLMWeight | decimal | YES | 18,4 | — |
| MaterialSpecificWeight | decimal | YES | 18,4 | — |
| STD1Zone1WaterFlow | decimal | YES | 18,4 | — |
| STD2Zone1WaterFlow | decimal | YES | 18,4 | — |
| STD3Zone1WaterFlow | decimal | YES | 18,4 | — |
| STD4Zone1WaterFlow | decimal | YES | 18,4 | — |
| STD5Zone1WaterFlow | decimal | YES | 18,4 | — |
| STD6Zone1WaterFlow | decimal | YES | 18,4 | — |
| STD1Zone2WaterFlow | decimal | YES | 18,4 | — |
| STD1Zone3WaterFlow | decimal | YES | 18,4 | — |
| STD2Zone2WaterFlow | decimal | YES | 18,4 | — |
| STD2Zone3WaterFlow | decimal | YES | 18,4 | — |
| STD3Zone2WaterFlow | decimal | YES | 18,4 | — |
| STD3Zone3WaterFlow | decimal | YES | 18,4 | — |
| STD4Zone2WaterFlow | decimal | YES | 18,4 | — |
| STD4Zone3WaterFlow | decimal | YES | 18,4 | — |
| STD5Zone2WaterFlow | decimal | YES | 18,4 | — |
| STD5Zone3WaterFlow | decimal | YES | 18,4 | — |
| STD6Zone2WaterFlow | decimal | YES | 18,4 | — |
| STD6Zone3WaterFlow | decimal | YES | 18,4 | — |
| TurretCastedWeightArm1 | decimal | YES | 18,4 | — |
| LiquidSteelWeight | decimal | YES | 18,4 | — |
| RemainingWeight | decimal | YES | 18,4 | — |
| Arm1Castposition | decimal | YES | 18,4 | — |
| Arm2Castposition | decimal | YES | 18,4 | — |
| Section | decimal | YES | 18,4 | — |
| RemainingCastingTime | varchar | YES | 100 | — |
| TotalRunningStrands | varchar | YES | 100 | — |
| SteamFan1Status | decimal | YES | 18,4 | — |
| SteamFan2Status | decimal | YES | 18,4 | — |
| LiquidTemperature | varchar | YES | 100 | — |
| LiquidusTemperature | varchar | YES | 100 | — |
| CCMHeatNo | varchar | YES | 100 | — |
| CVSPLCStatus | decimal | YES | 18,4 | — |
| CommonPLCStatus | decimal | YES | 18,4 | — |
| Strand1PLCStatus | decimal | YES | 18,4 | — |
| Strand2PLCStatus | decimal | YES | 18,4 | — |
| Strand3PLCStatus | decimal | YES | 18,4 | — |
| Strand4PLCStatus | decimal | YES | 18,4 | — |
| Strand5PLCStatus | decimal | YES | 18,4 | — |
| Strand6PLCStatus | decimal | YES | 18,4 | — |
| CCMLadleSequence | decimal | YES | 18,4 | — |
| CCMCastingDate | varchar | YES | 100 | — |
| CCMCastingTime | time | YES | — | — |
| SteelGrade | varchar | YES | 100 | — |
| TotalCastedBillets | decimal | YES | 18,4 | — |
| Cuttinglength | int | YES | 10,0 | — |
| Productivity | decimal | YES | 18,2 | — |
| Strand1StraightnerPressure | decimal | YES | 18,4 | — |
| Strand2StraightnerPressure | decimal | YES | 18,4 | — |
| Strand3StraightnerPressure | decimal | YES | 18,4 | — |
| Strand4StraightnerPressure | decimal | YES | 18,4 | — |
| Strand5StraightnerPressure | decimal | YES | 18,4 | — |
| Strand6StraightnerPressure | decimal | YES | 18,4 | — |
| Strand1WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand2WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand3WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand4WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand5WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand6WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand1BilletSpecificWeight | decimal | YES | 18,4 | — |
| Strand2BilletSpecificWeight | decimal | YES | 18,4 | — |
| Strand3BilletSpecificWeight | decimal | YES | 18,4 | — |
| Strand4BilletSpecificWeight | decimal | YES | 18,4 | — |
| Strand5BilletSpecificWeight | decimal | YES | 18,4 | — |
| Strand6BilletSpecificWeight | decimal | YES | 18,4 | — |
| TotalBillet | decimal | YES | 18,4 | — |
| RemainingCastingTimeMES | varchar | YES | 100 | — |
| RemainingCastingTimeActualTag | decimal | YES | 18,4 | — |
| CCMTundishTemp | decimal | YES | 18,4 | — |
| CastingTimeHHMMSS | varchar | YES | 100 | — |
| StartTime | datetime | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7D12EDCC-A927-4E23-B68E-60DBA7710834 | NULL | NULL | NULL | NULL | 2025-07-11T17:28:14.9130000 | 2026-09-02T10:48:14.9900000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Data.CastingTimeHHMMSS` -> `XStudio_XBatch.CCM_Per_Heat.CastingStartTime` (Many to One)
- `XStudio_XBatch.CCM_Data.EquipmentID` -> `XStudio_XBatch.CCM_Mst_Tbl.ID` (Many to One)
