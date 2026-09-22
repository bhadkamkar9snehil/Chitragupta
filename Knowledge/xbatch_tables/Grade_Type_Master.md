# XStudio_Xbatch.dbo.Grade_Type_Master

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference grade, type.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-12-12T08:14:30.0000000 to 2026-06-10T11:29:01.0000000  

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
| GradeType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7CA40AAC-BE69-4ACD-812D-6CFCD4F0D8A8 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-12T08:14:30.5270000 | 2025-12-12T08:14:30.0000000 | False | False | NULL |
| 475A4FF7-9ECE-4BFF-A4E0-6A50AF966402 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-12T08:14:51.7500000 | 2025-12-12T08:14:51.0000000 | False | False | NULL |
| 70A8CDFA-5D5C-4D13-A162-24BDC74772CC | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2025-12-12T08:14:42.9100000 | 2026-03-15T16:57:20.0000000 | False | False | NULL |
| 09E8D044-2319-4E06-83FC-F922A3D7E4E2 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-12T08:14:18.6700000 | 2026-06-10T11:29:01.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Grade_Master.GradeType` -> `XStudio_XBatch.Grade_Type_Master.GradeType` (Many to One)
