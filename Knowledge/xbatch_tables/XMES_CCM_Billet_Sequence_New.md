# XStudio_Xbatch.dbo.XMES_CCM_Billet_Sequence_New

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference sequence, strand, current, heat.

**Primary Key:** ID  
**Row Count:** 14,245  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| CurrentSequence | int | YES | 10,0 | — |
| StrandNo | varchar | YES | 100 | — |
| StrandSequence | int | YES | 10,0 | — |
| HeatNo | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002300D0-22D2-43A6-AE6B-96CF6843F46E | NULL | NULL | 2026-07-04T21:20:34.9900000 | NULL | False | False | NULL | NULL | NULL |
| 0020CDE8-E860-4F8C-89BF-827638399E4D | NULL | NULL | 2026-06-22T23:43:06.8300000 | NULL | False | False | NULL | NULL | NULL |
| 001D09EB-6FFF-42BE-87C5-EE9E42F27BB5 | NULL | NULL | 2026-06-27T16:26:00.8500000 | NULL | False | False | NULL | NULL | NULL |
| 0017D630-98DD-4592-A094-A60A21ACB6FB | NULL | NULL | 2026-06-30T16:24:58.8970000 | NULL | False | False | NULL | NULL | NULL |
| 001754E3-3BAA-4691-819B-6A65211F0F1C | NULL | NULL | 2026-06-26T19:10:54.8770000 | NULL | False | False | NULL | NULL | NULL |
| 000C0C50-FED9-424C-AF28-FD26A3C9121A | NULL | NULL | 2026-07-06T10:31:32.9600000 | NULL | False | False | NULL | NULL | NULL |
| 0007F2AE-AC05-421C-B39B-62DB927409D5 | NULL | NULL | 2026-07-08T18:57:28.6600000 | NULL | False | False | NULL | NULL | NULL |
| 000689D2-7581-4DE8-B365-6D94E48697CD | NULL | NULL | 2026-06-29T08:57:36.4000000 | NULL | False | False | NULL | NULL | NULL |
| 00067D96-147F-4C75-95B1-BFAEAC54F15E | NULL | NULL | 2026-06-30T13:35:14.0870000 | NULL | False | False | NULL | NULL | NULL |
| 0004FA7E-F1E9-4C14-BB3F-9BF1DCE54C79 | NULL | NULL | 2026-07-07T13:41:14.0700000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002300D0-22D2-43A6-AE6B-96CF6843F46E | NULL | NULL | 2026-07-04T21:20:34.9900000 | NULL | False | False | NULL | NULL | NULL |
| 0020CDE8-E860-4F8C-89BF-827638399E4D | NULL | NULL | 2026-06-22T23:43:06.8300000 | NULL | False | False | NULL | NULL | NULL |
| 001D09EB-6FFF-42BE-87C5-EE9E42F27BB5 | NULL | NULL | 2026-06-27T16:26:00.8500000 | NULL | False | False | NULL | NULL | NULL |
| 0017D630-98DD-4592-A094-A60A21ACB6FB | NULL | NULL | 2026-06-30T16:24:58.8970000 | NULL | False | False | NULL | NULL | NULL |
| 001754E3-3BAA-4691-819B-6A65211F0F1C | NULL | NULL | 2026-06-26T19:10:54.8770000 | NULL | False | False | NULL | NULL | NULL |
| 000C0C50-FED9-424C-AF28-FD26A3C9121A | NULL | NULL | 2026-07-06T10:31:32.9600000 | NULL | False | False | NULL | NULL | NULL |
| 0007F2AE-AC05-421C-B39B-62DB927409D5 | NULL | NULL | 2026-07-08T18:57:28.6600000 | NULL | False | False | NULL | NULL | NULL |
| 000689D2-7581-4DE8-B365-6D94E48697CD | NULL | NULL | 2026-06-29T08:57:36.4000000 | NULL | False | False | NULL | NULL | NULL |
| 00067D96-147F-4C75-95B1-BFAEAC54F15E | NULL | NULL | 2026-06-30T13:35:14.0870000 | NULL | False | False | NULL | NULL | NULL |
| 0004FA7E-F1E9-4C14-BB3F-9BF1DCE54C79 | NULL | NULL | 2026-07-07T13:41:14.0700000 | NULL | False | False | NULL | NULL | NULL |

---
