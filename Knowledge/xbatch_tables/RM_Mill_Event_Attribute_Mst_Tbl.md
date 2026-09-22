# XStudio_Xbatch.dbo.RM_Mill_Event_Attribute_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference attribute, name, tag, template, type.

**Primary Key:** ID  
**Row Count:** 3  

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
| TemplateID | varchar | YES | 36 | — |
| AttributeName | varchar | YES | 100 | — |
| TagType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6677AE14-EF0C-4BFC-A8BC-96C38F2A5A96 | NULL | 50BEF313-1A52-46B9-8D3D-583A923B47E0 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-10-30T13:18:08.0000000 | NULL | False | False | NULL |
| 35730406-ACEC-4F4E-955A-EBF75B281F5F | NULL | 50BEF313-1A52-46B9-8D3D-583A923B47E0 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-11-03T10:48:30.0000000 | NULL | False | False | NULL |
| 2ABD8392-F310-4624-8AB8-692A6513576B | NULL | 50BEF313-1A52-46B9-8D3D-583A923B47E0 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-10-30T13:19:19.0000000 | NULL | False | False | NULL |

---
