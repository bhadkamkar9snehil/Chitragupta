# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference zone, actual, set, bottom, soaking, top, airflow, gasflow, heating, left, right, descaler.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-08-31T10:35:09.2770000 to 2026-08-31T10:35:09.2770000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| RMCallBillet | decimal | YES | 18,4 | — |
| RMReady | decimal | YES | 18,4 | — |
| FurnaceReady | decimal | YES | 18,4 | — |
| SNGLineOn | decimal | YES | 18,4 | — |
| NGLineOn | decimal | YES | 18,4 | — |
| NGActualHour | decimal | YES | 18,4 | — |
| NGActualShift | decimal | YES | 18,4 | — |
| NGActualDay | decimal | YES | 18,4 | — |
| SNGActualHour | decimal | YES | 18,4 | — |
| SNGActualShift | decimal | YES | 18,4 | — |
| SNGActualDay | decimal | YES | 18,4 | — |
| NGPreviousHour | decimal | YES | 18,4 | — |
| NGPreviousShift | decimal | YES | 18,4 | — |
| NGPreviousDay | decimal | YES | 18,4 | — |
| SNGPreviousHour | decimal | YES | 18,4 | — |
| SNGPreviousShift | decimal | YES | 18,4 | — |
| SNGPreviousDay | decimal | YES | 18,4 | — |
| TotalEnergy | decimal | YES | 18,4 | — |
| NGEnergy | decimal | YES | 18,4 | — |
| SNGEnergy | decimal | YES | 18,4 | — |
| PreHeatingZoneTopSet | decimal | YES | 18,4 | — |
| PreHeatingZoneBottomSet | decimal | YES | 18,4 | — |
| HeatingZoneTopSet | decimal | YES | 18,4 | — |
| HeatingZoneBottomSet | decimal | YES | 18,4 | — |
| SoakingZoneRightTopSet | decimal | YES | 18,4 | — |
| SoakingZoneRightBottomSet | decimal | YES | 18,4 | — |
| SoakingZoneLeftTopSet | decimal | YES | 18,4 | — |
| SoakingZoneLeftBottomSet | decimal | YES | 18,4 | — |
| SoakingZoneLeftBottomActual | decimal | YES | 18,4 | — |
| SoakingZoneLeftTopActual | decimal | YES | 18,4 | — |
| SoakingZoneRightBottomActual | decimal | YES | 18,4 | — |
| SoakingZoneRightTopActual | decimal | YES | 18,4 | — |
| CombustionAirPressureActual | decimal | YES | 18,4 | — |
| CombustionAirPressureSet | decimal | YES | 18,4 | — |
| FurnacePressureSet | decimal | YES | 18,4 | — |
| FurnacePressureActual | decimal | YES | 18,4 | — |
| PreHeatingZoneTopActual | decimal | YES | 18,4 | — |
| PreHeatingZoneBottomActual | decimal | YES | 18,4 | — |
| HeatingZoneTopActual | decimal | YES | 18,4 | — |
| HeatingZoneBottomActual | decimal | YES | 18,4 | — |
| PreheatingZoneTopAirflowActual | decimal | YES | 18,4 | — |
| PreheatingZoneTopAirflowSet | decimal | YES | 18,4 | — |
| PreheatingZoneTopGasflowSet | decimal | YES | 18,4 | — |
| PreheatingZoneTopGasflowActual | decimal | YES | 18,4 | — |
| PreheatingZoneBottomAirflowSet | decimal | YES | 18,4 | — |
| PreheatingzoneBottomAirflowActual | decimal | YES | 18,4 | — |
| PreheatingzoneBottomGasflowActual | decimal | YES | 18,4 | — |
| PreheatingZoneBottomGasflowSet | decimal | YES | 18,4 | — |
| HeatingZoneTopAirflowActual | decimal | YES | 18,4 | — |
| HeatingZoneTopAirflowSet | decimal | YES | 18,4 | — |
| HeatingZoneTopGasflowSet | decimal | YES | 18,4 | — |
| HeatingZoneTopGasflowActual | decimal | YES | 18,4 | — |
| HeatingZoneBottomAirflowActual | decimal | YES | 18,4 | — |
| HeatingZoneBottomAirflowSet | decimal | YES | 18,4 | — |
| HeatingZoneBottomGasflowSet | decimal | YES | 18,4 | — |
| HeatingZoneBottomGasflowActual | decimal | YES | 18,4 | — |
| SoakingTopLeftAirflowSet | decimal | YES | 18,4 | — |
| SoakingTopLeftAirflowActual | decimal | YES | 18,4 | — |
| SoakingTopLeftGasflowActual | decimal | YES | 18,4 | — |
| SoakingTopLeftGasflowSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftAirflowSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftAirflowActual | decimal | YES | 18,4 | — |
| SoakingBottomLeftGasflowActual | decimal | YES | 18,4 | — |
| SoakingBottomLeftGasflowSet | decimal | YES | 18,4 | — |
| SoakingTopRightAirflowSet | decimal | YES | 18,4 | — |
| SoakingTopRightAirflowActual | decimal | YES | 18,4 | — |
| SoakingTopRightGasflowActual | decimal | YES | 18,4 | — |
| SoakingTopRightGasflowSet | decimal | YES | 18,4 | — |
| SoakingBottomRightAirflowSet | decimal | YES | 18,4 | — |
| SoakingBottomRightAirflowActual | decimal | YES | 18,4 | — |
| SoakingBottomRightGasflowActual | decimal | YES | 18,4 | — |
| SoakingBottomRightGasflowSet | decimal | YES | 18,4 | — |
| DescalerPump1RunningStatus | decimal | YES | 18,4 | — |
| DescalerPump2RunningStatus | decimal | YES | 18,4 | — |
| DescalerPump3RunningStatus | decimal | YES | 18,4 | — |
| DeacalerPressure | decimal | YES | 18,4 | — |
| DescalerDRT1Speed | decimal | YES | 18,4 | — |
| DescalerDRT2Speed | decimal | YES | 18,4 | — |
| DescalerDRT3Speed | decimal | YES | 18,4 | — |
| DescalerDRT4Speed | decimal | YES | 18,4 | — |
| ChargingDoorOpenStatus | decimal | YES | 18,4 | — |
| ChargingDoorCloseStatus | decimal | YES | 18,4 | — |
| DischargingDoorCloseStatus | decimal | YES | 18,4 | — |
| DischargingDoorOpenStatus | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 512AE8EA-772F-45DB-95E1-13F0D3378B06 | NULL | NULL | NULL | 2025-09-03T15:11:36.9600000 | 2026-08-31T10:35:09.2770000 | False | False | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Reheating_Furnace_Data.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
