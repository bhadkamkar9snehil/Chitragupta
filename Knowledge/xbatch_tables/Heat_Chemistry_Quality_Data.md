# XStudio_Xbatch.dbo.Heat_Chemistry_Quality_Data

**table_kind:** production_data

### What this table is for

- **Curated domain match (quality):** Chemistry, spectro sample, result recording, Usage Decision, Repeat Result, or quality-deviation issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** billets, cast, chemistry, core, count, data, flow, insert, quality, routing, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference sample, heat, name, per, time, ceq, chemist, date, grade, insp, inspection, instrument.

**Primary Key:** ID  
**Row Count:** 23,023  
**Date Range (ModifiedOn):** 2025-11-01T00:02:42.0000000 to 2026-07-09T07:14:45.0000000  

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
| Ceq | decimal | YES | 18,4 | — |
| W | decimal | YES | 18,4 | — |
| ReportedTime | datetime | YES | — | — |
| Nb | decimal | YES | 18,4 | — |
| HeatNo | varchar | YES | 100 | — |
| Chemist | varchar | YES | 100 | — |
| Pb | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 100 | — |
| Sn | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| Remarks | varchar | YES | -1 | — |
| Ca | decimal | YES | 18,4 | — |
| MnPerSi | decimal | YES | 18,4 | — |
| Al | decimal | YES | 18,4 | — |
| Si | decimal | YES | 18,4 | — |
| SampleType | varchar | YES | 100 | — |
| C | decimal | YES | 18,4 | — |
| Cu | decimal | YES | 18,4 | — |
| V | decimal | YES | 18,4 | — |
| N2PPM | decimal | YES | 18,4 | — |
| SampleName | varchar | YES | 100 | — |
| SampleID | varchar | YES | 36 | — |
| Section | varchar | YES | 100 | — |
| TI | decimal | YES | 18,4 | — |
| Date | datetime | YES | — | — |
| S | decimal | YES | 18,4 | — |
| SrNo | int | YES | 10,0 | — |
| Mo | decimal | YES | 18,4 | — |
| ReportDate | varchar | YES | 100 | — |
| Ni | decimal | YES | 18,4 | — |
| Cr | decimal | YES | 18,4 | — |
| Co | decimal | YES | 18,4 | — |
| MnPerS | decimal | YES | 18,4 | — |
| P | decimal | YES | 18,4 | — |
| ReceivedTime | datetime | YES | — | — |
| B | decimal | YES | 18,4 | — |
| As | decimal | YES | 18,4 | — |
| Mn | decimal | YES | 18,4 | — |
| XMLCreatedon | datetime | YES | — | — |
| MethodName | varchar | YES | 100 | — |
| Instrument | varchar | YES | 100 | — |
| Status | varchar | YES | 50 | — |
| Ag | decimal | YES | 18,4 | — |
| Bi | decimal | YES | 18,4 | — |
| Fe | decimal | YES | 18,4 | — |
| Sb | decimal | YES | 18,4 | — |
| Ta | decimal | YES | 18,4 | — |
| Zr | decimal | YES | 18,4 | — |
| Ce | decimal | YES | 18,4 | — |
| SampleNo | varchar | YES | 100 | — |
| IsLatestSample | bit | YES | — | — |
| InspectionLot | varchar | YES | 100 | — |
| IsUDStatus | bit | YES | — | — |
| RRStatus | varchar | YES | 100 | — |
| SAPTransactionID | varchar | YES | 100 | — |
| Message | varchar | YES | -1 | — |
| SAPStatus | varchar | YES | 50 | — |
| InspOper | varchar | YES | 100 | — |
| N2 | decimal | YES | 18,4 | — |
| HeatSequence | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0000F0D6-ABAF-4BAB-AAB7-4AC8E6236139 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-04-24T18:24:06.4000000 | NULL | False | False | NULL | NULL | NULL |
| 0000BAEE-C523-41DE-9AF6-18297E6D1048 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-02-19T13:34:05.1570000 | NULL | False | False | NULL | NULL | NULL |
| 000577EF-ABC4-467F-AC8F-9DB6C7BDB9F5 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2025-12-30T07:59:05.0870000 | NULL | False | False | NULL | NULL | NULL |
| 001944C6-1F77-4EF2-B63C-7EAEA9EA9050 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-01-29T19:54:05.7900000 | NULL | False | False | NULL | NULL | NULL |
| 001D8074-CD5F-490D-8135-7A31D902FCE5 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-04-29T05:59:06.4000000 | NULL | False | False | NULL | NULL | NULL |
| 001D8EC3-42E3-4747-8D2C-035BCB45BB6E | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-02-06T05:19:04.6930000 | NULL | False | False | NULL | NULL | NULL |
| 002F1CC9-F302-4804-BC9E-922E782A0FB4 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-01-06T06:44:04.6430000 | NULL | False | False | NULL | NULL | NULL |
| 0035F8E6-9F42-4465-85C3-13377C2508E8 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-01-17T20:44:03.9130000 | NULL | False | False | NULL | NULL | NULL |
| 0045E6C7-CEA8-4419-B6E7-A3B7A73D315E | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2026-02-01T16:59:04.6430000 | NULL | False | False | NULL | NULL | NULL |
| 0050819A-8F8B-4033-9936-66FD8D9521DA | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | NULL | 2025-12-19T04:44:06.0670000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BA41E60D-8A4C-497B-B345-48CA44F34171 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T21:14:05.1530000 | 2026-07-09T07:14:45.0000000 | False | False | NULL |  | NULL |
| F9EC5B70-C836-48B0-9B8D-1B7AEDEED112 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T17:46:05.2900000 | 2026-07-08T23:44:53.7330000 | False | False | NULL |  | NULL |
| 84E8FC88-FA35-411F-A030-B5DAEB95C305 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T16:50:05.3370000 | 2026-07-08T21:20:13.3930000 | False | False | NULL |  | NULL |
| 7F5A9A2A-F233-4857-878E-58B77520CD1C | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T17:42:05.3400000 | 2026-07-08T21:19:39.0000000 | False | False | NULL |  | NULL |
| 60986B2D-9925-4634-8060-F31B42087303 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T17:32:05.3870000 | 2026-07-08T21:19:24.0000000 | False | False | NULL |  | NULL |
| 18088554-E29C-4706-B991-004D2C114B79 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T16:58:05.4000000 | 2026-07-08T19:30:53.7100000 | False | False | NULL |  | NULL |
| 866419E2-B98B-4E4F-A318-4FE60E6AE5F7 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T17:18:05.3570000 | 2026-07-08T19:30:53.7100000 | False | False | NULL |  | NULL |
| 61BB6472-A2A5-4E34-8EA6-2C32C22D3EF8 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T16:45:05.4370000 | 2026-07-08T18:23:06.6930000 | False | False | NULL |  | NULL |
| B6528B57-76E9-4CE0-A576-F351F4229D07 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T16:35:05.3230000 | 2026-07-08T18:23:06.6930000 | False | False | NULL |  | NULL |
| B7B0922F-DA6E-4C68-8655-8790EC5B8610 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-07-08T16:23:05.4570000 | 2026-07-08T18:23:06.6930000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Heat_Chemistry_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.Heat_Chemistry_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Heat_Chemistry_Quality_Data.ModifiedBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_SAP_Production_Trn_Tbl.Sampleid` -> `XStudio_XBatch.Heat_Chemistry_Quality_Data.ID` (Many to One)
