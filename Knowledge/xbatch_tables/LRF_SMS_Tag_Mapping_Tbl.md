# XStudio_Xbatch.dbo.LRF_SMS_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 57  
**Date Range (ModifiedOn):** 2025-09-05T10:23:31.8800000 to 2026-05-30T10:34:04.2300000  

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
| 18E9EA59-B7F4-4878-B2B5-38564C9C58BB | NULL | NULL | NULL | NULL | 2025-09-09T09:54:07.4700000 | NULL | False | False | NULL |
| 2D8C5A15-FA17-4653-BC17-C13D05C90A6D | NULL | NULL | NULL | NULL | 2026-06-15T08:50:26.6270000 | NULL | False | False | NULL |
| 39C8AE5D-C196-429A-959C-22C5186D9698 | NULL | NULL | NULL | NULL | 2025-07-22T16:13:59.1270000 | NULL | False | False | NULL |
| 8A4905BD-D796-44CE-BCBE-310DCB25EE91 | NULL | NULL | NULL | NULL | 2025-09-09T09:54:07.4700000 | NULL | False | False | NULL |
| 9677DBC4-73A0-4F2D-AE26-86A284D8B5EA | NULL | NULL | NULL | NULL | 2025-09-19T10:48:18.8800000 | NULL | False | False | NULL |
| F601D99A-C9B6-4831-ABC0-3D324F70D251 | NULL | NULL | NULL | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-07-22T10:36:31.6830000 | 2025-09-05T10:23:31.8800000 | False | False | NULL |
| 00F4608D-98BE-4C86-A0ED-67B3C05DC4A5 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-22T10:36:31.6830000 | 2025-09-16T10:47:12.4500000 | False | False | NULL |
| 18B796C2-4407-4199-88A0-1B24870B5841 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-22T16:13:59.1270000 | 2025-09-16T10:47:12.4500000 | False | False | NULL |
| 1857144A-E645-4E2C-8F77-7F1F937805A3 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-09T09:54:07.4700000 | 2025-09-16T10:47:12.4500000 | False | False | NULL |
| 1811C733-B909-4F0B-865C-890B44BFD894 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-22T10:36:31.6830000 | 2025-09-16T10:47:12.4500000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 82F3F53E-E944-43C0-A808-135F6AC3FB7F | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T10:33:50.0800000 | 2026-05-30T10:34:04.2300000 | False | False | NULL |
| 7058DF24-6F2C-4DC8-A998-A4518B6BCD30 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-22T16:13:59.1270000 | 2026-01-02T15:52:20.4200000 | False | False | NULL |
| BFF477F5-D61E-4B3C-B6F8-656FE7EB4147 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-22T10:36:31.6830000 | 2026-01-02T15:52:20.4200000 | False | False | NULL |
| 1B860D2F-10FF-434F-87E9-82CFC6BC10E5 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-10-15T09:23:09.7870000 | 2025-10-15T09:24:52.6170000 | False | False | NULL |
| F15E71B3-C63B-4E3D-A9F9-DB5C4E28E433 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-10-14T16:06:53.9230000 | 2025-10-14T16:08:02.0370000 | False | False | NULL |
| 5E283601-111C-4680-9AA4-D1268C59F18E | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-13T11:27:29.5930000 | 2025-10-14T11:05:27.3670000 | False | False | NULL |
| BF4A9644-DA84-44AE-B784-D52A01C67D1B | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-19T10:48:18.8800000 | 2025-10-13T14:31:30.1530000 | False | False | NULL |
| 2719E452-F3E4-4725-A3A2-4B4615E5147D | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-22T11:01:02.5200000 | 2025-10-13T14:30:14.9030000 | False | False | NULL |
| 32C691B9-1739-4F44-B238-9928B7FE5568 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-10-13T11:26:31.2570000 | 2025-10-13T11:32:28.9270000 | False | False | NULL |
| 9DF6DC94-5EF2-4507-AD88-2D36862CB400 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-10-13T11:26:12.8500000 | 2025-10-13T11:32:28.9270000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_SMS_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
