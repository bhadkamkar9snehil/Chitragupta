# XStudio_Xbatch.dbo.EAF_Transformer_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temperature, hvbushing, reactor, cooler, tap, changer, flexible, lvtube, oil, phase, sec, breather.

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
| TransformerCurver | int | YES | 10,0 | — |
| PowerMW | decimal | YES | 18,4 | — |
| TapChangerCounter | int | YES | 10,0 | — |
| VCBCounter | int | YES | 10,0 | — |
| OilTemperature | int | YES | 10,0 | — |
| MainTank | int | YES | 10,0 | — |
| TapChanger | int | YES | 10,0 | — |
| Phase1B7A | int | YES | 10,0 | — |
| Phase2B7B | int | YES | 10,0 | — |
| Phase3B7C | int | YES | 10,0 | — |
| HVBushingTemperature1U | decimal | YES | 18,4 | — |
| HVBushingTemperature1V | decimal | YES | 18,4 | — |
| HVBushingTemperature1W | decimal | YES | 18,4 | — |
| HVBushingReactorU1 | decimal | YES | 18,4 | — |
| HVBushingReactorU2 | decimal | YES | 18,4 | — |
| HVBushingReactorV1 | decimal | YES | 18,4 | — |
| HVBushingReactorV2 | decimal | YES | 18,4 | — |
| HVBushingReactorW1 | decimal | YES | 18,4 | — |
| HVBushingReactorW2 | decimal | YES | 18,4 | — |
| LVTubeTemperature2UE1 | decimal | YES | 18,4 | — |
| LVTubeTemperature2VE2 | decimal | YES | 18,4 | — |
| LVTubeTemperature2WE3 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2UE1 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2VE2 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2WE3 | decimal | YES | 18,4 | — |
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
