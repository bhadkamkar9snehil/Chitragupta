# XStudio_Xbatch.dbo.EAF_SMS_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 144  
**Date Range (ModifiedOn):** 2025-07-16T09:08:36.7230000 to 2026-07-07T12:55:12.6600000  

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
| Attribute | varchar | YES | 100 | — |
| DataSourceID | varchar | YES | 36 | — |
| TagName | varchar | YES | 100 | — |
| InstrumentTag | varchar | YES | 100 | — |
| HHRange | decimal | YES | 18,4 | — |
| HRange | decimal | YES | 18,4 | — |
| LRange | decimal | YES | 18,4 | — |
| LLRange | decimal | YES | 18,4 | — |
| ColorGTHH | varchar | YES | 100 | — |
| ColorBWHHH | varchar | YES | 100 | — |
| ColorBWHL | varchar | YES | 100 | — |
| ColorBWLLL | varchar | YES | 100 | — |
| ColorLTLL | varchar | YES | 100 | — |
| DocumentGTHH | varchar | YES | 8000 | — |
| DocumentBWHHH | varchar | YES | 8000 | — |
| DocumentBWHL | varchar | YES | 8000 | — |
| DocumentBWLLL | varchar | YES | 8000 | — |
| DocumentLTLL | varchar | YES | 8000 | — |
| Type | varchar | YES | 100 | — |
| IsXBatchTag | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11E06DB9-A503-4C4C-A0B3-901C00AD1E19 | NULL | NULL | NULL | NULL | 2026-05-22T10:28:34.9300000 | NULL | False | False | NULL |
| 1192E798-AA68-4816-8916-575C72C058E9 | NULL | NULL | NULL | NULL | 2026-05-22T10:28:52.4670000 | NULL | False | False | NULL |
| 09AD0C65-2F30-43D8-B8D8-A5344F1589F4 | NULL | NULL | NULL | NULL | 2026-05-22T10:27:53.9600000 | NULL | False | False | NULL |
| 05E5414E-0270-4688-8FE4-9B1578205200 | NULL | NULL | NULL | NULL | 2026-05-22T10:27:26.1170000 | NULL | False | False | NULL |
| 0C118840-5D24-4476-9CE5-CEBB33F0AD11 | NULL | NULL | NULL | NULL | 2026-05-22T10:29:14.7870000 | NULL | False | False | NULL |
| 20AA33E3-0746-444A-B7F4-A84E81BB2B88 | NULL | NULL | NULL | NULL | 2025-07-19T14:32:17.4970000 | NULL | False | False | NULL |
| 23082931-4B3F-4CEC-B64B-15DD5C4007F6 | NULL | NULL | NULL | NULL | 2025-07-19T14:32:17.4970000 | NULL | False | False | NULL |
| 2A24501A-1C8C-4DBE-BB11-8CAA3B7AF859 | NULL | NULL | NULL | NULL | 2025-07-19T14:32:17.4970000 | NULL | False | False | NULL |
| 349A7B26-19EE-4BA4-9B8B-7E7C92D4F3FD | NULL | NULL | NULL | NULL | 2026-05-22T10:29:35.0530000 | NULL | False | False | NULL |
| 3802FCCF-E78D-43BB-8707-57DFA6DA20BC | NULL | NULL | NULL | NULL | 2026-05-22T10:26:24.9270000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2082B9D1-DD86-41B6-9478-D2FE19004C40 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-07T10:44:31.9400000 | 2026-07-07T12:55:12.6600000 | False | False | NULL |
| 2BD544CB-7B8E-4497-8BAA-2FAF55FFDDF6 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-07T10:44:51.7270000 | 2026-07-07T12:55:12.6600000 | False | False | NULL |
| 43C1CAE2-C8EA-43F1-89ED-BC3598A15365 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-07T10:45:35.7200000 | 2026-07-07T12:55:12.6600000 | False | False | NULL |
| BD9F5B96-9407-4490-B948-757A54F48EBD | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T10:32:50.7400000 | 2026-05-30T10:33:23.5330000 | False | False | NULL |
| 3FBEA02D-F76E-497C-A5E8-1B657A418BEA | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-23T16:27:17.2770000 | 2026-04-23T16:28:09.3970000 | False | False | NULL |
| 4AD8DFD7-FCCA-4231-ADF4-506A76AFC877 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-23T16:27:29.9800000 | 2026-04-23T16:28:09.3970000 | False | False | NULL |
| 4A44D4D5-0708-4C1C-9740-87E0A1A07B1E | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-20T08:52:40.1870000 | 2026-03-20T08:57:31.0330000 | False | False | NULL |
| C15489D8-3C96-4CDA-A0F7-4207A5BCB953 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-20T08:51:35.5670000 | 2026-03-20T08:57:31.0330000 | False | False | NULL |
| 2A47E04B-5F27-4970-B4DB-5E9FD8ADD510 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-19T16:04:23.3300000 | 2026-03-19T16:05:52.2200000 | False | False | NULL |
| 7F5C1FBE-78E7-4185-A144-F94C328B68F6 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-19T16:04:07.4430000 | 2026-03-19T16:05:52.2200000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_SMS_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
