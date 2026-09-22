# XStudio_Xbatch.dbo.XBatch_Material_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference number, type, code, expire, format, inventory, lot, stock, can, colour, days, description.

**Primary Key:** ID  
**Row Count:** 213  
**Date Range (ModifiedOn):** 2025-12-10T16:15:33.0000000 to 2026-08-19T14:31:45.0000000  

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
| TypeID | varchar | NO | 36 | — |
| UnitID | varchar | YES | 36 | — |
| Number | varchar | NO | 100 | — |
| StockType | varchar | NO | 100 | — |
| Quantity | decimal | YES | 18,4 | — |
| Description | varchar | YES | -1 | — |
| IsEnabled | bit | YES | — | — |
| CanExpire | bit | YES | — | — |
| ExpireDays | int | YES | 10,0 | — |
| MinInventoryLevel | decimal | YES | 18,4 | — |
| MaxOrderSize | decimal | YES | 18,4 | — |
| LotNumberFormat | varchar | YES | 100 | — |
| SubLotNumberFormat | varchar | YES | 100 | — |
| ColourCode | varchar | YES | 50 | — |
| PageID | varchar | YES | -1 | — |
| PlantID | varchar | YES | 36 | — |
| StoragelocationID | varchar | YES | 36 | — |
| Grade | varchar | YES | 100 | — |
| RawMaterialName | varchar | YES | -1 | — |
| SAPColorCode | varchar | YES | 100 | — |
| InventorySpecialStockType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 09F14143-EEB3-493B-97F1-EB67C2FFCCCD | S275_GLS | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-12-17T08:06:22.0530000 | NULL | False | False | NULL |
| 025DF9DC-CC9A-440D-9516-6CADD4A4630F | SCRAP MIX ROUNDBILLETS | NULL | NULL | NULL | 2025-12-19T08:39:01.2670000 | NULL | False | False | NULL |
| 0F45E920-7EA8-4164-A105-BA9B21C609E7 | SCRAP LIGHT FOR EAF CHARGING | NULL | NULL | NULL | 2025-12-19T08:51:53.7800000 | NULL | False | False | NULL |
| 156A6C90-7030-429C-92B5-1BFF5E451553 | SKULL EAF | NULL | NULL | NULL | 2025-12-19T09:06:18.6730000 | NULL | False | False | NULL |
| 1B26DFEE-2AED-4A60-B7E3-0C1A9B2A98F2 | BL_SAE1018_130X130 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-12-17T08:37:41.3730000 | NULL | False | False | NULL |
| 1C7B66B3-70E4-48EA-99B9-DC654EAF9D2E | SCRAP LIGHT MELTING BALED STEEL | NULL | NULL | NULL | 2025-12-19T08:51:53.7800000 | NULL | False | False | NULL |
| 245F54A3-6964-4330-ADF4-203044A47F77 | REBAR BILLET ENDCUT/DEFECTIVE/REJECTED | NULL | NULL | NULL | 2025-12-19T08:41:12.4630000 | NULL | False | False | NULL |
| 2574CA25-EAA3-41BA-BA5B-71751802B4EF | BL_SAE1008_150X150_RAW | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-12-17T08:37:41.3700000 | NULL | False | False | NULL |
| 2991D35B-4A71-4A96-81F5-A62056E547EE | SAE1018_GLS | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-12-17T08:06:22.0570000 | NULL | False | False | NULL |
| 2C0A7BDF-4217-4985-A370-9129C77513ED | BL_SAE1018_150X150 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-12-17T08:37:41.3730000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BCFDB4CF-D4A9-4BAE-AE49-47B5753D996A | MILL SCALE | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-07T15:41:47.5500000 | 2026-08-19T14:31:45.0000000 | False | False | NULL |
| D0570782-6BED-422F-9CF0-94B5C259060F | MILL_SCRAP | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-07T15:43:58.2630000 | 2026-08-19T11:18:29.0000000 | False | False | NULL |
| 359336A3-A2B8-4A71-833A-61158484A565 | END CUT | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-19T09:06:18.6570000 | 2026-08-19T11:17:24.0000000 | False | False | NULL |
| 6120578A-6EAB-4BD0-955A-DCF69596DBBC | END CUT WIRE ROD | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-19T09:06:18.6670000 | 2026-08-19T11:16:41.0000000 | False | False | NULL |
| D2C41A4F-1317-4E7C-9C2F-07251263A4CC | RC_B500B_8.0DIA | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-14T10:03:33.9700000 | 2026-08-18T10:43:33.0000000 | False | False | NULL |
| C5CF0E76-2BFD-422B-A1CD-0F76043AD75D | RC_B500B_16.0DIA | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-14T11:05:39.1500000 | 2026-08-18T10:42:55.0000000 | False | False | NULL |
| 1237CEC0-1632-4783-9BE3-659B6988CF8B | RB_B500B_5.5DIA | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-28T11:03:01.9700000 | 2026-08-18T10:41:28.0000000 | False | False | NULL |
| 5789E0A9-710B-41AD-8776-A1D1B42E2B34 | RB_B500B_40.0DIA | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-13T09:40:54.6000000 | 2026-08-18T10:40:54.0000000 | False | False | NULL |
| 2F601111-10BD-4882-BC68-D803CB66B43D | RB_B500B_32.0DIA | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-10T13:20:42.0900000 | 2026-08-18T10:40:21.0000000 | False | False | NULL |
| E61A1D64-A311-4349-93F8-22F6313372E3 | RB_B500B_25.0DIA | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-09T15:54:52.7100000 | 2026-08-18T10:39:43.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_Inventory.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Order_Configurator.Itemid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Materialid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_SAP_Inventory_Stock_Data_Tbl.Material` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.Number` (Many to One)
- `XStudio_XBatch.RM_Charging_Plan.MaterialId` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Rolling_Plan.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Sales_Order.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SAP_Posting_Tbl.MaterialCode` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ItemID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.OutputMaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Trn_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Dtl_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Per_WorkOrder_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Trn_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
