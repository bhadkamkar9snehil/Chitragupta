# XStudio_Xbatch.dbo.XBatch_Measurement_Unit_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference code, colour, description.

**Primary Key:** ID  
**Row Count:** 13  
**Date Range (ModifiedOn):** 2026-01-13T13:45:52.0000000 to 2026-07-31T10:35:42.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | NO | 100 | — |
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
| Description | varchar | YES | -1 | — |
| ColourCode | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E813324C-B2EC-4BF5-A0D3-4CF53F4AF6EE | % | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-07-22T20:37:35.1400000 | 2026-01-13T13:45:52.0000000 | False | False | NULL |
| 9E07A299-BAF0-45E5-8653-C6AF38DF467C | cm | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-06-07T15:34:55.9930000 | 2026-01-13T13:53:09.0000000 | False | False | NULL |
| A1ABD1A3-D847-4BD2-BC8B-7B375943C1A3 | in | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-06-07T15:35:17.4070000 | 2026-01-13T13:53:40.0000000 | False | False | NULL |
| 640E879D-F79E-49DA-A23F-F261D1F11C81 | kg | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-05-30T17:04:36.2630000 | 2026-01-13T13:54:10.0000000 | False | False | NULL |
| F47C1306-58E9-4952-8561-8B5368D92993 | KWH | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-19T09:32:24.3600000 | 2026-01-13T13:54:32.0000000 | False | False | NULL |
| 2EA4A15B-FC50-4C1A-BB81-B957F1D658DA | ltr | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-05-30T17:05:14.9700000 | 2026-01-13T13:54:40.0000000 | False | False | NULL |
| F157357E-509B-462C-A8F8-0618BCEE5AC9 | M3 | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-19T09:33:41.6670000 | 2026-01-13T13:55:13.0000000 | False | False | NULL |
| 059E7B2F-1029-444F-BFB3-93FA9CC65C04 | MBT | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-19T09:33:56.4170000 | 2026-01-13T13:55:30.0000000 | False | False | NULL |
| 2095DF88-C3E3-4184-BA44-BBBB0696FF14 | MT | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-06-25T16:40:36.4830000 | 2026-01-13T13:56:02.0000000 | False | False | NULL |
| 645211DE-C133-4D5B-BBF9-8AF7FD0B1165 | mtr | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-06-07T15:35:04.0030000 | 2026-01-13T13:56:35.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D76950D1-BAA7-462B-84A7-39CB372B1419 | Nm3 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-31T10:35:42.6730000 | 2026-07-31T10:35:42.0000000 | False | False | NULL |
| 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | ton | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-05-30T17:04:44.2300000 | 2026-01-13T13:57:09.0000000 | False | False | NULL |
| 96A468CE-D34F-4CA4-81B3-305071232110 | Qty | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-06-07T15:34:43.1330000 | 2026-01-13T13:56:50.0000000 | False | False | NULL |
| 645211DE-C133-4D5B-BBF9-8AF7FD0B1165 | mtr | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-06-07T15:35:04.0030000 | 2026-01-13T13:56:35.0000000 | False | False | NULL |
| 2095DF88-C3E3-4184-BA44-BBBB0696FF14 | MT | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-06-25T16:40:36.4830000 | 2026-01-13T13:56:02.0000000 | False | False | NULL |
| 059E7B2F-1029-444F-BFB3-93FA9CC65C04 | MBT | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-19T09:33:56.4170000 | 2026-01-13T13:55:30.0000000 | False | False | NULL |
| F157357E-509B-462C-A8F8-0618BCEE5AC9 | M3 | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-19T09:33:41.6670000 | 2026-01-13T13:55:13.0000000 | False | False | NULL |
| 2EA4A15B-FC50-4C1A-BB81-B957F1D658DA | ltr | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-05-30T17:05:14.9700000 | 2026-01-13T13:54:40.0000000 | False | False | NULL |
| F47C1306-58E9-4952-8561-8B5368D92993 | KWH | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-19T09:32:24.3600000 | 2026-01-13T13:54:32.0000000 | False | False | NULL |
| 640E879D-F79E-49DA-A23F-F261D1F11C81 | kg | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2023-05-30T17:04:36.2630000 | 2026-01-13T13:54:10.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_Inventory.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Order_Configurator.Unitid` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Unitid` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Trn_Tbl.Unit` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.QuantityUnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Dtl_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Per_WorkOrder_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Sub_Item_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
