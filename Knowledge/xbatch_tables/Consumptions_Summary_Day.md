# XStudio_Xbatch.dbo.Consumptions_Summary_Day

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference transformer, mva, eaf, lrf, mill, oxygen, plant, rolling, wrm.

**Primary Key:** ID  
**Row Count:** 1,348  
**Date Range (ModifiedOn):** 2025-07-23T13:17:32.8970000 to 2026-09-02T07:12:11.6570000  

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
| LRF | decimal | YES | 18,4 | — |
| Transformer33kv2 | decimal | YES | 18,4 | — |
| Transformer24MVA | decimal | YES | 18,4 | — |
| OxygenPlant4A | decimal | YES | 18,4 | — |
| RollingMill | decimal | YES | 18,4 | — |
| EAF | decimal | YES | 18,4 | — |
| Transformer132kv1 | decimal | YES | 18,4 | — |
| WRM | decimal | YES | 18,4 | — |
| Transformer132kv2 | decimal | YES | 18,4 | — |
| Transformer15MVA | decimal | YES | 18,4 | — |
| Transformer33kv1 | decimal | YES | 18,4 | — |
| Transformer132kv2_YD | decimal | YES | 18,4 | — |
| OxygenPlant4A_YD | decimal | YES | 18,4 | — |
| Transformer15MVA_YD | decimal | YES | 18,4 | — |
| RollingMill_YD | decimal | YES | 18,4 | — |
| Transformer24MVA_YD | decimal | YES | 18,4 | — |
| LRF_YD | decimal | YES | 18,4 | — |
| WRM_YD | decimal | YES | 18,4 | — |
| Transformer132kv1_YD | decimal | YES | 18,4 | — |
| Transformer33kv1_YD | decimal | YES | 18,4 | — |
| EAF_YD | decimal | YES | 18,4 | — |
| Transformer33kv2_YD | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0154074F-A452-43EC-A017-BFB0FE796A85 | NULL | NULL | NULL | NULL | 2026-02-26T00:34:01.4170000 | NULL | False | False | NULL |
| 013EE9BC-8E3F-4FDD-9ED1-DCDC2AC5A51A | NULL | NULL | NULL | NULL | 2026-04-09T08:32:45.3100000 | NULL | False | False | NULL |
| 009AF2F1-14A3-45C8-ADA2-38003D884A97 | NULL | NULL | NULL | NULL | 2026-02-09T13:17:32.7200000 | NULL | False | False | NULL |
| 020D9C28-9C1D-42E3-815A-FC98F8D6405E | NULL | NULL | NULL | NULL | 2026-06-03T00:32:42.4900000 | NULL | False | False | NULL |
| 02932C41-AE2C-499A-9031-29B384AAE2C8 | NULL | NULL | NULL | NULL | 2026-09-01T07:41:37.4330000 | NULL | False | False | NULL |
| 0383336F-9B21-4862-815F-C6FC50AA8984 | NULL | NULL | NULL | NULL | 2026-02-10T16:53:59.1070000 | NULL | False | False | NULL |
| 039924EF-BE80-4180-8F04-A562214FD9FE | NULL | NULL | NULL | NULL | 2026-02-16T14:19:34.8100000 | NULL | False | False | NULL |
| 04750B90-381E-498A-B0CE-81540C7F5C09 | NULL | NULL | NULL | NULL | 2026-02-10T16:55:49.2100000 | NULL | False | False | NULL |
| 0499E7B1-3B6F-4ABA-AA36-03F48BDBFAAC | NULL | NULL | NULL | NULL | 2026-02-07T11:54:57.6470000 | NULL | False | False | NULL |
| 05D1D8E5-F2BC-445B-8477-AD7AEF8D50AE | NULL | NULL | NULL | NULL | 2026-04-21T04:18:52.5770000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B8AB25DB-1B63-4D05-9FB7-5D64551F2796 | NULL | NULL | NULL | NULL | 2026-09-02T07:10:21.4930000 | 2026-09-02T07:12:11.6570000 | False | False | NULL |
| 55C18880-EFAA-47C7-9267-89B425B409E9 | NULL | NULL | NULL | NULL | 2026-09-01T07:41:37.4170000 | 2026-09-01T07:43:37.5600000 | False | False | NULL |
| 67D3CFF9-221D-4B64-901D-0A71811D01B3 | NULL | NULL | NULL | NULL | 2026-08-31T17:29:33.4770000 | 2026-08-31T17:31:23.5630000 | False | False | NULL |
| E1770C04-4391-4A11-B8D9-FB9A65DE134E | NULL | NULL | NULL | NULL | 2026-08-30T08:02:37.9600000 | 2026-08-30T08:04:48.1030000 | False | False | NULL |
| AD0553D8-0A1B-43A5-9CE4-1D151195E4EA | NULL | NULL | NULL | NULL | 2026-08-29T06:42:53.4470000 | 2026-08-29T06:54:54.1230000 | False | False | NULL |
| 350457CC-7EC9-4D14-9E46-7A0A9F9DD1F8 | NULL | NULL | NULL | NULL | 2026-08-27T10:03:55.9970000 | 2026-08-28T07:09:47.1400000 | False | False | NULL |
| 4407F44B-05F7-4AB9-BAB3-4CDB8DC50B68 | NULL | NULL | NULL | NULL | 2026-08-28T06:58:56.5630000 | 2026-08-28T07:09:47.1400000 | False | False | NULL |
| E4A348A5-B8C2-4698-89C8-04C3429548E0 | NULL | NULL | NULL | NULL | 2026-08-26T07:23:31.1500000 | 2026-08-26T07:25:31.3730000 | False | False | NULL |
| 59781158-1FBB-4CCC-95E1-0DB5C49D0CBA | NULL | NULL | NULL | NULL | 2026-08-25T07:00:55.3400000 | 2026-08-25T07:03:45.5130000 | False | False | NULL |
| D9EFE740-AF18-4928-9925-FE86C673BBF2 | NULL | NULL | NULL | NULL | 2026-08-24T06:48:50.6900000 | 2026-08-24T06:51:00.8130000 | False | False | NULL |

---
