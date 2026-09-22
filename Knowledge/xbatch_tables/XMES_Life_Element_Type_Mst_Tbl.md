# XStudio_Xbatch.dbo.XMES_Life_Element_Type_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference srno.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2026-03-06T17:15:45.0000000 to 2026-03-07T13:09:32.0000000  

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
| Name | varchar | YES | 100 | — |
| Srno | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0400000 | 2026-03-06T17:15:45.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| 66A8C44E-B9D9-4088-A59D-EEEF2A8E0189 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0730000 | 2026-03-06T17:15:59.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| F44C4579-A241-47A5-86BF-A503C8CA3555 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:07.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| D3DC8F8D-2ED7-409C-B7A4-D916055DAE33 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:13.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| C415A162-9804-4029-AED9-07989791BD40 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:19.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| C6E7D609-D6A7-40DF-8128-BA910B66C0E7 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:25.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| BCE2C14C-72ED-42F0-8245-1A0E9D16CC42 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:32.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:39.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| F701E12D-9AEE-4999-94D1-EB71A16E8306 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0770000 | 2026-03-06T17:16:45.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| 4C247527-1739-4411-AFD6-375FD37F3288 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-06T15:59:37.0730000 | 2026-03-07T13:09:32.0000000 | False | False | NULL | 100.110.87.137 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Element_Life_Type_Mapping_Mst_Tbl.ElementType` -> `XStudio_XBatch.XMES_Life_Element_Type_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_Life_Element_Type_Mst_Tbl.ID` (Many to One)
