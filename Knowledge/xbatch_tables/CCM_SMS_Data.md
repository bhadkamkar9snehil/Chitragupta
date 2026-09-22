# XStudio_Xbatch.dbo.CCM_SMS_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference plcstatus, strand, ccmtundish, common, cuttinglength, cvsplcstatus, equipment, temp.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-09-02T10:48:15.0070000 to 2026-09-02T10:48:15.0070000  

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
| CVSPLCStatus | decimal | YES | 18,4 | — |
| CommonPLCStatus | decimal | YES | 18,4 | — |
| Strand1PLCStatus | decimal | YES | 18,4 | — |
| Strand2PLCStatus | decimal | YES | 18,4 | — |
| Strand3PLCStatus | decimal | YES | 18,4 | — |
| Strand4PLCStatus | decimal | YES | 18,4 | — |
| Strand5PLCStatus | decimal | YES | 18,4 | — |
| Strand6PLCStatus | decimal | YES | 18,4 | — |
| Cuttinglength | int | YES | 10,0 | — |
| CCMTundishTemp | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E4424BF3-1744-4287-A29F-34F5E9B41C0B | NULL | NULL | NULL | NULL | 2025-08-27T17:29:51.1470000 | 2026-09-02T10:48:15.0070000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_SMS_Data.EquipmentID` -> `XStudio_XBatch.CCM_SMS_Mst_Tbl.ID` (Many to One)
