# XStudio_Xbatch.dbo.RM_Rebar_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 75  
**Date Range (ModifiedOn):** 2025-11-26T11:04:48.6200000 to 2025-11-26T11:32:02.6230000  

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
| 86BA93E0-7B8B-4A33-952D-53C90497EDB1 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:19:43.1600000 | 2025-11-26T11:04:48.6200000 | False | False | NULL |
| 548F285A-BF56-4673-BBF6-CE8288885F16 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:20:47.6230000 | 2025-11-26T11:07:04.6100000 | False | False | NULL |
| 57AA30DE-3FA4-44AE-9952-48F6ADE9282D | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:20:28.5870000 | 2025-11-26T11:07:04.6100000 | False | False | NULL |
| B9330CEB-1819-49A8-AADE-CA209E946ECC | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:20:04.3730000 | 2025-11-26T11:07:04.6100000 | False | False | NULL |
| 0BD411B8-1797-43D2-80F6-AD7F1AE14819 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:21:07.5070000 | 2025-11-26T11:07:55.4770000 | False | False | NULL |
| 049965DA-69F0-4BFD-B9B4-DA325C1E5B20 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:21:25.8500000 | 2025-11-26T11:07:55.4770000 | False | False | NULL |
| 57AE3F39-6757-40D8-B976-AE60D3D4EA5D | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:21:47.0600000 | 2025-11-26T11:08:40.1070000 | False | False | NULL |
| CF3301D6-84D7-46F9-BEF0-D02E96022A58 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:22:38.7770000 | 2025-11-26T11:08:40.1070000 | False | False | NULL |
| 78B542F4-6988-4B2F-88B8-4BC9EFA2ED66 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:23:10.7930000 | 2025-11-26T11:09:07.5100000 | False | False | NULL |
| CEFF3E2B-513C-4964-B388-2B895FD060A8 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:23:32.6170000 | 2025-11-26T11:09:25.8870000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33CB3353-BBB7-4683-B21D-54FFB1C2D887 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:58:03.5070000 | 2025-11-26T11:32:02.6230000 | False | False | NULL |
| 2576B998-8E18-4B91-9EEC-A4E18AF1E567 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:57:48.8200000 | 2025-11-26T11:31:48.6870000 | False | False | NULL |
| 47A23013-75A2-43A8-8F4D-65BB1A95C75B | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:57:34.9170000 | 2025-11-26T11:31:34.4130000 | False | False | NULL |
| 7EA92683-C286-47F1-A91C-F2AB8B3D6829 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:57:21.5830000 | 2025-11-26T11:31:21.1970000 | False | False | NULL |
| 861505CA-AFE9-4556-A78E-6DE1EB1E76C4 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:57:06.8430000 | 2025-11-26T11:31:08.6500000 | False | False | NULL |
| 9418C650-5838-42E9-9219-033FBBC0D83E | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:56:52.3970000 | 2025-11-26T11:30:57.4600000 | False | False | NULL |
| A4C04082-2049-4F27-9285-53B7451B2390 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:56:34.5630000 | 2025-11-26T11:30:42.8130000 | False | False | NULL |
| A50FE212-B069-4E8E-B6CF-F9B9F1449337 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:56:03.9330000 | 2025-11-26T11:30:29.8470000 | False | False | NULL |
| F68EEFD3-DD73-4E4C-B02D-3F8C83C7CBFF | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:55:48.9730000 | 2025-11-26T11:30:16.5870000 | False | False | NULL |
| 8276DC57-5592-4110-9E47-CD46F9BA31C5 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:55:33.6900000 | 2025-11-26T11:30:03.7370000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Rebar_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Rebar_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_Rebar_Mst_Tbl.ID` (Many to One)
