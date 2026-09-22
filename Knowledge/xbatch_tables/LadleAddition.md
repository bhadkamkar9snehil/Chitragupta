# XStudio_Xbatch.dbo.LadleAddition

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** data, eaf, flow, heat, insert, per (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference silo, time, end, equipment, heat, start, status.

**Primary Key:** ID  
**Row Count:** 5,703  
**Date Range (ModifiedOn):** 2025-09-22T16:34:58.7470000 to 2026-07-08T17:53:52.6400000  

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
| Silo3KG | decimal | YES | 18,4 | — |
| Silo4KG | decimal | YES | 18,4 | — |
| Silo5KG | decimal | YES | 18,4 | — |
| Silo6KG | decimal | YES | 18,4 | — |
| Silo7KG | decimal | YES | 18,4 | — |
| Silo8KG | decimal | YES | 18,4 | — |
| HeatNo | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A37F90BD-F9B9-4474-B2D1-4ECC360C43F3 | NULL | NULL | NULL | NULL | 2025-09-22T16:34:30.8000000 | 2025-09-22T16:34:58.7470000 | False | False | NULL |
| A5EF4009-EB8B-466D-A813-FA7ED4696432 | NULL | NULL | NULL | NULL | 2025-09-22T17:58:17.7930000 | 2025-09-22T17:59:57.9600000 | False | False | NULL |
| 0EA89D9B-EA7C-4741-8141-0FDEA6AC698D | NULL | NULL | NULL | NULL | 2025-09-22T19:05:18.2100000 | 2025-09-22T19:05:49.2000000 | False | False | NULL |
| AD92E430-97E9-44F7-A36B-D3428375F736 | NULL | NULL | NULL | NULL | 2025-09-22T20:00:47.1500000 | 2025-09-22T20:01:20.7170000 | False | False | NULL |
| BC487F25-14B2-4881-ADB8-C7636D303EFA | NULL | NULL | NULL | NULL | 2025-09-22T21:00:48.9400000 | 2025-09-22T21:01:19.9600000 | False | False | NULL |
| 4E95AD49-8251-4980-A358-7371369D331B | NULL | NULL | NULL | NULL | 2025-09-22T21:55:48.7800000 | 2025-09-22T21:56:22.8670000 | False | False | NULL |
| EFDF2A64-AD66-4F39-8FEA-92B4256384AB | NULL | NULL | NULL | NULL | 2025-09-22T22:53:30.7800000 | 2025-09-22T22:54:11.9870000 | False | False | NULL |
| 0BDC8FF5-9860-46C7-9569-B5CEAAA4DFC6 | NULL | NULL | NULL | NULL | 2025-09-22T23:48:43.0770000 | 2025-09-22T23:49:16.1170000 | False | False | NULL |
| 9A2837BA-0D32-4E00-8C9B-BFEBE19B9814 | NULL | NULL | NULL | NULL | 2025-09-23T00:36:58.9900000 | 2025-09-23T00:37:33.0730000 | False | False | NULL |
| 9EB09BE2-D8B2-4E12-87C6-75DA311A9C09 | NULL | NULL | NULL | NULL | 2025-09-23T01:35:08.0470000 | 2025-09-23T01:36:08.0600000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 65846582-E5C8-4AA9-9C77-379C17C17B4E | NULL | NULL | NULL | NULL | 2026-07-08T17:53:12.9000000 | 2026-07-08T17:53:52.6400000 | False | False | NULL |
| 5664E74C-DF2B-406B-B2AE-998189F66E4C | NULL | NULL | NULL | NULL | 2026-07-08T16:55:31.8470000 | 2026-07-08T16:56:47.6170000 | False | False | NULL |
| 8BBC215E-1C08-48F1-BF74-5798CAE79742 | NULL | NULL | NULL | NULL | 2026-07-08T15:53:52.7670000 | 2026-07-08T15:54:47.6700000 | False | False | NULL |
| 973D3A9A-D42D-4D14-BB52-18E252E605E5 | NULL | NULL | NULL | NULL | 2026-07-08T14:50:08.9100000 | 2026-07-08T14:50:39.4400000 | False | False | NULL |
| 173113AF-9352-4F59-88A5-FAF0BE69F866 | NULL | NULL | NULL | NULL | 2026-07-08T13:52:30.4570000 | 2026-07-08T13:53:09.6200000 | False | False | NULL |
| 975C433F-D34C-4D7B-A9B7-EDFD8F26122A | NULL | NULL | NULL | NULL | 2026-07-08T12:52:31.8130000 | 2026-07-08T12:53:37.7870000 | False | False | NULL |
| FF4CCCB6-387C-4C08-9970-56BA3AAE5AA5 | NULL | NULL | NULL | NULL | 2026-07-08T11:46:38.6700000 | 2026-07-08T11:47:04.5270000 | False | False | NULL |
| 168302C1-F4E4-4BE6-A936-7CB9E803F817 | NULL | NULL | NULL | NULL | 2026-07-08T10:40:38.7770000 | 2026-07-08T10:41:21.4570000 | False | False | NULL |
| 8CDE34C2-E1CB-4B02-AB2F-2F68F136CC80 | NULL | NULL | NULL | NULL | 2026-07-08T09:45:27.6230000 | 2026-07-08T09:46:10.8400000 | False | False | NULL |
| 48AAF551-8E61-4D44-9117-AD66BF80CFFB | NULL | NULL | NULL | NULL | 2026-07-08T08:46:41.7730000 | 2026-07-08T08:47:39.7570000 | False | False | NULL |

---
