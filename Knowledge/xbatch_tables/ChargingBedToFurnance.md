# XStudio_Xbatch.dbo.ChargingBedToFurnance

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, billet, end, equipment, start, ton, weight, workflow.

**Primary Key:** ID  
**Row Count:** 66,871  
**Date Range (ModifiedOn):** 2026-07-30T12:52:01.9500000 to 2026-08-31T10:34:50.2430000  

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
| EquipmentID | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| WorkflowStatus | varchar | YES | 50 | — |
| BilletWeightTon | decimal | YES | 18,3 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6BC0CD39-5F35-4356-A28E-42E5028C3EE2 | NULL | NULL | NULL |  | 2026-07-30T12:51:59.8970000 | 2026-07-30T12:52:01.9500000 | False | False | NULL |
| 7032EBD9-31A2-4DE6-AA1E-6626689B088B | NULL | NULL | NULL |  | 2026-07-30T12:53:01.8730000 | 2026-07-30T12:53:18.6600000 | False | False | NULL |
| F4F80B35-7D80-4A03-BA7F-C7E59A7D7336 | NULL | NULL | NULL |  | 2026-07-30T12:52:31.6900000 | 2026-07-30T12:53:20.9400000 | False | False | NULL |
| 52DBB2F1-211E-48A8-92C9-8E66336F8445 | NULL | NULL | NULL |  | 2026-07-30T12:54:22.8070000 | 2026-07-30T12:54:39.5870000 | False | False | NULL |
| 41538B43-B9D0-418E-BD54-CBF4E4F6E861 | NULL | NULL | NULL |  | 2026-07-30T12:53:44.8400000 | 2026-07-30T12:54:41.8800000 | False | False | NULL |
| E551AC84-80E2-4C5C-A187-73853FE82FE9 | NULL | NULL | NULL |  | 2026-07-30T12:55:35.4630000 | 2026-07-30T12:55:53.9300000 | False | False | NULL |
| 46435AAC-914F-4B61-BF25-3E3D9444A128 | NULL | NULL | NULL |  | 2026-07-30T12:55:27.6370000 | 2026-07-30T12:55:55.6130000 | False | False | NULL |
| F8AA509E-49D7-48DF-AB71-4F0DE57A69AE | NULL | NULL | NULL |  | 2026-07-30T12:56:48.7130000 | 2026-07-30T12:57:05.5670000 | False | False | NULL |
| 24E7E18B-AE4B-4E83-B90A-AA805BF5D3CB | NULL | NULL | NULL |  | 2026-07-30T12:56:19.6030000 | 2026-07-30T12:57:07.8130000 | False | False | NULL |
| 1DB70CBB-EB50-40B2-B729-1BDC6CE82CDE | NULL | NULL | NULL |  | 2026-07-30T12:58:00.6630000 | 2026-07-30T12:58:17.4900000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D71489DC-162D-45F4-BA4A-B50A49F0D9F7 | NULL | NULL | NULL |  | 2026-08-31T01:22:49.5130000 | 2026-08-31T10:34:50.2430000 | False | False | NULL |
| 8121F099-1B00-4DC1-AFD0-8ADF61938F21 | NULL | NULL | NULL |  | 2026-08-31T10:34:21.1930000 | 2026-08-31T10:34:22.5570000 | False | False | NULL |
| 963EA6C0-678B-41E7-B4B1-C2812FCBA0B2 | NULL | NULL | NULL |  | 2026-08-27T03:41:59.2130000 | 2026-08-31T10:30:41.4130000 | False | False | NULL |
| C177A0D6-AC66-484F-AAC6-FAC1532D9F48 | NULL | NULL | NULL |  | 2026-08-31T03:51:35.7300000 | 2026-08-31T03:51:42.1030000 | False | False | NULL |
| 283093D9-A2FC-4916-A8C7-C09A3D9F1937 | NULL | NULL | NULL |  | 2026-08-31T03:46:54.5800000 | 2026-08-31T03:46:55.9070000 | False | False | NULL |
| 2C79C37B-AAA1-4E9D-84D3-BB53783FA4C8 | NULL | NULL | NULL |  | 2026-08-31T03:44:13.4930000 | 2026-08-31T03:44:22.6970000 | False | False | NULL |
| BB6D80C1-5F25-4749-9D72-C15B81FB2598 | NULL | NULL | NULL |  | 2026-08-31T03:43:56.5970000 | 2026-08-31T03:44:01.8600000 | False | False | NULL |
| 82978636-BB70-4F35-A808-2AFFF425BC48 | NULL | NULL | NULL |  | 2026-08-31T03:43:52.6700000 | 2026-08-31T03:43:55.1200000 | False | False | NULL |
| 7FE3B080-3DAB-4C23-9558-86257AA3A4A3 | NULL | NULL | NULL |  | 2026-08-31T03:43:27.9370000 | 2026-08-31T03:43:51.7500000 | False | False | NULL |
| 7AB3EB40-D811-408F-9AE0-82C5DC2B946A | NULL | NULL | NULL |  | 2026-08-31T03:43:25.6730000 | 2026-08-31T03:43:26.9870000 | False | False | NULL |

---
