# XStudio_Xbatch.dbo.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, order, quantity, uomid, work.

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-12-01T17:10:18.0000000 to 2025-12-01T17:11:44.0000000  

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
| WorkOrder | varchar | YES | 36 | — |
| MaterialID | varchar | YES | 36 | — |
| Quantity | decimal | YES | 18,4 | — |
| UOMID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5A0BC867-F89C-47E5-8830-C672851F2CAA | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-01T17:07:48.4430000 | 2025-12-01T17:10:18.0000000 | False | False | NULL |
| 2A16F8A3-B4E9-41D6-AD8B-008CEA1CE3D5 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-01T17:07:48.4430000 | 2025-12-01T17:11:05.0000000 | False | False | NULL |
| 1DD5095A-7A85-46D4-AEFC-526A5203849B | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-01T17:08:20.9000000 | 2025-12-01T17:11:15.0000000 | False | False | NULL |
| A1AFFF1D-8F9A-4FAD-B916-A127CAB7357B | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-01T17:08:20.9000000 | 2025-12-01T17:11:25.0000000 | False | False | NULL |
| 2677086F-9194-4256-A1E6-4913A24BB467 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-01T17:08:03.1830000 | 2025-12-01T17:11:34.0000000 | False | False | NULL |
| 10667476-807C-4B0F-B37B-09E6C8596954 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-01T17:08:03.1830000 | 2025-12-01T17:11:44.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
