# XStudio_Xbatch.dbo.LRF_Manual_Entry_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, consumption, temperature, addition, alloy, caster, consuption, dololime, electrode, end, gas, heat.

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
| IsProcessed | bit | YES | — | — |
| ElectrodeConsumption | int | YES | 10,0 | — |
| LaddleHoldTime | int | YES | 10,0 | — |
| LRFTreatmentEndTime | datetime | YES | — | — |
| LFInTime | datetime | YES | — | — |
| LimeConsuption | decimal | YES | 18,4 | — |
| AlloyAdditionPerTonOfSteel | int | YES | 10,0 | — |
| TemperatureLifting | decimal | YES | 18,4 | — |
| Temperature2 | decimal | YES | 18,4 | — |
| LFProcessTime | int | YES | 10,0 | — |
| HeatNo | int | YES | 10,0 | — |
| Name | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| CasterStartTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| Temperature1 | decimal | YES | 18,4 | — |
| LFOutTime | datetime | YES | — | — |
| NitrogenGasConsumption | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |
| DololimeConsumption | decimal | YES | 18,4 | — |

---
