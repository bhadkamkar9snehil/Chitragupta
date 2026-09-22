# XStudio_Xbatch.dbo.CCM_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 122  
**Date Range (ModifiedOn):** 2025-09-05T08:47:26.7530000 to 2026-05-30T10:35:37.1730000  

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
| 1BAB4427-5F9F-40E9-9E8B-CAFAA1280AF9 | NULL | NULL | NULL | NULL | 2025-09-17T09:54:54.4730000 | NULL | False | False | NULL |
| 1ED36ADC-132A-4E96-A175-7D0503E13EC2 | NULL | NULL | NULL | NULL | 2025-09-17T09:54:54.4730000 | NULL | False | False | NULL |
| 29B59BE2-52AA-4085-AE40-9B68B06E7E2A | NULL | NULL | NULL | NULL | 2025-09-17T09:54:54.4730000 | NULL | False | False | NULL |
| 2B3860F0-78A6-44A9-8326-FE09FE728D5E | NULL | NULL | NULL | NULL | 2025-09-05T11:28:54.0400000 | NULL | False | False | NULL |
| 326E8442-B864-4BEA-A475-C50BFA98B5DF | NULL | NULL | NULL | NULL | 2025-09-05T11:28:54.0400000 | NULL | False | False | NULL |
| 32C88C7C-70E9-454C-B1E3-47038F340B11 | NULL | NULL | NULL | NULL | 2025-09-05T11:28:54.0400000 | NULL | False | False | NULL |
| 37183D69-7865-46B0-9723-49E959CE4FF1 | NULL | NULL | NULL | NULL | 2025-09-17T09:54:54.4730000 | NULL | False | False | NULL |
| 3C82FB35-E3A9-4679-95CA-8F544E02FE28 | NULL | NULL | NULL | NULL | 2025-07-16T09:34:56.4900000 | NULL | False | False | NULL |
| 87145EA7-A9E4-4001-B0D4-28DB446537FD | NULL | NULL | NULL | NULL | 2026-05-30T12:55:45.7870000 | NULL | False | False | NULL |
| A638B95B-1D26-4568-A1A9-F65878C61082 | NULL | NULL | NULL | NULL | 2026-06-15T08:52:10.3870000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 498360EC-57CC-46BD-BE31-012412FB7D6A | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T10:34:33.7470000 | 2026-05-30T10:35:37.1730000 | False | False | NULL |
| 92DE5DC1-DF5E-4620-98DC-7FFA289A4384 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-13T10:31:28.9270000 | 2026-03-13T10:32:32.5100000 | False | False | NULL |
| FBA93939-A7F3-474D-B183-7C693E2E1AB4 | NULL | NULL | NULL | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-07-21T16:23:44.6600000 | 2026-01-02T15:52:20.4330000 | False | False | NULL |
| 3DADCEEA-D939-44F5-80AE-3ECBB3D306F3 | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-10-15T10:45:59.0670000 | 2025-10-15T10:47:08.1370000 | False | False | NULL |
| 0449B713-575D-46FD-AA3D-0BA0CCF465E0 | NULL | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-10-15T10:32:33.0930000 | 2025-10-15T10:33:50.1830000 | False | False | NULL |
| 1AA3B04F-085D-452E-A0CB-BC73E48A28A3 | NULL | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-10-15T10:32:15.0370000 | 2025-10-15T10:33:50.1830000 | False | False | NULL |
| 2BD54BF7-DBF2-4B93-942C-7274256CFE1F | NULL | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-10-15T10:32:05.9870000 | 2025-10-15T10:33:50.1830000 | False | False | NULL |
| 41E087B0-14F0-4211-A9A7-4BFE884D72AE | NULL | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-10-15T10:32:25.1100000 | 2025-10-15T10:33:50.1830000 | False | False | NULL |
| 653808D7-6921-41D0-B933-C863921B058C | NULL | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-10-15T10:32:50.4130000 | 2025-10-15T10:33:50.1830000 | False | False | NULL |
| 924FEC48-0C6C-4529-9410-8CCBF8E3A18D | NULL | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-10-15T10:32:41.3470000 | 2025-10-15T10:33:50.1830000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.CCM_Mst_Tbl.ID` (Many to One)
