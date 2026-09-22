# XStudio_Xbatch.dbo.RM_Rolling_Plan

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference rolling, qty, material, assigned, customer, date, grade, ponumber, release, sequence, size, status.

**Primary Key:** ID  
**Row Count:** 13  

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
| PONumber | varchar | YES | 100 | — |
| Customer | varchar | YES | 36 | — |
| Size | varchar | YES | 100 | — |
| ReleaseRollingQty | int | YES | 10,0 | — |
| SequenceNo | int | YES | 10,0 | — |
| RollingDate | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| RollingQty | int | YES | 10,0 | — |
| RollingID | varchar | YES | 100 | — |
| AssignedQty | decimal | YES | 18,4 | — |
| MaterialGrade | varchar | YES | 36 | — |
| MaterialID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEBFAD70-D998-43E2-87EC-89F286CE4C68 | NULL | NULL | NULL | NULL | 2025-07-10T09:08:27.4830000 | NULL | False | False | NULL |
| CE2C7667-8ED6-4591-AFF1-868D0F3D9D01 | NULL | NULL | NULL | NULL | 2025-07-10T09:03:38.8600000 | NULL | False | False | NULL |
| CE0C9032-71C3-4323-A3FA-EE595AEF6CE8 | NULL | NULL | NULL | NULL | 2025-07-10T09:08:45.6930000 | NULL | False | False | NULL |
| BFD8C46D-9023-45F0-8F34-027DA1F7A7A6 | NULL | NULL | NULL | NULL | 2025-07-10T09:09:49.1500000 | NULL | False | False | NULL |
| B15AF75D-ACA6-4FD5-A9A2-CD0F1DF187D7 | NULL | NULL | NULL | NULL | 2025-07-10T09:00:42.7470000 | NULL | False | False | NULL |
| 7827588C-8229-44E3-9C13-CF61D1DE97A4 | NULL | NULL | NULL | NULL | 2025-07-10T09:10:36.3930000 | NULL | False | False | NULL |
| 59A791CE-607B-408F-8BE0-FC1CCC89EC22 | NULL | NULL | NULL | NULL | 2025-07-10T09:06:08.3200000 | NULL | False | False | NULL |
| 4005F1E2-62C2-4029-8522-661175BD8F4A | NULL | NULL | NULL | NULL | 2025-07-10T09:02:22.1500000 | NULL | False | False | NULL |
| 38E58B48-9676-4182-BC32-05EF4AC475C1 | NULL | NULL | NULL | NULL | 2025-07-10T09:04:22.3000000 | NULL | False | False | NULL |
| 0DD12AB9-6D2E-40A7-83E3-8AD886CD68F7 | NULL | NULL | NULL | NULL | 2025-07-10T09:04:06.6370000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEBFAD70-D998-43E2-87EC-89F286CE4C68 | NULL | NULL | NULL | NULL | 2025-07-10T09:08:27.4830000 | NULL | False | False | NULL |
| CE2C7667-8ED6-4591-AFF1-868D0F3D9D01 | NULL | NULL | NULL | NULL | 2025-07-10T09:03:38.8600000 | NULL | False | False | NULL |
| CE0C9032-71C3-4323-A3FA-EE595AEF6CE8 | NULL | NULL | NULL | NULL | 2025-07-10T09:08:45.6930000 | NULL | False | False | NULL |
| BFD8C46D-9023-45F0-8F34-027DA1F7A7A6 | NULL | NULL | NULL | NULL | 2025-07-10T09:09:49.1500000 | NULL | False | False | NULL |
| B15AF75D-ACA6-4FD5-A9A2-CD0F1DF187D7 | NULL | NULL | NULL | NULL | 2025-07-10T09:00:42.7470000 | NULL | False | False | NULL |
| 7827588C-8229-44E3-9C13-CF61D1DE97A4 | NULL | NULL | NULL | NULL | 2025-07-10T09:10:36.3930000 | NULL | False | False | NULL |
| 59A791CE-607B-408F-8BE0-FC1CCC89EC22 | NULL | NULL | NULL | NULL | 2025-07-10T09:06:08.3200000 | NULL | False | False | NULL |
| 4005F1E2-62C2-4029-8522-661175BD8F4A | NULL | NULL | NULL | NULL | 2025-07-10T09:02:22.1500000 | NULL | False | False | NULL |
| 38E58B48-9676-4182-BC32-05EF4AC475C1 | NULL | NULL | NULL | NULL | 2025-07-10T09:04:22.3000000 | NULL | False | False | NULL |
| 0DD12AB9-6D2E-40A7-83E3-8AD886CD68F7 | NULL | NULL | NULL | NULL | 2025-07-10T09:04:06.6370000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Rolling_Plan.Customer` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Rolling_Plan.MaterialGrade` -> `XStudio_XBatch.Steel_Grade_Master.ID` (Many to One)
- `XStudio_XBatch.RM_Rolling_Plan.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
