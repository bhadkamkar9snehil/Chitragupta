# XStudio_Xbatch.dbo.RM_Billet_Charging_And_Discharging_Logsheet

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, cold, discharged, grade, heat, hot, length, meters, remarks, shift, size, sizemm.

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
| Shift | varchar | YES | 100 | — |
| Size | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| SlNo | int | YES | 10,0 | — |
| HeatNo | int | YES | 10,0 | — |
| BilletNo | int | YES | 10,0 | — |
| TypeOfBilletHotOrCold | bit | YES | — | — |
| BilletSizemm | decimal | YES | 18,4 | — |
| BilletLengthMeters | decimal | YES | 18,4 | — |
| BilletDischargedTime | time | YES | — | — |
| Remarks | varchar | YES | 100 | — |

---
