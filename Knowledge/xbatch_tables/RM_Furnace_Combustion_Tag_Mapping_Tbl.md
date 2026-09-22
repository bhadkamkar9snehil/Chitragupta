# XStudio_Xbatch.dbo.RM_Furnace_Combustion_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 62  
**Date Range (ModifiedOn):** 2026-08-14T14:17:02.3970000 to 2026-08-18T13:32:04.1770000  

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
| 06786436-49B1-4888-8B59-232B399E6B4C | NULL | NULL | NULL | NULL | 2026-08-14T13:20:13.1470000 | NULL | False | False | NULL |
| 2C6BB588-A9D6-4ACC-B154-327E44620BA6 | NULL | NULL | NULL | NULL | 2026-08-14T13:22:00.1600000 | NULL | False | False | NULL |
| 2EF30531-AF71-42C8-BF53-1783E255CCB5 | NULL | NULL | NULL | NULL | 2026-08-14T13:22:28.2800000 | NULL | False | False | NULL |
| 820D103B-3237-446A-9B26-15CEF1B1D61A | NULL | NULL | NULL | NULL | 2026-08-14T13:21:41.4370000 | NULL | False | False | NULL |
| 9C57C0B2-367A-4DB9-91DF-97575820FB5F | NULL | NULL | NULL | NULL | 2026-08-14T13:20:58.0900000 | NULL | False | False | NULL |
| DD317529-9EDC-4B3D-9A43-22CDB81D7294 | NULL | NULL | NULL | NULL | 2026-08-14T13:21:20.3630000 | NULL | False | False | NULL |
| 16E831A8-E39A-47F6-B031-B7CF6B80D2BB | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:59:07.2300000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 151302D1-3E1F-4F9E-B818-551D4B2E20CE | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:57:07.6170000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 13289265-B428-4662-92C0-D08FE3485727 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:30:17.9730000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 112B1493-D554-4BFD-82DF-63287F8821A2 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:34:39.1800000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1BE66421-4DD7-4748-A04E-97AD563FF483 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:15:01.2200000 | 2026-08-18T13:32:04.1770000 | False | False | NULL |
| A0A1CAA1-2965-4F67-B4B1-7A5E3E2AFBDD | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:58:14.6400000 | 2026-08-18T13:12:36.0300000 | False | False | NULL |
| C01E46F9-0F37-414B-8DC0-7BE4CAC51B39 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:57:56.6430000 | 2026-08-14T16:36:44.5370000 | False | False | NULL |
| 3E3703C7-995A-44DE-8775-BC1FFE9D5F6A | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:17:38.5800000 | 2026-08-14T15:26:14.9670000 | False | False | NULL |
| 4C7D9907-4B5C-4E06-AAE0-D4B7E8EB09FB | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:19:29.5500000 | 2026-08-14T15:25:21.9870000 | False | False | NULL |
| 16E831A8-E39A-47F6-B031-B7CF6B80D2BB | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:59:07.2300000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 151302D1-3E1F-4F9E-B818-551D4B2E20CE | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:57:07.6170000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 13289265-B428-4662-92C0-D08FE3485727 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:30:17.9730000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 112B1493-D554-4BFD-82DF-63287F8821A2 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:34:39.1800000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |
| 0D073E36-CBF5-4294-8491-A6283631951E | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T13:31:06.9300000 | 2026-08-14T14:17:02.3970000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Furnace_Combustion_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Combustion_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.ID` (Many to One)
