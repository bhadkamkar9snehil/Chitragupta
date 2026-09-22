# XStudio_Xbatch.dbo.CCM_Event_Action_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, action, active, configuration, mode, type.

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-07-11T17:36:02.0000000 to 2026-05-30T12:57:20.0000000  

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
| StateID | varchar | YES | 36 | — |
| Configuration | varchar | YES | -1 | — |
| ActionType | varchar | YES | 100 | — |
| StateMode | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DDE9B798-6520-4481-8E4A-0B538E28FAAE | ADD Data | E31469BE-E764-490D-BFA7-8E4BAE685886 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-11T18:09:08.0000000 | 2025-07-11T17:36:02.0000000 | False | False | NULL |
| 0A36D500-88E1-4E19-9013-01722851B277 | Arm 1 Cast Position | C7CA0D68-DDA9-41B0-A369-1B99FFBD4FCA | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-06-17T16:32:41.0000000 | 2025-08-21T21:14:58.0000000 | False | False | NULL |
| 307A561C-428F-4E92-8A47-F11FCCF12516 | Arm 2 Cast Position | C7CA0D68-DDA9-41B0-A369-1B99FFBD4FCA | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-06-17T16:32:54.0000000 | 2025-08-21T21:17:29.0000000 | False | False | NULL |
| 408845CA-EE4D-4EA7-89E6-FD8D222C63AB | Billets Produces Start | 662EFDDE-A612-4D27-A21B-560B0896A616 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-04T15:39:38.0000000 | 2025-08-21T21:44:49.0000000 | False | False | NULL |
| F0D00540-9A47-4108-93D4-FB6B2BFB7447 | Actual Billets Count | 662EFDDE-A612-4D27-A21B-560B0896A616 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T12:57:20.2530000 | 2026-05-30T12:57:20.0000000 | False | False | NULL |

---
