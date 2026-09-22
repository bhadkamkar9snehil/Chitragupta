# XStudio_Xbatch.dbo.Roll_History_Card

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference roll, hardness, mill, adressing, barrel, bdressing, campaign, cumulate, dateof, dept, diadiscard, dianew.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-12-08T08:32:18.0000000 to 2025-12-08T08:32:18.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| DateofProcurement | date | YES | — | — |
| StandNo | varchar | YES | 100 | — |
| SetNo | int | YES | 10,0 | — |
| RollNumber | varchar | YES | 100 | — |
| Hardness | varchar | YES | 100 | — |
| Supplier | varchar | YES | 100 | — |
| BarrelLength | varchar | YES | 100 | — |
| RollDIANew | varchar | YES | 100 | — |
| RollGrade | varchar | YES | 100 | — |
| PONo | int | YES | 10,0 | — |
| RollDIADiscard | varchar | YES | 100 | — |
| SINo | int | YES | 10,0 | — |
| DressNo | varchar | YES | 100 | — |
| BDressing | varchar | YES | 100 | — |
| ADressing | varchar | YES | 100 | — |
| MillIn | date | YES | — | — |
| MillOut | date | YES | — | — |
| Campaign | int | YES | 10,0 | — |
| Cumulate | varchar | YES | 100 | — |
| Remarks | varchar | YES | -1 | — |
| ScrapedOn | date | YES | — | — |
| ReasonforScrap | varchar | YES | 100 | — |
| Signature | varchar | YES | 36 | — |
| RTShop | varchar | YES | 100 | — |
| DeptHead | varchar | YES | 36 | — |
| Hardness1 | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8795C114-F26C-45F7-9EF8-DABAE3ADAE0B | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-06T09:33:52.1730000 | 2025-12-08T08:32:18.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Roll_History_Card.DeptHead` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Roll_History_Card.Signature` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
