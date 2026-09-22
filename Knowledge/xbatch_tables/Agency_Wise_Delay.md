# XStudio_Xbatch.dbo.Agency_Wise_Delay

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, delay, entities, entity, from, highlights, oee, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference duration, agency, durationmmss, remaining, remark, second.

**Primary Key:** ID  
**Row Count:** 1,38,596  
**Date Range (ModifiedOn):** 2025-09-29T12:13:53.0000000 to 2026-01-28T14:28:23.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Agency | varchar | YES | 36 | — |
| Duration | decimal | YES | 18,2 | — |
| Remark | varchar | YES | -1 | — |
| RemainingDuration | decimal | YES | 18,2 | — |
| Durationmmss | varchar | YES | 100 | — |
| DurationInSecond | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00058A5A-63F7-48C1-B744-F0862EBF375C | NULL | 4FCA1F79-F229-4A38-8B73-578899049B05 | NULL | NULL | 2026-04-27T23:48:29.1570000 | NULL | False | False | NULL |
| 00058169-4308-41D4-BCF0-709F96D75C4E | NULL | EAC7DB58-B99C-46F5-8E3C-0D119351926C | NULL | NULL | 2026-03-19T20:23:04.0100000 | NULL | False | False | NULL |
| 00049113-65A2-4554-B695-CFECD6DEA8C8 | NULL | BC05A185-B8EC-4DC2-9562-8DAD44856481 | NULL | NULL | 2026-03-22T21:31:10.7570000 | NULL | False | False | NULL |
| 0003F554-147F-4750-B292-1631BA415750 | NULL | D343ECB0-B096-48FB-98A5-0F66F412DBC3 | NULL | NULL | 2025-12-27T08:31:39.9500000 | NULL | False | False | NULL |
| 000377C5-122D-4B61-A859-92DA1F80401C | NULL | 7197592C-9158-4B5C-AA12-097700DC5568 | NULL | NULL | 2026-06-05T16:59:59.8870000 | NULL | False | False | NULL |
| 00034EA8-8140-4869-953C-A097E0EDF7BF | NULL | E6FD126B-BB45-4B92-8A0F-058D2F503728 | NULL | NULL | 2026-05-29T09:00:11.1930000 | NULL | False | False | NULL |
| 0002B6DF-4EED-4F61-8DDA-C284902AB032 | NULL | 5345BB11-7276-48A2-8A01-7C9E8B8C449A | NULL | NULL | 2026-03-28T01:38:19.2970000 | NULL | False | False | NULL |
| 0001DA24-06E4-4934-885C-35A436D2D1C8 | NULL | C19775AF-5690-46A9-92CC-3F64926A0526 | NULL | NULL | 2026-01-10T10:17:53.9800000 | NULL | False | False | NULL |
| 000189B0-FDE9-459D-B5A7-9A13884A74A2 | NULL | E6965AB4-2DD9-4151-88F9-5F00960CC629 | NULL | NULL | 2026-04-01T02:20:18.8900000 | NULL | False | False | NULL |
| 00016BCE-7060-40BC-B944-AF08D3E8A440 | NULL | A96C7675-4F28-44F0-8663-89D5E47C565F | NULL | NULL | 2026-03-27T02:01:31.5970000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ADD4F964-0CF9-4A8D-8A1D-AEFB3FE3D956 | NULL | 2C7F07C3-41F0-4493-839F-0B42B90EE468 | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-27T03:03:06.4600000 | 2026-01-28T14:28:23.0000000 | False | False | NULL |
| 3EC4E43E-A637-429B-8C6D-92F78C86DC61 | NULL | 64987D5E-A46D-4C26-8A36-705899FA1BFA | NULL | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-27T01:06:10.2500000 | 2026-01-28T14:25:13.0000000 | False | False | NULL |
| 9B9F24B6-9B39-4812-AC07-0CBE027081B2 | NULL | 912AC1D4-230A-460C-8D75-C68EE58E98CA | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-06T06:58:29.4530000 | 2026-01-06T11:16:00.0000000 | False | False | NULL |
| 4E87D1F2-B298-43B6-995F-B3145FDD2CB7 | NULL | 07B02A47-1586-44B8-8842-3B09ED40CDDC | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-06T08:56:03.5200000 | 2026-01-06T09:14:14.0000000 | False | False | NULL |
| B324ACBE-8E94-488D-83D9-2D78A4D7420F | NULL | D73A9FD0-5DF4-467B-A2DC-4AD7FD5ED03F | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-01-05T09:18:20.4770000 | 2026-01-05T13:37:30.0000000 | False | False | NULL |
| D6691D33-730D-4C1E-994F-1E2E71AC54B1 | NULL | 4FEE80BB-8B13-432E-BC6B-E7A7A198643B | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-01-05T07:27:13.9600000 | 2026-01-05T12:14:56.0000000 | False | False | NULL |
| DBD67B64-326E-421C-8A17-2EE725BF307E | NULL | 4FEE80BB-8B13-432E-BC6B-E7A7A198643B | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-01-05T07:27:13.9600000 | 2026-01-05T12:14:55.0000000 | False | False | NULL |
| 883DC934-83FB-4C2C-BFE1-C7E1CDB4C08E | NULL | BADFB356-27EB-4EF6-A33F-EF51BEE74BEB | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-01-05T10:14:05.4000000 | 2026-01-05T12:04:29.0000000 | False | False | NULL |
| 3D13601C-B020-41AE-9266-DA2E12C9F360 | NULL | DB747034-5C23-46AD-AC7C-DC73BA2A330B | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-02T10:15:56.5830000 | 2026-01-02T10:20:22.0000000 | False | False | NULL |
| DDEF0B6E-A5FB-4B18-A748-EEFB4F70C7B3 | NULL | 51F4CC77-6375-41BD-B9F2-1BC195EB0A95 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | 2025-12-28T07:59:05.9330000 | 2025-12-28T10:54:55.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Agency_Wise_Delay.Agency` -> `XStudio_XBatch.DelayAgency_Master.ID` (Many to One)
- `XStudio_XBatch.Agency_Wise_Delay.ID` -> `XStudio_XBatch.RMShiftDelayEntry_CAPA.AgencyTransactionid` (One to One)
- `XStudio_XBatch.Agency_Wise_Delay.ParentID` -> `XStudio_XBatch.ShiftDelayEntry.ID` (Many to One)
- `XStudio_XBatch.Equipment_Wise_Delay.ParentID` -> `XStudio_XBatch.Agency_Wise_Delay.ID` (Many to One)
