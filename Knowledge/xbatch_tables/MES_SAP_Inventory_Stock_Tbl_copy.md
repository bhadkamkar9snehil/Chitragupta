# XStudio_Xbatch.dbo.MES_SAP_Inventory_Stock_Tbl_copy

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference base, inventory, material, matl, sddocument, stock, type, unit, batch, customer, data, element.

**Primary Key:** —  
**Row Count:** 49,334  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | — |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | — |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | — |
| IsSystem | bit | YES | — | — |
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
| StorageLocation | int | YES | 10,0 | — |
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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000CB5D6-AAEC-4B51-8DB2-08F12DB723DD | NULL | NULL | NULL | NULL | 2026-01-09T11:00:33.1500000 | NULL | False | False | NULL |
| 000BF279-8C3F-4423-BA09-5A47F6246BA7 | NULL | NULL | NULL | NULL | 2026-01-19T11:00:29.9270000 | NULL | False | False | NULL |
| 000B0F05-E830-4525-8E07-4D27ECB8103B | NULL | NULL | NULL | NULL | 2026-01-07T11:00:26.7770000 | NULL | False | False | NULL |
| 000955E2-AA69-4E9A-91E9-17CF3338EEDD | NULL | NULL | NULL | NULL | 2026-01-20T11:00:26.8930000 | NULL | False | False | NULL |
| 0008260E-0F86-4DB2-80A2-37776E2659F7 | NULL | NULL | NULL | NULL | 2026-01-06T11:00:35.5570000 | NULL | False | False | NULL |
| 000784E8-7B86-4E96-A02D-C53657FBB7F6 | NULL | NULL | NULL | NULL | 2026-01-13T11:00:57.9300000 | NULL | False | False | NULL |
| 00073DA1-B3BC-4659-8658-56730CB50BFD | NULL | NULL | NULL | NULL | 2026-01-28T11:00:35.8930000 | NULL | False | False | NULL |
| 0006C840-BD0E-498A-936F-1CFFA86D907C | NULL | NULL | NULL | NULL | 2026-01-17T11:00:24.4000000 | NULL | False | False | NULL |
| 00048A90-9260-467A-A585-735CFD639B2A | NULL | NULL | NULL | NULL | 2026-01-26T11:00:29.7130000 | NULL | False | False | NULL |
| 0003BDC2-C6DC-4756-9A6A-E53764EF752C | NULL | NULL | NULL | NULL | 2026-01-22T11:00:39.8330000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000CB5D6-AAEC-4B51-8DB2-08F12DB723DD | NULL | NULL | NULL | NULL | 2026-01-09T11:00:33.1500000 | NULL | False | False | NULL |
| 000BF279-8C3F-4423-BA09-5A47F6246BA7 | NULL | NULL | NULL | NULL | 2026-01-19T11:00:29.9270000 | NULL | False | False | NULL |
| 000B0F05-E830-4525-8E07-4D27ECB8103B | NULL | NULL | NULL | NULL | 2026-01-07T11:00:26.7770000 | NULL | False | False | NULL |
| 000955E2-AA69-4E9A-91E9-17CF3338EEDD | NULL | NULL | NULL | NULL | 2026-01-20T11:00:26.8930000 | NULL | False | False | NULL |
| 0008260E-0F86-4DB2-80A2-37776E2659F7 | NULL | NULL | NULL | NULL | 2026-01-06T11:00:35.5570000 | NULL | False | False | NULL |
| 000784E8-7B86-4E96-A02D-C53657FBB7F6 | NULL | NULL | NULL | NULL | 2026-01-13T11:00:57.9300000 | NULL | False | False | NULL |
| 00073DA1-B3BC-4659-8658-56730CB50BFD | NULL | NULL | NULL | NULL | 2026-01-28T11:00:35.8930000 | NULL | False | False | NULL |
| 0006C840-BD0E-498A-936F-1CFFA86D907C | NULL | NULL | NULL | NULL | 2026-01-17T11:00:24.4000000 | NULL | False | False | NULL |
| 00048A90-9260-467A-A585-735CFD639B2A | NULL | NULL | NULL | NULL | 2026-01-26T11:00:29.7130000 | NULL | False | False | NULL |
| 0003BDC2-C6DC-4756-9A6A-E53764EF752C | NULL | NULL | NULL | NULL | 2026-01-22T11:00:39.8330000 | NULL | False | False | NULL |

---
