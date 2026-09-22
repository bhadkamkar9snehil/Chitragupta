# XStudio_Xbatch.dbo.SMS_Production_Summary_Copy

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference best, date, day, month, ftdpercentage, ftdton, mtdpercentage, mtdton, particulars, reportdatetext, target, type.

**Primary Key:** —  
**Row Count:** 10,743  
**Date Range (ModifiedOn):** 2026-01-06T07:55:03.0000000 to 2026-01-06T08:21:40.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | — |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | — |
| IsSystem | bit | YES | — | — |
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

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7612CB16-4F2B-494E-AD6D-6CB4DB514973 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| ABE068FF-ACDD-46C9-8A02-3011563C0570 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 51DED547-A7B5-474F-8284-11A72EED4267 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 6A235D86-9850-44B7-A458-67DE68ECFF4D | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 7D38537B-135F-4EF1-9726-2ECDB35CECF8 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 9CA17DF6-09B1-4EF2-B4FE-6DA32AB36A35 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 35C8D4AB-ECE2-4453-953B-4259BAF72D84 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 577A2D22-9F7A-4232-9130-D5256A18178D | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| 68960717-2A47-4949-8343-BE460B97E1D7 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |
| E768B8BF-C540-44F9-AFF5-EA338763B6D8 | NULL | NULL | 2026-02-26T06:00:08.9770000 | NULL | False | False | NULL | NULL | NULL |

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
