# XStudio_Xbatch.dbo.xbatch_material_inventory_trn_history_tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, quantity, billet, count, external, grade, ismodified, location, lot, name, number, plant.

**Primary Key:** —  
**Row Count:** 1,225  
**Date Range (ModifiedOn):** 2026-07-18T11:23:43.6070000 to 2026-07-18T11:23:43.6070000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | — |
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
| MaterialGrade | varchar | YES | 100 | — |
| PostingMaterialType | varchar | YES | 100 | — |
| PlantName | varchar | YES | 36 | — |
| ParentID | varchar | NO | 36 | — |
| Quantity | decimal | NO | 18,3 | — |
| StorageLocation | varchar | YES | 36 | — |
| QuantityinCount | int | YES | 10,0 | — |
| UOMID | varchar | NO | 36 | — |
| LotNumber | varchar | NO | 100 | — |
| Ismodified | bit | YES | — | — |
| BilletNo | varchar | YES | 100 | — |
| isExternal | bit | YES | — | — |
| TotalQuantity | decimal | YES | 18,3 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 71198092-9314-432E-9CCF-B8285A65BAE1 | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| 7167C360-CB02-4F31-B4A3-2988F2AEA6DA | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| E2797B61-E309-4EC8-80F9-E66A2B14116D | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| 06391473-3FBE-4616-9E0E-BC68722A0300 | NULL | NULL | 2026-08-13T10:27:34.3400000 | NULL | False | False | NULL | NULL | NULL |
| 064330F5-B3A7-4A07-8F71-263EEAFA5C53 | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| 5895B326-F858-485B-AF1C-D3D358F04FA1 | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| 1BB46D56-1555-4A6F-BA19-54A40DB9B138 | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| 09E9FF43-6B93-434A-AB1F-A10A9179695B | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| 47F50E01-EEE6-4AC0-8AD1-32C825A981F8 | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |
| DAB9B7C5-C892-4DC6-BE0A-F655D16C1179 | NULL | NULL | 2026-08-07T10:00:33.7200000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E563110F-87A0-47A1-BFB6-EAC9BCA83C98 | NULL | NULL | 2026-07-07T11:33:22.6200000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| E50C20EE-366C-4345-A107-6D2462ADCF89 | NULL | NULL | 2026-07-08T14:10:04.3900000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 61B2699B-78FE-4BE2-BB91-C56DDEF92524 | NULL | NULL | 2026-07-08T10:26:36.7730000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 61A0D9EA-4F3A-43AA-8EB3-9978F5C093A4 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-07T15:48:35.8200000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 6BD4C55D-3963-4D26-89B2-1081F49D3296 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-08T14:50:43.0370000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 6BAAFB22-1A1C-4C54-B003-D706C75C3DF8 | NULL | NULL | 2026-07-07T14:12:13.9370000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 6BA7B084-26C1-4F17-B5A5-08D3E0166225 | NULL | NULL | 2026-07-06T22:20:29.0930000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 7134B1B0-E4AB-4B63-81F1-3B6396A1E630 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-07T19:40:51.0400000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| 718D738B-6B17-4B6F-8C3D-AE4C096BCBE4 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-07T17:43:20.8270000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |
| FA4297D4-A4FB-404C-B2FA-A3F40CEFD8F3 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-07-07T11:14:38.2900000 | 2026-07-18T11:23:43.6070000 | False | False | NULL | NULL | NULL |

---
