# XStudio_Xbatch.dbo.RM_Delays

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** delay, oee (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, end, equipment, flow, start, work.

**Primary Key:** ID  
**Row Count:** 50,526  
**Date Range (ModifiedOn):** 2025-09-09T08:18:37.1930000 to 2026-08-30T15:47:21.3530000  

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
| WorkFlowStatus | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19BCF433-9524-4E2D-96CE-779D9427A6BF | NULL | NULL | NULL | NULL | 2025-09-16T16:44:04.4170000 | NULL | False | False | NULL |
| 24E6D1CA-0547-4C68-B1A8-42773B74F11B | NULL | NULL | NULL | NULL | 2026-08-29T10:27:06.9830000 | NULL | False | False | NULL |
| A659F79C-7662-46EC-B83F-60CFB7680BFE | NULL | NULL | NULL | NULL | 2025-09-16T16:43:14.3100000 | NULL | False | False | NULL |
| BAF8C3CA-9933-421B-989C-28B04F13A39A | NULL | NULL | NULL | NULL | 2025-11-03T14:13:15.1800000 | NULL | False | False | NULL |
| D6CC9A39-98B7-4DDC-BD8F-6150BEB66D4F | NULL | NULL | NULL | NULL | 2025-10-30T13:32:27.6770000 | NULL | False | False | NULL |
| E2D7EC63-9963-43B6-A5C8-B530CAE2ACCF | NULL | NULL | NULL | NULL | 2026-08-27T06:59:53.7430000 | NULL | False | False | NULL |
| 974BDC5B-E938-47EE-8CD7-A942BCFB0F0A | NULL | NULL | NULL | NULL | 2025-09-09T08:18:11.1030000 | 2025-09-09T08:18:37.1930000 | False | False | NULL |
| F2B14205-F49F-402B-9F07-AC7B5D36E3FE | NULL | NULL | NULL | NULL | 2025-09-09T08:18:53.9600000 | 2025-09-09T08:19:18.0470000 | False | False | NULL |
| BE09EFD0-4170-40F9-921E-BC45A04068A7 | NULL | NULL | NULL | NULL | 2025-09-09T08:19:58.1470000 | 2025-09-09T08:21:02.0800000 | False | False | NULL |
| 2E56D1F8-A811-46B3-9016-2313BDD1EF53 | NULL | NULL | NULL | NULL | 2025-09-09T08:21:18.8730000 | 2025-09-09T08:21:42.9700000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D5C16CAE-E604-46D4-BF32-C88F521AA132 | NULL | NULL | NULL | NULL | 2026-08-30T15:47:20.2330000 | 2026-08-30T15:47:21.3530000 | False | False | NULL |
| BA7EA8BA-1C20-4565-B44C-1F2DB8DDF8AF | NULL | NULL | NULL | NULL | 2026-08-29T19:55:53.7700000 | 2026-08-30T09:54:51.7470000 | False | False | NULL |
| 71772E6F-BAD5-4241-A44B-0522AF43BB7C | NULL | NULL | NULL | NULL | 2026-08-29T19:55:08.7800000 | 2026-08-29T19:55:16.0870000 | False | False | NULL |
| E2B86FF6-99A6-4D09-A5E7-AE5079EFABD2 | NULL | NULL | NULL | NULL | 2026-08-29T19:54:42.9800000 | 2026-08-29T19:54:51.9330000 | False | False | NULL |
| 098A1F84-B9D8-43B2-A784-0D01DF66E4AF | NULL | NULL | NULL | NULL | 2026-08-29T19:54:09.2770000 | 2026-08-29T19:54:28.9430000 | False | False | NULL |
| 699D3E6C-E9FD-4188-9142-908E804B66C4 | NULL | NULL | NULL | NULL | 2026-08-29T19:53:55.7970000 | 2026-08-29T19:54:04.2170000 | False | False | NULL |
| 6F7EC214-5488-448B-B018-392B69A23B21 | NULL | NULL | NULL | NULL | 2026-08-29T19:52:48.0400000 | 2026-08-29T19:53:02.0630000 | False | False | NULL |
| EC5D4642-1FD3-450D-A63B-D7841009C017 | NULL | NULL | NULL | NULL | 2026-08-29T19:48:57.9630000 | 2026-08-29T19:50:10.9530000 | False | False | NULL |
| 2D1F8CE3-18D9-453A-852C-42AEC1096314 | NULL | NULL | NULL | NULL | 2026-08-29T19:48:33.2700000 | 2026-08-29T19:48:41.1230000 | False | False | NULL |
| 17549B14-937C-4E68-B3E9-B0F97123EB13 | NULL | NULL | NULL | NULL | 2026-08-29T19:47:14.1330000 | 2026-08-29T19:47:25.8970000 | False | False | NULL |

---
