# XStudio_Xbatch.dbo.RM_WRM_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 194  
**Date Range (ModifiedOn):** 2025-11-26T12:58:14.5330000 to 2025-11-28T08:51:16.2930000  

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
| 13A40F8F-D68F-48E9-8615-B34D2B679DAA | NULL | NULL | NULL | NULL | 2025-11-28T08:47:38.1170000 | NULL | False | False | NULL |
| 40C1463D-C12A-47B4-AE4F-C54F7106A184 | NULL | NULL | NULL | NULL | 2025-09-16T15:26:29.7700000 | NULL | False | False | NULL |
| 46EB019F-DB49-48F9-B969-5776CAA1A96F | NULL | NULL | NULL | NULL | 2025-09-16T15:26:29.7700000 | NULL | False | False | NULL |
| 48954865-1758-4BA9-9D7E-44622F4B223E | NULL | NULL | NULL | NULL | 2025-09-24T14:07:49.6800000 | NULL | False | False | NULL |
| 588F0DA4-55EB-4BFD-BAB6-EACF33DF73F6 | NULL | NULL | NULL | NULL | 2025-09-16T15:26:29.7700000 | NULL | False | False | NULL |
| 9D6F2C69-252A-4FCD-9553-DBA7A3DE3ED8 | NULL | NULL | NULL | NULL | 2025-09-16T15:26:29.7700000 | NULL | False | False | NULL |
| 9FA53710-927A-49E6-80C5-1A18E63D3237 | NULL | NULL | NULL | NULL | 2025-09-16T15:26:29.7700000 | NULL | False | False | NULL |
| 1361C997-3BFA-432F-A172-A7B72CB145BC | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-24T14:07:49.6800000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 1049490F-4417-4F4F-A7FF-79E0EC66C93A | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-16T15:26:29.7700000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0FDB5C55-7E9F-4A06-95F0-0C77DB765C05 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:13:03.1130000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9C87EDC6-4934-44D5-B71D-BC5D2DF8437B | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-24T17:15:14.7370000 | 2025-11-28T08:51:16.2930000 | False | False | NULL |
| DEDFEC9C-B3BA-4F90-A7E5-915BF4A7E5BB | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-11-28T08:46:26.1170000 | 2025-11-28T08:47:38.8200000 | False | False | NULL |
| 1361C997-3BFA-432F-A172-A7B72CB145BC | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-24T14:07:49.6800000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 1049490F-4417-4F4F-A7FF-79E0EC66C93A | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-16T15:26:29.7700000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0FDB5C55-7E9F-4A06-95F0-0C77DB765C05 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T10:13:03.1130000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0BA15F80-334E-42E6-9B58-78FCDADAA5B7 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T09:30:29.1830000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0B9279B3-F792-438D-8D98-D5584E846FA6 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T09:12:36.1100000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0ABF1A78-4C4F-4870-9E86-6DCCE1E3F2E8 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-24T14:07:49.6800000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0AB23512-1E1B-41DE-9F8F-5C279451AE25 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-24T14:07:49.6800000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |
| 0907FF15-5D8D-44C6-B2F2-1F72E4B96846 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-16T15:26:29.7700000 | 2025-11-26T12:58:14.5330000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_WRM_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_WRM_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_WRM_Mst_Tbl.ID` (Many to One)
