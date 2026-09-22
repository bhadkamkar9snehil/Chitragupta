# XStudio_Xbatch.dbo.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference mould, operator, shift, ccmoperator, charge, dateyyyymmdd, eafoperator, lrfoperator, scrap, supervision, yard.

**Primary Key:** ID  
**Row Count:** 146  
**Date Range (ModifiedOn):** 2026-04-30T08:15:17.0000000 to 2026-06-29T14:59:52.0000000  

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
| Name | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Shift | varchar | YES | 36 | — |
| EAFOperator | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| CCMOperator | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| Dateyyyymmdd | varchar | YES | 100 | — |
| LRFOperator | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| ShiftInCharge | varchar | YES | 36 | — |
| ScrapYardSupervision | varchar | YES | 36 | — |
| MouldOperator1 | varchar | YES | 36 | — |
| MouldOperator2 | varchar | YES | 36 | — |
| MouldOperator3 | varchar | YES | 36 | — |
| MouldOperator4 | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0ECA46D7-042E-4DFD-A819-F37473D4211E | NULL | NULL | 2026-03-11T17:15:36.4230000 | NULL | False | False | NULL | NULL | NULL |
| 0DB6E31F-A4E5-448C-964D-3B38548B7557 | NULL | NULL | 2026-03-11T17:15:27.0270000 | NULL | False | False | NULL | NULL | NULL |
| 0D400FC5-EF49-4AEB-BDF1-8A097C018312 | NULL | NULL | 2026-03-11T17:19:00.7670000 | NULL | False | False | NULL | NULL | NULL |
| 0C4062FB-0300-4881-A81F-84C70A6BB989 | NULL | NULL | 2026-03-11T17:16:11.9500000 | NULL | False | False | NULL | NULL | NULL |
| 0BCAF9DB-8B34-46B3-9146-538B1326FFE5 | NULL | NULL | 2026-03-11T17:18:03.6600000 | NULL | False | False | NULL | NULL | NULL |
| 0B01F7AD-8BB8-4645-BB80-68910DC77108 | NULL | NULL | 2026-03-11T17:19:23.9730000 | NULL | False | False | NULL | NULL | NULL |
| 0ADAEDA4-617F-42B4-9A07-CF4FED107F32 | NULL | NULL | 2026-03-11T17:17:42.4330000 | NULL | False | False | NULL | NULL | NULL |
| 05C38CC9-D52D-4E05-AC88-C397ED71A415 | NULL | NULL | 2026-03-11T17:14:08.5230000 | NULL | False | False | NULL | NULL | NULL |
| 048293AD-1B83-4C5F-ADC7-4D53D49533E3 | NULL | NULL | 2026-03-11T17:19:21.6300000 | NULL | False | False | NULL | NULL | NULL |
| 0154E53B-2F0F-44C7-8412-D27BF903CFBA | NULL | NULL | 2026-03-11T17:19:10.2330000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4DF7FCF7-3B5D-43AA-B5B7-835E90E4B0DC | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-29T14:59:52.6270000 | 2026-06-29T14:59:52.0000000 | False | False | NULL |  | NULL |
| 14788EFC-E06D-4468-8530-1701D0A0DFFE | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-24T20:13:11.0330000 | 2026-06-24T20:13:11.0000000 | False | False | NULL |  | NULL |
| 6DF9D475-ABDB-425D-A608-DA2AD50A0BC9 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-08T21:38:12.2300000 | 2026-06-08T21:38:12.0000000 | False | False | NULL |  | NULL |
| CE96A7C4-E2B2-4EFB-A4D7-1B2AC93E7610 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-05-14T13:56:44.4730000 | 2026-05-28T15:06:49.0000000 | False | False | NULL |  | NULL |
| 3BDC5052-2C8B-46E8-88DF-8DAAF73B89FE | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-05-04T17:20:10.3930000 | 2026-05-04T17:20:10.0000000 | False | False | NULL | 10.76.20.92 | NULL |
| 76135AC5-B432-4EEF-B03A-4900EC86A3DB | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-30T08:15:17.8800000 | 2026-04-30T08:15:17.0000000 | False | False | NULL | 100.110.87.137 | NULL |
| 0ECA46D7-042E-4DFD-A819-F37473D4211E | NULL | NULL | 2026-03-11T17:15:36.4230000 | NULL | False | False | NULL | NULL | NULL |
| 0DB6E31F-A4E5-448C-964D-3B38548B7557 | NULL | NULL | 2026-03-11T17:15:27.0270000 | NULL | False | False | NULL | NULL | NULL |
| 0D400FC5-EF49-4AEB-BDF1-8A097C018312 | NULL | NULL | 2026-03-11T17:19:00.7670000 | NULL | False | False | NULL | NULL | NULL |
| 0C4062FB-0300-4881-A81F-84C70A6BB989 | NULL | NULL | 2026-03-11T17:16:11.9500000 | NULL | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.CCMOperator` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.EAFOperator` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.LRFOperator` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator1` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator2` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator3` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator4` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ScrapYardSupervision` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.Shift` -> `XStudio_XBatch.XStudio_Shift_Dtl_Tbl.ID` (Many to One)
- `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.LFEngineer` -> `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.LRFOperator` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.Melter` -> `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.EAFOperator` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.ShiftManager` -> `XStudio_XBatch.SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge` (Many to One)
