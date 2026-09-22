# XStudio_Xbatch.dbo.XMES_API_Transaction_Summary_Fact_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (api_transaction):** API failed, response error, transaction ID mentioned, or whether an API call happened at all.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** api, core, cross, cutting, diagnostic, routing, summary, transaction (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference response, data, datetime, entity, request, action, apiname, apisource, apistatus, body, error, insertion.

**Primary Key:** ID  
**Row Count:** 44,107  
**Date Range (ModifiedOn):** 2026-03-12T17:02:45.4270000 to 2026-03-12T17:02:45.4270000  

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
| TransactionID | varchar | YES | 100 | — |
| APIName | varchar | YES | 100 | — |
| APIStatus | varchar | YES | 50 | — |
| APISource | varchar | YES | 100 | — |
| RequestedDatetime | datetime | YES | — | — |
| ResponseDatetime | datetime | YES | — | — |
| RequestURL | varchar | YES | 100 | — |
| RequestBody | varchar | YES | -1 | — |
| ResponseData | varchar | YES | -1 | — |
| ResponseDataInsertion | varchar | YES | -1 | — |
| ResponseError | varchar | YES | -1 | — |
| RecordID | varchar | YES | 100 | — |
| EntityID | varchar | YES | 100 | — |
| LVid | varchar | YES | 100 | — |
| LVName | varchar | YES | 100 | — |
| ActionUserName | varchar | YES | 100 | — |
| ResolvedEntityTable | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000A9D4D-8176-4BE2-A040-6D82C3058489 | NULL | NULL | NULL | NULL | 2026-03-05T14:16:20.3730000 | NULL | False | False | NULL |
| 000A7F97-3BD0-4CA9-89CE-AC514E5BF94F | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-04-17T14:41:16.2070000 | NULL | False | False | NULL |
| 000A3B92-514E-4857-8AA7-27895ED616E0 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-06-08T02:36:52.2430000 | NULL | False | False | NULL |
| 000A04A6-DCC4-49B7-8B0D-684BE94A9238 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-04T22:49:08.5000000 | NULL | False | False | NULL |
| 0009E47B-862A-47E2-A553-831A7EE34736 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-04-19T11:36:20.6300000 | NULL | False | False | NULL |
| 0005BC02-1684-4B95-B5AE-F277A1307E15 | NULL | NULL | NULL | NULL | 2026-03-09T20:36:01.3130000 | NULL | False | False | NULL |
| 00041152-3A0A-483E-B3FC-5351923CE03A | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | NULL | 2026-06-29T15:05:15.3200000 | NULL | False | False | NULL |
| 00040E76-62EE-49D9-9B75-9868381A3993 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-18T13:35:19.2900000 | NULL | False | False | NULL |
| 0003D508-43AE-4BC2-AD1B-CA21B9F4E98A | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-11T11:31:32.6430000 | NULL | False | False | NULL |
| 000090D1-BE7A-4D76-879C-A9504AF2AC06 | NULL | NULL | NULL | NULL | 2026-02-21T23:18:50.3070000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5CCB7F62-C05B-4494-8F8C-5B28D87E1A08 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-12T14:17:06.0630000 | 2026-03-12T17:02:45.4270000 | False | False | NULL |
| 000A9D4D-8176-4BE2-A040-6D82C3058489 | NULL | NULL | NULL | NULL | 2026-03-05T14:16:20.3730000 | NULL | False | False | NULL |
| 000A7F97-3BD0-4CA9-89CE-AC514E5BF94F | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-04-17T14:41:16.2070000 | NULL | False | False | NULL |
| 000A3B92-514E-4857-8AA7-27895ED616E0 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-06-08T02:36:52.2430000 | NULL | False | False | NULL |
| 000A04A6-DCC4-49B7-8B0D-684BE94A9238 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-04T22:49:08.5000000 | NULL | False | False | NULL |
| 0009E47B-862A-47E2-A553-831A7EE34736 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-04-19T11:36:20.6300000 | NULL | False | False | NULL |
| 0005BC02-1684-4B95-B5AE-F277A1307E15 | NULL | NULL | NULL | NULL | 2026-03-09T20:36:01.3130000 | NULL | False | False | NULL |
| 00041152-3A0A-483E-B3FC-5351923CE03A | NULL | NULL | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | NULL | 2026-06-29T15:05:15.3200000 | NULL | False | False | NULL |
| 00040E76-62EE-49D9-9B75-9868381A3993 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-18T13:35:19.2900000 | NULL | False | False | NULL |
| 0003D508-43AE-4BC2-AD1B-CA21B9F4E98A | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-05-11T11:31:32.6430000 | NULL | False | False | NULL |

---
