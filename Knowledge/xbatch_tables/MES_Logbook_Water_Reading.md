# XStudio_Xbatch.dbo.MES_Logbook_Water_Reading

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference difference, entire, fmreading, plant, common, mill, reading, rmfmreading, rmreading, scale, smsfmreading, smsreading.

**Primary Key:** ID  
**Row Count:** 244  
**Date Range (ModifiedOn):** 2026-04-11T12:21:40.0000000 to 2026-09-02T01:17:59.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| CommonFMReading | int | YES | 10,0 | — |
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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| RMFMReading | int | YES | 10,0 | — |
| SMSFMReading | int | YES | 10,0 | — |
| MillScale | decimal | YES | 18,2 | — |
| SMSScale | decimal | YES | 18,2 | — |
| EntirePlantFMReading | int | YES | 10,0 | — |
| RMReadingDifference | int | YES | 10,0 | — |
| SMSReadingDifference | int | YES | 10,0 | — |
| EntirePlantReadingDifference | int | YES | 10,0 | — |

### Top 10 Records

| ID | CommonFMReading | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 066085E7-7104-45CD-A589-EDC6CAC61B1B | 99532 | NULL | NULL | 2026-04-11T12:17:27.5130000 | NULL | False | False | NULL | NULL |
| 064E6EE1-9597-478C-9831-C461060C0181 | 146349 | NULL | NULL | 2026-04-11T12:17:27.5270000 | NULL | False | False | NULL | NULL |
| 11084400-3EA9-4817-92FA-7E7B09CC0F80 | 121432 | NULL | NULL | 2026-04-11T12:17:27.5200000 | NULL | False | False | NULL | NULL |
| 1A659390-B96D-476D-9BC1-966E37E7D1F2 | 172185 | NULL | NULL | 2026-04-11T12:17:27.5500000 | NULL | False | False | NULL | NULL |
| 1B8AFF76-9CBD-4503-B893-4340EF9AACBD | 173497 | NULL | NULL | 2026-04-11T12:17:27.5500000 | NULL | False | False | NULL | NULL |
| 1BEA073D-48D7-4892-9DCB-0AAE95CCA635 | 122147 | NULL | NULL | 2026-04-11T12:17:27.5200000 | NULL | False | False | NULL | NULL |
| 1E61D844-B051-43F5-99D0-5F658823F64C | 100550 | NULL | NULL | 2026-04-11T12:17:27.5130000 | NULL | False | False | NULL | NULL |
| 24DBA3BD-3067-4135-9F3E-1243CF74405F | 151250 | NULL | NULL | 2026-04-11T12:17:27.5300000 | NULL | False | False | NULL | NULL |
| 267097B0-0759-498A-9633-612B8172F027 | 173065 | NULL | NULL | 2026-04-11T12:17:27.5500000 | NULL | False | False | NULL | NULL |
| 2B1A55CC-FF3D-4444-B5AF-639A00DEC2D7 | 143646 | NULL | NULL | 2026-04-11T12:17:27.5270000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | CommonFMReading | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03BBC716-D4CD-428A-AFD8-325D36F2C8D5 | 304331 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-09-02T01:17:59.6400000 | 2026-09-02T01:17:59.0000000 | False | False | NULL | 10.76.12.13 |
| 0158A3A6-160E-47F9-9430-887A282F903E | 303856 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-09-01T00:51:27.8400000 | 2026-09-01T00:51:27.0000000 | False | False | NULL | 10.76.12.13 |
| 79255ABE-0302-4491-9282-A5B1B4C19150 | 303074 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-31T00:43:18.1800000 | 2026-08-31T00:43:18.0000000 | False | False | NULL | 10.76.12.13 |
| 8FD1296A-7D44-481D-B25E-9D53E1FEC151 | 303035 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-30T00:09:24.0200000 | 2026-08-30T00:09:24.0000000 | False | False | NULL | 10.76.12.13 |
| F52A3700-C931-4B9B-9B56-0606CEBBC8B4 | 303029 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-29T01:39:18.2000000 | 2026-08-29T01:39:18.0000000 | False | False | NULL | 10.76.12.13 |
| 7AB64AB1-BF4E-4D89-97E3-05E72A83BFE5 | 303008 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-28T00:20:58.2630000 | 2026-08-28T00:20:58.0000000 | False | False | NULL | 10.76.12.13 |
| 7559B9BD-CDA5-48F9-9A88-E7E310050C9B | 302941 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-27T00:16:23.7670000 | 2026-08-27T00:16:23.0000000 | False | False | NULL | 10.76.12.13 |
| FCEEFA14-2F03-462B-B216-9BC16B3B84A7 | 302691 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-26T00:16:17.9930000 | 2026-08-26T00:16:17.0000000 | False | False | NULL | 10.76.12.13 |
| 61D3675B-5EDC-44AE-8BE6-253DE94E5597 | 302070 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-25T00:21:18.6970000 | 2026-08-25T00:21:18.0000000 | False | False | NULL | 10.76.12.13 |
| 02EC77E1-6619-421A-BC97-80A6E62304E2 | 301193 | 0593A479-C644-4774-9590-5FCE23352F38 | 0593A479-C644-4774-9590-5FCE23352F38 | 2026-08-24T00:41:04.5070000 | 2026-08-24T00:41:04.0000000 | False | False | NULL | 10.76.12.13 |

---
