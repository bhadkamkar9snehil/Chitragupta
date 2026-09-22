# XStudio_Xbatch.dbo.SMS_Delay_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** delay, entities, event, from, map, oee, procedure, sohar, stored, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, end, equipment, heat, start, workflow.

**Primary Key:** ID  
**Row Count:** 15,428  
**Date Range (ModifiedOn):** 2026-01-06T15:27:08.9400000 to 2026-08-10T09:48:25.6130000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| HeatNo | int | YES | 10,0 | — |
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
| WorkflowStatus | varchar | YES | 50 | — |

### Top 10 Records

| ID | HeatNo | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BA4AE34B-0383-45F0-A9F2-CB7AA7D71FBF | 1604015 | NULL | NULL | NULL | 2026-08-10T09:48:31.2070000 | NULL | False | False | NULL |
| 93BA5342-61CD-4BE2-988F-504151D0D402 | 1600141 | NULL | NULL |  | 2026-01-06T15:24:41.8770000 | 2026-01-06T15:27:08.9400000 | False | False | NULL |
| E3D7C4BC-31D8-4D37-92A0-1E163FC9236B | 1600141 | NULL | NULL |  | 2026-01-06T15:25:06.2570000 | 2026-01-06T15:27:24.8000000 | False | False | NULL |
| A6F3C2FD-0EF7-44B1-B441-104FCF3C9013 | 1600142 | NULL | NULL |  | 2026-01-06T15:28:34.7870000 | 2026-01-06T15:30:24.3130000 | False | False | NULL |
| 566CA707-7197-4079-A47C-5FEF5C5566A5 | 1600142 | NULL | NULL |  | 2026-01-06T15:28:34.8330000 | 2026-01-06T15:30:24.3730000 | False | False | NULL |
| 8C62E40B-5305-4F18-A4CD-CAF69CBA2678 | 1600142 | NULL | NULL |  | 2026-01-06T16:18:46.9500000 | 2026-01-06T16:20:57.9770000 | False | False | NULL |
| 7693EC7F-97ED-4D9B-850D-701B84DD5A2E | 1600142 | NULL | NULL |  | 2026-01-06T16:18:54.4530000 | 2026-01-06T16:21:07.6270000 | False | False | NULL |
| ED7B2D76-24BB-4C8E-AD19-7B576860B879 | 1600143 | NULL | NULL |  | 2026-01-06T16:22:57.8430000 | 2026-01-06T16:24:48.1500000 | False | False | NULL |
| 24A1B9EA-A519-479B-AD4E-31D31C0B9612 | 1600143 | NULL | NULL |  | 2026-01-06T16:22:57.8970000 | 2026-01-06T16:24:48.2000000 | False | False | NULL |
| 114FBBCB-70D3-4E9E-8986-225050E68C8D | 1600143 | NULL | NULL |  | 2026-01-06T17:11:35.3500000 | 2026-01-06T17:13:43.5730000 | False | False | NULL |

### Bottom 10 Records

| ID | HeatNo | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D0D29D51-D6BB-481C-B5EA-99397B430B84 | 1604015 | NULL | NULL |  | 2026-08-10T09:39:17.3300000 | 2026-08-10T09:48:25.6130000 | False | False | NULL |
| DB5BDB92-5690-4841-B4C8-47869182E8BA | 1604015 | NULL | NULL |  | 2026-08-09T11:28:08.1670000 | 2026-08-09T11:28:16.9170000 | False | False | NULL |
| 5D8D7206-67BF-4306-90B5-03EB518EE655 | 1604015 | NULL | NULL |  | 2026-08-09T11:24:32.7070000 | 2026-08-09T11:24:42.0070000 | False | False | NULL |
| 0BABCED7-DA8B-40B7-8C79-4C6E167C75E3 | 1604015 | NULL | NULL |  | 2026-08-09T11:22:14.8670000 | 2026-08-09T11:22:20.0770000 | False | False | NULL |
| 5C339612-273C-4ED7-8641-39EB347EEC2E | 1604015 | NULL | NULL |  | 2026-08-09T11:21:59.7000000 | 2026-08-09T11:22:11.1530000 | False | False | NULL |
| 66D021FE-497A-436B-99E8-48DEEFC3EB6A | 1604015 | NULL | NULL |  | 2026-08-04T17:23:14.8430000 | 2026-08-04T17:23:17.9430000 | False | False | NULL |
| AAF0ACA0-F77D-47CC-B751-4AEAD0889E07 | 1604015 | NULL | NULL |  | 2026-08-04T17:23:04.7300000 | 2026-08-04T17:23:09.9070000 | False | False | NULL |
| 943C33F5-D3B1-4026-A7DA-C2C3D0505E48 | 1604015 | NULL | NULL |  | 2026-08-04T17:11:26.8670000 | 2026-08-04T17:11:31.0070000 | False | False | NULL |
| 99EA14D3-050E-42B8-AFF4-07E8D80F9226 | 1604015 | NULL | NULL |  | 2026-08-04T17:10:42.0800000 | 2026-08-04T17:11:25.0400000 | False | False | NULL |
| 9A5ACFC0-1742-4192-951C-1899B1BBDECD | 1604015 | NULL | NULL |  | 2026-08-04T17:09:51.6570000 | 2026-08-04T17:09:57.8230000 | False | False | NULL |

---
