# XStudio_Xbatch.dbo.Procedure_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference area, duration, frequency, generation, limit, time, unit.

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
| AreaID | varchar | YES | 36 | — |
| DurationUnit | varchar | YES | 36 | — |
| FrequencyID | varchar | YES | 36 | — |
| GenerationTimeLimit | int | YES | 10,0 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Procedure_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Procedure_Steps_Mst_Tbl.ProcedureID` -> `XStudio_XBatch.Procedure_Mst_Tbl.ID` (Many to One)
