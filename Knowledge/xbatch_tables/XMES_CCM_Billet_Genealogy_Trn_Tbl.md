# XStudio_Xbatch.dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, inventory, yard (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, cut, produced, billet, end, event, sequence, start, strand, charge, heat, status.

**Primary Key:** ID  
**Row Count:** 14,245  
**Date Range (ModifiedOn):** 2026-06-19T17:58:13.5830000 to 2026-08-10T15:38:28.5400000  

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
| CutEventID | varchar | YES | 36 | — |
| Status | varchar | YES | 50 | — |
| ChargeType | varchar | YES | 100 | — |
| StrandSequence | int | YES | 10,0 | — |
| IsProcessed | bit | YES | — | — |
| StrandNo | varchar | YES | 100 | — |
| BilletSequence | int | YES | 10,0 | — |
| HeatNo | varchar | YES | 100 | — |
| BilletNo | varchar | YES | 100 | — |
| CutStartTime | datetime | YES | — | — |
| CutEndTime | datetime | YES | — | — |
| ProducedStartTime | datetime | YES | — | — |
| ProducedEndTime | datetime | YES | — | — |
| ProducedEventID | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 007BF781-CD15-45A6-BA77-072BCF962F47 | NULL | NULL | 2026-06-23T06:36:47.8630000 | NULL | False | False | NULL | NULL | NULL |
| 00D212ED-46A9-4F4D-B0BA-39EFAC2BF7BA | NULL | NULL | 2026-06-29T14:13:55.9670000 | NULL | False | False | NULL | NULL | NULL |
| 00D2539F-C759-43B7-9B4E-F09A60FF64C5 | NULL | NULL | 2026-06-30T08:15:00.3130000 | NULL | False | False | NULL | NULL | NULL |
| 0112C4F2-001B-4A0B-AB9F-A5F693EC0DDD | NULL | NULL | 2026-06-28T15:33:29.1970000 | NULL | False | False | NULL | NULL | NULL |
| 01EEA28F-8BCA-428F-8B17-36CEBE1E669A | NULL | NULL | 2026-06-19T17:42:53.6430000 | NULL | False | False | NULL | NULL | NULL |
| 02821399-B31F-484A-933E-1B8A2D73E940 | NULL | NULL | 2026-06-25T19:39:26.0400000 | NULL | False | False | NULL | NULL | NULL |
| 02C8CDAA-339F-4888-BBA1-A1D942157F03 | NULL | NULL | 2026-07-01T14:42:52.1530000 | NULL | False | False | NULL | NULL | NULL |
| 02EE11C3-70AE-41A6-B186-C37D951B81A8 | NULL | NULL | 2026-07-01T10:18:17.4730000 | NULL | False | False | NULL | NULL | NULL |
| 03253B85-CE31-4058-A374-0EF17BD15503 | NULL | NULL | 2026-06-25T20:29:22.2400000 | NULL | False | False | NULL | NULL | NULL |
| 03275329-6516-4D6D-8A9B-379733BB723A | NULL | NULL | 2026-07-08T14:17:05.5130000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FE671801-D6D9-43FD-9727-54525B2E769D | NULL | T-SQL | 2026-07-08T19:50:47.9200000 | 2026-08-10T15:38:28.5400000 | False | False | NULL | NULL | NULL |
| 83C8A7E2-D71F-48D5-BFE9-93383E9EA110 | NULL | T-SQL | 2026-07-08T19:50:53.4470000 | 2026-08-10T15:38:28.2400000 | False | False | NULL | NULL | NULL |
| C6323E67-8DDB-424F-942E-C31B3D8E87CC | NULL | T-SQL | 2026-07-08T19:48:50.8500000 | 2026-08-10T14:56:07.1230000 | False | False | NULL | NULL | NULL |
| 31574D82-0A1C-4CB1-9292-A86D1D58603F | NULL | T-SQL | 2026-07-08T19:49:26.4970000 | 2026-08-10T14:56:06.8500000 | False | False | NULL | NULL | NULL |
| 7D72D2C2-B010-42EA-987F-4398F132DCDC | NULL | T-SQL | 2026-07-08T19:14:38.2500000 | 2026-07-08T19:15:33.7670000 | False | False | NULL | NULL | NULL |
| A3ED39D6-8C6D-4232-A31B-B128DB6CA614 | NULL | T-SQL | 2026-07-08T19:11:40.5970000 | 2026-07-08T19:12:08.1030000 | False | False | NULL | NULL | NULL |
| E5A4E1EE-1430-4E8C-B6C4-5C888AF126EA | NULL | T-SQL | 2026-07-08T19:09:07.9300000 | 2026-07-08T19:09:54.7870000 | False | False | NULL | NULL | NULL |
| 301AAF92-F3B5-4D7D-B908-664722113594 | NULL | T-SQL | 2026-07-08T19:07:11.9600000 | 2026-07-08T19:07:45.0900000 | False | False | NULL | NULL | NULL |
| E317D8DC-C9D2-41F0-9314-E5EF29FEF0B0 | NULL | T-SQL | 2026-07-08T19:06:58.7770000 | 2026-07-08T19:07:21.6530000 | False | False | NULL | NULL | NULL |
| EC76951F-4ABC-40D1-A1B7-75757311C8A7 | NULL | T-SQL | 2026-07-08T19:03:18.0600000 | 2026-07-08T19:03:50.1030000 | False | False | NULL | NULL | NULL |

---
