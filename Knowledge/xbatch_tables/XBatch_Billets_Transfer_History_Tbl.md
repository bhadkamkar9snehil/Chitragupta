# XStudio_Xbatch.dbo.XBatch_Billets_Transfer_History_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference date, billet, inward, location, outward, recieved, status, action, assigned, current, grade, inventory.

**Primary Key:** ID  
**Row Count:** 2,23,053  

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
| BilletNo | varchar | YES | 100 | — |
| SubLotNo | varchar | YES | 100 | — |
| RecievedDate | datetime | YES | — | — |
| InventoryID | varchar | YES | 36 | — |
| LocationType | varchar | YES | 100 | — |
| RecievedBy | varchar | YES | 100 | — |
| StackID | varchar | YES | 36 | — |
| LayerID | varchar | YES | 36 | — |
| MaterialGrade | varchar | YES | 100 | — |
| LocationAssignedDate | datetime | YES | — | — |
| ActionBy | varchar | YES | 36 | — |
| CurrentStatus | varchar | YES | 100 | — |
| InwardStatus | varchar | YES | 100 | — |
| IsInward | bit | YES | — | — |
| Isoutward | bit | YES | — | — |
| OutwardBy | varchar | YES | 36 | — |
| outwardDate | datetime | YES | — | — |
| BilletLength | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00027713-53FF-46D2-99CF-FADAEE93017A | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-10-06T20:02:04.5500000 | NULL | False | False | NULL |
| 00026D0F-A104-4215-B74E-465513BEEBB7 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-11-22T05:16:40.0670000 | NULL | False | False | NULL |
| 00020B8C-9C72-4112-86B9-7F63E87D5F68 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-23T18:06:35.9070000 | NULL | False | False | NULL |
| 00017E62-F3D0-44D6-975A-3BD24797A3F2 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-18T18:39:24.8900000 | NULL | False | False | NULL |
| 00017114-F139-4702-A66E-D0C947E31BFC | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-03-25T03:48:48.8870000 | NULL | False | False | NULL |
| 00015408-3EF3-452F-A42A-0E5CC28C7E0E | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-03-19T19:39:14.9000000 | NULL | False | False | NULL |
| 0000B5E4-0185-4C0B-ACF3-284102D09A65 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-27T10:12:34.4730000 | NULL | False | False | NULL |
| 000086C7-D2A6-4D80-BAE6-66B7A6A05645 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-10-30T09:42:27.9730000 | NULL | False | False | NULL |
| 00004DA3-5D84-48D7-B8EC-58871927F1DB | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-20T16:37:05.2400000 | NULL | False | False | NULL |
| 00003CBD-307C-43C3-AC21-3AB97ABD731A | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-04T19:45:35.5800000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00027713-53FF-46D2-99CF-FADAEE93017A | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-10-06T20:02:04.5500000 | NULL | False | False | NULL |
| 00026D0F-A104-4215-B74E-465513BEEBB7 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-11-22T05:16:40.0670000 | NULL | False | False | NULL |
| 00020B8C-9C72-4112-86B9-7F63E87D5F68 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-23T18:06:35.9070000 | NULL | False | False | NULL |
| 00017E62-F3D0-44D6-975A-3BD24797A3F2 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-18T18:39:24.8900000 | NULL | False | False | NULL |
| 00017114-F139-4702-A66E-D0C947E31BFC | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-03-25T03:48:48.8870000 | NULL | False | False | NULL |
| 00015408-3EF3-452F-A42A-0E5CC28C7E0E | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-03-19T19:39:14.9000000 | NULL | False | False | NULL |
| 0000B5E4-0185-4C0B-ACF3-284102D09A65 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-27T10:12:34.4730000 | NULL | False | False | NULL |
| 000086C7-D2A6-4D80-BAE6-66B7A6A05645 | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-10-30T09:42:27.9730000 | NULL | False | False | NULL |
| 00004DA3-5D84-48D7-B8EC-58871927F1DB | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-20T16:37:05.2400000 | NULL | False | False | NULL |
| 00003CBD-307C-43C3-AC21-3AB97ABD731A | NULL | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-04T19:45:35.5800000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Billets_Transfer_History_Tbl.ActionBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Billets_Transfer_History_Tbl.InventoryID` -> `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Billets_Transfer_History_Tbl.OutwardBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
