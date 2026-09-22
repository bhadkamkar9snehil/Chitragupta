# XStudio_Xbatch.dbo.MES_SAP_Inventory_Stock_Data_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference stock, base, blocked, inventory, location, material, matl, plant, sddocument, stockin, storage, transfer.

**Primary Key:** ID  
**Row Count:** 3,961  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Supplier | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| Name | varchar | YES | 100 | — |
| Material | varchar | YES | 100 | — |
| SDDocument | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| InventoryStockType | varchar | YES | 100 | — |
| MatlWrhsStkQtyInMatlBaseUnit | decimal | YES | 18,4 | — |
| SDDocumentItem | int | YES | 10,0 | — |
| Customer | varchar | YES | 100 | — |
| MaterialBaseUnit | varchar | YES | 100 | — |
| Plant | int | YES | 10,0 | — |
| Batch | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| InventorySpecialStockType | varchar | YES | 100 | — |
| WebElementInternalID | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| MetaData | varchar | YES | -1 | — |
| UnrestrictedUseStock | varchar | YES | 100 | — |
| StockinQualityInspection | varchar | YES | 100 | — |
| Returns | varchar | YES | 100 | — |
| StockTransferStorageLocation | varchar | YES | 100 | — |
| StockTransferPlant | varchar | YES | 100 | — |
| StockinTransit | varchar | YES | 100 | — |
| BlockedStock | varchar | YES | 100 | — |
| RestrictedUseStock | varchar | YES | 100 | — |
| TiedEmpties | varchar | YES | 100 | — |
| ValuatedGoodsReceiptBlockedStock | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00B76142-70C7-4E42-A44E-06A5DB8DA99D | NULL | NULL | 2026-09-02T09:03:12.6970000 | NULL | False | False | NULL | NULL | NULL |
| 00B5B89E-9897-4225-A4A8-D0B2C6A6F04A | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 00B39715-979D-4E00-9B42-B6465433B265 | NULL | NULL | 2026-09-02T09:30:16.3970000 | NULL | False | False | NULL | NULL | NULL |
| 00AB5A2D-AD0F-4E07-855E-0145749B9D73 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 00A4C93F-57BE-4EDD-8E7B-DE0A8617D2E2 | NULL | NULL | 2026-09-02T09:05:16.4100000 | NULL | False | False | NULL | NULL | NULL |
| 0091A10E-FAED-481A-8E25-EFCD4E3EF700 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 007A3E9F-B3CC-4639-B920-51DE3769439C | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 003CDF16-AFD9-49C9-BFA1-A6544146E4D4 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 0034EB07-5D6C-4F66-AE77-33FE93C8D855 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 002740DC-9200-44AD-ACC3-CF2C66CCD1C3 | NULL | NULL | 2026-09-02T09:30:16.3970000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00B76142-70C7-4E42-A44E-06A5DB8DA99D | NULL | NULL | 2026-09-02T09:03:12.6970000 | NULL | False | False | NULL | NULL | NULL |
| 00B5B89E-9897-4225-A4A8-D0B2C6A6F04A | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 00B39715-979D-4E00-9B42-B6465433B265 | NULL | NULL | 2026-09-02T09:30:16.3970000 | NULL | False | False | NULL | NULL | NULL |
| 00AB5A2D-AD0F-4E07-855E-0145749B9D73 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 00A4C93F-57BE-4EDD-8E7B-DE0A8617D2E2 | NULL | NULL | 2026-09-02T09:05:16.4100000 | NULL | False | False | NULL | NULL | NULL |
| 0091A10E-FAED-481A-8E25-EFCD4E3EF700 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 007A3E9F-B3CC-4639-B920-51DE3769439C | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 003CDF16-AFD9-49C9-BFA1-A6544146E4D4 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 0034EB07-5D6C-4F66-AE77-33FE93C8D855 | NULL | NULL | 2026-09-02T10:00:48.3130000 | NULL | False | False | NULL | NULL | NULL |
| 002740DC-9200-44AD-ACC3-CF2C66CCD1C3 | NULL | NULL | 2026-09-02T09:30:16.3970000 | NULL | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_Inventory_Stock_Data_Tbl.Material` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.Number` (Many to One)
