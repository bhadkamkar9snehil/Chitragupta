# XStudio_Xbatch.dbo.Equipment_Wise_Delay

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, delay, entities, entity, from, highlights, oee, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference duration, equipment, name, agency, delay, durationmmss, remark, second, sub.

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2025-09-27T13:22:04.0000000 to 2026-01-28T14:25:38.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| EquipmentName | varchar | YES | -1 | — |
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
| DelayAgency | varchar | YES | 36 | — |
| Duration | decimal | YES | 18,4 | — |
| Remark | varchar | YES | -1 | — |
| SubEquipmentName | varchar | YES | -1 | — |
| Durationmmss | varchar | YES | 100 | — |
| DurationInSecond | int | YES | 10,0 | — |

### Top 10 Records

| ID | EquipmentName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 947E7D22-7993-4CC0-BCE6-D585D04A8B35 | EAF | 0CBC3841-6678-44CE-AEA9-4BA90CA1A37F | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-27T13:22:04.9730000 | 2025-09-27T13:22:04.0000000 | False | False | NULL |
| E746AEE6-6C80-41FA-B364-1163260C38A5 | EAF | 5C15B32F-6CE6-4C9F-84F2-4D6525F14E9E | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-29T13:01:59.2430000 | 2025-09-29T13:01:59.0000000 | False | False | NULL |
| 4771ED41-4D56-40A4-898F-C2D84C70E955 | EAF | 5C15B32F-6CE6-4C9F-84F2-4D6525F14E9E | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-29T13:02:18.8330000 | 2025-09-29T13:02:18.0000000 | False | False | NULL |
| C8EA317C-B62B-4ECD-A7D5-318F9DD81ECD | EAF | F021D261-F114-44DF-8717-B74773C42209 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-29T16:13:52.5530000 | 2025-09-29T16:13:52.0000000 | False | False | NULL |
| 6D3FD20F-5AD7-4DF8-A272-FFA675E00BD0 | EAF | 982DAA4E-0644-4DF6-976A-577BB84A4428 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-09-30T08:38:26.2170000 | 2025-09-30T08:38:26.0000000 | False | False | NULL |
| 65C1E01C-46E5-4D4A-9377-1D3E0A211546 | EAF | 982DAA4E-0644-4DF6-976A-577BB84A4428 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-09-30T08:38:53.7070000 | 2025-09-30T08:38:53.0000000 | False | False | NULL |
| 47140E09-9302-4B28-B206-1A0AA693EC28 | EAF | D42FB7A6-320C-4332-B19F-FFC56263885C | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-30T08:35:26.6830000 | 2025-09-30T11:03:27.0000000 | False | False | NULL |
| F0649141-A146-483B-BC75-CF3B6E3A3E59 | EAF | D42FB7A6-320C-4332-B19F-FFC56263885C | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-10-01T14:45:56.3030000 | 2025-10-01T15:57:00.0000000 | False | False | NULL |
| 54DEBDA1-EA64-4425-A121-66F5389E1C1E | CCM | 3EC4E43E-A637-429B-8C6D-92F78C86DC61 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-28T14:25:38.5870000 | 2026-01-28T14:25:38.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Equipment_Wise_Delay.DelayAgency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.Equipment_Wise_Delay.EquipmentName` -> `XStudio_XBatch.Equipment.Name` (Many to One)
- `XStudio_XBatch.Equipment_Wise_Delay.ParentID` -> `XStudio_XBatch.Agency_Wise_Delay.ID` (Many to One)
- `XStudio_XBatch.Equipment_Wise_Delay.SubEquipmentName` -> `XStudio_XBatch.SubEquipment.Name` (Many to One)
