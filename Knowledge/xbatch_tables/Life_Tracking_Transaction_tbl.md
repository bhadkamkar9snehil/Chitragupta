# XStudio_Xbatch.dbo.Life_Tracking_Transaction_tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billets, cast, catalog, count, data, entities, entity, flow, from, highlights, insert, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference life, percentage, alert, consume, current, heat, remarks, type.

**Primary Key:** ID  
**Row Count:** 66,316  
**Date Range (ModifiedOn):** 2025-11-25T08:45:18.0000000 to 2025-11-25T08:45:18.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| HeatID | varchar | YES | 100 | — |
| Life | varchar | YES | 100 | — |
| LifeType | varchar | YES | 100 | — |
| CurrentLife | int | YES | 10,0 | — |
| ConsumePercentage | decimal | YES | 18,4 | — |
| AlertPercentage | varchar | YES | 100 | — |
| Remarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000C562F-75D8-4A0B-A2DC-D5FDBAAD951B | NULL | NULL | NULL | NULL | 2025-11-27T00:37:44.3000000 | NULL | False | False | NULL |
| 000AF6C1-7E63-412F-A8BF-34B149E59FF0 | NULL | NULL | NULL | NULL | 2026-04-21T11:46:17.3970000 | NULL | False | False | NULL |
| 0008D44C-2F14-48E5-99DE-662F26D4C11C | NULL | NULL | NULL | NULL | 2026-01-10T23:58:36.0100000 | NULL | False | False | NULL |
| 00073209-D539-4A9E-9CCF-D509A73B81D7 | NULL | NULL | NULL | NULL | 2026-02-22T22:52:00.2770000 | NULL | False | False | NULL |
| 0006386D-2D58-4CF3-8C46-5CF3FFE586DE | NULL | NULL | NULL | NULL | 2025-12-03T02:48:46.0100000 | NULL | False | False | NULL |
| 000507AD-0B71-4B22-8983-E9339BD64A02 | NULL | NULL | NULL | NULL | 2026-02-22T21:15:58.9900000 | NULL | False | False | NULL |
| 0002C428-9C8B-4060-A14E-D29A9111D9A2 | NULL | NULL | NULL | NULL | 2026-02-06T11:31:08.1000000 | NULL | False | False | NULL |
| 0002B660-1D6D-4080-B57F-DB90823D6982 | NULL | NULL | NULL | NULL | 2026-05-21T00:53:32.9430000 | NULL | False | False | NULL |
| 00025543-C4A2-4B24-9F64-1FBC5E64E466 | NULL | NULL | NULL | NULL | 2026-03-12T14:14:48.2100000 | NULL | False | False | NULL |
| 0001C0E8-19E6-4C8F-B4FB-F2C2806DF604 | NULL | NULL | NULL | NULL | 2026-01-11T06:37:15.6070000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C360CB75-D9A6-497C-8CD2-0E167835ED6E | EAF Porous Plug Life	 | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-25T08:45:18.6670000 | 2025-11-25T08:45:18.0000000 | False | False | NULL |
| 000C562F-75D8-4A0B-A2DC-D5FDBAAD951B | NULL | NULL | NULL | NULL | 2025-11-27T00:37:44.3000000 | NULL | False | False | NULL |
| 000AF6C1-7E63-412F-A8BF-34B149E59FF0 | NULL | NULL | NULL | NULL | 2026-04-21T11:46:17.3970000 | NULL | False | False | NULL |
| 0008D44C-2F14-48E5-99DE-662F26D4C11C | NULL | NULL | NULL | NULL | 2026-01-10T23:58:36.0100000 | NULL | False | False | NULL |
| 00073209-D539-4A9E-9CCF-D509A73B81D7 | NULL | NULL | NULL | NULL | 2026-02-22T22:52:00.2770000 | NULL | False | False | NULL |
| 0006386D-2D58-4CF3-8C46-5CF3FFE586DE | NULL | NULL | NULL | NULL | 2025-12-03T02:48:46.0100000 | NULL | False | False | NULL |
| 000507AD-0B71-4B22-8983-E9339BD64A02 | NULL | NULL | NULL | NULL | 2026-02-22T21:15:58.9900000 | NULL | False | False | NULL |
| 0002C428-9C8B-4060-A14E-D29A9111D9A2 | NULL | NULL | NULL | NULL | 2026-02-06T11:31:08.1000000 | NULL | False | False | NULL |
| 0002B660-1D6D-4080-B57F-DB90823D6982 | NULL | NULL | NULL | NULL | 2026-05-21T00:53:32.9430000 | NULL | False | False | NULL |
| 00025543-C4A2-4B24-9F64-1FBC5E64E466 | NULL | NULL | NULL | NULL | 2026-03-12T14:14:48.2100000 | NULL | False | False | NULL |

---
