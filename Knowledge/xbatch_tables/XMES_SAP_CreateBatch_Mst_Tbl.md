# XStudio_Xbatch.dbo.XMES_SAP_CreateBatch_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference batch, date, origin, supplier, time, change, country, creation, deletion, ext, for, heat.

**Primary Key:** ID  
**Row Count:** 3,616  
**Date Range (ModifiedOn):** 2026-01-30T10:45:33.1630000 to 2026-07-08T23:43:25.1670000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Batch | varchar | YES | 100 | — |
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
| Material | varchar | YES | 100 | — |
| BatchIdentifyingPlant | varchar | YES | 100 | — |
| BatchIsMarkedForDeletion | varchar | YES | 100 | — |
| MatlBatchIsInRstrcdUseStock | varchar | YES | 100 | — |
| Supplier | varchar | YES | 100 | — |
| BatchBySupplier | varchar | YES | 100 | — |
| CountryOfOrigin | varchar | YES | 100 | — |
| RegionOfOrigin | varchar | YES | 100 | — |
| CreationDateTime | datetime | YES | — | — |
| LastChangeDateTime | datetime | YES | — | — |
| BatchExtWhseMgmtInternalId | varchar | YES | 100 | — |
| SAPTransactionID | varchar | YES | 100 | — |
| SAPPostingStatus | varchar | YES | 50 | — |
| HeatNo | int | YES | 10,0 | — |

### Top 10 Records

| ID | Batch | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 075028D4-1290-4119-A58C-C0C45AE1B65D | 1600747_12 | NULL | NULL | NULL | 2026-02-02T17:02:32.7900000 | NULL | False | False | NULL |
| 0CD2D4B2-E8AA-4C71-92D2-A558D662E71B | 1600733_12 | NULL | NULL | NULL | 2026-02-02T05:01:50.4470000 | NULL | False | False | NULL |
| 118215D4-349D-4D9B-A7D4-01D942DA8AE3 | 1600817_12 | NULL | NULL | NULL | 2026-02-05T10:11:14.0770000 | NULL | False | False | NULL |
| 11F96DBA-F943-40E4-A423-4E1F0E53DA9D | 1600754_12 | NULL | NULL | NULL | 2026-02-02T17:17:15.7870000 | NULL | False | False | NULL |
| 155EBDAD-C1A1-4311-930C-B227267662FB | 1600755_12 | NULL | NULL | NULL | 2026-02-03T09:21:30.5400000 | NULL | False | False | NULL |
| 1A01AA7B-CA94-4ED1-9D32-A3AB29D9BD5B | 1600735_12 | NULL | NULL | NULL | 2026-02-02T05:02:15.2670000 | NULL | False | False | NULL |
| 1D4C1E38-8154-4D2E-8865-557EE943D3C2 | 1600716_12 | NULL | NULL | NULL | 2026-02-01T16:54:40.7470000 | NULL | False | False | NULL |
| 21B7D442-8C91-48B2-A80E-531D75D32BFC | 1600758_12 | NULL | NULL | NULL | 2026-02-02T21:19:10.7470000 | NULL | False | False | NULL |
| 2385D99F-EBBB-4E66-A71B-AC5935CC82D9 | 1600718_12 | NULL | NULL | NULL | 2026-02-01T16:55:00.5000000 | NULL | False | False | NULL |
| 26F32321-1F2C-48FC-85C7-F2CC675CBBA1 | 1600815_12 | NULL | NULL | NULL | 2026-02-05T10:09:00.1500000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Batch | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2F44BAE9-634B-445E-A0AE-C214E32D5975 | 1604014_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:07.6770000 | 2026-07-08T23:43:25.1670000 | False | False | NULL |
| 7B498C57-0C77-4142-85E9-44E803DE17A3 | 1604014_10 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:07.6770000 | 2026-07-08T23:43:21.5670000 | False | False | NULL |
| 7E0C7971-520C-4C60-AA82-0175BD98484B | 1604013_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:49.5900000 | 2026-07-08T23:42:02.8570000 | False | False | NULL |
| 1C210747-412D-4595-AF8D-CF32899761B3 | 1604012_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:21.9000000 | 2026-07-08T18:00:30.8300000 | False | False | NULL |
| FCBCE987-E2B9-4270-ADBD-B4FAAB8DF27A | 1604011_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T16:48:41.5470000 | 2026-07-08T16:48:56.3370000 | False | False | NULL |
| 1919CE29-ADF1-4536-9F95-60574C9728AC | 1604010_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:38:52.9300000 | 2026-07-08T15:39:20.6870000 | False | False | NULL |
| B2CF0C3A-74F0-4FEB-94F8-A252D488FDB3 | 1604009_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:38:24.5930000 | 2026-07-08T15:38:30.6730000 | False | False | NULL |
| 4E4C682A-127A-4AB5-BBD9-AE8F5730060A | 1604008_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:37:58.7570000 | 2026-07-08T15:38:12.1370000 | False | False | NULL |
| D3C8BB66-7801-4318-AED5-7E100E06A95E | 1604007_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T12:24:42.3870000 | 2026-07-08T12:24:50.2670000 | False | False | NULL |
| 0A2F5CFF-7541-4AD7-AA45-46AA12D133A4 | 1604006_12 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T11:40:05.6370000 | 2026-07-08T11:40:16.5370000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_SAP_CreateBatch_Mst_Tbl.SAPTransactionID` -> `XStudio_XBatch.XMES_SAP_API_Batch_Creation_Error.TransactionID` (One to One)
