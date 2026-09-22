# XStudio_Xbatch.dbo.Quality_Spectro_Result

**table_kind:** production_data

### What this table is for

- **Curated domain match (quality):** Chemistry, spectro sample, result recording, Usage Decision, Repeat Result, or quality-deviation issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference limit, result, type, element, line, max, min, name, replicate, sample, stat, status.

**Primary Key:** ID  
**Row Count:** 19,55,354  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| LineName | varchar | YES | 100 | — |
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
| ReplicateNo | int | YES | 10,0 | — |
| Element | varchar | YES | 100 | — |
| ResultType | varchar | YES | 100 | — |
| StatType | varchar | YES | 100 | — |
| ResultValue | decimal | YES | 18,4 | — |
| Unit | varchar | YES | 20 | — |
| Status | varchar | YES | 100 | — |
| MinLimit | decimal | YES | 18,4 | — |
| MaxLimit | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | LineName | SampleID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00004CC8-CB9B-4493-8525-B5A4248F6846 | S | 5306EDC1-C458-4B68-A19F-2C4D63C2F3D1 | NULL | NULL | 2026-05-26T10:04:05.5330000 | NULL | False | False | NULL |
| 00003E29-F9D3-4469-BD74-00A6EB9E8B2A | Ta | DA73A0E3-041B-4C6B-8A16-EF172982ECA9 | NULL | NULL | 2026-04-08T11:19:04.5130000 | NULL | False | False | NULL |
| 0000362C-E652-4B30-A4AE-5A716D846E66 | Cu | C6404106-171C-41A9-B913-F15D782CDEAE | NULL | NULL | 2026-04-22T22:34:05.6830000 | NULL | False | False | NULL |
| 000031E2-5B0D-4D89-8D17-6AC475CF318F | P | A5882091-E1C6-4DEB-B4C7-C7B6DC5F66E0 | NULL | NULL | 2026-02-26T10:34:05.6270000 | NULL | False | False | NULL |
| 00002FCE-9F0C-4B73-A1D6-B9B898D5F923 | Zr | 0EBBB312-E9F5-43C4-9A97-979770A5673C | NULL | NULL | 2026-03-01T15:14:05.4100000 | NULL | False | False | NULL |
| 00002DB0-BD75-4325-BCAD-282427E98C63 | Si | 9619B93F-7C46-481D-BACA-03B2B884FB43 | NULL | NULL | 2026-07-05T15:40:04.0670000 | NULL | False | False | NULL |
| 00002881-AD1E-45E6-83EC-2EE515E1437B | Mn | 8BA66E5F-5994-4D99-BCBC-72D1861513F3 | NULL | NULL | 2026-06-03T10:30:04.4600000 | NULL | False | False | NULL |
| 0000255D-0E16-4E82-9A91-9418964F5ED2 | Fe | 5E7F5EDC-C9A9-4D99-AAA2-B1737215121E | NULL | NULL | 2026-04-05T05:29:04.1270000 | NULL | False | False | NULL |
| 000014AF-A020-482B-BECF-E52E0BC956D7 | Mn/Si | 0B279446-74AC-4AF8-8BA4-75F985B2B576 | NULL | NULL | 2026-03-12T20:29:05.1070000 | NULL | False | False | NULL |
| 00001132-F469-4D78-9DCD-8817AA798B96 | Cu | E0570F26-6BC5-4AF8-ADA9-B0A019CBCA81 | NULL | NULL | 2026-03-26T08:34:05.8300000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | LineName | SampleID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00004CC8-CB9B-4493-8525-B5A4248F6846 | S | 5306EDC1-C458-4B68-A19F-2C4D63C2F3D1 | NULL | NULL | 2026-05-26T10:04:05.5330000 | NULL | False | False | NULL |
| 00003E29-F9D3-4469-BD74-00A6EB9E8B2A | Ta | DA73A0E3-041B-4C6B-8A16-EF172982ECA9 | NULL | NULL | 2026-04-08T11:19:04.5130000 | NULL | False | False | NULL |
| 0000362C-E652-4B30-A4AE-5A716D846E66 | Cu | C6404106-171C-41A9-B913-F15D782CDEAE | NULL | NULL | 2026-04-22T22:34:05.6830000 | NULL | False | False | NULL |
| 000031E2-5B0D-4D89-8D17-6AC475CF318F | P | A5882091-E1C6-4DEB-B4C7-C7B6DC5F66E0 | NULL | NULL | 2026-02-26T10:34:05.6270000 | NULL | False | False | NULL |
| 00002FCE-9F0C-4B73-A1D6-B9B898D5F923 | Zr | 0EBBB312-E9F5-43C4-9A97-979770A5673C | NULL | NULL | 2026-03-01T15:14:05.4100000 | NULL | False | False | NULL |
| 00002DB0-BD75-4325-BCAD-282427E98C63 | Si | 9619B93F-7C46-481D-BACA-03B2B884FB43 | NULL | NULL | 2026-07-05T15:40:04.0670000 | NULL | False | False | NULL |
| 00002881-AD1E-45E6-83EC-2EE515E1437B | Mn | 8BA66E5F-5994-4D99-BCBC-72D1861513F3 | NULL | NULL | 2026-06-03T10:30:04.4600000 | NULL | False | False | NULL |
| 0000255D-0E16-4E82-9A91-9418964F5ED2 | Fe | 5E7F5EDC-C9A9-4D99-AAA2-B1737215121E | NULL | NULL | 2026-04-05T05:29:04.1270000 | NULL | False | False | NULL |
| 000014AF-A020-482B-BECF-E52E0BC956D7 | Mn/Si | 0B279446-74AC-4AF8-8BA4-75F985B2B576 | NULL | NULL | 2026-03-12T20:29:05.1070000 | NULL | False | False | NULL |
| 00001132-F469-4D78-9DCD-8817AA798B96 | Cu | E0570F26-6BC5-4AF8-ADA9-B0A019CBCA81 | NULL | NULL | 2026-03-26T08:34:05.8300000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Quality_Spectro_Result.SampleID` -> `XStudio_XBatch.Quality_Spectro_Sample.ID` (Many to One)
