# XStudio_Xbatch.dbo.Power_Consumption_Report

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference transformer, total, mill, mva, mvalosses, plant, rolling, smsaux, eaf, lrf, ngconsumption, oxygen.

**Primary Key:** ID  
**Row Count:** 245  
**Date Range (ModifiedOn):** 2026-04-15T08:35:40.9100000 to 2026-09-02T07:10:18.9300000  

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
| OxygenPlant4A | decimal | YES | 18,4 | — |
| SMSTotal | decimal | YES | 18,4 | — |
| Transformer132kv2 | decimal | YES | 18,4 | — |
| Transformer132kv1 | decimal | YES | 18,4 | — |
| Transformer63MVALosses | decimal | YES | 18,4 | — |
| Transformer33kv1 | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| WRM | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| RollingMill | decimal | YES | 18,4 | — |
| Transformer15MVA | decimal | YES | 18,4 | — |
| SMSAuxWithO2 | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| Transformer33kv2 | decimal | YES | 18,4 | — |
| TotalRollingMill | decimal | YES | 18,4 | — |
| LRF | decimal | YES | 18,4 | — |
| Transformer125MVALosses | decimal | YES | 18,4 | — |
| PlantTotal | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| SMSAuxWithoutO2 | decimal | YES | 18,4 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| EAF | decimal | YES | 18,4 | — |
| Transformer24MVA | decimal | YES | 18,4 | — |
| SMSConsumption | decimal | YES | 18,4 | — |
| TotalProduction | decimal | YES | 18,4 | — |
| RMNGConsumption | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2A6D11DC-70F8-49A1-9494-484CE612EA6D | NULL | NULL | 2026-09-02T07:10:18.9770000 | NULL | False | False | NULL | NULL | NULL |
| 370FEC98-28BF-4094-922B-0CA12BD8A7FF | NULL | NULL | 2026-02-20T16:17:29.2600000 | NULL | False | False | NULL | NULL | NULL |
| 4414E0EB-A39A-481D-A359-BDDED7C3A691 | NULL | NULL | 2026-04-17T02:05:28.5030000 | NULL | False | False | NULL | NULL | NULL |
| 5B91F148-BCA7-4C7D-8ABD-A54D33E9A44C | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:40.9100000 | False | False | NULL | NULL | NULL |
| 4B36B296-A846-48DF-91AD-1C814507BD55 | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:41.0030000 | False | False | NULL | NULL | NULL |
| 1DD9603B-AEEF-4161-920A-EBC2E38BD2F1 | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:41.0070000 | False | False | NULL | NULL | NULL |
| 3DA24599-31B0-4AB2-B35C-342B22C5C53A | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:41.0100000 | False | False | NULL | NULL | NULL |
| BDA9CAD9-DAC9-4936-B6F8-F4CC11F4CC5E | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:41.0170000 | False | False | NULL | NULL | NULL |
| 01A1547B-E335-4973-8115-EFE99C8EB82B | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:41.0200000 | False | False | NULL | NULL | NULL |
| A86656FA-7C0E-4388-ACC0-E501240D2467 | NULL | NULL | 2026-02-20T16:17:29.2600000 | 2026-04-15T08:35:41.0230000 | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C6E40E8C-2A7B-43C1-BA26-7496CF1FA6B0 | NULL | NULL | 2026-09-01T07:41:34.7130000 | 2026-09-02T07:10:18.9300000 | False | False | NULL | NULL | NULL |
| D6F86E0C-952C-423E-A46A-7B2D5952E71C | NULL | NULL | 2026-08-31T17:29:31.3400000 | 2026-09-01T07:41:34.6700000 | False | False | NULL | NULL | NULL |
| 5AC5E2CA-70E5-4FDF-9F6D-F8F9A4789836 | NULL | NULL | 2026-08-30T08:02:35.1670000 | 2026-08-31T17:29:31.2930000 | False | False | NULL | NULL | NULL |
| 195306C1-AD57-4725-8763-CB90EAAC0E07 | NULL | NULL | 2026-08-29T06:42:51.1970000 | 2026-08-30T08:02:35.1330000 | False | False | NULL | NULL | NULL |
| 9A0159F3-1B8C-4910-9017-006462257452 | NULL | NULL | 2026-08-28T06:58:53.8470000 | 2026-08-29T06:42:51.1600000 | False | False | NULL | NULL | NULL |
| 2E2BB8D0-7EDF-48C0-8E32-898802AFADDA | NULL | NULL | 2026-08-27T10:03:54.1400000 | 2026-08-28T06:58:53.8070000 | False | False | NULL | NULL | NULL |
| DD7A2BD1-E993-4F40-B747-8FCED5A2EFBB | NULL | NULL | 2026-08-26T07:23:29.3530000 | 2026-08-27T10:03:54.1000000 | False | False | NULL | NULL | NULL |
| 9B091528-2DB6-4BDC-B55D-A9C80C5E1043 | NULL | NULL | 2026-08-25T07:00:52.6500000 | 2026-08-26T07:23:29.3100000 | False | False | NULL | NULL | NULL |
| D19748A0-0EEC-4812-82FF-7C093A813C2F | NULL | NULL | 2026-08-24T06:48:42.3570000 | 2026-08-25T07:00:52.6000000 | False | False | NULL | NULL | NULL |
| 9BEFB4EA-102F-4D0A-84EF-99D7C0A4A118 | NULL | NULL | 2026-08-23T07:20:40.3770000 | 2026-08-24T06:48:42.3170000 | False | False | NULL | NULL | NULL |

---
