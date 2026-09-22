# XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (sap_posting):** SAP production/consumption/by-product posting failed, pending, duplicate, or missing a material document.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** core, errors, integration, posting, routing, sap (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, document, type, date, billet, creation, entry, for, goods, inventory, movement, posting.

**Primary Key:** ID  
**Row Count:** 7,913  
**Date Range (ModifiedOn):** 2025-12-24T17:16:22.1500000 to 2026-08-26T15:56:56.3530000  

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
| InventorySpecialStockType | varchar | YES | 100 | — |
| RawMaterialRecordID | varchar | YES | 100 | — |
| FurnaceBilletStatus | varchar | YES | 100 | — |
| Cutlength | decimal | YES | 18,4 | — |
| SAPQuantity | decimal | YES | 18,3 | — |
| BilletNo | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00266854-224B-43D3-AF10-49F80E961334 | NULL | NULL | 2025-12-29T06:20:11.4830000 | NULL | False | False | NULL | NULL | NULL |
| 0093763D-F7F7-49AF-9ABA-D644D156CAA6 | NULL | NULL | 2025-12-31T19:06:51.7330000 | NULL | False | False | NULL | NULL | NULL |
| 009D1B3C-F216-40D8-8181-16157335982C | NULL | NULL | 2026-03-10T15:41:59.3470000 | NULL | False | False | NULL | NULL | NULL |
| 0149E705-618E-4342-BBFA-4AAE7AAC1868 | NULL | NULL | 2026-08-22T00:10:09.0630000 | NULL | False | False | NULL | NULL | NULL |
| 01E39C7B-AA62-4317-8AC8-2394D59B684A | NULL | NULL | 2025-12-24T12:38:49.6400000 | NULL | False | False | NULL | NULL | NULL |
| 02116ED4-C444-4FE6-AC24-2FFEAD9620A3 | NULL | NULL | 2026-01-30T09:56:58.4870000 | NULL | False | False | NULL | NULL | NULL |
| 023DCCB9-3102-4E2A-8308-59EECF45EA9B | NULL | NULL | 2026-02-08T04:42:00.8670000 | NULL | False | False | NULL | NULL | NULL |
| 025B93BE-0229-434A-8AF3-8C095D6D8AF4 | NULL | NULL | 2026-01-07T00:23:58.8470000 | NULL | False | False | NULL | NULL | NULL |
| 0281231D-79F9-4DA6-BC6F-EE21D79BF53D | NULL | NULL | 2026-01-29T18:01:23.4170000 | NULL | False | False | NULL | NULL | NULL |
| 0347B4F3-7DFB-48F0-9122-4D2B6247ACF5 | NULL | NULL | 2026-08-18T18:53:49.3500000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 98E6FD55-97DF-44E0-9D7F-68D72B7378E7 | NULL | NULL | 2026-08-26T15:56:51.4600000 | 2026-08-26T15:56:56.3530000 | False | False | NULL | NULL | NULL |
| 0C0ACE1E-2AB2-4ECA-BB10-685F781CA37C | NULL | NULL | 2026-08-26T15:56:49.9400000 | 2026-08-26T15:56:55.5070000 | False | False | NULL | NULL | NULL |
| 9BE27147-7B60-421E-B550-605394B2DFB8 | NULL | NULL | 2026-08-26T15:56:49.0870000 | 2026-08-26T15:56:54.6570000 | False | False | NULL | NULL | NULL |
| 0EC33F05-CDC5-4098-ACA1-5AADA37F9D12 | NULL | NULL | 2026-08-26T15:56:48.2000000 | 2026-08-26T15:56:53.8130000 | False | False | NULL | NULL | NULL |
| DA41EA20-924B-4655-B823-D9902EC645A0 | NULL | NULL | 2026-08-26T15:56:47.3470000 | 2026-08-26T15:56:52.7930000 | False | False | NULL | NULL | NULL |
| 3E307370-5598-40D8-B994-4513CB1844B7 | NULL | NULL | 2026-08-26T15:56:46.5070000 | 2026-08-26T15:56:51.2730000 | False | False | NULL | NULL | NULL |
| 553B33E0-A45D-4A50-A8D7-3720A5F5B74A | NULL | NULL | 2026-08-26T15:56:45.8100000 | 2026-08-26T15:56:49.8770000 | False | False | NULL | NULL | NULL |
| B7053D2F-9699-4DDA-B5D2-ECE6699473C9 | NULL | NULL | 2026-08-26T15:56:44.9430000 | 2026-08-26T15:56:49.0230000 | False | False | NULL | NULL | NULL |
| 936EE275-EBFC-4B1C-B5D0-7D0734068463 | NULL | NULL | 2026-08-26T15:56:44.1100000 | 2026-08-26T15:56:48.1300000 | False | False | NULL | NULL | NULL |
| 721705D2-C126-4E30-962C-78B195A86776 | NULL | NULL | 2026-08-26T15:56:43.2530000 | 2026-08-26T15:56:47.2900000 | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_Consumption_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_GoodsMovement_Error.TransactionID` (Many to One)
