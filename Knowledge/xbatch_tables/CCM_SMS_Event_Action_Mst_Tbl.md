# XStudio_Xbatch.dbo.CCM_SMS_Event_Action_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, action, active, configuration, mode, type.

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2025-09-02T17:46:45.0000000 to 2026-06-10T08:44:19.0000000  

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
| D18194D3-0433-47FE-A7F3-130A47A628B5 | HeatNo | 461E3E14-FFA5-4A32-BCFD-C797F990A9AF | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-02T17:46:45.2300000 | 2025-09-02T17:46:45.0000000 | False | False | NULL |
| F6C345F2-0B36-469E-BDBD-74E7EBCF0D9E | Capture HeatNo | 461E3E14-FFA5-4A32-BCFD-C797F990A9AF | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-02T17:47:26.2070000 | 2025-09-02T17:47:26.0000000 | False | False | NULL |
| 3E5D417C-1B75-4EEF-BA2B-D37FA8C6CE1E | Capture Total Billets | 9CF8771A-53FB-44FA-A922-9034930FF13A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-10T09:26:13.0000000 | 2026-06-10T08:42:38.0000000 | False | False | NULL |
| 58B64386-1433-4D49-8C60-050EAB067564 | Capture Total Billets | 9CF8771A-53FB-44FA-A922-9034930FF13A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-10T09:21:24.0000000 | 2026-06-10T08:43:02.0000000 | False | False | NULL |
| 465C6ACC-3A57-4F98-9AED-7C150CFE4147 | Capture Total Billets | 9CF8771A-53FB-44FA-A922-9034930FF13A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-10T09:21:46.0000000 | 2026-06-10T08:43:20.0000000 | False | False | NULL |
| F615DD74-548B-486D-B70D-1579089A8ED8 | Capture Total Billets | 9CF8771A-53FB-44FA-A922-9034930FF13A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-10T09:22:16.0000000 | 2026-06-10T08:43:38.0000000 | False | False | NULL |
| 94E0751B-DFF2-4103-9DD3-1B14154E88CC | Capture Total Billets | 9CF8771A-53FB-44FA-A922-9034930FF13A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-10T09:22:43.0000000 | 2026-06-10T08:43:59.0000000 | False | False | NULL |
| 680B5948-FD9A-4F13-A127-2BF53BBDF22D | Capture Total Billets | 9CF8771A-53FB-44FA-A922-9034930FF13A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-10T09:23:12.0000000 | 2026-06-10T08:44:19.0000000 | False | False | NULL |

---
