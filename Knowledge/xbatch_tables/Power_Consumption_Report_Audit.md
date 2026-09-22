# XStudio_Xbatch.dbo.Power_Consumption_Report_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference transformer, mill, mva, mvalosses, plant, rolling, smsaux, total, eaf, lrf, ngconsumption, oxygen.

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
| OxygenPlant4A | decimal | YES | 18,4 | — |
| SMSTotal | decimal | YES | 18,4 | — |
| Transformer132kv2 | decimal | YES | 18,4 | — |
| Transformer132kv1 | decimal | YES | 18,4 | — |
| Transformer63MVALosses | decimal | YES | 18,4 | — |
| Transformer33kv1 | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| WRM | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| RollingMill | decimal | YES | 18,4 | — |
| Transformer15MVA | decimal | YES | 18,4 | — |
| SMSAuxWithO2 | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| Transformer33kv2 | decimal | YES | 18,4 | — |
| TotalRollingMill | decimal | YES | 18,4 | — |
| LRF | decimal | YES | 18,4 | — |
| Transformer125MVALosses | decimal | YES | 18,4 | — |
| PlantTotal | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| SMSAuxWithoutO2 | decimal | YES | 18,4 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| EAF | decimal | YES | 18,4 | — |
| Transformer24MVA | decimal | YES | 18,4 | — |

---
