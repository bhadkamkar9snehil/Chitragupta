# XStudio_Xbatch.dbo.RM_Shift_Producation_Report

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, delay, action, cause, code, corrective, duration, from, grade, misroll, nature, production.

**Primary Key:** ID  
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
| Size | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| ProductionTime | time | YES | — | — |
| TimeFrom | time | YES | — | — |
| TimeTo | time | YES | — | — |
| TimeDuration | decimal | YES | 18,4 | — |
| DelayCode | varchar | YES | 100 | — |
| Misroll | varchar | YES | 100 | — |
| NatureOfDelay | varchar | YES | 100 | — |
| RootCause | varchar | YES | 100 | — |
| CorrectiveAction | varchar | YES | 100 | — |
| Remarks | varchar | YES | -1 | — |

---
