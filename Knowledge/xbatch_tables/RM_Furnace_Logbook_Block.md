# XStudio_Xbatch.dbo.RM_Furnace_Logbook_Block

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temp, zone, actual, set, bottom, soaking, top, pressure, gas, heating, left, preheating.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Remarks | varchar | YES | -1 | — |
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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| PreheatingTopZone1TempSet | decimal | YES | 18,4 | — |
| PreheatingTopZone1TempActual | decimal | YES | 18,4 | — |
| PreheatingBottomZone2TempSet | decimal | YES | 18,4 | — |
| PreheatingBottomZone2TempActual | decimal | YES | 18,4 | — |
| HeatingTopZone3TempSet | decimal | YES | 18,4 | — |
| HeatingTopZone3TempActual | decimal | YES | 18,4 | — |
| HeatingBottomZone4TempSet | decimal | YES | 18,4 | — |
| HeatingBottomZone4TempActual | decimal | YES | 18,4 | — |
| SoakingTopLeftZone5TempSet | decimal | YES | 18,4 | — |
| SoakingTopLeftZone5TempActual | decimal | YES | 18,4 | — |
| SoakingTopRightZone6TempSet | decimal | YES | 18,4 | — |
| SoakingTopRightZone6TempActual | decimal | YES | 18,4 | — |
| SoakingBottomLeftZone7TempSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftZone7TempActual | decimal | YES | 18,4 | — |
| SoakingBottomRightZone8TempSet | decimal | YES | 18,4 | — |
| SoakingBottomRightZone8TempActual | decimal | YES | 18,4 | — |
| RecuperatorAirOutletTemp | decimal | YES | 18,4 | — |
| RecuperatorFlueGasInletTemp | decimal | YES | 18,4 | — |
| RecuperatorFlueGasOutletTemp | decimal | YES | 18,4 | — |
| RecuperatorDamperPosition | decimal | YES | 18,4 | — |
| PressureCombustionAirSet | decimal | YES | 18,4 | — |
| PressureCombustionAirActual | decimal | YES | 18,4 | — |
| PressureNaturalGasBeforePRV | decimal | YES | 18,4 | — |
| PressureNaturalGasAfterPRV | decimal | YES | 18,4 | — |
| PressureFurnaceSet | decimal | YES | 18,4 | — |
| PressureFurnaceActual | decimal | YES | 18,4 | — |
| OperatorName | varchar | YES | 36 | — |
| ProductDIA | varchar | YES | 100 | — |
| BilletLength | varchar | YES | 100 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Furnace_Logbook_Block.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Logbook_Block.OperatorName` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
