# XStudio_Xbatch.dbo.NM3_To_MMBTU_Factor

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference factor, rod, rebar, tie, coil, cut, end, mmbtufactor, month, scaleloss, wrmtie.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-08-06T16:32:19.0000000 to 2026-08-06T16:32:19.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Month | date | YES | — | — |
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
| Nm3toMMBTUFactor | decimal | YES | 18,3 | — |
| RebarTieRodFactor | decimal | YES | 18,1 | — |
| WRMTieRodFactor | decimal | YES | 18,1 | — |
| RebarCoilTieRodFactor | decimal | YES | 18,1 | — |
| ScalelossFactor | decimal | YES | 18,1 | — |
| EndCutFactor | decimal | YES | 18,1 | — |

### Top 10 Records

| ID | Month | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 307361F9-E237-4D36-8897-6E183F2D7147 | 2026-07-31T00:00:00.0000000 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-31T13:40:37.8830000 | 2026-08-06T16:32:19.0000000 | False | False | NULL | 172.16.7.110 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.NM3_To_MMBTU_Factor.CreatedBy` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
