# XStudio_Xbatch.dbo.CCM_Summary_Shift

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference strand, billet, casting, counter, oscspeed, speed, std, production, actual, count, total, billets.

**Primary Key:** ID  
**Row Count:** 5,679  
**Date Range (ModifiedOn):** 2025-08-28T17:54:06.7770000 to 2026-08-12T08:44:31.9670000  

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
| ReportDate | varchar | YES | 100 | — |
| Entrydatetime | datetime | YES | — | — |
| ShiftName | varchar | YES | 100 | — |
| STD4OSCSpeed | decimal | YES | 18,4 | — |
| Strand2BilletCounter | int | YES | 10,0 | — |
| HeatID | decimal | YES | 18,4 | — |
| Strand3BilletCounter | int | YES | 10,0 | — |
| STD6OSCSpeed | decimal | YES | 18,4 | — |
| Strand2CastingSpeed | decimal | YES | 18,4 | — |
| Strand6BilletCounter | int | YES | 10,0 | — |
| Strand1CastingSpeed | decimal | YES | 18,4 | — |
| Strand3CastingSpeed | decimal | YES | 18,4 | — |
| Strand5CastingSpeed | decimal | YES | 18,4 | — |
| STD2OSCSpeed | decimal | YES | 18,4 | — |
| TotalProduction | decimal | YES | 18,4 | — |
| STD5OSCSpeed | decimal | YES | 18,4 | — |
| Strand5BilletCounter | int | YES | 10,0 | — |
| Strand4BilletCounter | int | YES | 10,0 | — |
| Strand6CastingSpeed | decimal | YES | 18,4 | — |
| STD3OSCSpeed | decimal | YES | 18,4 | — |
| STD1OSCSpeed | decimal | YES | 18,4 | — |
| TotalBilletsCount | decimal | YES | 18,4 | — |
| Strand1BilletCounter | int | YES | 10,0 | — |
| Strand4CastingSpeed | decimal | YES | 18,4 | — |
| MTDPlannedProduction | decimal | YES | 18,4 | — |
| TodayPlannedProduction | decimal | YES | 18,4 | — |
| MonthlyTarget | decimal | YES | 18,4 | — |
| ActualBilletWeightTon | decimal | YES | 18,4 | — |
| ActualBilletCount | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000E02B3-45CE-4151-BA52-F42B1654F7AB | NULL | NULL | NULL | NULL | 2026-02-14T03:23:56.3470000 | NULL | False | False | NULL |
| 0093CF09-C776-4010-B023-2540048AA562 | NULL | NULL | NULL | NULL | 2026-06-16T18:40:02.0030000 | NULL | False | False | NULL |
| 006D649A-E478-466C-8F6C-C044C0088814 | NULL | NULL | NULL | NULL | 2026-05-21T05:03:06.5900000 | NULL | False | False | NULL |
| 006C2584-DE19-4D38-B3C7-5424AE9CCC11 | NULL | NULL | NULL | NULL | 2026-06-22T14:20:07.2230000 | NULL | False | False | NULL |
| 00639B15-3E55-4B8A-BB0A-D2616BBA5DDB | NULL | NULL | NULL | NULL | 2025-12-22T17:45:55.0930000 | NULL | False | False | NULL |
| 00637D7C-3D2E-434B-BE51-07CE88FC3C0E | NULL | NULL | NULL | NULL | 2026-06-23T08:33:08.8370000 | NULL | False | False | NULL |
| 00614035-2743-49FC-9CFE-627C57497B48 | NULL | NULL | NULL | NULL | 2026-06-05T08:56:37.2770000 | NULL | False | False | NULL |
| 0048F6AA-264D-4B4E-9F87-D1E2486F7137 | NULL | NULL | NULL | NULL | 2026-04-05T00:34:43.0070000 | NULL | False | False | NULL |
| 003DE525-09D5-4FEB-B1B4-2F393E2933BA | NULL | NULL | NULL | NULL | 2026-06-08T23:01:43.0230000 | NULL | False | False | NULL |
| 00254509-3D78-420F-A31B-5F2AA71522A7 | NULL | NULL | NULL | NULL | 2026-06-12T03:28:26.8670000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AE64C838-BD5D-4827-9456-C3E9DC36C480 | NULL | NULL | NULL | NULL | 2026-07-08T04:01:58.5230000 | 2026-08-12T08:44:31.9670000 | False | False | NULL |
| 33C25BF6-B092-4CF9-8B9E-C95F7B660BAA | NULL | NULL | NULL | NULL | 2026-07-07T06:13:22.2600000 | 2026-07-19T18:16:46.1530000 | False | False | NULL |
| 3833CD18-B40C-41DB-A650-A0DBC5582611 | NULL | NULL | NULL | NULL | 2026-02-21T02:23:33.4500000 | 2026-07-17T17:19:46.3070000 | False | False | NULL |
| 93B16134-22A1-4675-A2B4-3E1DF79A1E47 | NULL | NULL | NULL | NULL | 2026-02-20T02:24:34.2700000 | 2026-07-17T17:19:44.6600000 | False | False | NULL |
| B6E5AF11-4818-4689-8C5E-9F42B6D1C61C | NULL | NULL | NULL | NULL | 2026-02-22T02:07:22.7830000 | 2026-07-17T17:19:36.8700000 | False | False | NULL |
| FAEA135A-C6C8-4CF3-82B1-C33AB2C7EDBB | NULL | NULL | NULL | NULL | 2026-02-19T01:57:23.0070000 | 2026-07-17T17:19:29.7470000 | False | False | NULL |
| 6C3FD0E0-602D-4FFF-9EFC-0E49A7BEDCDC | NULL | NULL | NULL | NULL | 2026-02-23T02:29:33.1270000 | 2026-07-17T17:19:28.5270000 | False | False | NULL |
| 3D3315BD-CDCE-4526-AAAC-28B963AA55FB | NULL | NULL | NULL | NULL | 2026-02-24T02:23:28.4000000 | 2026-07-17T17:19:27.0330000 | False | False | NULL |
| D5621183-F2C7-4083-A010-DA57DF3865DF | NULL | NULL | NULL | NULL | 2026-02-18T02:34:57.2000000 | 2026-07-17T17:19:23.0200000 | False | False | NULL |
| 1F6B3884-C5E0-4045-ADFC-4A23ABC19E4C | NULL | NULL | NULL | NULL | 2026-02-17T01:40:35.7300000 | 2026-07-17T17:19:01.2370000 | False | False | NULL |

---
