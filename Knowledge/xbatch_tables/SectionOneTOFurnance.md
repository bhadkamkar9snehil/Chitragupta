# XStudio_Xbatch.dbo.SectionOneTOFurnance

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, end, equipment, start, status.

**Primary Key:** ID  
**Row Count:** 40  
**Date Range (ModifiedOn):** 2026-06-06T09:33:10.4630000 to 2026-06-06T10:56:37.9200000  

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
| EquipmentID | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FB037EC7-7F89-46AF-88D1-E65EA51A66B7 | NULL | NULL | NULL | NULL | 2026-06-06T10:57:42.5170000 | NULL | False | False | NULL |
| B0450377-2160-4B84-8B7E-91C5DDA06FD2 | NULL | NULL | NULL | NULL | 2026-06-06T09:17:08.9970000 | 2026-06-06T09:33:10.4630000 | False | False | NULL |
| 246426D7-AC71-4ABF-8FD2-7844FCE64924 | NULL | NULL | NULL | NULL | 2026-06-06T09:33:26.6800000 | 2026-06-06T09:35:33.6870000 | False | False | NULL |
| 57D9C221-EC23-4A3A-8644-92829276922B | NULL | NULL | NULL | NULL | 2026-06-06T09:35:49.4000000 | 2026-06-06T09:37:57.5030000 | False | False | NULL |
| 841D0DF0-BEA8-4EB0-8E95-29ADA26D3490 | NULL | NULL | NULL | NULL | 2026-06-06T09:38:13.7170000 | 2026-06-06T09:40:22.3530000 | False | False | NULL |
| 121D04D8-F15E-4FDC-BD7B-76207E6A9764 | NULL | NULL | NULL | NULL | 2026-06-06T09:40:38.5730000 | 2026-06-06T09:43:00.0000000 | False | False | NULL |
| 2D990245-600D-4777-9E7F-D28D83D33C86 | NULL | NULL | NULL | NULL | 2026-06-06T09:43:00.3270000 | 2026-06-06T09:45:52.8130000 | False | False | NULL |
| 15D3021A-1D92-442A-A2B2-8C80A9B38806 | NULL | NULL | NULL | NULL | 2026-06-06T09:46:50.6530000 | 2026-06-06T09:47:33.6230000 | False | False | NULL |
| 15DBC7E0-58FA-4854-8457-3BEB482A7CC8 | NULL | NULL | NULL | NULL | 2026-06-06T09:47:49.6170000 | 2026-06-06T09:50:50.7670000 | False | False | NULL |
| 93C1420A-174B-49B3-A473-3C2023D9D957 | NULL | NULL | NULL | NULL | 2026-06-06T09:50:50.7800000 | 2026-06-06T09:52:17.2400000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D7DAB440-0BC6-47D4-852C-D3B5E75F717C | NULL | NULL | NULL | NULL | 2026-06-06T10:54:31.7030000 | 2026-06-06T10:56:37.9200000 | False | False | NULL |
| 3D064810-E964-4896-A9C9-9CEFC15EB8FD | NULL | NULL | NULL | NULL | 2026-06-06T10:52:07.5400000 | 2026-06-06T10:54:15.4500000 | False | False | NULL |
| 6866FE57-AB3A-4B1A-ADCC-AB4667A83EC0 | NULL | NULL | NULL | NULL | 2026-06-06T10:49:45.6400000 | 2026-06-06T10:51:51.8370000 | False | False | NULL |
| AE5B0EE3-017A-436C-8602-798EBE632789 | NULL | NULL | NULL | NULL | 2026-06-06T10:47:22.4700000 | 2026-06-06T10:49:28.8300000 | False | False | NULL |
| A011D6C9-E0D2-40DD-9BEF-3A0E67D7D3C7 | NULL | NULL | NULL | NULL | 2026-06-06T10:44:59.4430000 | 2026-06-06T10:47:06.7800000 | False | False | NULL |
| 47FC1910-85CB-4348-98F9-A893CEF11607 | NULL | NULL | NULL | NULL | 2026-06-06T10:42:35.7070000 | 2026-06-06T10:44:42.6070000 | False | False | NULL |
| 81A0EE5A-49FF-48F1-A711-C2B2C4E5CD03 | NULL | NULL | NULL | NULL | 2026-06-06T10:40:12.6530000 | 2026-06-06T10:42:19.4600000 | False | False | NULL |
| DDAC2033-EBE1-41B9-849C-245180744252 | NULL | NULL | NULL | NULL | 2026-06-06T10:37:48.3770000 | 2026-06-06T10:39:56.3130000 | False | False | NULL |
| 5A429D12-8AC4-4907-A719-5E78BE1F440E | NULL | NULL | NULL | NULL | 2026-06-06T10:35:25.3870000 | 2026-06-06T10:37:31.5930000 | False | False | NULL |
| 70762D59-B0CA-4563-9E78-F9BDFE61A922 | NULL | NULL | NULL | NULL | 2026-06-06T10:33:05.5730000 | 2026-06-06T10:35:09.6800000 | False | False | NULL |

---
