# XStudio_Xbatch.dbo.RM_Water_Box_Setting_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference bar, block, pressure, temperature, box, coldms, entry, exit, flowm, grade, inlet, lhtemperature.

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
| Size | decimal | YES | 18,4 | — |
| Speed | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 100 | — |
| WaterBoxNo | int | YES | 10,0 | — |
| Flowm3Perhour | decimal | YES | 18,4 | — |
| InletPressureBar | decimal | YES | 18,4 | — |
| OutletPressureBar | decimal | YES | 18,4 | — |
| BlockTemperatureEntry | decimal | YES | 18,4 | — |
| BlockTemperatureExit | decimal | YES | 18,4 | — |
| NonColdms | int | YES | 10,0 | — |
| LHTemperature | decimal | YES | 18,4 | — |
| Remarks | varchar | YES | 100 | — |

---
