# XStudio_Xbatch.dbo.RM_Quality_Data_Summary

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference area, cross, sample, actual, agt, billet, campaign, grade, line, mtr, nom, nominal.

**Primary Key:** ID  
**Row Count:** 83,188  
**Date Range (ModifiedOn):** 2026-09-01T16:06:09.6630000 to 2026-09-02T10:48:13.6200000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Product | varchar | YES | 100 | — |
| SampleID | varchar | YES | 36 | — |
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
| SampleRecievingTime | time | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Shift | varchar | YES | 100 | — |
| Campaign | varchar | YES | 100 | — |
| Line | varchar | YES | 100 | — |
| Nom | decimal | YES | 18,4 | — |
| ActualCrossSectionalArea | decimal | YES | 18,2 | — |
| NominalCrossSectionArea | decimal | YES | 18,2 | — |
| WtMtr | decimal | YES | 18,3 | — |
| Tolerance | decimal | YES | 18,4 | — |
| YSMPa | decimal | YES | 18,0 | — |
| UTSMPa | decimal | YES | 18,0 | — |
| UTSorYSRatio | decimal | YES | 18,4 | — |
| Agt | decimal | YES | 18,4 | — |
| BilletGrade | varchar | YES | 100 | — |

### Top 10 Records

| ID | Product | SampleID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1B9ECE9E-39A6-4CF0-BB19-DB3744C2EF31 | Rebar Coil | 02A8FAC1-BF61-4725-A9E5-0CEAE0C778A8 | NULL | NULL | 2026-09-02T10:48:14.5500000 | NULL | False | False | NULL |
| CFAB6731-C127-4614-A2E4-D5DE745DB229 | Rebar | DFAFA592-9F85-423C-8A18-E4638131AC41 | NULL | NULL | 2026-09-01T09:16:41.4400000 | NULL | False | False | NULL |
| 000D54A3-A461-4B74-9EDE-877FC0FFA8E1 | Rebar | 8E11C13E-BAE1-436A-8DAC-29938A08F4FC | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 000C347E-1C02-4452-9529-593C143107B1 | Rebar | EA7B38A5-510F-46C9-8F3C-85424673E8B2 | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 000EC07A-260D-42BB-B48C-163C9E38892D | Rebar | E45D063C-C49D-4ABA-9739-A0803551CCF0 | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 00083FCC-2EC5-4974-9E74-40677273972D | Rebar | 723312EB-B549-4B84-8E98-115AE9ACAF67 | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 0014459F-F3FC-4833-98B6-E53AE5E9973C | Rebar | 8079D53F-5ACA-493A-A58C-3EE0FDA6ED94 | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 00171CAD-F6E6-4952-AD56-4A8D7EA765CF | Rebar | BAE47E80-9B4D-4CFF-AEFA-AD6FB0AE526F | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 002108F5-3591-45D1-B6A4-4DBAA3F26456 | Rebar | 0961A039-E3E2-4FED-B24A-624AF06659EF | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |
| 0025AF4D-929E-441A-83BB-85B4729ACC5B | Rebar | 1CF4F31C-AC0C-49C2-B896-52912F2A5146 | NULL | NULL | 2026-09-01T09:16:41.4400000 | 2026-09-01T16:06:09.6630000 | False | False | NULL |

### Bottom 10 Records

| ID | Product | SampleID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0008E8F5-0375-4FC0-8960-8F1A4FCFE303 | Rebar Coil | D8E22B4D-C43F-4119-B9D0-05008D0091AD | NULL | NULL | 2026-09-01T13:17:36.2670000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 000E6070-28FB-4FD3-868E-D96D1D965DF9 | Rebar Coil | 36215D57-9873-424E-8E99-36AB09E96058 | NULL | NULL | 2026-09-01T09:35:18.7600000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 0004ABA0-1F10-407F-BEAF-F65395300B4E | Rebar Coil | D680AA8A-E593-40D9-886C-F41164603FC7 | NULL | NULL | 2026-09-01T15:33:36.2370000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 0007DA93-3640-4783-AA9A-86514ACFF745 | Rebar Coil | CAAC394E-28B4-4FEC-8D9C-12EC64EEDD39 | NULL | NULL | 2026-09-02T10:47:11.5530000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 00067229-2F09-42F9-A058-CA463E50A29B | Rebar Coil | 74342533-48C0-4FA0-8ECA-62AB807B30F1 | NULL | NULL | 2026-09-01T09:35:18.7600000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 000F97BE-42F5-4653-AA4B-75A5C108406B | Rebar Coil | 47405E4E-6691-4112-A4B9-6A337E142338 | NULL | NULL | 2026-09-01T18:54:21.8730000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 000F9E3D-9641-4A4A-8F7A-F7E837D37B80 | Rebar Coil | 28A4D28F-628E-436D-BEB3-70F0E5A6F3F8 | NULL | NULL | 2026-09-01T14:26:47.3000000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 000FB379-7EA1-4DD2-89DE-4A7EC8DFA92A | Rebar Coil | 453D1F6B-C857-48A5-A3CD-982A4C9F33DF | NULL | NULL | 2026-09-02T10:23:51.0830000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 00104ECD-7044-4EEF-9CC9-F47184C0AEB8 | Rebar Coil | 7D3E8836-C23D-4E0F-9EB6-4531326585D9 | NULL | NULL | 2026-09-01T17:02:46.2470000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |
| 0010CCF5-3002-4B28-99BC-F0449F333A68 | Rebar Coil | 7BAC4A87-2EFC-43AF-A86B-EC98BC19724D | NULL | NULL | 2026-09-01T17:23:40.1530000 | 2026-09-02T10:48:13.6200000 | False | False | NULL |

---
