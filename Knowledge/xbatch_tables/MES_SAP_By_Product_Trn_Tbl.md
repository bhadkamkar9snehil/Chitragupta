# XStudio_Xbatch.dbo.MES_SAP_By_Product_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** errors, integration, posting, sap (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference document, material, date, type, creation, entry, for, goods, movement, posting, quantity, unit.

**Primary Key:** ID  
**Row Count:** 7,968  
**Date Range (ModifiedOn):** 2026-01-06T10:40:29.3800000 to 2026-07-08T23:44:50.4900000  

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
| Grade | varchar | YES | 100 | — |
| GoodsMovementCode | varchar | YES | 100 | — |
| PostingDate | datetime | YES | — | — |
| DocumentDate | datetime | YES | — | — |
| StorageLocation | varchar | YES | 100 | — |
| InspectionLot | int | YES | 10,0 | — |
| CtrlPostForWhseMgmtSyst | varchar | YES | 100 | — |
| CreatedByUser | varchar | YES | 100 | — |
| EntryUnit | varchar | YES | 100 | — |
| ManualPrintLsTriggered | varchar | YES | 100 | — |
| ReferenceDocument | varchar | YES | 100 | — |
| InventoryTransactionType | varchar | YES | 100 | — |
| Material | varchar | YES | 100 | — |
| VersionForPrintingSlip | int | YES | 10,0 | — |
| QuantityInEntryUnit | decimal | YES | 18,3 | — |
| MaterialDocumentItem | varchar | YES | 100 | — |
| QuantityInCount | int | YES | 10,0 | — |
| SAPPostingStatus | varchar | YES | 50 | — |
| CreationDate | date | YES | — | — |
| CreationTime | time | YES | — | — |
| GoodsMovementType | int | YES | 10,0 | — |
| Plant | varchar | YES | 100 | — |
| MaterialDocumentYear | int | YES | 10,0 | — |
| MaterialDocumentHeaderText | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| HeatNo | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |
| MaterialDocument | varchar | YES | 100 | — |
| Saptransactionid | varchar | YES | 36 | — |
| Batch | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| ManufacturingOrder | varchar | YES | 100 | — |
| PostingMaterialType | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Name | varchar | YES | 100 | — |
| SuccessMessage | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000730B3-5919-4000-AE93-9F7FE1683D37 | NULL | NULL | 2026-02-09T07:55:03.3030000 | NULL | False | False | NULL | NULL | NULL |
| 002A06DE-6043-424C-89D4-1395A9E94703 | NULL | NULL | 2025-12-28T12:27:25.4070000 | NULL | False | False | NULL | NULL | NULL |
| 005FE427-F5D4-4FD1-8C47-BF79782F550E | NULL | NULL | 2026-02-02T15:39:37.4670000 | NULL | False | False | NULL | NULL | NULL |
| 007A5EBC-5B6B-47E2-8800-3498677FE4F0 | NULL | NULL | 2025-12-29T06:15:57.9800000 | NULL | False | False | NULL | NULL | NULL |
| 00B2D48F-3687-42C9-AB46-721D64191ED1 | NULL | NULL | 2026-02-02T05:02:02.7100000 | NULL | False | False | NULL | NULL | NULL |
| 00CF7D01-CACA-409A-BB80-858F9157BEB8 | NULL | NULL | 2026-02-16T08:19:00.8870000 | NULL | False | False | NULL | NULL | NULL |
| 00E0F272-00C0-4519-AAE8-8B9DE54705DD | NULL | NULL | 2026-02-12T03:25:16.7770000 | NULL | False | False | NULL | NULL | NULL |
| 012A43B5-C7A9-412C-970F-68B9EC96A212 | NULL | NULL | 2025-12-31T17:37:48.9000000 | NULL | False | False | NULL | NULL | NULL |
| 012D68E0-1424-454F-8B29-47FE07328814 | NULL | NULL | 2026-02-14T19:32:03.7200000 | NULL | False | False | NULL | NULL | NULL |
| 014D9A17-FB12-4A83-8C8A-021366D854CD | NULL | NULL | 2026-02-12T03:22:28.0030000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F9D7A8F6-43AA-497A-96CD-217FF8F0E8EE | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:08.9870000 | 2026-07-08T23:44:50.4900000 | False | False | NULL | NULL | NULL |
| F3660874-9014-4823-A263-2D62594DDF29 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:08.9870000 | 2026-07-08T23:44:47.1870000 | False | False | NULL | NULL | NULL |
| 7DC44A73-4E44-4EE7-89D1-4A56836C6459 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:08.9870000 | 2026-07-08T23:44:44.0330000 | False | False | NULL | NULL | NULL |
| 902DEBA9-6FA6-431E-9B5F-C915C82C6022 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:08.9870000 | 2026-07-08T23:44:40.8500000 | False | False | NULL | NULL | NULL |
| BDC9460D-07F8-4DE0-9A48-192D98E0650E | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:50.9400000 | 2026-07-08T23:43:14.1770000 | False | False | NULL | NULL | NULL |
| 5A75BFF6-9EE1-4732-ACF9-2A21988919FA | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:50.9400000 | 2026-07-08T23:43:10.9770000 | False | False | NULL | NULL | NULL |
| 421C1CD3-252A-4CBA-A7CC-BC41C5EE5584 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:23.4200000 | 2026-07-08T18:01:42.5930000 | False | False | NULL | NULL | NULL |
| D550D62D-1544-41BC-9765-5B5AA9A66994 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:23.4200000 | 2026-07-08T18:01:39.1070000 | False | False | NULL | NULL | NULL |
| 32A32F6E-EA18-4B25-A297-0F99E641C2BF | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T16:48:43.1030000 | 2026-07-08T16:50:18.0900000 | False | False | NULL | NULL | NULL |
| CAC020A3-92D9-4D9B-911C-7CF258DEFBFA | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T16:48:43.1030000 | 2026-07-08T16:50:14.5500000 | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_By_Product_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_GoodsMovement_Error.TransactionID` (Many to One)
