# XStudio_Xbatch.dbo.Product_Master

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference name, short.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2026-01-13T10:57:07.0000000 to 2026-08-14T15:30:56.0000000  

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
| ShortName | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 789D978B-7EAC-4D64-A39F-F3E423699D7F | Round Bar | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-13T10:57:07.4970000 | 2026-01-13T10:57:07.0000000 | False | False | NULL |
| 9603C554-4B0F-401F-AA30-E93E2CCB2F05 | Rebar | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-13T10:56:34.1900000 | 2026-08-14T15:30:47.0000000 | False | False | NULL |
| 8DD3AEC9-378F-4320-BF02-B061CE7FFF7C | Rebar in Coil | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-13T10:56:52.6930000 | 2026-08-14T15:30:52.0000000 | False | False | NULL |
| 50CE5468-A131-4306-B93A-29BCF0FAE0FE | WRM | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-13T10:56:42.2400000 | 2026-08-14T15:30:56.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Product_Master.Name` -> `XStudio_XBatch.XMES_Billet_Strand_tracking.EndProduct` (One to Many)
- `XStudio_XBatch.Quality_Deviation_Master.Product` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.Size_Nominal_Wt_Value_Master.Product` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_Strand_tracking.EndProduct` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_Campaign_Plan_Mst.Productname` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Heated_Billet_trn_tbl.ProductType` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Tag_Printing_MST.Product` -> `XStudio_XBatch.Product_Master.Name` (Many to One)
- `XStudio_XBatch.XMES_RM_Tag_Printing_TRN.Product` -> `XStudio_XBatch.Product_Master.Name` (Many to One)
