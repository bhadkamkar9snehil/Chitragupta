# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Event_Action_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, action, active, configuration, mode, type.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-09-08T18:15:22.0000000 to 2026-06-09T15:16:19.0000000  

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
| 1464CA61-38BA-46C4-A5C2-FA9946C8B0B4 | Delay Trigger | F2A00B44-251D-45AD-8FC9-9217F7FD8647 | E85231EB-0A04-42D6-A407-328F17EADEFE | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-16T16:48:40.0000000 | 2025-09-08T18:15:22.0000000 | False | False | NULL |
| 5CF35CA8-1BAB-462A-A400-6BA722C7A9A4 | Ready Contact Delay | F2A00B44-251D-45AD-8FC9-9217F7FD8647 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-10T16:46:23.0000000 | 2025-09-08T18:15:41.0000000 | False | False | NULL |
| 92B026CD-1FB1-4617-8C1D-39FEFA1EB531 | Furnace Ready Delay | F2A00B44-251D-45AD-8FC9-9217F7FD8647 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-10T16:46:53.0000000 | 2025-09-08T18:16:01.0000000 | False | False | NULL |
| CA365057-8C6D-46D0-B2E7-F28FCCB853EC | Capture Billet Weight | 2FAB31D6-55BE-45CC-A7E5-30B5D68A2CC9 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-10T10:22:21.0000000 | 2026-06-09T15:16:19.0000000 | True | False | NULL |

---
