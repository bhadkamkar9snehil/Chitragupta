# XStudio_Xbatch.dbo.RMShiftDelayEntry_CAPA

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** delay, oee (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference reason, date, review, agency, action, time, capa, close, equipment, responsibility, transactionid, after.

**Primary Key:** ID  
**Row Count:** 30  
**Date Range (ModifiedOn):** 2025-11-12T15:49:28.0000000 to 2026-03-13T03:58:38.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Stepstorestartmill | varchar | YES | -1 | — |
| DelayTransactionid | varchar | YES | 36 | — |
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
| Reason1 | varchar | YES | -1 | — |
| Reason2 | varchar | YES | -1 | — |
| Reason3 | varchar | YES | -1 | — |
| Reason4 | varchar | YES | -1 | — |
| Reason5 | varchar | YES | -1 | — |
| CorrectiveAction | varchar | YES | -1 | — |
| ProposedAction | varchar | YES | -1 | — |
| Responsibility | varchar | YES | 36 | — |
| TargetDate | date | YES | — | — |
| File | varchar | YES | 8000 | — |
| CAPANO | varchar | YES | 100 | — |
| Area | varchar | YES | 100 | — |
| AgencyTransactionid | varchar | YES | 36 | — |
| Agency | varchar | YES | 36 | — |
| OpenDate | datetime | YES | — | — |
| DateofBD | date | YES | — | — |
| Equipment | varchar | YES | 36 | — |
| SubEquipment | varchar | YES | 36 | — |
| Status | varchar | YES | 50 | — |
| Close | varchar | YES | 100 | — |
| CAPACloseDate | date | YES | — | — |
| FromTime | datetime | YES | — | — |
| ToTime | datetime | YES | — | — |
| TotalTime | decimal | YES | 18,2 | — |
| AgencyBeforeCAPA | varchar | YES | 36 | — |
| AgencyAfterCAPA | varchar | YES | 36 | — |
| TypeofBD | varchar | YES | 36 | — |
| SequenceofBD | varchar | YES | -1 | — |
| ContainmentAction | varchar | YES | -1 | — |
| ImplementDate | datetime | YES | — | — |
| Photos | varchar | YES | 8000 | — |
| ListofDocument | varchar | YES | 8000 | — |
| Review | varchar | YES | -1 | — |
| ReviewResponsibility | varchar | YES | 36 | — |
| ReviewClosedBy | varchar | YES | 36 | — |
| ReviewDepartment | varchar | YES | 100 | — |
| ReviewTelephone | int | YES | 10,0 | — |
| VerifiedBy | varchar | YES | 36 | — |
| CloseDate | datetime | YES | — | — |
| NotificationNumber | int | YES | 10,0 | — |
| FunctionalLocation | varchar | YES | 100 | — |
| Component | varchar | YES | 100 | — |
| Cause | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| Remark | varchar | YES | 100 | — |
| DealyReason | varchar | YES | -1 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | Stepstorestartmill | DelayTransactionid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24192FEA-22BA-495F-B944-7DA4AE9396A8 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-12T15:49:28.7100000 | 2025-11-12T15:49:28.0000000 | False | False | NULL |
| 9214DB77-8395-4B2D-A429-17465CEBF85D | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-12T15:49:55.8000000 | 2025-11-12T15:53:12.0000000 | False | False | NULL |
| E596C7F0-237C-4F6E-AEF9-648E4B828812 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-12T15:53:39.2330000 | 2025-11-12T15:53:39.0000000 | False | False | NULL |
| 9D9F9BFB-0EFB-4A24-A452-AA71DF2A8B29 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-13T10:00:25.4170000 | 2025-11-13T10:00:25.0000000 | False | False | NULL |
| 72690152-DE34-483A-9BF9-4596C3C243C3 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-13T10:00:47.7930000 | 2025-11-13T10:00:47.0000000 | False | False | NULL |
| 4E40D9ED-17CD-4E6E-8383-C6A0695CD0A2 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-13T09:49:28.0100000 | 2025-11-13T10:01:02.0000000 | False | False | NULL |
| 8A6D5494-ACB2-49FA-9B4A-87F4CC6A2566 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-13T10:01:02.5300000 | 2025-11-13T10:01:02.0000000 | False | False | NULL |
| 9E8FE8C1-70FE-4F48-8987-CC3FACF39DF7 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-13T10:01:16.9370000 | 2025-11-13T10:01:16.0000000 | False | False | NULL |
| 95E40606-1AA6-466A-9026-E2A1A4619E41 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-13T10:02:00.4900000 | 2025-11-13T10:02:00.0000000 | False | False | NULL |
| B4C87144-9F06-42C5-B650-1A0F274EE8D6 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-13T10:02:20.5570000 | 2025-11-13T10:02:20.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Stepstorestartmill | DelayTransactionid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 53808450-9EC4-4114-B728-670AFF25C6AA | NULL | E55330AB-BD52-4677-B946-FB9BDEAF8ED1 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-03-13T03:58:38.0070000 | 2026-03-13T03:58:38.0000000 | False | False | NULL |
| F0B04C36-0709-4318-9DFE-D7A97F947E40 | NULL | 15870AFF-1D36-4DD3-91B0-071E99B81169 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-10T17:46:19.9300000 | 2026-03-10T17:47:34.4770000 | False | False | NULL |
| F0CD1425-94B2-42E2-AC26-83CE389440F3 | NULL | 5D6C6B57-634A-4CBD-BC5D-67F0979BA879 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-03-09T07:44:13.9630000 | 2026-03-09T07:44:28.8700000 | False | False | NULL |
| 0A220CA4-4244-4EC0-A309-629994982FF9 | NULL | 7A2312F6-06FF-4A43-AC44-3244A99F478D | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-01-09T16:39:11.4870000 | 2026-01-09T16:39:11.0000000 | False | False | NULL |
| 29F9DD2F-0AE4-4479-B685-785A8A871CDB | NULL | D92561C5-C353-4CE9-91BD-1192A4EE8321 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-01-09T16:35:48.6800000 | 2026-01-09T16:35:48.0000000 | False | False | NULL |
| 67C4DBF5-67BD-46E2-BA36-07D3C9FFCD1C | NULL | FC7F4BF4-B297-4180-BB6A-B23B8DABD12C | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-01-09T16:32:52.8270000 | 2026-01-09T16:32:52.0000000 | False | False | NULL |
| DD0DFDAB-3A33-45ED-8FDB-76257E9C71CA | NULL | F8D43704-0F9F-4EED-B275-1C51FC906686 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-01-09T16:27:40.1330000 | 2026-01-09T16:27:40.0000000 | False | False | NULL |
| 0FA95AF0-76A6-4B8A-B596-6F3D402C474A | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-11-14T16:22:11.9300000 | 2025-11-20T08:04:50.0000000 | False | False | NULL |
| 0EDE84FC-9E98-47CC-844A-A243D9DC6344 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-11-14T16:21:32.1100000 | 2025-11-18T14:12:28.6670000 | False | False | NULL |
| DB9F73F2-E0B1-4527-B647-CA90FBEA4068 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-11-12T10:30:52.8530000 | 2025-11-18T12:57:16.4630000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Agency_Wise_Delay.ID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.AgencyTransactionid` (One to One)
- `XStudio_XBatch.CAPA_CorrectiveAction.CAPANO` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.CAPANO` (Many to One)
- `XStudio_XBatch.CAPA_CorrectiveAction.ParentID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.ID` (Many to One)
- `XStudio_XBatch.CAPA_PreventiveAction.ParentID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.ID` (Many to One)
- `XStudio_XBatch.CAPA_ProblemSolvingTeam.ParentID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.Agency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.AgencyAfterCAPA` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.AgencyBeforeCAPA` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.DelayTransactionid` -> `XStudio_XBatch.ShiftDelayEntry.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.Equipment` -> `XStudio_XBatch.Equipment.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.ID` -> `XStudio_XBatch.CAPA_CorrectiveAction.ParentID` (One to Many)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.Photos` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.ProposedAction` -> `XStudio_XBatch.CAPA_PreventiveAction.ParentID` (One to Many)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.Responsibility` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.SubEquipment` -> `XStudio_XBatch.SubEquipment.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.ID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.DelayTransactionid` (One to One)
