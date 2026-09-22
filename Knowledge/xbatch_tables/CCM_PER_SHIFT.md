# XStudio_Xbatch.dbo.CCM_PER_SHIFT

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference strand, billet, casting, counter, flow, speed, zone, time, tap, argon, end, equipment.

**Primary Key:** ID  
**Row Count:** 12  

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
| EquipmentID | varchar | YES | 36 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| TapToTapTime | decimal | YES | 18,4 | — |
| Argon | decimal | YES | 18,4 | — |
| Strand1Zone1Flow | decimal | YES | 18,4 | — |
| Strand2Zone1Flow | decimal | YES | 18,4 | — |
| Strand3Zone1Flow | decimal | YES | 18,4 | — |
| Strand4Zone1Flow | decimal | YES | 18,4 | — |
| Strand5Zone1Flow | decimal | YES | 18,4 | — |
| Strand6Zone1Flow | decimal | YES | 18,4 | — |
| Strand1CastingSpeed | decimal | YES | 18,4 | — |
| Strand2CastingSpeed | decimal | YES | 18,4 | — |
| Strand3CastingSpeed | decimal | YES | 18,4 | — |
| Strand4CastingSpeed | decimal | YES | 18,4 | — |
| Strand5CastingSpeed | decimal | YES | 18,4 | — |
| Strand6CastingSpeed | decimal | YES | 18,4 | — |
| Strand1BilletCounter | decimal | YES | 18,4 | — |
| Strand2BilletCounter | decimal | YES | 18,4 | — |
| Strand3BilletCounter | decimal | YES | 18,4 | — |
| Strand4BilletCounter | decimal | YES | 18,4 | — |
| Strand5BilletCounter | decimal | YES | 18,4 | — |
| Strand6BilletCounter | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 997F494D-2CA6-425C-B7BE-903FABC4FA33 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T14:06:14.8830000 | NULL | False | False | NULL |
| 91D532EF-51AD-4CE6-93AC-F90F27874C83 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:53:42.8270000 | NULL | False | False | NULL |
| 8EC69D03-C071-40F7-A104-CE420E76D7F8 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:42:27.7270000 | NULL | False | False | NULL |
| 8E3E7DED-8973-4B0B-927A-415C99D0F6F3 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:47:06.0070000 | NULL | False | False | NULL |
| 55750D37-A700-44D1-87FF-11B78FEEDF63 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:15:03.8200000 | NULL | False | False | NULL |
| 5470BE6F-EE97-4BB9-80F2-3FD7558745E5 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T14:06:57.9530000 | NULL | False | False | NULL |
| 3F694E50-136F-43E3-8009-CEA4FD4FBE64 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T14:04:34.1700000 | NULL | False | False | NULL |
| 0ED87DEB-81DB-4852-B402-C51D8B1215A3 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:49:04.8130000 | NULL | False | False | NULL |
| 0A9BB3CA-8D09-4D43-B8D7-60AA36439A2C | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:57:11.2170000 | NULL | False | False | NULL |
| 09C9B5D7-8B5A-48B3-9AE2-1FB9DF00587D | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:26:04.2000000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 997F494D-2CA6-425C-B7BE-903FABC4FA33 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T14:06:14.8830000 | NULL | False | False | NULL |
| 91D532EF-51AD-4CE6-93AC-F90F27874C83 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:53:42.8270000 | NULL | False | False | NULL |
| 8EC69D03-C071-40F7-A104-CE420E76D7F8 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:42:27.7270000 | NULL | False | False | NULL |
| 8E3E7DED-8973-4B0B-927A-415C99D0F6F3 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:47:06.0070000 | NULL | False | False | NULL |
| 55750D37-A700-44D1-87FF-11B78FEEDF63 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:15:03.8200000 | NULL | False | False | NULL |
| 5470BE6F-EE97-4BB9-80F2-3FD7558745E5 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T14:06:57.9530000 | NULL | False | False | NULL |
| 3F694E50-136F-43E3-8009-CEA4FD4FBE64 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T14:04:34.1700000 | NULL | False | False | NULL |
| 0ED87DEB-81DB-4852-B402-C51D8B1215A3 | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:49:04.8130000 | NULL | False | False | NULL |
| 0A9BB3CA-8D09-4D43-B8D7-60AA36439A2C | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:57:11.2170000 | NULL | False | False | NULL |
| 09C9B5D7-8B5A-48B3-9AE2-1FB9DF00587D | Mahesh | NULL | Mahesh | NULL | 2026-03-07T13:26:04.2000000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_PER_SHIFT.EquipmentID` -> `XStudio_XBatch.CCM_Mst_Tbl.ID` (Many to One)
