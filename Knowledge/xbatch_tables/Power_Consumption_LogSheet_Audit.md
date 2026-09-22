# XStudio_Xbatch.dbo.Power_Consumption_LogSheet_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference transformer, mva, mvalossesk, eaf, lrf, mill, ngactual, ngconsumption, oxygen, plant, reading, rolling.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Transformer132kv1 | decimal | YES | 18,4 | — |
| Transformer132kv2 | decimal | YES | 18,4 | — |
| Transformer33kv1 | decimal | YES | 18,4 | — |
| Transformer33kv2 | decimal | YES | 18,4 | — |
| EAF | decimal | YES | 18,4 | — |
| LRF | decimal | YES | 18,4 | — |
| Transformer24MVA | decimal | YES | 18,4 | — |
| Transformer15MVA | decimal | YES | 18,4 | — |
| RollingMill | decimal | YES | 18,4 | — |
| WRM | decimal | YES | 18,4 | — |
| OxygenPlant4A | decimal | YES | 18,4 | — |
| NGConsumptionSm3 | decimal | YES | 18,4 | — |
| Transformer63MVALosseskWH | decimal | YES | 18,4 | — |
| Transformer125MVALosseskWH | decimal | YES | 18,4 | — |
| NGActualReading | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |

---
