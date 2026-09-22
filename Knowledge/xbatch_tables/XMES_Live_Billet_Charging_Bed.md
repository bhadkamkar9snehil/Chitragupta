# XStudio_Xbatch.dbo.XMES_Live_Billet_Charging_Bed

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, status, time, tracking, area, batch, bed, length, out, rolled, sequence, stage.

**Primary Key:** ID  
**Row Count:** 1,641  
**Date Range (ModifiedOn):** 2026-07-30T14:58:09.8870000 to 2026-08-31T10:30:41.3200000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| BilletNo | varchar | YES | 100 | — |
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
| InTIme | datetime | YES | — | — |
| OutTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| BedNo | varchar | YES | 100 | — |
| Status | varchar | YES | 100 | ('Entered') |
| BatchNo | varchar | YES | 100 | — |
| SequenceNo | int | YES | 10,0 | — |
| BilletTrackingStatus | varchar | YES | 50 | — |
| BilletAreaWiseTracking | varchar | YES | 100 | — |
| BilletLength | varchar | YES | 100 | — |
| RolledBilletStage | varchar | YES | 100 | — |

### Top 10 Records

| ID | BilletNo | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 064CF988-C110-4C9E-B54E-0BD63DB120B4 | 2605979_00_07 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 0668C03C-9BA9-45E5-8DB8-B692C3B718E4 | 2605979_00_53 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 071E6405-518E-41F0-85A0-79A85071473B | 2605979_00_28 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 0BAC2C73-04C6-417F-9ED0-F8608B0313E4 | 2605979_00_35 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 0F0A2BF9-910C-4103-9FC9-E3A92F629D83 | 2605979_00_31 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 0F220F6C-31FB-4823-9C14-DF2FCE977EC5 | 2605979_00_78 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 0FB2BCAF-FCEB-4408-9FC1-28E731CF428B | 2605979_00_10 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 13F08C4E-8D66-44CD-B453-32CE25FC7723 | 2605979_00_40 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 141EF798-FA05-4A51-9AD7-2459039EC8EC | 2605979_00_54 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |
| 1566FD6A-0E39-406E-BACF-B6A46DC29334 | 2605979_00_06 | A427F348-BF0C-42ED-A2F8-913C4D440200 | NULL | NULL | 2026-08-27T13:50:30.4230000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | BilletNo | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD25C91E-48BF-4B05-9416-3773DE00E396 | 2603931_00_01 | 9DE2D5C9-4B7C-4B05-B4E9-9A77F8C725D8 | NULL | NULL | 2026-08-27T13:47:14.7600000 | 2026-08-31T10:30:41.3200000 | False | False | NULL |
| C07229E4-C844-43B5-BEED-B9706BEFE06A | 1260781_00_01 | E3194CF3-5CAC-48B8-8846-32F798C2A4EE | NULL | NULL | 2026-08-25T14:28:59.5100000 | 2026-08-25T18:47:28.7000000 | False | False | NULL |
| F3ED0813-56B1-42E0-A26B-F261AEC210FC | 1260773_00_01 | B44EAB30-A0C0-43B8-9032-2CC826DA1978 | NULL | NULL | 2026-08-25T13:40:37.0530000 | 2026-08-25T18:43:51.9200000 | False | False | NULL |
| 50D9BA0F-CFF0-4ED9-9C6F-99763033599B | 1260817_00_46 | 9418E30A-86F5-4CF0-8B27-22B36272A133 | NULL | NULL | 2026-08-25T13:04:29.5630000 | 2026-08-25T18:38:27.5730000 | False | False | NULL |
| 717DE7F6-ACDE-407F-AEDC-07A4545DE08B | 1260817_00_45 | 29F85326-B938-4A40-BEC0-A6045A0667DB | NULL | NULL | 2026-08-24T16:02:52.0600000 | 2026-08-24T19:08:46.9530000 | False | False | NULL |
| 66FEE8E7-D57F-415A-9266-4F2AE5723820 | 1260817_00_44 | 29F85326-B938-4A40-BEC0-A6045A0667DB | NULL | NULL | 2026-08-24T16:02:52.0600000 | 2026-08-24T19:07:14.9730000 | False | False | NULL |
| 9AD11696-179B-482A-AEC8-3AD3F5862E31 | 1260817_00_43 | 29F85326-B938-4A40-BEC0-A6045A0667DB | NULL | NULL | 2026-08-24T16:02:52.0600000 | 2026-08-24T19:05:44.4370000 | False | False | NULL |
| 14A85A2D-23A1-4F9C-94F1-4C96531E4D1C | 1260817_00_42 | 29F85326-B938-4A40-BEC0-A6045A0667DB | NULL | NULL | 2026-08-24T16:02:52.0600000 | 2026-08-24T19:04:13.3000000 | False | False | NULL |
| EB791963-1D8D-4C39-AEE7-F701E0F7EC26 | 1260817_00_41 | 29F85326-B938-4A40-BEC0-A6045A0667DB | NULL | NULL | 2026-08-24T16:02:52.0600000 | 2026-08-24T19:02:41.4930000 | False | False | NULL |
| 807993BD-77E8-4C4F-8AF9-CAF9DB20A181 | 1260817_00_40 | 29F85326-B938-4A40-BEC0-A6045A0667DB | NULL | NULL | 2026-08-24T16:02:52.0600000 | 2026-08-24T19:01:10.3330000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.ChargingBedBilletNo` -> `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.BilletNo` (Many to One)
- `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.ID` -> `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.ParentID` (Many to One)
- `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.ParentID` -> `XStudio_XBatch.RM_Operator_HeatSelection.ID` (Many to One)
- `XStudio_XBatch.XMES_Live_Charging_SECT1.ParentID` -> `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.ID` (Many to One)
