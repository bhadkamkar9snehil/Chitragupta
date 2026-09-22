# XStudio_Xbatch.dbo.RM_Furnace_Parameter_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temp, zone, actual, bottom, set, soaking, top, gas, heating, left, preheating, pressuremm.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
**Row Count:** 0  

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
| Shift | varchar | YES | 100 | — |
| OperatorName | varchar | YES | 36 | — |
| ProductDia | varchar | YES | 100 | — |
| BilletLength | int | YES | 10,0 | — |
| PreheatingTopZone1TempSet | decimal | YES | 18,4 | — |
| PreheatingTopZone1TempActual | decimal | YES | 18,4 | — |
| PreheatingBottomZone2TempActual | decimal | YES | 18,4 | — |
| PreheatingBottomZone2TempSet | decimal | YES | 18,4 | — |
| HeatingTopBottomZone3TempSet | decimal | YES | 18,4 | — |
| HeatingTopBottomZone3TempActual | decimal | YES | 18,4 | — |
| HeatingBottomZone4TempActual | decimal | YES | 18,4 | — |
| HeatingBottomZone4TempSet | decimal | YES | 18,4 | — |
| SoakingTopLeftZone5TempSet | decimal | YES | 18,4 | — |
| SoakingTopLeftZone5TempActual | decimal | YES | 18,4 | — |
| SoakingTopRightZone6TempActual | decimal | YES | 18,4 | — |
| SoakingTopRightZone6TempSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftZone7TempSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftZone7TempActual | decimal | YES | 18,4 | — |
| SoakingBottomRightZone8TempActual | decimal | YES | 18,4 | — |
| SoakingBottomRightZone8TempSet | decimal | YES | 18,4 | — |
| RecuperatorAirOutletTemp | decimal | YES | 18,4 | — |
| RecuperatorFlueGasInletTemp | decimal | YES | 18,4 | — |
| RecuperatorFlueGasOutletTemp | decimal | YES | 18,4 | — |
| RecuperatorDamperPosition | decimal | YES | 18,4 | — |
| PressuremmWCCombustionAirSet | decimal | YES | 18,4 | — |
| PressuremmWCCombustionAirActual | decimal | YES | 18,4 | — |
| PressuremmWCNaturalGasBeforePRV | decimal | YES | 18,4 | — |
| PressuremmWCNaturalGasAfterPRV | decimal | YES | 18,4 | — |
| PressureFurnaceSet | decimal | YES | 18,4 | — |
| PressureFurnaceActual | decimal | YES | 18,4 | — |
| Remarks | varchar | YES | -1 | — |

---
