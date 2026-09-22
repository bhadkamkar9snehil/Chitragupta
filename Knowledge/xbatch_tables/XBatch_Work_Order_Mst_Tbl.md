# XStudio_Xbatch.dbo.XBatch_Work_Order_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (work_order):** Work order missing, wrong state, cancelled/aborted, campaign-linked, or order-creation issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** core, data, eaf, execution, flow, heat, insert, order, per, routing, work (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference order, mfg, date, time, planned, production, billets, bundles, end, name, scheduled, start.

**Primary Key:** ID  
**Row Count:** 54  
**Date Range (ModifiedOn):** 2026-03-10T15:40:25.8870000 to 2026-09-01T00:00:25.2700000  

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
| WorkOrderNumber | varchar | YES | 100 | — |
| SerialNumber | int | YES | 10,0 | — |
| Quantity | decimal | NO | 18,2 | — |
| UnitID | varchar | YES | 36 | — |
| ItemID | varchar | NO | 36 | — |
| Status | varchar | YES | 50 | — |
| Description | varchar | YES | 1000 | — |
| HeatNo | varchar | YES | 36 | — |
| SalesOrder | varchar | YES | 36 | — |
| Equipment | varchar | YES | -1 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| ProgressTonnage | decimal | YES | 18,4 | — |
| ProgressDuration | decimal | YES | 18,4 | — |
| RemainingTonnage | decimal | YES | 18,4 | — |
| ProgressPercentage | decimal | YES | 18,4 | — |
| ManufacturingOrderCategory | varchar | YES | 100 | — |
| ManufacturingOrderType | varchar | YES | 100 | — |
| ManufacturingOrderImportance | varchar | YES | 100 | — |
| OrderIsCreated | varchar | YES | 100 | — |
| OrderIsReleased | varchar | YES | 100 | — |
| OrderIsPrinted | varchar | YES | 100 | — |
| OrderIsConfirmed | varchar | YES | 100 | — |
| OrderIsPartiallyConfirmed | varchar | YES | 100 | — |
| OrderIsDelivered | varchar | YES | 100 | — |
| OrderIsDeleted | varchar | YES | 100 | — |
| OrderIsPreCosted | varchar | YES | 100 | — |
| SettlementRuleIsCreated | varchar | YES | 100 | — |
| OrderIsPartiallyReleased | varchar | YES | 100 | — |
| OrderIsLocked | varchar | YES | 100 | — |
| OrderIsTechnicallyCompleted | varchar | YES | 100 | — |
| OrderIsClosed | varchar | YES | 100 | — |
| OrderIsPartiallyDelivered | varchar | YES | 100 | — |
| OrderIsMarkedForDeletion | varchar | YES | 100 | — |
| SettlementRuleIsCrtedManually | varchar | YES | 100 | — |
| OrderIsScheduled | varchar | YES | 100 | — |
| OrderHasGeneratedOperations | varchar | YES | 100 | — |
| OrderIsToBeHandledInBatches | varchar | YES | 100 | — |
| MaterialAvailyIsNotChecked | varchar | YES | 100 | — |
| MfgOrderCreationDate | datetime | YES | — | — |
| MfgOrderCreationTime | time | YES | — | — |
| LastChangeDateTime | datetime | YES | — | — |
| StorageLocation | varchar | YES | 100 | — |
| GoodsRecipientName | varchar | YES | 100 | — |
| UnloadingPointName | varchar | YES | 100 | — |
| InventoryUsabilityCode | varchar | YES | 100 | — |
| MaterialGoodsReceiptDuration | int | YES | 10,0 | — |
| QuantityDistributionKey | varchar | YES | 100 | — |
| StockSegment | varchar | YES | 100 | — |
| OrderInternalBillOfOperations | varchar | YES | 100 | — |
| ProductionPlant | int | YES | 10,0 | — |
| Plant | varchar | YES | 100 | — |
| MRPArea | varchar | YES | 100 | — |
| MRPController | varchar | YES | 100 | — |
| ProductionSupervisor | varchar | YES | 100 | — |
| ProductionVersion | varchar | YES | 100 | — |
| PlannedOrder | varchar | YES | 100 | — |
| SalesOrderItem | varchar | YES | 100 | — |
| BasicSchedulingType | varchar | YES | 100 | — |
| ManufacturingObject | varchar | YES | 100 | — |
| ProductConfiguration | varchar | YES | 100 | — |
| OrderSequenceNumber | varchar | YES | 100 | — |
| BusinessArea | varchar | YES | 100 | — |
| CompanyCode | int | YES | 10,0 | — |
| ProfitCenter | varchar | YES | 100 | — |
| ActualCostsCostingVariant | varchar | YES | 100 | — |
| PlannedCostsCostingVariant | varchar | YES | 100 | — |
| FunctionalArea | varchar | YES | 100 | — |
| MfgOrderPlannedStartDate | datetime | YES | — | — |
| MfgOrderPlannedStartTime | time | YES | — | — |
| MfgOrderPlannedEndDate | datetime | YES | — | — |
| MfgOrderPlannedEndTime | time | YES | — | — |
| MfgOrderScheduledStartDate | datetime | YES | — | — |
| MfgOrderScheduledStartTime | time | YES | — | — |
| MfgOrderScheduledEndDate | datetime | YES | — | — |
| MfgOrderScheduledEndTime | time | YES | — | — |
| MfgOrderActualReleaseDate | varchar | YES | 100 | — |
| ProductionUnit | varchar | YES | 100 | — |
| ProductionUnitISOCode | varchar | YES | 100 | — |
| ProductionUnitSAPCode | varchar | YES | 100 | — |
| MfgOrderPlannedScrapQty | decimal | YES | 18,4 | — |
| MfgOrderConfirmedYieldQty | decimal | YES | 18,4 | — |
| CustomerName | varchar | YES | 100 | — |
| WBSElementExternalID | varchar | YES | 100 | — |
| OrderLongText | varchar | YES | 100 | — |
| ColourCode | varchar | YES | 50 | — |
| Sn | int | YES | 10,0 | — |
| MaterialName | varchar | YES | 100 | — |
| SalesOrderName | varchar | YES | 100 | — |
| ReleasedDate | datetime | YES | — | — |
| ActualCompletionDate | datetime | YES | — | — |
| SAPTransactionID | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| CampaignId | varchar | YES | 100 | — |
| Length | decimal | YES | 18,4 | — |
| Size | varchar | YES | 100 | — |
| MinBundles | decimal | YES | 18,4 | — |
| MaxBundles | decimal | YES | 18,4 | — |
| MinQtyToRoll | decimal | YES | 18,4 | — |
| NoOfPiecesInBundles | int | YES | 10,0 | — |
| BilletsRolled | int | YES | 10,0 | — |
| BilletsCobble | int | YES | 10,0 | — |
| BilletsHotout | int | YES | 10,0 | — |
| BilletDischarged | int | YES | 10,0 | — |
| BilletsRemaining | int | YES | 10,0 | — |
| TotalBillets | int | YES | 10,0 | — |
| BilletDischargedWeight | decimal | YES | 18,4 | — |
| BundlesProduce | int | YES | 10,0 | — |
| BundlesRemaining | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4538FA74-5DD5-4056-8A87-C1BE0B532173 | CP5_28072026_WO_2 | NULL | NULL | NULL | 2026-07-30T12:55:13.1900000 | NULL | False | False | NULL |
| 7E0FD9ED-14F4-4D19-8A50-6BD39D8179A0 | CP5_28072026_WO_6 | NULL | NULL | NULL | 2026-07-30T12:55:13.1900000 | NULL | False | False | NULL |
| 935D06D1-D370-46BB-9216-695961215CEA | CP5_28072026_WO_4 | NULL | NULL | NULL | 2026-07-30T12:55:13.1900000 | NULL | False | False | NULL |
| F7F7FC26-4EEB-4D49-BC39-94B6E0A915D6 | CP5_28072026_WO_3 | NULL | NULL | NULL | 2026-07-30T12:55:13.1900000 | NULL | False | False | NULL |
| 8F2941E3-BE0C-4006-BD2B-E441C96861A2 | MES_2026031015_LS | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-03-10T15:40:25.7600000 | 2026-03-10T15:40:25.8870000 | False | False | NULL |
| 961DF619-27F2-4364-86EB-75DD51F7FD35 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-03-10T13:07:36.1430000 | 2026-04-01T21:12:28.4800000 | False | False | NULL |
| 820F590A-E35A-4247-8DC2-D553545F70AA | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-01T00:00:07.8670000 | 2026-04-02T10:07:03.7000000 | False | False | NULL |
| 058412B5-AABA-46A8-9257-60F1FD68D443 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-10T13:06:48.0030000 | 2026-04-02T21:12:17.5800000 | False | False | NULL |
| 3B0C40DC-5EC4-4361-AC51-76AD4CDB8307 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-11T20:12:24.9230000 | 2026-04-12T03:29:02.7630000 | False | False | NULL |
| F60C2B8F-DC30-4468-B3E4-C58B1EF7FD88 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-11T20:22:37.4630000 | 2026-04-12T03:29:02.7900000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 37259A41-757B-4D2B-9AC6-760B9B254371 | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-09-01T00:00:00.1500000 | 2026-09-01T00:00:25.2700000 | False | False | NULL |
| 28DAB47B-8B1A-4D58-A7C3-C7588863D300 | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-09-01T00:00:00.2370000 | 2026-09-01T00:00:21.0700000 | False | False | NULL |
| 9212319F-69E1-4C23-ACEF-D81E75491309 | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-01T00:00:06.0000000 | 2026-09-01T00:00:00.6930000 | False | False | NULL |
| 8BBEE5CE-7461-41D0-BE78-7B8E29336E2F | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-08-01T00:00:05.9500000 | 2026-09-01T00:00:00.6330000 | False | False | NULL |
| BB3D6FE9-CEBD-447F-BE45-891548BEC566 | CP3_21082026_RB25mm_WO_2 | NULL | NULL |  | 2026-08-21T15:52:07.4500000 | 2026-08-24T16:05:08.7200000 | False | False | NULL |
| 180EACB3-BBC6-4DA8-AF75-21A68771A773 | CP3_21082026_RB25mm_WO_1 | NULL | NULL |  | 2026-08-21T15:52:07.3570000 | 2026-08-24T16:05:08.5600000 | False | False | NULL |
| 4FE84B02-CC1C-47D4-83E4-97B969F6D293 | CP1_17082026_RB25mm_WO_1 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-17T16:54:20.5970000 | 2026-08-21T15:57:57.0800000 | False | False | NULL |
| A04CA69B-0C00-4975-99FA-32D5E08BB95B | CP3_21082026_RB25mm_WO_6 | NULL | NULL | NULL | 2026-08-21T15:52:07.5570000 | 2026-08-21T15:53:19.3370000 | False | False | NULL |
| 89A05C05-4320-44C1-9374-8977EC5C7A64 | CP3_21082026_RB25mm_WO_7 | NULL | NULL | NULL | 2026-08-21T15:52:07.5830000 | 2026-08-21T15:53:12.4270000 | False | False | NULL |
| C4BED4DE-E69C-4A60-8256-7711A0B693C6 | CP3_21082026_RB25mm_WO_4 | NULL | NULL | NULL | 2026-08-21T15:52:07.5030000 | 2026-08-21T15:53:08.9000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Per_Heat.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_PER_HEAT.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_Per_Heat.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_SAP_WorkOrder_Movements_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_TMT.workorder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_WRM.Workorder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Operator_HeatSelection.length` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.Length` (Many to Many)
- `XStudio_XBatch.RM_Operator_HeatSelection.workorder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SAP_Posting_Tbl.WorkOrderNo` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.WorkOrderNumber` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.WorkOrderID` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Cons_Per_WorkOrder_Tbl.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.CCMWorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.EAFWorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_MES_Heat_Tracking.LRFWorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.CampaignId` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.Equipment` -> `XStudio_XBatch.Equipment.Name` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ItemID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ManufacturingOrderType` -> `XStudio_XBatch.Order_Type_MST.OrderType` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ProductionPlant` -> `XStudio_XBatch.Plant_Mst_Tbl.Name` (Many to One)
