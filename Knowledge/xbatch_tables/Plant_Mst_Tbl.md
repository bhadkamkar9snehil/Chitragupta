# XStudio_Xbatch.dbo.Plant_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference latitude, location, longitude.

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-07-11T11:46:55.0000000 to 2025-09-03T15:09:17.0000000  

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
| Location | varchar | YES | 100 | — |
| Latitude | decimal | YES | 18,4 | — |
| Longitude | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3EFA5ED2-CE26-4963-8D83-9BCFAEFB17AC | SMS | E92DA561-DC73-44B1-BDF4-5E375A53D06F | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11T11:46:55.8200000 | 2025-07-11T11:46:55.0000000 | False | False | NULL |
| F3DFBC4E-C2AD-46F6-A07C-CDF8F13B51FE | RM | E92DA561-DC73-44B1-BDF4-5E375A53D06F | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-03T15:09:17.2470000 | 2025-09-03T15:09:17.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Area_Mst_Tbl.ParentID` -> `XStudio_XBatch.Plant_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Plant_Mst_Tbl.ParentID` -> `XStudio_XBatch.Organisation_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Plant_Mst_Tbl.ParentID` -> `XStudio_XBatch.Organization_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ProductionPlant` -> `XStudio_XBatch.Plant_Mst_Tbl.Name` (Many to One)
