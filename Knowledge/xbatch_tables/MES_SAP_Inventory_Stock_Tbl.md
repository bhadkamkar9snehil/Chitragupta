# XStudio_Xbatch.dbo.MES_SAP_Inventory_Stock_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** errors, integration, posting, sap (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference base, inventory, material, matl, plant, sddocument, stock, type, unit, batch, customer, data.

**Primary Key:** ID  
**Row Count:** 3,967  

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
| Material | varchar | YES | 100 | — |
| Plant | int | YES | 10,0 | — |
| StorageLocation | varchar | YES | 100 | — |
| Batch | varchar | YES | 100 | — |
| Supplier | varchar | YES | 100 | — |
| Customer | varchar | YES | 100 | — |
| WebElementInternalID | varchar | YES | 100 | — |
| SDDocument | varchar | YES | 100 | — |
| SDDocumentItem | int | YES | 10,0 | — |
| InventorySpecialStockType | varchar | YES | 100 | — |
| InventoryStockType | varchar | YES | 100 | — |
| MaterialBaseUnit | varchar | YES | 100 | — |
| MatlWrhsStkQtyInMatlBaseUnit | decimal | YES | 18,4 | — |
| MetaData | varchar | YES | -1 | — |
| PlantName | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 004F4F4E-E1A8-4CFB-B7E0-0E19DE8B4530 | NULL | NULL | NULL | NULL | 2026-09-02T09:05:15.8170000 | NULL | False | False | NULL |
| 004E36AA-F8FB-4668-926D-C6B1FBD03497 | NULL | NULL | NULL | NULL | 2026-09-02T10:00:47.3670000 | NULL | False | False | NULL |
| 00493845-B49F-4AAF-AA50-4C0F42B7CE64 | NULL | NULL | NULL | NULL | 2026-09-02T10:00:47.8700000 | NULL | False | False | NULL |
| 0043A651-934E-4D91-A119-63D94F0F1FCB | NULL | NULL | NULL | NULL | 2026-09-02T10:00:46.7700000 | NULL | False | False | NULL |
| 0042B84B-18B0-4498-B20A-0D3023989B9A | NULL | NULL | NULL | NULL | 2026-09-02T10:00:47.5130000 | NULL | False | False | NULL |
| 003B4C55-6A68-49E0-9A95-2162FFF5BDE9 | NULL | NULL | NULL | NULL | 2026-09-02T09:25:14.6470000 | NULL | False | False | NULL |
| 0039E012-4795-45D5-807E-9851A9BA2521 | NULL | NULL | NULL | NULL | 2026-09-02T09:30:16.2000000 | NULL | False | False | NULL |
| 0035916E-CC0F-404F-A002-CD78AA6BB07B | NULL | NULL | NULL | NULL | 2026-09-02T10:00:38.9600000 | NULL | False | False | NULL |
| 0024C707-5539-4F12-878C-2294C20017EF | NULL | NULL | NULL | NULL | 2026-09-02T10:00:42.5730000 | NULL | False | False | NULL |
| 00123525-C044-481C-873B-FCA1AFB863EB | NULL | NULL | NULL | NULL | 2026-09-02T09:05:15.7100000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 004F4F4E-E1A8-4CFB-B7E0-0E19DE8B4530 | NULL | NULL | NULL | NULL | 2026-09-02T09:05:15.8170000 | NULL | False | False | NULL |
| 004E36AA-F8FB-4668-926D-C6B1FBD03497 | NULL | NULL | NULL | NULL | 2026-09-02T10:00:47.3670000 | NULL | False | False | NULL |
| 00493845-B49F-4AAF-AA50-4C0F42B7CE64 | NULL | NULL | NULL | NULL | 2026-09-02T10:00:47.8700000 | NULL | False | False | NULL |
| 0043A651-934E-4D91-A119-63D94F0F1FCB | NULL | NULL | NULL | NULL | 2026-09-02T10:00:46.7700000 | NULL | False | False | NULL |
| 0042B84B-18B0-4498-B20A-0D3023989B9A | NULL | NULL | NULL | NULL | 2026-09-02T10:00:47.5130000 | NULL | False | False | NULL |
| 003B4C55-6A68-49E0-9A95-2162FFF5BDE9 | NULL | NULL | NULL | NULL | 2026-09-02T09:25:14.6470000 | NULL | False | False | NULL |
| 0039E012-4795-45D5-807E-9851A9BA2521 | NULL | NULL | NULL | NULL | 2026-09-02T09:30:16.2000000 | NULL | False | False | NULL |
| 0035916E-CC0F-404F-A002-CD78AA6BB07B | NULL | NULL | NULL | NULL | 2026-09-02T10:00:38.9600000 | NULL | False | False | NULL |
| 0024C707-5539-4F12-878C-2294C20017EF | NULL | NULL | NULL | NULL | 2026-09-02T10:00:42.5730000 | NULL | False | False | NULL |
| 00123525-C044-481C-873B-FCA1AFB863EB | NULL | NULL | NULL | NULL | 2026-09-02T09:05:15.7100000 | NULL | False | False | NULL |

---
