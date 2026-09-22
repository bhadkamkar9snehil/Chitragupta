# XStudio_Xbatch.dbo.MES_Order_Configurator

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference equipment, itemid, order, quantity, type, unitid.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2026-04-02T09:52:58.0000000 to 2026-06-01T16:01:03.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Equipment | varchar | YES | 100 | — |
| Itemid | varchar | YES | 36 | — |
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
| Quantity | decimal | YES | 18,2 | — |
| Unitid | varchar | YES | 36 | — |
| OrderType | varchar | YES | 100 | — |
| SrNo | int | YES | 10,0 | — |

### Top 10 Records

| ID | Equipment | Itemid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2FC0B0BC-1B37-4F7F-9D58-84C90825D5A8 | EAF | 1500E229-B686-4B06-9646-FFDFF2877A03 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-22T09:32:21.0330000 | 2026-04-02T09:52:58.0000000 | False | False | NULL |
| 62468584-82C0-41AF-8D42-E3403F90C1F5 | CCM | 82BA40F7-5AE4-46DE-A0E9-101F782A5FBE | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-22T09:33:38.7000000 | 2026-04-02T09:55:14.0000000 | False | False | NULL |
| B8D97595-DF46-40E1-A03F-1BEEF8CB383F | LRF | 89D5F6CE-6338-41EF-846A-A52D59A71CA2 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-22T09:33:01.2300000 | 2026-06-01T16:01:03.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_Order_Configurator.CreatedBy` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Order_Configurator.Itemid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Order_Configurator.ModifiedBy` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Order_Configurator.Unitid` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
