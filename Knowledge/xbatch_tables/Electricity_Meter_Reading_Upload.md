# XStudio_Xbatch.dbo.Electricity_Meter_Reading_Upload

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference file, upload, kvic, mva, all, eaf, lrf, rollingmill, status.

**Primary Key:** ID  
**Row Count:** 211  
**Date Range (ModifiedOn):** 2026-03-07T00:44:22.5930000 to 2026-09-02T07:10:19.6770000  

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
| IsProcessed | bit | YES | — | — |
| FIleUpload132KVIC1 | varchar | YES | 8000 | — |
| FIleUpload132KVIC2 | varchar | YES | 8000 | — |
| FIleUpload33KVIC1 | varchar | YES | 8000 | — |
| FIleUpload33KVIC2 | varchar | YES | 8000 | — |
| FIleUploadEAF | varchar | YES | 8000 | — |
| FIleUploadLRF | varchar | YES | 8000 | — |
| FIleUpload24MVA | varchar | YES | 8000 | — |
| FIleUpload15MVA | varchar | YES | 8000 | — |
| FIleUploadROLLINGMILL | varchar | YES | 8000 | — |
| Status | varchar | YES | 50 | — |
| Reportdate | date | YES | — | — |
| AllFIleUpload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7EADB407-33FC-46BE-B344-F3292EF9A565 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-11T08:10:31.2200000 | 2026-03-07T00:44:22.5930000 | False | False | NULL |  | NULL |
| BDC9AD52-CD58-4E37-AB58-A6333A233C98 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-11T08:12:34.4270000 | 2026-03-07T00:46:34.1300000 | False | False | NULL |  | NULL |
| FB59373C-A3DB-4CBA-86A9-7533D97B8089 | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-12T15:36:23.6170000 | 2026-03-07T00:46:45.0570000 | False | False | NULL |  | NULL |
| DB349358-F068-453E-8A22-87EC5611BA4C | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-12T15:38:23.3900000 | 2026-03-07T00:46:52.4370000 | False | False | NULL |  | NULL |
| DAFD5470-408E-4EC5-BEF2-3BD006EFDE42 | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-12T15:38:36.9370000 | 2026-03-07T00:47:11.7200000 | False | False | NULL |  | NULL |
| C79BAD9C-75E7-4091-A357-1B41A670D848 | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-13T00:41:12.3130000 | 2026-03-07T00:47:18.8500000 | False | False | NULL |  | NULL |
| 47DB4FD1-3266-4F87-8730-B3562CA1DC3B | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-14T01:25:53.9230000 | 2026-03-07T00:47:25.9300000 | False | False | NULL |  | NULL |
| 42538A4F-CEEE-4848-B537-17CD5B871EA1 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-15T00:28:09.0300000 | 2026-03-07T00:48:20.3370000 | False | False | NULL |  | NULL |
| BA585FA8-9ABB-44BA-B625-33196B558DC4 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-16T00:33:51.7000000 | 2026-03-07T00:48:28.2230000 | False | False | NULL |  | NULL |
| BF86141D-94FC-48DA-8124-FE2599074794 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-02-17T00:56:49.5630000 | 2026-03-07T00:48:35.3670000 | False | False | NULL |  | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8C2561A9-EFBC-400E-9A9B-688203C1F318 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:10:09.8170000 | 2026-09-02T07:10:19.6770000 | False | False | NULL | 172.16.4.185 | NULL |
| CC840F24-E467-436A-8DFD-3CBF2F520500 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:41:19.1170000 | 2026-09-01T07:41:35.3100000 | False | False | NULL |  | NULL |
| EC048E08-2049-4C61-A697-BDC7EADF4918 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T17:28:33.9300000 | 2026-08-31T17:29:32.0030000 | False | False | NULL |  | NULL |
| 77B388AE-AE81-491D-9F2D-D271B83D055C | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T08:02:20.6100000 | 2026-08-30T08:02:35.8100000 | False | False | NULL |  | NULL |
| A58FB192-B4C1-4966-8741-65BE65578AA1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T06:42:38.9570000 | 2026-08-29T06:42:51.8300000 | False | False | NULL |  | NULL |
| B9FFA86D-0F69-40AA-BC98-04707AC51F43 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-28T06:58:37.4570000 | 2026-08-28T06:58:54.4070000 | False | False | NULL |  | NULL |
| 309A5948-F573-482D-B49F-3F7CF9743712 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T10:03:38.6630000 | 2026-08-27T10:03:54.7130000 | False | False | NULL |  | NULL |
| 68ECA645-2225-4C79-ABE9-4BCAD3E91211 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-26T07:23:19.2930000 | 2026-08-26T07:23:29.8800000 | False | False | NULL | 172.16.4.185 | NULL |
| 7CC84501-F309-401B-9D9F-1C9A70120D6F | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-25T07:00:35.6500000 | 2026-08-25T07:00:53.7670000 | False | False | NULL |  | NULL |
| DA7F8194-75BA-42D4-9E36-9AAC4D21C1FD | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-24T06:48:22.9730000 | 2026-08-24T06:48:42.9770000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electricity_Meter_Reading_Upload.AllFIleUpload` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUpload132KVIC1` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUpload132KVIC2` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUpload15MVA` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUpload24MVA` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUpload33KVIC1` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUpload33KVIC2` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUploadEAF` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUploadLRF` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electricity_Meter_Reading_Upload.FIleUploadROLLINGMILL` -> `XStudio_Configuration_XBatch.XStudio_Notes_Mst_Tbl.ID` (Many to One)
