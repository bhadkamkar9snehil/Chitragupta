# XStudio_Xbatch.dbo.XMES_SAP_PlantToPlantTransfer_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, document, date, order, type, batch, creation, entry, for, goods, issg, issuing.

**Primary Key:** ID  
**Row Count:** 2,091  
**Date Range (ModifiedOn):** 2026-02-05T16:15:11.8830000 to 2026-07-08T16:49:38.4070000  

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
| DocumentDate | datetime | YES | — | — |
| PostingDate | datetime | YES | — | — |
| MaterialDocumentHeaderText | varchar | YES | 100 | — |
| ReferenceDocument | varchar | YES | 100 | — |
| Material | varchar | YES | 100 | — |
| Plant | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |
| Batch | varchar | YES | 100 | — |
| GoodsMovementType | varchar | YES | 100 | — |
| EntryUnit | varchar | YES | 100 | — |
| QuantityInEntryUnit | varchar | YES | 100 | — |
| ManufacturingOrder | varchar | YES | 100 | — |
| Supplier | varchar | YES | 100 | — |
| Customer | varchar | YES | 100 | — |
| SalesOrder | varchar | YES | 100 | — |
| SalesOrderItem | varchar | YES | 100 | — |
| IssgOrRcvgMaterial | varchar | YES | 100 | — |
| IssgOrRcvgBatch | varchar | YES | 100 | — |
| IssuingOrReceivingPlant | varchar | YES | 100 | — |
| IssuingOrReceivingStorageLoc | varchar | YES | 100 | — |
| MaterialDocumentYear | varchar | YES | 100 | — |
| MaterialDocument | varchar | YES | 100 | — |
| InventoryTransactionType | varchar | YES | 100 | — |
| CreationDate | datetime | YES | — | — |
| CreationTime | datetime | YES | — | — |
| CreatedByUser | varchar | YES | 100 | — |
| VersionForPrintingSlip | varchar | YES | 100 | — |
| ManualPrintIsTriggered | varchar | YES | 100 | — |
| CtrlPostgForExtWhseMgmtSyst | varchar | YES | 100 | — |
| GoodsMovementCode | varchar | YES | 100 | — |
| SAPPostingStatus | varchar | YES | 50 | — |
| SAPTransactionID | varchar | YES | 100 | — |
| QuantityInCount | int | YES | 10,0 | — |
| HeatNo | int | YES | 10,0 | — |
| PostingMaterialType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01F65E83-FC2F-4F04-BAE4-56AAB374FC08 | NULL | NULL | NULL | NULL | 2026-03-06T05:08:16.2900000 | NULL | False | False | NULL |
| 025447FE-B2AA-4DDF-878A-74D728F182C6 | NULL | NULL | NULL | NULL | 2026-03-01T04:37:18.4670000 | NULL | False | False | NULL |
| 02856EE9-AE48-4622-BAB1-A88C1EA0C274 | NULL | NULL | NULL | NULL | 2026-02-13T06:30:07.5970000 | NULL | False | False | NULL |
| 02B323AB-7083-454B-8CEF-6B944452EBF6 | NULL | NULL | NULL | NULL | 2026-02-13T04:31:27.5500000 | NULL | False | False | NULL |
| 04386CC4-70E0-41B6-9F48-ABA80E3544B8 | NULL | NULL | NULL | NULL | 2026-02-09T07:51:37.9770000 | NULL | False | False | NULL |
| 0485DB22-2DE1-457A-A95E-BF052176349C | NULL | NULL | NULL | NULL | 2026-03-03T05:18:15.6030000 | NULL | False | False | NULL |
| 049FB480-54F9-4EB3-987C-8330033887E6 | NULL | NULL | NULL | NULL | 2026-02-24T23:07:00.6700000 | NULL | False | False | NULL |
| 05463994-DC6A-45FF-ACCF-1DE21ACC5E50 | NULL | NULL | NULL | NULL | 2026-03-07T05:30:44.5370000 | NULL | False | False | NULL |
| 05A728C2-0E9A-43A7-B1B3-56B5ACA751AF | NULL | NULL | NULL | NULL | 2026-03-05T21:31:59.2970000 | NULL | False | False | NULL |
| 05A7CF62-9201-4793-A6FD-40FF363AC504 | NULL | NULL | NULL | NULL | 2026-03-05T08:44:49.2330000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C26BD91E-4D4E-41C3-8AC7-4CE98232170E | NULL | NULL | NULL | NULL | 2026-07-08T16:48:41.4200000 | 2026-07-08T16:49:38.4070000 | False | False | NULL |
| 6A587072-4147-4509-857A-2990C5A84099 | NULL | NULL | NULL | NULL | 2026-07-08T15:38:52.8170000 | 2026-07-08T15:40:10.4300000 | False | False | NULL |
| 075AE440-636B-4613-8485-7025495EB03C | NULL | NULL | NULL | NULL | 2026-07-08T15:38:24.4770000 | 2026-07-08T15:39:23.9670000 | False | False | NULL |
| 8450DEBB-A1BF-46DF-B8A3-C1F708A6B52B | NULL | NULL | NULL | NULL | 2026-07-08T15:37:58.6270000 | 2026-07-08T15:38:54.7570000 | False | False | NULL |
| 1CC5AFC0-8D90-4F09-B9D7-51BB086FAEC6 | NULL | NULL | NULL | NULL | 2026-07-08T12:24:42.2500000 | 2026-07-08T12:25:32.1030000 | False | False | NULL |
| 77F9E71F-66F7-4A32-A9EB-E222CA40F71B | NULL | NULL | NULL | NULL | 2026-07-08T11:31:54.7270000 | 2026-07-08T11:33:02.0830000 | False | False | NULL |
| 861BEEFA-80CF-4453-9A2F-AB19E527C4DF | NULL | NULL | NULL | NULL | 2026-07-08T09:34:27.1130000 | 2026-07-08T09:35:19.4600000 | False | False | NULL |
| CD8749C5-7F62-4B88-9644-4D07390A6BF4 | NULL | NULL | NULL | NULL | 2026-07-08T09:32:49.7130000 | 2026-07-08T09:33:45.6500000 | False | False | NULL |
| E7850995-D138-4129-A7D8-EE6A3C22CA54 | NULL | NULL | NULL | NULL | 2026-07-08T09:32:11.6330000 | 2026-07-08T09:33:15.8030000 | False | False | NULL |
| D6F9FC55-EDB5-4D79-8E29-10CE99E06115 | NULL | NULL | NULL | NULL | 2026-07-08T07:10:52.3400000 | 2026-07-08T07:11:45.7000000 | False | False | NULL |

---
