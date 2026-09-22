# XStudio_Xbatch.dbo.sysdiagrams

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference definition, diagram, principal, version.

**Primary Key:** diagram_id  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| name | nvarchar | NO | 128 | — |
| principal_id | int | NO | 10,0 | — |
| diagram_id | int | NO | 10,0 | — |
| version | int | YES | 10,0 | — |
| definition | varbinary | YES | -1 | — |

---
