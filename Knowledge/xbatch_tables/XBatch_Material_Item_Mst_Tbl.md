# XStudio_Xbatch.dbo.XBatch_Material_Item_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference location, date, number, description, expired, expiry, grade, grnnumber, invoice, lot, name, ponumber.

**Primary Key:** ID  
**Row Count:** 4,347  
**Date Range (ModifiedOn):** 2025-07-03T17:51:02.0000000 to 2026-07-29T14:27:53.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Vendor | varchar | YES | 100 | — |
| LotNumber | varchar | YES | 100 | — |
| Quantity | decimal | YES | 18,4 | — |
| Price | decimal | YES | 18,4 | — |
| PONumber | varchar | YES | 100 | — |
| InvoiceNumber | varchar | YES | 100 | — |
| ReceivedDate | datetime | YES | — | — |
| LocationType | varchar | YES | 100 | — |
| LocationID | varchar | YES | 36 | — |
| LocationName | varchar | YES | 100 | — |
| ExpiryDate | date | YES | — | — |
| IsExpired | bit | YES | — | — |
| UOMID | varchar | YES | 36 | — |
| GradeID | varchar | YES | 36 | — |
| GRNNumber | varchar | YES | 100 | — |
| Description | varchar | YES | 1000 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00A3EB07-A685-4662-849D-2A105E2C3C5B | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-04-05T16:45:55.0300000 | NULL | False | False | NULL | NULL |
| 00A19573-3280-479C-8B1C-545B9145E801 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-31T14:42:32.5000000 | NULL | False | False | NULL | NULL |
| 009B8E1B-96AD-41C8-B8DA-59724BF10CD5 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-18T14:39:06.1770000 | NULL | False | False | NULL | NULL |
| 00738B8E-0E2C-4267-856C-6D0903F387E7 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-03-29T03:56:54.5930000 | NULL | False | False | NULL | NULL |
| 006DD9C1-58C1-4245-A765-1247631A3BB3 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-11-26T15:45:14.6900000 | NULL | False | False | NULL | NULL |
| 00576FEA-EBA2-4A4C-A9F6-2099E5787E1D | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-04-08T08:58:22.2400000 | NULL | False | False | NULL | NULL |
| 00376A9A-8334-4D55-A74A-BA70D7EDB4D0 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-01-07T14:55:34.1930000 | NULL | False | False | NULL | NULL |
| 001D4A59-367B-4A08-AD9A-84320DE23272 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2025-12-20T21:14:44.2630000 | NULL | False | False | NULL | NULL |
| 000DAF5E-6F08-4FCC-9F9A-2A277BA03893 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-02-07T14:25:41.0730000 | NULL | False | False | NULL | NULL |
| 000869C5-AFAE-4491-90D7-650FD61A8E38 | C56EF29E-7267-4B98-88DD-CB3BA0D4AC6A | NULL | NULL | 2026-02-27T14:02:25.8300000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42D476DC-BDB8-43C2-961B-C7E127303CB7 | 0924E17A-FCBB-46BA-9CEB-FA718C19773D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-29T14:27:53.8300000 | 2026-07-29T14:27:53.0000000 | False | False | NULL | 100.110.123.120 |
| C11652A1-A81E-4A49-B7C8-722BB3945D9C | 466154FE-4E29-4BBC-97D0-D73812E0DC6E | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-29T14:26:42.4570000 | 2026-07-29T14:26:42.0000000 | False | False | NULL | 100.110.123.120 |
| CF584A9B-3457-4179-99B3-479C3438B171 | 623C1A28-8F7B-411B-8187-2A20854182DB | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:42:14.5430000 | 2026-07-28T15:42:14.0000000 | False | False | NULL |  |
| 07D892A0-4C34-43D3-A316-279113C7DEB3 | 83528728-8810-43DB-A13B-EE9CBDF72FC7 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:41:07.9230000 | 2026-07-28T15:41:07.0000000 | False | False | NULL |  |
| 128E2507-69B6-4BED-B635-3C5BCB31CA88 | 4617BA9E-2211-49B7-8AD1-A9CB138344BF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T13:39:53.6570000 | 2026-07-28T13:39:53.0000000 | False | False | NULL |  |
| 231F85BE-AAB4-4702-A740-BC415F7D06EC | 6E91E75F-19C7-41E9-B3FC-7C2FE395CF46 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:12:53.4300000 | 2026-07-06T11:12:53.0000000 | False | False | NULL | 100.110.190.241 |
| D30ECFD9-7FF6-4A0B-B93F-2E0C222875D2 | BA3AA53B-D072-47D0-87FD-F414DE15918A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:12:11.8230000 | 2026-07-06T11:12:11.0000000 | False | False | NULL | 100.110.190.241 |
| EF572CB0-F02F-4D7B-A496-E87925E368BF | 2979D331-03C3-460D-9ED3-10A4C8757365 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:11:11.3630000 | 2026-07-06T11:11:11.0000000 | False | False | NULL | 100.110.190.241 |
| 0468AF59-C308-4C8A-B75B-BFE990C44FE2 | 438AD51B-27AD-4873-8942-E93D80CF79EF | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-06T11:08:40.8730000 | 2026-07-06T11:08:40.0000000 | False | False | NULL | 100.110.190.241 |
| 57402517-8018-4007-80AA-12A95117F0C6 | F81ACBF8-37A8-47B5-A458-328635559004 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-04T08:56:54.0700000 | 2026-07-04T08:56:54.0000000 | False | False | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.GradeID` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Sub_Item_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.ID` (Many to One)
