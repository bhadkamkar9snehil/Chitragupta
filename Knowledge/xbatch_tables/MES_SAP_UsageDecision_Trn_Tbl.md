# XStudio_Xbatch.dbo.MES_SAP_UsageDecision_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (quality):** Chemistry, spectro sample, result recording, Usage Decision, Repeat Result, or quality-deviation issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** chemistry, core, errors, integration, posting, quality, routing, sap, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference code, dec, heat, inspection, lot, material, message, sapposting, saptransaction, status, type, usg.

**Primary Key:** ID  
**Row Count:** 4,883  
**Date Range (ModifiedOn):** 2026-02-05T09:29:41.8000000 to 2026-07-08T23:45:00.7830000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| InspectionLot | varchar | YES | 100 | — |
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
| UsgDecCode | varchar | YES | 100 | — |
| Message | varchar | YES | 100 | — |
| SAPPostingStatus | varchar | YES | 50 | — |
| SAPTransactionID | varchar | YES | 100 | — |
| HeatNo | int | YES | 10,0 | — |
| MaterialType | varchar | YES | 100 | — |

### Top 10 Records

| ID | InspectionLot | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10320FD6-D8D8-4059-938C-F97D94F480B8 | 40002770663 | NULL | NULL | NULL | 2026-02-16T07:44:37.3830000 | NULL | False | False | NULL |
| 11895E2A-DAC1-4AC5-A033-59421CD231FD | 40002998512 | NULL | NULL | NULL | 2026-03-10T13:56:47.7370000 | NULL | False | False | NULL |
| 15429BBA-2E09-4062-8B56-370D0180CAE5 | 40002996511 | NULL | NULL | NULL | 2026-02-05T10:09:57.0770000 | NULL | False | False | NULL |
| 1B784348-6143-44D0-A25C-BE1F37E4BD03 | 40002996241 | NULL | NULL | NULL | 2026-02-02T21:20:09.2900000 | NULL | False | False | NULL |
| 1F3923AE-BC1C-47B9-B129-9329188D9628 | 40002996249 | NULL | NULL | NULL | 2026-02-03T01:39:30.3700000 | NULL | False | False | NULL |
| 2436D993-1B80-4F7B-810E-D969B762657C | 40002996479 | NULL | NULL | NULL | 2026-02-04T18:03:04.1270000 | NULL | False | False | NULL |
| 2775D598-1B84-472C-A055-67168314F8E2 | 40002996284 | NULL | NULL | NULL | 2026-02-03T10:27:37.2500000 | NULL | False | False | NULL |
| 293071BB-7CAF-443E-A424-793A53A1A835 | 40002996453 | NULL | NULL | NULL | 2026-02-04T16:35:21.8400000 | NULL | False | False | NULL |
| 29E828E0-88E2-4941-861F-779F1E429F67 | 40002996270 | NULL | NULL | NULL | 2026-02-03T09:31:23.0930000 | NULL | False | False | NULL |
| 2DC2AC92-5B19-4C2F-BB7F-DE26047F71AD | 40002996491 | NULL | NULL | NULL | 2026-02-05T03:16:56.3130000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | InspectionLot | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 320F6D4E-FC60-413B-ADA7-67BBDB57A820 | 40004283079 | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T23:44:31.0170000 | 2026-07-08T23:45:00.7830000 | False | False | NULL |
| 6FE2071F-4ED4-4AC7-B2C3-ADA31DC81515 | 40004282950 | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T21:19:59.0030000 | 2026-07-08T21:20:22.1370000 | False | False | NULL |
| AEBC8141-80CD-4A44-96C8-3F3FDF1CC093 | 40004282913 | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T16:50:14.6170000 | 2026-07-08T16:50:34.7300000 | False | False | NULL |
| 81CEF8B5-9376-41A0-B189-A3EADB307457 | 40004282912 | NULL | NULL | NULL | 2026-07-08T16:49:15.3100000 | 2026-07-08T16:49:24.8830000 | False | False | NULL |
| 2090B386-1685-451D-A615-63D46452A0EE | 40004282873 | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T15:40:40.7430000 | 2026-07-08T15:40:59.9670000 | False | False | NULL |
| 5413A682-F458-4840-91FE-A9C9A61A507E | 40004282869 | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T15:40:27.0370000 | 2026-07-08T15:40:50.0130000 | False | False | NULL |
| 2601CDA9-0514-41DA-A8F1-A299BCF8061E | 40004282872 | NULL | NULL | NULL | 2026-07-08T15:39:51.2400000 | 2026-07-08T15:40:00.2000000 | False | False | NULL |
| 9ECE6113-8EF5-41DE-9F63-445DAEB9B7AE | 40004282867 | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T15:39:30.1200000 | 2026-07-08T15:39:54.6930000 | False | False | NULL |
| 039756C8-A963-4532-A9D7-91770A0CB654 | 40004282868 | NULL | NULL | NULL | 2026-07-08T15:38:51.2200000 | 2026-07-08T15:39:13.7970000 | False | False | NULL |
| 329A2508-DF2F-4EB3-9678-76AEE31D9715 | 40004282866 | NULL | NULL | NULL | 2026-07-08T15:38:34.9870000 | 2026-07-08T15:38:44.0130000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_UsageDecision_Trn_Tbl.SAPTransactionID` -> `XStudio_XBatch.XMES_SAP_API_UsageDecision_Error.TransactionID` (One to One)
