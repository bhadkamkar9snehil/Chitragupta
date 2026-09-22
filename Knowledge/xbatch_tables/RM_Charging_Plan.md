# XStudio_Xbatch.dbo.RM_Charging_Plan

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference rolling, time, billet, current, date, heat, location, material, mill, rhftime, sequence, size.

**Primary Key:** ID  
**Row Count:** 16  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| HeatNo | varchar | YES | 100 | — |
| BilletNo | varchar | YES | 100 | — |
| PO | varchar | YES | 100 | — |
| Size | varchar | YES | 100 | — |
| CurrentLocation | varchar | YES | 100 | — |
| SequenceNo | int | YES | 10,0 | — |
| RollingID | varchar | YES | 100 | — |
| RollingDate | date | YES | — | — |
| MaterialId | varchar | YES | 100 | — |
| RHFTime | datetime | YES | — | — |
| MillTime | datetime | YES | — | — |
| YardTime | datetime | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1424F30-C8F8-476D-B940-D694F568D4E2 | NULL | NULL | 2025-07-10T09:16:10.9200000 | NULL | False | False | NULL | NULL |  |
| 9875C6F8-10D6-4C83-B2D6-96C46126F366 | NULL | NULL | 2025-07-10T09:15:35.5730000 | NULL | False | False | NULL | NULL |  |
| 96FDF224-783E-4ABC-85A6-BB7CAA978BC7 | NULL | NULL | 2025-07-10T09:15:35.5730000 | NULL | False | False | NULL | NULL |  |
| 9345B933-4148-4931-A092-5B53EF5B7675 | NULL | NULL | 2025-07-10T09:17:36.8930000 | NULL | False | False | NULL | NULL |  |
| 832CB498-368C-4C21-A179-36B6A73DE782 | NULL | NULL | 2025-07-10T09:17:36.8930000 | NULL | False | False | NULL | NULL |  |
| 7F6698D8-9109-460B-A770-B4A6A8AD1CD5 | NULL | NULL | 2025-07-10T09:18:24.4230000 | NULL | False | False | NULL | NULL |  |
| 637D1A0B-BE9D-4A44-99A1-9AA53AAA5282 | NULL | NULL | 2025-07-10T09:13:55.0700000 | NULL | False | False | NULL | NULL |  |
| 55768DD4-5513-467C-9A62-A5B01A0A09FE | NULL | NULL | 2025-07-10T09:16:10.9200000 | NULL | False | False | NULL | NULL |  |
| 398AC428-FF47-42C3-A3BA-272BB41E2645 | NULL | NULL | 2025-07-10T09:15:35.5730000 | NULL | False | False | NULL | NULL |  |
| 2A85F9D6-83F0-47AF-A8A3-2FB9DF2309A2 | NULL | NULL | 2025-07-10T09:17:36.8930000 | NULL | False | False | NULL | NULL |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1424F30-C8F8-476D-B940-D694F568D4E2 | NULL | NULL | 2025-07-10T09:16:10.9200000 | NULL | False | False | NULL | NULL |  |
| 9875C6F8-10D6-4C83-B2D6-96C46126F366 | NULL | NULL | 2025-07-10T09:15:35.5730000 | NULL | False | False | NULL | NULL |  |
| 96FDF224-783E-4ABC-85A6-BB7CAA978BC7 | NULL | NULL | 2025-07-10T09:15:35.5730000 | NULL | False | False | NULL | NULL |  |
| 9345B933-4148-4931-A092-5B53EF5B7675 | NULL | NULL | 2025-07-10T09:17:36.8930000 | NULL | False | False | NULL | NULL |  |
| 832CB498-368C-4C21-A179-36B6A73DE782 | NULL | NULL | 2025-07-10T09:17:36.8930000 | NULL | False | False | NULL | NULL |  |
| 7F6698D8-9109-460B-A770-B4A6A8AD1CD5 | NULL | NULL | 2025-07-10T09:18:24.4230000 | NULL | False | False | NULL | NULL |  |
| 637D1A0B-BE9D-4A44-99A1-9AA53AAA5282 | NULL | NULL | 2025-07-10T09:13:55.0700000 | NULL | False | False | NULL | NULL |  |
| 55768DD4-5513-467C-9A62-A5B01A0A09FE | NULL | NULL | 2025-07-10T09:16:10.9200000 | NULL | False | False | NULL | NULL |  |
| 398AC428-FF47-42C3-A3BA-272BB41E2645 | NULL | NULL | 2025-07-10T09:15:35.5730000 | NULL | False | False | NULL | NULL |  |
| 2A85F9D6-83F0-47AF-A8A3-2FB9DF2309A2 | NULL | NULL | 2025-07-10T09:17:36.8930000 | NULL | False | False | NULL | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Charging_Plan.MaterialId` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
