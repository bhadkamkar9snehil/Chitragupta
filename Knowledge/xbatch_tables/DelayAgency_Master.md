# XStudio_Xbatch.dbo.DelayAgency_Master

**table_kind:** production_data

### What this table is for

- **Curated domain match (performance):** Delay, OEE, downtime, shift-delay, equipment-delay, agency-delay, or performance issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** core, delay, oee, routing (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference area, name.

**Primary Key:** ID  
**Row Count:** 23  
**Date Range (ModifiedOn):** 2025-09-02T16:32:04.0000000 to 2026-01-06T15:58:58.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
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
| AreaName | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC934F3F-1DC4-4EEE-A69A-4F44635EC2DD | Electrical | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-01T16:34:21.6470000 | 2025-09-02T16:32:04.0000000 | False | False | NULL | 172.16.100.58 |
| 0198A42E-52A8-4DAA-AD53-2B50298397AA | Mechanical | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-01T16:34:29.8830000 | 2025-09-02T16:32:09.0000000 | False | False | NULL | 172.16.100.58 |
| 3254B0D7-4DDB-4B79-9B46-73EEA2501AB3 | Operation | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-01T16:34:40.8570000 | 2025-09-02T16:32:13.0000000 | False | False | NULL | 172.16.100.58 |
| 62AD6B30-E19E-4C7D-810F-CCE411E7ED9C | Refractory | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-01T16:34:54.2600000 | 2025-09-02T16:32:22.0000000 | False | False | NULL | 172.16.100.58 |
| 4EFA97FA-9B17-421B-8F11-D3A45920903B | Other | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-01T16:34:59.9100000 | 2025-09-02T17:40:49.0000000 | False | False | NULL | 172.16.100.58 |
| AB63C24F-9C1D-4969-8DD5-2929C2EE252D | Electrical | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-02T17:41:19.1000000 | 2025-09-02T17:41:19.0000000 | False | False | NULL | 172.16.100.58 |
| B760A32F-FF04-4165-8256-DD9C43956307 | Mechanical | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-02T17:41:37.4800000 | 2025-09-02T17:41:37.0000000 | False | False | NULL | 172.16.100.58 |
| 45C22327-5C8D-48CF-9743-B58842CED1CE | Operation | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-02T17:42:25.9130000 | 2025-09-02T17:42:25.0000000 | False | False | NULL | 172.16.100.58 |
| 51864DC6-4570-415F-A502-DA71F2398F4B | Other | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-09-21T08:44:19.3070000 | 2025-09-21T08:44:19.0000000 | False | False | NULL | 172.16.2.147 |
| A8D8655D-23F3-4801-8518-85BC18A42062 | Roll Shop | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-09-21T08:44:10.8530000 | 2025-09-21T08:44:26.0000000 | False | False | NULL | 172.16.2.147 |

### Bottom 10 Records

| ID | Name | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DF8F06BE-B8AD-476D-9341-5BF56BAD36A5 | Process Requirement | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-06T15:58:58.9670000 | 2026-01-06T15:58:58.0000000 | False | False | NULL |  |
| A430E501-9682-4D58-A8BD-8ED2D6C5077A | WTP/VMD/MRSS | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-26T16:47:03.6930000 | 2025-12-26T16:47:03.0000000 | False | False | NULL | 10.76.15.11 |
| FCFF842C-1232-4EDF-B2D9-3533B3421594 | CRANE MAINT | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-26T16:46:55.0270000 | 2025-12-26T16:46:55.0000000 | False | False | NULL | 10.76.15.11 |
| FDA104D8-ADBC-42C9-A430-3E8B701D3648 | TRM | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-26T16:46:44.9970000 | 2025-12-26T16:46:44.0000000 | False | False | NULL | 10.76.15.11 |
| A92617E5-EFB8-4874-A307-FF54B5C0112B | PPC/Commercial | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-26T16:46:22.1470000 | 2025-12-26T16:46:22.0000000 | False | False | NULL | 10.76.15.11 |
| CFE8EF94-B52A-4F23-B160-DF04B7C339B5 | Std Delay | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-26T16:45:54.8430000 | 2025-12-26T16:45:54.0000000 | False | False | NULL | 10.76.15.11 |
| 27C1DB45-03C1-4309-A722-5682E9773432 | IT (Information Technology) | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-04T08:53:17.3830000 | 2025-11-04T09:09:18.0000000 | False | False | NULL | 172.16.6.41 |
| 6104A0F7-8822-49CE-A897-A6E243EE01F0 | PPC (Production Planning & Control) | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-09-21T08:45:25.4630000 | 2025-11-04T08:52:20.0000000 | False | False | NULL | 172.16.6.41 |
| ABCA42BE-3828-4DAB-84D8-58607CE7DF78 | Quality | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-09-21T08:45:40.3500000 | 2025-09-21T08:45:40.0000000 | False | False | NULL | 172.16.2.147 |
| 30E97344-C4ED-4ADA-AD8E-D956B8C51F4C | SMS | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2025-09-21T08:45:31.6600000 | 2025-09-21T08:45:31.0000000 | False | False | NULL | 172.16.2.147 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Agency_Wise_Delay.Agency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.Equipment_Wise_Delay.DelayAgency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.Agency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.AgencyAfterCAPA` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.AgencyBeforeCAPA` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.AreaName` -> `XStudio_XBatch.DelayAgency_Master.AreaName` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.DelayAgency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
