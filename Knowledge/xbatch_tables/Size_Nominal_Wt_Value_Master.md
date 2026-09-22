# XStudio_Xbatch.dbo.Size_Nominal_Wt_Value_Master

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference cross, nominal, product, section, size, value.

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2026-01-13T12:59:27.0000000 to 2026-01-13T13:00:00.0000000  

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
| Size | int | YES | 10,0 | — |
| NominalWtValue | decimal | YES | 18,4 | — |
| CrossSection | decimal | YES | 18,4 | — |
| Product | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 042C9249-800D-4DB3-83B9-56A1339D7C99 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:30:08.5530000 | 2026-01-13T12:59:27.0000000 | False | False | NULL |
| 47E2BEEB-3C0A-4C60-9092-860593EC5F40 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:32:35.2770000 | 2026-01-13T12:59:27.0000000 | False | False | NULL |
| C516F53B-D13F-400E-AB7A-B08F7ED69A75 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:31:40.5330000 | 2026-01-13T12:59:27.0000000 | False | False | NULL |
| 96AC2796-5D7F-431A-928B-9F6892786E65 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:29:30.7970000 | 2026-01-13T12:59:27.0000000 | False | False | NULL |
| FEA8B71E-F2AF-4084-88A0-F2C46DA735B7 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:33:15.3830000 | 2026-01-13T12:59:59.0000000 | False | False | NULL |
| EED91D29-302A-4D50-BA9E-44F1D8EDE751 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:37:55.1170000 | 2026-01-13T13:00:00.0000000 | False | False | NULL |
| 79E342D9-EA6E-4B26-AFA3-D9E3C25A8BBC | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:37:20.6700000 | 2026-01-13T13:00:00.0000000 | False | False | NULL |
| 2DC0ABBF-9477-4C4A-A51E-DC07D05D0DDE | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:36:33.1170000 | 2026-01-13T13:00:00.0000000 | False | False | NULL |
| 007D94FB-4188-4C06-9EE3-50CEB1E4FDBC | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-12T09:38:22.7600000 | 2026-01-13T13:00:00.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Quality_Deviation_Master.Size` -> `XStudio_XBatch.Size_Nominal_Wt_Value_Master.ID` (Many to One)
- `XStudio_XBatch.Size_Nominal_Wt_Value_Master.Product` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
