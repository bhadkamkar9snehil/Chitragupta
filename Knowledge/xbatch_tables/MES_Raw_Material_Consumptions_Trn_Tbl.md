# XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference order, quantity, work, captured, declared, difference, lot, number, price, sapworkflow, status, type.

**Primary Key:** ID  
**Row Count:** 11,073  
**Date Range (ModifiedOn):** 2026-01-10T11:16:11.0000000 to 2026-08-08T08:47:15.4330000  

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
| ReportDate | date | YES | — | — |
| CapturedQuantity | decimal | YES | 18,2 | — |
| DeclaredQuantity | decimal | YES | 18,2 | — |
| Unit | varchar | YES | 36 | — |
| WorkOrder | varchar | YES | 36 | — |
| SAPWorkflowStatus | varchar | YES | 50 | — |
| LotNumber | varchar | YES | -1 | — |
| Price | decimal | YES | 18,2 | — |
| Difference | decimal | YES | 18,4 | — |
| OrderType | varchar | YES | 100 | — |
| WorkOrderNo | varchar | YES | 100 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002649A7-81A8-4A9F-9E95-9F2C7809FA9B | 3189E856-BAA1-4AC1-92F6-C722D6028AEC | NULL | NULL | 2026-08-01T09:00:06.9170000 | NULL | False | False | NULL | NULL |
| 002473E6-9E31-4DDF-84E6-BB37FC4E6D71 | 056DECE8-A33F-4F85-BCC7-E7EE6715D6AD | NULL | NULL | 2026-07-23T09:00:04.2030000 | NULL | False | False | NULL | NULL |
| 00210CB5-14BC-4FA8-B437-17AE6F9A617B | EADA1951-EAA7-450F-9EE2-3A5BF1F8CCF0 | NULL | NULL | 2026-05-24T09:00:07.6100000 | NULL | False | False | NULL | NULL |
| 002060C0-B672-42AD-AD97-76BD8C075D84 | B0790BAA-F7C2-4690-A404-84210655F8F7 | NULL | NULL | 2026-06-14T09:00:04.5900000 | NULL | False | False | NULL | NULL |
| 00155DEA-8C00-4A76-8AC2-81A410542BBC | AA366314-5C63-4732-8A9A-D5C04BAB5DA8 | NULL | NULL | 2026-02-18T09:00:06.5770000 | NULL | False | False | NULL | NULL |
| 0011CF38-CE92-4509-B4B0-781BA47BA2BD | EDCEBEA7-4708-4C86-8926-1CFC320917A5 | NULL | NULL | 2026-02-15T09:00:01.8130000 | NULL | False | False | NULL | NULL |
| 00119655-111C-4346-B207-B11FFB09896C | E2524692-29D6-4B78-BE95-E7C42E5EAFE8 | NULL | NULL | 2026-03-01T09:00:04.8100000 | NULL | False | False | NULL | NULL |
| 000D6B48-688A-48E4-BAFB-A85E03A2213F | B5F8DA4A-A3BF-4FAB-8729-D37060C94F78 | NULL | NULL | 2026-02-19T09:00:03.6630000 | NULL | False | False | NULL | NULL |
| 000CE5F7-F9B6-4E45-9C94-D81122A0280D | 6C897D7F-2B8E-4BB0-8235-0A3EDD8CAE4C | NULL | NULL | 2026-07-20T09:00:08.6600000 | NULL | False | False | NULL | NULL |
| 000A1EC2-A003-426C-8DD8-73B5FA950F5B | 8A9A2C9A-BC4D-44D9-8503-1A9F959064F5 | NULL | NULL | 2026-03-30T09:00:09.8200000 | NULL | False | False | NULL | NULL |

### Bottom 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 960220D6-2683-4147-893E-67AA20A3D2BE | E94CC7C7-FDFB-44AF-B43F-2678CE504C8F | NULL | NULL | 2026-08-08T00:22:01.9570000 | 2026-08-08T08:47:15.4330000 | False | False | NULL | NULL |
| B329FEA5-55E0-4A80-A2D7-D6BA664CFA4F | A60A06F4-A232-4F5E-91B1-CC8413D98BE8 | NULL | NULL | 2026-08-08T00:22:01.9570000 | 2026-08-08T08:47:15.4330000 | False | False | NULL | NULL |
| 556E146F-5EC7-4576-8B71-98CDAF45FA18 | 71000F40-C648-46AD-966D-A8EE932DA7CB | NULL | NULL | 2026-08-08T08:30:03.8600000 | 2026-08-08T08:30:54.5570000 | False | False | NULL | NULL |
| 60E6DDAF-5A74-4F52-8EB4-9C7975336F1A | 9EBCF9E6-5289-40A4-A819-B896EEF883BF | NULL | NULL | 2026-08-08T08:30:03.8600000 | 2026-08-08T08:30:54.5570000 | False | False | NULL | NULL |
| 475F39B1-67AF-472F-852C-874A20E615A8 | E94CC7C7-FDFB-44AF-B43F-2678CE504C8F | NULL | NULL | 2026-08-08T08:30:03.7030000 | 2026-08-08T08:30:54.4200000 | False | False | NULL | NULL |
| 63FF8256-61AE-4FAD-8EAD-9C8747839051 | E94CC7C7-FDFB-44AF-B43F-2678CE504C8F | NULL | NULL | 2026-08-06T23:52:25.5030000 | 2026-08-08T08:30:54.4200000 | True | False | NULL | NULL |
| 64F9318E-280E-4C4C-BC5E-BC21B23BC1CC | A60A06F4-A232-4F5E-91B1-CC8413D98BE8 | NULL | NULL | 2026-08-06T23:52:25.5030000 | 2026-08-08T08:30:54.4200000 | True | False | NULL | NULL |
| 8AC9902E-109C-4AB2-9E5B-2D5ED6CBA07C | A60A06F4-A232-4F5E-91B1-CC8413D98BE8 | NULL | NULL | 2026-08-08T08:30:03.7030000 | 2026-08-08T08:30:54.4200000 | False | False | NULL | NULL |
| 8E1629ED-B7A1-4879-835C-915DDF1DA5DD | 593B174A-543B-42E6-A0E9-2623E0BF9CA7 | NULL | NULL | 2026-08-06T09:09:39.2870000 | 2026-08-08T07:02:50.0800000 | False | False | NULL | NULL |
| E9B5BDF9-9E61-4012-A3A2-A44EE00F1347 | 593B174A-543B-42E6-A0E9-2623E0BF9CA7 | NULL | NULL | 2026-08-06T09:09:39.2870000 | 2026-08-08T07:02:50.0800000 | False | False | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_Raw_Material_Consumptions_Trn_Tbl.ParentID` -> `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Trn_Tbl.SalesOrder` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Trn_Tbl.Unit` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
