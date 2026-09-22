# XStudio_Xbatch.dbo.CCM_Manual_Entry_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference heat, tundish, ash, laddle, liquidus, super, temp, time, turrent, consumption, end, mould.

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
| Name | varchar | YES | 100 | — |
| LiquidusAsh2 | decimal | YES | 18,4 | — |
| SuperHeatT2 | decimal | YES | 18,4 | — |
| LiquidusAsh1 | decimal | YES | 18,4 | — |
| LaddleOnTurrentEndTime | datetime | YES | — | — |
| SuperHeatT3 | decimal | YES | 18,4 | — |
| TundishTemp2 | decimal | YES | 18,4 | — |
| LaddleOnTurretTime | int | YES | 10,0 | — |
| LiquidusAsh3 | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| TundishTemp3 | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| HeatNo | int | YES | 10,0 | — |
| SuperHeatT1 | decimal | YES | 18,4 | — |
| TundishNumber | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| LaddleOnTurrentStartTime | datetime | YES | — | — |
| TundishTemp1 | decimal | YES | 18,4 | — |
| MouldOilConsumption | decimal | YES | 18,4 | — |

---
