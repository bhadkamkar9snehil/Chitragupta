# XStudio_Xbatch.dbo.RM_Mill_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 1,820  
**Date Range (ModifiedOn):** 2025-11-26T08:06:38.3000000 to 2025-11-26T15:43:17.0430000  

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
| 00FEE648-46DA-47A5-834C-9CC328089349 | NULL | NULL | NULL | NULL | 2025-10-30T10:46:23.0330000 | NULL | False | False | NULL |
| 00B2AAFF-9A02-498F-AFCC-DF193836D0E8 | NULL | NULL | NULL | NULL | 2025-11-26T15:33:20.3070000 | NULL | False | False | NULL |
| 007495D6-5A8F-40D4-8DED-9075E920E29A | NULL | NULL | NULL | NULL | 2025-10-30T10:38:09.3830000 | NULL | False | False | NULL |
| 006861D8-E3AA-472C-AEC8-A6EB94F3C934 | NULL | NULL | NULL | NULL | 2025-10-30T10:47:22.2100000 | NULL | False | False | NULL |
| 00394E97-5F53-4EF2-B17E-C9E0004B079F | NULL | NULL | NULL | NULL | 2025-11-26T15:34:58.6500000 | NULL | False | False | NULL |
| 01A2DE75-35DF-4414-A8AA-E0F0606BA4C8 | NULL | NULL | NULL | NULL | 2025-10-30T10:39:26.8470000 | NULL | False | False | NULL |
| 01613B6F-241D-4962-AB03-A47CFA78936E | NULL | NULL | NULL | NULL | 2025-11-26T15:37:06.5200000 | NULL | False | False | NULL |
| 0226B340-75C1-4E12-BFCB-F2A9C720B815 | NULL | NULL | NULL | NULL | 2025-10-30T10:38:38.4970000 | NULL | False | False | NULL |
| 01DB9AD1-0745-4956-AE2A-B4B3ED948EE8 | NULL | NULL | NULL | NULL | 2025-10-30T10:43:10.9300000 | NULL | False | False | NULL |
| 02331BAC-4E4E-4ADA-A598-D37B57AC0952 | NULL | NULL | NULL | NULL | 2025-10-30T10:46:46.4870000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12280AAD-EA01-4DD2-B0BD-94F82D27F6D9 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:32:40.5630000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| 27ACA55B-405A-4E40-9B25-E43B8C68E19F | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:36:46.3370000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| 52074287-CED3-4C46-A3C1-CC980C815F05 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:32:59.7470000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| 62735ACD-9E38-451C-8DA1-00733883694C | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:34:44.7230000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| 7EBF9CD8-7DF4-4FAA-AC1D-8A19BF9F0FA7 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:33:20.3070000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| 9A3DA9D5-087F-4018-875F-9D7E0DB9A9DB | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:37:06.4330000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| 9A7A08DE-B5FC-420A-928A-B1C0D8242C33 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:35:37.4800000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| A7A2D5D2-3885-4F2C-AB26-9B7CC7FBE778 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:28:22.7900000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| B2FA68E6-F64F-47BB-B53A-A4BC55D2C1C8 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:35:16.4970000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |
| B4EC04D3-1A0F-4988-826F-FA92D59EFF3D | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T15:33:37.6600000 | 2025-11-26T15:43:17.0430000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Mill_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Mill_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_Mill_Mst_Tbl.ID` (Many to One)
