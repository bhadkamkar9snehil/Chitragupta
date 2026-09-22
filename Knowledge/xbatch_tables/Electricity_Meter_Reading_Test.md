# XStudio_Xbatch.dbo.Electricity_Meter_Reading_Test

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference consumption, date, end, feeder, month, name, number, position, price, quality, status, time.

**Primary Key:** ID  
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
| Price | varchar | YES | 100 | — |
| EndDateTime | datetime | YES | — | — |
| Consumption | decimal | YES | 18,4 | — |
| Quality | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |
| MonthNumber | int | YES | 10,0 | — |
| Status | varchar | YES | 50 | — |
| Value | decimal | YES | 18,4 | — |
| FeederName | varchar | YES | 100 | — |
| Position | int | YES | 10,0 | — |

---
