# XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (sap_posting):** SAP production/consumption/by-product posting failed, pending, duplicate, or missing a material document.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** core, errors, integration, posting, routing, sap (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference document, material, date, type, creation, entry, for, goods, movement, post, posting, quantity.

**Primary Key:** ID  
**Row Count:** 11,836  
**Date Range (ModifiedOn):** 2025-12-24T17:04:38.4830000 to 2026-07-08T23:44:11.0030000  

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
| HeatNo | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Material | varchar | YES | 100 | — |
| Plant | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |
| Batch | varchar | YES | 100 | — |
| ManufacturingOrder | varchar | YES | 100 | — |
| QuantityInEntryUnit | decimal | YES | 18,3 | — |
| InspectionLot | varchar | YES | 100 | — |
| MaterialDocument | bigint | YES | 19,0 | — |
| InventoryTransactionType | varchar | YES | 100 | — |
| MaterialDocumentYear | int | YES | 10,0 | — |
| DocumentDate | datetime | YES | — | — |
| PostingDate | datetime | YES | — | — |
| CreationDate | date | YES | — | — |
| CreationTime | time | YES | — | — |
| CreatedByUser | varchar | YES | 100 | — |
| MaterialDocumentHeaderText | varchar | YES | 100 | — |
| ReferenceDocument | varchar | YES | 100 | — |
| VersionForPrintingSlip | int | YES | 10,0 | — |
| ManualPrintLsTriggered | varchar | YES | 100 | — |
| CtrlPostForWhseMgmtSyst | varchar | YES | 100 | — |
| GoodsMovementCode | varchar | YES | 100 | — |
| MaterialDocumentItem | varchar | YES | 100 | — |
| Saptransactionid | varchar | YES | 36 | — |
| GoodsMovementType | int | YES | 10,0 | — |
| EntryUnit | varchar | YES | 100 | — |
| QuantityInCount | int | YES | 10,0 | — |
| PostingMaterialType | varchar | YES | 100 | — |
| SAPPostingStatus | varchar | YES | 50 | — |
| Sampleid | varchar | YES | 36 | — |
| IsReversal | bit | YES | — | — |
| SuccessMessage | varchar | YES | 100 | — |
| IsAutoPost | bit | YES | — | — |
| Cutlength | decimal | YES | 18,2 | — |
| BilletNo | int | YES | 10,0 | — |
| SectionLength | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0031371D-7B10-4596-9F9E-A642C7919668 | NULL | NULL | NULL | NULL | 2026-02-01T05:14:10.8000000 | NULL | False | False | NULL |
| 01032A53-2131-4FBB-9D44-61720D4458AF | NULL | NULL | NULL | NULL | 2025-12-28T11:40:18.8930000 | NULL | False | False | NULL |
| 010A5D68-12FF-4587-8459-4C6CDED9EB44 | NULL | NULL | NULL | NULL | 2026-01-05T16:24:54.7270000 | NULL | False | False | NULL |
| 0128A096-C529-4D15-B8D4-37915E367F2C | NULL | NULL | NULL | NULL | 2025-12-22T15:20:14.4900000 | NULL | False | False | NULL |
| 0144A12B-5535-4A92-8212-AA76A7772839 | NULL | NULL | NULL | NULL | 2025-12-28T12:23:52.5400000 | NULL | False | False | NULL |
| 015BB3D5-D177-464C-92D2-BFF981228549 | NULL | NULL | NULL | NULL | 2026-01-30T13:18:37.3670000 | NULL | False | False | NULL |
| 01A27D83-F776-4561-8681-60DD950A2F3C | NULL | NULL | NULL | NULL | 2025-12-28T11:39:52.5030000 | NULL | False | False | NULL |
| 01E695BB-520A-4376-9019-4B19F50390D7 | NULL | NULL | NULL | NULL | 2026-01-05T14:27:39.8500000 | NULL | False | False | NULL |
| 026FA84C-0951-43AA-827B-65E42676409B | NULL | NULL | NULL | NULL | 2026-02-01T05:15:41.1700000 | NULL | False | False | NULL |
| 029C378B-7A08-4E55-8AD5-37BE1F0238DE | NULL | NULL | NULL | NULL | 2025-12-22T15:20:31.8370000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1FA2E82E-4B4E-421D-A1F6-609B994D187B | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:08.6730000 | 2026-07-08T23:44:11.0030000 | False | False | NULL |
| 94EE2D55-A833-48CB-BF84-2992BE7AB51B | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:08.5600000 | 2026-07-08T23:43:57.6330000 | False | False | NULL |
| 3924725C-CE30-420D-93C1-19A73C199F8E | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:07.5530000 | 2026-07-08T23:43:46.0470000 | False | False | NULL |
| 2C259F84-3CFF-464A-B4DD-D920DD76160E | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:07.6170000 | 2026-07-08T23:43:42.0700000 | False | False | NULL |
| 3D62C26F-BC73-4568-966C-5225E0792CF4 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:50.6200000 | 2026-07-08T23:42:41.0500000 | False | False | NULL |
| 10A76CFE-BCA1-4D78-BE5A-5A9BB021C4F4 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:50.5170000 | 2026-07-08T23:42:31.9370000 | False | False | NULL |
| 9B14BDBF-433C-4726-8AD0-A672B8D73618 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:49.4870000 | 2026-07-08T23:42:21.6270000 | False | False | NULL |
| 178DC560-64CE-4F06-B5D7-E295EC06DE80 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:23.0630000 | 2026-07-08T18:01:09.0430000 | False | False | NULL |
| D69912ED-181C-40B6-9BB7-76707C8EDFE5 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:22.9600000 | 2026-07-08T18:01:00.1100000 | False | False | NULL |
| BA3AE096-D9ED-4C56-BB0B-A6E50B76AA20 | NULL | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:21.8270000 | 2026-07-08T18:00:50.5800000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_Production_Trn_Tbl.HeatNo` -> `XStudio_XBatch.CCM_Per_Heat.HeatID` (Many to One)
- `XStudio_XBatch.MES_SAP_Production_Trn_Tbl.Sampleid` -> `XStudio_XBatch.Heat_Chemistry_Quality_Data.ID` (Many to One)
- `XStudio_XBatch.MES_SAP_Production_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_GoodsMovement_Error.TransactionID` (Many to One)
