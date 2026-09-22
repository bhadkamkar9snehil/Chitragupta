# XStudio_Xbatch.dbo.CCM_SMS_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 130  
**Date Range (ModifiedOn):** 2025-09-05T08:47:26.6870000 to 2026-05-30T10:55:26.8600000  

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
| 010E2771-3482-49B5-A0BB-1EA2540A525A | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 1015554C-32D7-490A-A17A-7701B8C5D95B | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 0C405515-5DA7-428D-8CFB-C9129928E22C | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 0A1BB0A0-C313-4C83-BDA2-4061F60421B7 | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 05A18C57-5570-43EF-9BF7-2722779F0B1C | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 0515A08A-84A9-4400-BBA5-0BC636AEA89E | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 03D0E99E-C691-40A0-AE8C-B1A516D4C76F | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 1732388C-0760-4703-9749-77B8CA62296E | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 1FC3035C-AB40-40BA-9C50-BB46A1CC2BCC | NULL | NULL | NULL | NULL | 2025-09-16T14:44:07.1970000 | NULL | False | False | NULL |
| 2AE175DC-2279-4391-85B5-F74476C62C34 | NULL | NULL | NULL | NULL | 2025-08-28T10:47:06.3530000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4B159E43-32AE-4B5A-BA95-35DF1D3D695B | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T10:53:39.1100000 | 2026-05-30T10:55:26.8600000 | False | False | NULL |
| 12422E35-361F-439F-8CC6-36A311EE4EB4 | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:43:31.6400000 | 2025-10-10T16:47:16.7800000 | False | False | NULL |
| 18E1EE47-9996-4495-8B55-78B7618ADDFA | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:43:50.4730000 | 2025-10-10T16:47:16.7800000 | False | False | NULL |
| 383FC2CB-08F8-42B1-880E-93C2A7832C7D | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:43:11.7570000 | 2025-10-10T16:47:16.7800000 | False | False | NULL |
| 404E483B-758E-4587-B77D-F2C903552586 | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:44:23.8870000 | 2025-10-10T16:47:16.7800000 | False | False | NULL |
| CEC6033E-DC41-4CDF-9FC0-41841C829C16 | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:45:08.4630000 | 2025-10-10T16:47:16.7800000 | False | False | NULL |
| FE449EA8-79D7-40C3-8ACF-82F00100B231 | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:44:43.2200000 | 2025-10-10T16:47:16.7800000 | False | False | NULL |
| 25B46C59-C9E5-48B0-826B-AD6C9D65A4FC | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:37:16.2100000 | 2025-10-10T16:46:18.5030000 | False | False | NULL |
| 35F98B40-693B-410A-B63B-8129B302C294 | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:36:54.8200000 | 2025-10-10T16:46:18.5030000 | False | False | NULL |
| 452DB49C-2DED-4C25-AEC1-684495C9A02A | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-10T16:38:20.8630000 | 2025-10-10T16:46:18.5030000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_SMS_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_SMS_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.CCM_SMS_Mst_Tbl.ID` (Many to One)
