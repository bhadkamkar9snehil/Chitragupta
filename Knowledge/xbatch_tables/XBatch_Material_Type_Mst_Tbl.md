# XStudio_Xbatch.dbo.XBatch_Material_Type_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference can, color, consumed, description, icon, obsolete, produced, sold.

**Primary Key:** ID  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2025-12-11T13:21:14.0000000 to 2025-12-19T08:13:37.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | NO | 100 | — |
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
| Description | varchar | YES | -1 | — |
| Color | varchar | YES | 10 | — |
| Icon | varchar | YES | 8000 | — |
| CanProduced | bit | YES | — | — |
| CanConsumed | bit | YES | — | — |
| CanSold | bit | YES | — | — |
| CanObsolete | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BF2578F9-F7DA-4F84-991A-F633FE05220A | Raw Material | NULL | NULL | NULL | 2025-07-22T20:37:35.1400000 | NULL | False | False | NULL |
| 5A5E02E1-A4D9-479C-BBDD-7D85037FE911 | Packaging Material | NULL | NULL | NULL | 2025-07-22T20:37:35.1370000 | NULL | False | False | NULL |
| 2A4CFBD6-804D-4DB2-820D-DF8C0BF2C21C | Intermediate Product | NULL | NULL | NULL | 2025-07-22T20:37:35.1370000 | NULL | False | False | NULL |
| 1ED25421-A362-4E19-B18E-0AEF246B0981 | Finished Good | NULL | NULL | NULL | 2025-07-22T20:37:35.1370000 | NULL | False | False | NULL |
| 70B716B3-02DB-4D21-9DCC-A31807A4B6D5 | Byproduct | NULL | NULL | NULL | 2025-07-22T20:37:35.1370000 | NULL | False | False | NULL |
| 646C98CA-4D69-4AE3-A029-6B0432897B31 | Waste Material | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-22T20:37:35.1370000 | 2025-12-11T13:21:14.0000000 | False | False | NULL |
| A05C166F-6A57-413A-9B43-195E3002EEF4 | Utility | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-19T08:13:37.2300000 | 2025-12-19T08:13:37.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Mst_Tbl.TypeID` -> `XStudio_XBatch.XBatch_Material_Type_Mst_Tbl.ID` (Many to One)
