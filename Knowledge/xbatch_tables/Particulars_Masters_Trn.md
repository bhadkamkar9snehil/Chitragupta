# XStudio_Xbatch.dbo.Particulars_Masters_Trn

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference particulars, target, type, uom.

**Primary Key:** ID  
**Row Count:** 736  
**Date Range (ModifiedOn):** 2025-10-10T14:37:22.0000000 to 2025-12-04T09:34:40.0000000  

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
| SrNo | int | YES | 10,0 | — |
| Name | varchar | YES | 100 | — |
| Particulars | varchar | YES | 100 | — |
| Type | varchar | YES | 100 | — |
| UOM | varchar | YES | 100 | — |
| ReportDate | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Target | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03F1B137-C558-4142-8CA4-6C169476165F | NULL | NULL | 2026-04-01T09:10:00.2600000 | NULL | False | False | NULL | NULL | NULL |
| 03E8C600-1ACA-4392-91E5-920F3432DB42 | NULL | NULL | 2026-06-03T09:09:03.3570000 | NULL | False | False | NULL | NULL | NULL |
| 038CD1C8-F577-4084-8E14-A0AE990BFA4A | NULL | NULL | 2026-04-01T09:10:00.2600000 | NULL | False | False | NULL | NULL | NULL |
| 02E64C80-63FD-4CE3-AE17-10D42C43F62F | NULL | NULL | 2026-04-01T09:10:00.2600000 | NULL | False | False | NULL | NULL | NULL |
| 029A4CB7-B2AA-4D3E-865F-8BE4471B5C94 | NULL | NULL | 2026-07-01T16:36:43.1000000 | NULL | False | False | NULL | NULL | NULL |
| 0254F8D3-8991-40CA-8DCE-23C96C13978B | NULL | NULL | 2025-12-04T09:23:43.9300000 | NULL | False | False | NULL | NULL | NULL |
| 0184E60E-8A08-4555-9E0E-D730F8D8EAD8 | NULL | NULL | 2026-01-29T13:36:42.9430000 | NULL | False | False | NULL | NULL | NULL |
| 014AE34B-5B08-4A22-8588-8E2B805B7277 | NULL | NULL | 2026-03-02T16:26:56.7430000 | NULL | False | False | NULL | NULL | NULL |
| 011FA2C6-E92E-4C2B-9EC0-4F38C4EE197C | NULL | NULL | 2026-05-04T16:53:54.9030000 | NULL | False | False | NULL | NULL | NULL |
| 00E76941-FD47-40E7-BBB0-0609DF826029 | NULL | NULL | 2026-03-02T16:26:56.7430000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3029E822-7971-421A-A7F1-5705395D97EF | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| 45163C7E-5E7F-4E7D-B6DC-9CFDF441D634 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| 6A642EB0-990E-4416-8605-BA2A47B1AB1E | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| BB5BF7CB-E019-4CA9-86CD-5BBB2FE4B962 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| C8BD6E7C-BC67-45E0-B716-E6F2B588756B | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| E0E27C5D-9296-48CD-84C8-276292D74A11 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| FEE98F83-47E1-4806-A6AC-D3586506E0A0 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| FF94B989-2241-4FCE-BAE0-52320291AD95 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:40.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| D55A0FA5-C7EB-403A-9FC1-D8DB84F65171 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2025-12-04T09:23:43.9300000 | 2025-12-04T09:34:39.0000000 | False | False | NULL | 172.16.10.49 | NULL |
| 18A217CC-2450-4806-B586-F6B4A86DC0F9 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T14:33:18.8270000 | 2025-10-10T14:41:21.0000000 | False | False | NULL | 172.16.3.201 |  |

---
