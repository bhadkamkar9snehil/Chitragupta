# XStudio_Xbatch.dbo.EAF_Transformer_Reactor_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temperature, hvbushing, oil, cooler, tap, changer, divertor, phase, tank, breather, flow, flowm.

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
| HeatNo | varchar | YES | 100 | — |
| TapNo | int | YES | 10,0 | — |
| TapChangerCounter | int | YES | 10,0 | — |
| OilTremperature | int | YES | 10,0 | — |
| OilLevelReactor | int | YES | 10,0 | — |
| OilLevelTapChanger | int | YES | 10,0 | — |
| DivertorTankTemperaturePhase1B7A | int | YES | 10,0 | — |
| DivertorTankTemperaturePhase2B7B | int | YES | 10,0 | — |
| DivertorTankTemperaturePhase3B7C | int | YES | 10,0 | — |
| HVBushingTemperatureU1 | decimal | YES | 18,4 | — |
| HVBushingTemperatureU2 | decimal | YES | 18,4 | — |
| HVBushingTemperatureV1 | decimal | YES | 18,4 | — |
| HVBushingTemperatureV2 | decimal | YES | 18,4 | — |
| HVBushingTemperatureW1 | decimal | YES | 18,4 | — |
| HVBushingTemperatureW2 | decimal | YES | 18,4 | — |
| OilFlowRunningCooler1 | decimal | YES | 18,4 | — |
| OilFlowRunningCooler2 | decimal | YES | 18,4 | — |
| WaterFlowm3perhrCooler1 | decimal | YES | 18,4 | — |
| WaterFlowm3perhrCooler2 | decimal | YES | 18,4 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| Remarks | varchar | YES | 100 | — |
| Attendant | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |

---
