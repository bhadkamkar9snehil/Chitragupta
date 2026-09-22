# XStudio_Xbatch.dbo.SMS_Production_Summary

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference best, month, date, day, ftdpercentage, ftdton, mtdpercentage, mtdton, particulars, reportdatetext, target, type.

**Primary Key:** ID  
**Row Count:** 44,051  
**Date Range (ModifiedOn):** 2026-01-06T07:55:03.0000000 to 2026-01-06T08:21:40.0000000  

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
| Reportdatetext | varchar | YES | 100 | — |
| Target | decimal | YES | 18,4 | — |
| FTDPercentage | decimal | YES | 18,4 | — |
| BestMonth | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| Particulars | varchar | YES | 36 | — |
| Type | varchar | YES | 100 | — |
| FTDTon | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| MTDTon | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| BestDay | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| UOM | varchar | YES | 36 | — |
| MTDPercentage | decimal | YES | 18,4 | — |
| BestDayDate | date | YES | — | — |
| BestMonthDate | date | YES | — | — |
| MonthYear | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00159B21-10CF-449B-AEE8-0BAB208AABB9 | NULL | NULL | 2026-02-18T06:00:11.1700000 | NULL | True | False | NULL | NULL | NULL |
| 00149CE3-6185-40BC-9E21-D2236B032C4B | NULL | NULL | 2026-04-17T04:07:40.1870000 | NULL | True | False | NULL | NULL | NULL |
| 00138E74-DA47-41B6-B068-935191FF75E5 | NULL | NULL | 2026-07-30T06:00:20.5730000 | NULL | False | False | NULL | NULL | NULL |
| 00117391-0E12-4F33-B1C5-B32219093A2B | NULL | NULL | 2026-04-22T06:00:13.8900000 | NULL | False | False | NULL | NULL | NULL |
| 00111EF2-D756-4083-959E-B6EFEF791240 | NULL | NULL | 2026-08-23T01:30:16.4300000 | NULL | True | False | NULL | NULL | NULL |
| 000F2D65-AC9D-4E7B-8108-F4122EACF07A | NULL | NULL | 2026-04-14T00:27:59.6530000 | NULL | True | False | NULL | NULL | NULL |
| 000E8D3E-571C-4D16-9FE5-4097F7E3028C | NULL | NULL | 2026-02-23T06:00:13.1470000 | NULL | False | False | NULL | NULL | NULL |
| 00091AB3-060A-4121-9BD1-E4D316236793 | NULL | NULL | 2026-02-25T10:58:00.4730000 | NULL | True | False | NULL | NULL | NULL |
| 0006F5A7-C115-481B-A64A-EAF52B5E64BF | NULL | NULL | 2026-08-16T06:00:20.8030000 | NULL | False | False | NULL | NULL | NULL |
| 000665B7-68C8-400C-8C7B-453E850E99C7 | NULL | NULL | 2026-07-31T06:00:27.3670000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FCEDD463-D149-4BFD-9861-62C6623DBC6C | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:21:40.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| B5782E20-6AF3-4066-A26F-428FCA2DDA9D | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:21:26.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 2BD8D999-F1C1-454B-BE5E-F8D1C8A40EBB | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:20:52.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 42E34B9A-0AC2-43C3-A862-DB75676D8E5A | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:20:18.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 982613DC-AC64-4587-8CF1-062B786919B8 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:19:56.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 6CC34A08-343E-4BB1-8E8D-E535BF7A5E62 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:19:29.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 6A857D34-6B05-4BF9-9B10-0A78DB1C82BA | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:19:02.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 20EB482C-391A-4324-9349-BE2F347AD9B2 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:18:43.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 89381F38-578B-40D6-B363-7603B9731584 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:18:20.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| D7D2BF06-DBD0-4B2D-951A-E91158A922DC | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-31T15:39:15.9300000 | 2026-01-06T08:17:51.0000000 | False | False | NULL | 10.76.15.11 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SMS_Production_Summary.Particulars` -> `XStudio_XBatch.Particulars_Masters.Particulars` (Many to One)
- `XStudio_XBatch.SMS_Production_Summary.Type` -> `XStudio_XBatch.Particulars_Masters.Type` (Many to One)
- `XStudio_XBatch.SMS_Production_Summary.UOM` -> `XStudio_XBatch.Particulars_Masters.UOM` (Many to One)
