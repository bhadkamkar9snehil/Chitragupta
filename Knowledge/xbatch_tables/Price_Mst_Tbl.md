# XStudio_Xbatch.dbo.Price_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference unit, date, effective, item, measurement, price, remarks, type, usd.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-11-17T15:59:13.0000000 to 2025-11-17T15:59:13.0000000  

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
| ItemType | varchar | YES | 100 | — |
| UnitOfMeasurement | varchar | YES | 100 | — |
| UnitPriceUSD | decimal | YES | 18,4 | — |
| EffectiveDate | datetime | YES | — | — |
| Remarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CB96723B-A609-4DD8-9BBD-8E9C0E83EAD8 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-17T13:44:11.0400000 | 2025-11-17T15:59:13.0000000 | False | False | NULL |

---
