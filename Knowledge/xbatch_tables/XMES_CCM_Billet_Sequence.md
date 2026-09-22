# XStudio_Xbatch.dbo.XMES_CCM_Billet_Sequence

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference sequence, strand, current, heat.

**Primary Key:** ID  
**Row Count:** 8,218  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| HeatNo | varchar | YES | 100 | — |
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
| StrandNo | varchar | YES | 100 | — |
| CurrentSequence | int | YES | 10,0 | — |
| StrandSequence | int | YES | 10,0 | — |

### Top 10 Records

| ID | HeatNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00476744-8909-41C1-8ABB-09B595DB2A3C | 1603903 | NULL | NULL | 2026-07-03T12:45:35.6070000 | NULL | False | False | NULL | NULL |
| 00452016-70C2-45FA-8231-07C4A778D190 | 1603880 | NULL | NULL | 2026-07-02T13:02:37.6200000 | NULL | False | False | NULL | NULL |
| 002B49EC-5FA4-4A03-AA6B-006D094182D8 | 1603964 | NULL | NULL | 2026-07-06T12:53:23.3930000 | NULL | False | False | NULL | NULL |
| 0028CB08-AC54-4B41-96E0-BE2704FFDD12 | 1603892 | NULL | NULL | 2026-07-02T23:03:34.7300000 | NULL | False | False | NULL | NULL |
| 00281FAF-0FBC-4515-8E67-010AFB7DF781 | 1603991 | NULL | NULL | 2026-07-07T18:32:07.0730000 | NULL | False | False | NULL | NULL |
| 0026C187-E662-46A8-A1FC-A7B666B41015 | 1603972 | NULL | NULL | 2026-07-06T20:54:05.0970000 | NULL | False | False | NULL | NULL |
| 0018B906-BA84-4630-A0CE-9B0526E7709B | 1603985 | NULL | NULL | 2026-07-07T13:39:04.8670000 | NULL | False | False | NULL | NULL |
| 000CBCF5-71E0-4B2C-B920-1ECCDE1B1649 | 1604012 | NULL | NULL | 2026-07-08T16:38:34.1270000 | NULL | False | False | NULL | NULL |
| 000BE570-EE9C-46DD-AEF3-9B650AF0B2CB | 1603861 | NULL | NULL | 2026-07-01T13:31:08.8000000 | NULL | False | False | NULL | NULL |
| 0004C37B-20CD-4E90-927E-779882894A14 | 1603818 | NULL | NULL | 2026-06-29T12:13:06.5400000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | HeatNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00476744-8909-41C1-8ABB-09B595DB2A3C | 1603903 | NULL | NULL | 2026-07-03T12:45:35.6070000 | NULL | False | False | NULL | NULL |
| 00452016-70C2-45FA-8231-07C4A778D190 | 1603880 | NULL | NULL | 2026-07-02T13:02:37.6200000 | NULL | False | False | NULL | NULL |
| 002B49EC-5FA4-4A03-AA6B-006D094182D8 | 1603964 | NULL | NULL | 2026-07-06T12:53:23.3930000 | NULL | False | False | NULL | NULL |
| 0028CB08-AC54-4B41-96E0-BE2704FFDD12 | 1603892 | NULL | NULL | 2026-07-02T23:03:34.7300000 | NULL | False | False | NULL | NULL |
| 00281FAF-0FBC-4515-8E67-010AFB7DF781 | 1603991 | NULL | NULL | 2026-07-07T18:32:07.0730000 | NULL | False | False | NULL | NULL |
| 0026C187-E662-46A8-A1FC-A7B666B41015 | 1603972 | NULL | NULL | 2026-07-06T20:54:05.0970000 | NULL | False | False | NULL | NULL |
| 0018B906-BA84-4630-A0CE-9B0526E7709B | 1603985 | NULL | NULL | 2026-07-07T13:39:04.8670000 | NULL | False | False | NULL | NULL |
| 000CBCF5-71E0-4B2C-B920-1ECCDE1B1649 | 1604012 | NULL | NULL | 2026-07-08T16:38:34.1270000 | NULL | False | False | NULL | NULL |
| 000BE570-EE9C-46DD-AEF3-9B650AF0B2CB | 1603861 | NULL | NULL | 2026-07-01T13:31:08.8000000 | NULL | False | False | NULL | NULL |
| 0004C37B-20CD-4E90-927E-779882894A14 | 1603818 | NULL | NULL | 2026-06-29T12:13:06.5400000 | NULL | False | False | NULL | NULL |

---
