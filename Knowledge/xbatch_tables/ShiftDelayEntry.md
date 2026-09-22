# XStudio_Xbatch.dbo.ShiftDelayEntry

**table_kind:** production_data

### What this table is for

- **Curated domain match (performance):** Delay, OEE, downtime, shift-delay, equipment-delay, agency-delay, or performance issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** core, delay, entities, event, from, map, oee, procedure, routing, sohar, stored, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference delay, name, agency, duration, equipment, other, shift, time, area, caparecordid, cobble, date.

**Primary Key:** ID  
**Row Count:** 19,231  
**Date Range (ModifiedOn):** 2026-04-28T17:09:57.0000000 to 2026-08-03T22:10:04.0000000  

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
| DelayStartTime | datetime | YES | — | — |
| DelayInMinutes | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| DelayEndTime | datetime | YES | — | — |
| DelayReason | varchar | YES | -1 | — |
| DelayType | varchar | YES | 36 | — |
| DelayAgency | varchar | YES | 36 | — |
| AgencyOther | varchar | YES | 100 | — |
| HeatNo | int | YES | 10,0 | — |
| EquipmentName | varchar | YES | -1 | — |
| SubEquipmentName | varchar | YES | 36 | — |
| ReportDate | varchar | YES | 100 | — |
| AreaName | varchar | YES | -1 | — |
| ShiftManager | varchar | YES | 36 | — |
| OperatorName | varchar | YES | 36 | — |
| RMProduct | varchar | YES | 100 | — |
| DelaySubtypeid | varchar | YES | 36 | — |
| DelayInSecond | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| RMSection | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| Cobble | int | YES | 10,0 | — |
| Hotout | int | YES | 10,0 | — |
| Refractory | int | YES | 10,0 | — |
| Mechanical | int | YES | 10,0 | — |
| Electrical | int | YES | 10,0 | — |
| Operation | int | YES | 10,0 | — |
| OtherDelay | int | YES | 10,0 | — |
| RemainingDuration | decimal | YES | 18,2 | — |
| DelayDuration | varchar | YES | 100 | — |
| SMSReportDate | varchar | YES | 100 | — |
| CAPARecordid | varchar | YES | 36 | — |
| ShortDescription | varchar | YES | 100 | — |
| Issplit | bit | YES | — | — |
| Status | varchar | YES | 50 | ('Entered') |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00053E83-F99C-456C-AE36-4EF787512016 | NULL | NULL | 2026-06-02T20:02:45.2800000 | NULL | False | False | NULL | NULL | NULL |
| 000BA45B-6CA0-4172-8D16-F739DB46E217 | NULL | NULL | 2026-05-04T07:10:02.2830000 | NULL | False | False | NULL | NULL | NULL |
| 000D7380-3343-4CF5-810E-78DEAFC2833F | NULL | NULL | 2026-06-04T17:43:56.5500000 | NULL | False | False | NULL | NULL | NULL |
| 00332594-4345-4AA9-B8F8-AA2B3AE31160 | NULL | NULL | 2026-08-25T10:14:19.1700000 | NULL | False | False | NULL | NULL | NULL |
| 00484E9A-028D-4E39-BC08-BDDE8A80D813 | NULL | NULL | 2026-08-01T10:46:28.6330000 | NULL | False | False | NULL | NULL | NULL |
| 004A506B-D391-4CD1-AD99-29C0390CFC96 | NULL | NULL | 2026-05-29T09:56:00.4300000 | NULL | False | False | NULL | NULL | NULL |
| 00546C74-1BCF-4654-B83A-48DABBF84FD7 | NULL | NULL | 2026-05-14T15:39:24.2500000 | NULL | False | False | NULL | NULL | NULL |
| 0056027D-2752-406D-8CEF-881D0DD41844 | NULL | NULL | 2026-06-11T15:20:00.7870000 | NULL | False | False | NULL | NULL | NULL |
| 00703C70-97BE-4AF8-952F-CEF1F101D9CC | NULL | NULL | 2026-06-16T11:55:29.2800000 | NULL | False | False | NULL | NULL | NULL |
| 00738872-9863-4FE5-8666-14C30BD1EA75 | NULL | NULL | 2026-05-06T15:28:01.4830000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19A3A61D-FD2E-4DC4-A7C7-CC8DBA2E3178 | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-08-03T20:33:29.4730000 | 2026-08-03T22:10:04.0000000 | False | False | NULL | 10.76.111.2 | NULL |
| 04DBBCD1-0D2C-4CB0-A1E0-2107BC6241CC | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T16:55:17.8930000 | 2026-07-06T16:58:21.3430000 | True | False | NULL |  | NULL |
| 71F471A8-79DB-4B25-A4AC-DF8F7401A94C | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T16:40:34.2570000 | 2026-07-06T16:51:47.0000000 | False | False | NULL |  | NULL |
| DC47A0A9-2BAA-412F-B94E-338BC4AEFD01 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T16:41:27.6700000 | 2026-07-06T16:51:47.0000000 | False | False | NULL |  | NULL |
| 252F0657-899B-46D2-BC2B-CC5E34FA2004 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T16:15:07.9430000 | 2026-07-06T16:50:28.9530000 | True | False | NULL |  | NULL |
| 2A3DDE51-19BD-40F5-A313-3CB7C2D26A22 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T15:03:45.7700000 | 2026-07-06T16:41:14.0000000 | False | False | NULL |  | NULL |
| 0639FFCC-6C13-4B53-B26F-094C8747A5B7 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T16:38:25.3400000 | 2026-07-06T16:39:11.8270000 | True | False | NULL |  | NULL |
| BCBE917B-8BF3-4931-A38B-0F15EB09FD58 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T15:17:22.7300000 | 2026-07-06T16:37:51.8170000 | True | False | NULL |  | NULL |
| 30293F34-7AA9-434F-9CFE-75E32E3716F3 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T15:03:45.6070000 | 2026-07-06T16:34:00.0000000 | False | False | NULL |  | NULL |
| C2C505ED-B00A-42D5-B9F6-092A8ECDC786 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-06T15:03:45.4470000 | 2026-07-06T16:33:00.0000000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Agency_Wise_Delay.ParentID` -> `XStudio_XBatch.ShiftDelayEntry.ID` (Many to One)
- `XStudio_XBatch.RMShiftDelayEntry_CAPA.DelayTransactionid` -> `XStudio_XBatch.ShiftDelayEntry.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.AreaName` -> `XStudio_XBatch.DelayAgency_Master.AreaName` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.DelayAgency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.DelaySubtypeid` -> `XStudio_XBatch.DelaySubType_Master.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.DelayType` -> `XStudio_XBatch.DelayTypeMST.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.EquipmentName` -> `XStudio_XBatch.Equipment.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.ID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.DelayTransactionid` (One to One)
- `XStudio_XBatch.ShiftDelayEntry.ModifiedBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.OperatorName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.ShiftManager` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.ShiftDelayEntry.SubEquipmentName` -> `XStudio_XBatch.SubEquipment.ID` (Many to One)
- `XStudio_XBatch.SMS_DelayEntry_CAPA.DelayTransactionid` -> `XStudio_XBatch.ShiftDelayEntry.ID` (Many to One)
