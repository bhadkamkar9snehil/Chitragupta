# XStudio_Xbatch.dbo.Grade_FillSample_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference acceptable, limit, name, characteristic, gradename, lower, observation, test, upper, value.

**Primary Key:** ID  
**Row Count:** 25,970  
**Date Range (ModifiedOn):** 2025-08-20T10:09:15.0000000 to 2025-08-23T11:24:15.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CharacteristicName | varchar | YES | 100 | — |
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
| Value | decimal | YES | 18,4 | — |
| AcceptableLowerLimit | decimal | YES | 18,4 | — |
| AcceptableUpperLimit | decimal | YES | 18,4 | — |
| Observation | varchar | YES | 36 | — |
| TestName | varchar | YES | 100 | — |
| Gradename | varchar | YES | 36 | — |

### Top 10 Records

| ID | CharacteristicName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002B1E58-80FC-4E6F-A2EC-E30F36866E2E | % Mn | 8EC3E245-BC1C-454F-904C-708E0CCEB1B3 | NULL | NULL | 2025-11-04T03:04:22.0400000 | NULL | False | False | NULL |
| 0023BF62-824D-4121-83A3-2526911776DF | % S | 15326F05-5F4B-410F-99B5-19B3375313A2 | NULL | NULL | 2025-11-14T19:23:57.2830000 | NULL | False | False | NULL |
| 001EE273-780F-45EA-AF37-A760D8EF565C | % Ni | A8703E69-7C12-4318-BF88-32174DD61A3B | NULL | NULL | 2025-08-19T18:15:29.6200000 | NULL | False | False | NULL |
| 001600ED-A6C6-466B-A75D-564E0297D3F7 | % S | 3E79AB36-1B9E-490A-B670-EA0390E4C679 | NULL | NULL | 2025-08-21T05:57:19.9300000 | NULL | False | False | NULL |
| 00146261-0D96-4AA5-9862-13EA6A7A7702 | C | 045BC472-3568-4C95-B5AD-281FEBD2BA6F | NULL | NULL | 2025-08-30T22:44:58.6170000 | NULL | False | False | NULL |
| 0013EC6D-CA2F-4087-A78B-2ABE9F614034 | % P | ABF41AEC-BF8E-4F72-809B-1A4DC73B5153 | NULL | NULL | 2025-08-22T16:28:00.7470000 | NULL | False | False | NULL |
| 000D9882-514F-4EAC-AF8B-A50B4F161B34 | C | 893EEAAD-2C30-4E27-8A6F-D9FFA9BCF5DA | NULL | NULL | 2025-11-17T22:13:32.9430000 | NULL | False | False | NULL |
| 000BBC0D-7FC5-43FE-858C-02266A46A252 | % Si | 781CB401-6F61-442F-ADC8-EAF37C9A7F1A | NULL | NULL | 2025-10-19T20:05:13.4230000 | NULL | False | False | NULL |
| 000558BC-7351-4016-B87A-E6AE2E98C9EB | % C | 256615A5-1609-44F0-9222-C70B1A874A57 | NULL | NULL | 2025-11-18T15:37:42.9800000 | NULL | False | False | NULL |
| 0003604A-15C4-4D9F-8344-6DF3503C2B5F | % JNi | 69B4246C-3863-4F02-AF02-25AB2CDEBE79 | NULL | NULL | 2025-11-05T12:05:37.7270000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | CharacteristicName | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13AF348E-EC0D-4642-95D6-0691FEEF9F49 | % JNi | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| 2DB09C19-E7EF-498B-B575-1A7207B73551 | % Mn | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| 419D9861-05BE-40F5-8707-8749B4215F4E | Mn | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| 63CA8FEF-9B8A-4DA4-8D70-BE49FCEF5BED | Si | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| 65D06808-CD61-4382-803C-54D69A0B19D0 | % Si | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| 79046052-209E-44AD-BD25-C80ABCEC8475 | ng | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| 83D17DF6-4568-4F34-81B1-BA825155A407 | C | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| AA97AB84-039E-4D17-9ECE-B4F1C59843E3 | % P | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| AC14AA7D-32E2-444E-8AE6-9F443038C4D5 | c1 | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |
| ADA23756-3355-4AC8-A11C-3B27B9BACE95 | % S | 50C8E783-A870-4007-8602-913197104976 | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-23T10:06:13.2200000 | 2025-08-23T11:24:15.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Grade_FillSample_Data.ParentID` -> `XStudio_XBatch.Steel_Grade_Master.ID` (Many to One)
