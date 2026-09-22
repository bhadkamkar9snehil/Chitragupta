# XStudio_Xbatch.dbo.RM_WRM_Event_Attribute_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference attribute, name, tag, template, type.

**Primary Key:** ID  
**Row Count:** 4  

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
| D96BC660-9493-4C8D-B5C9-37FC04665A9C | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | NULL | 2026-07-06T08:06:07.0000000 | NULL | False | False | NULL |
| B2866EF8-1E88-4CD0-BA6A-73287EB54135 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | NULL | 2026-07-03T09:09:44.0000000 | NULL | False | False | NULL |
| A3E2B4B5-0834-4C81-A2C1-2AF979F58971 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | NULL | 2026-07-03T09:14:31.0000000 | NULL | False | False | NULL |
| 435E2F20-746C-4B04-B83C-FBABF5AD2DF0 | NULL | F1EFFCB7-3F87-4DA7-9DF5-19D505CB76D3 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | NULL | 2026-07-06T08:04:02.0000000 | NULL | True | False | NULL |

---
