# XStudio_Xbatch.dbo.Communication_System_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference plc, status, ccm, error, std, code, enable, licensed, text, eaf, cpu, furnace.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-09-02T10:48:05.2600000 to 2026-09-02T10:48:05.2600000  

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
| EquipmentID | varchar | YES | 36 | — |
| CCM_COMMON_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_COMMON_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_COMMON_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_COMMON_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_COMMON_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_CVS_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_CVS_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_CVS_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_CVS_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_CVS_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_1_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_1_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_STD_1_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_STD_1_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_1_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_2_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_2_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_STD_2_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_STD_2_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_2_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_3_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_3_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_STD_3_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_STD_3_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_3_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_4_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_4_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_STD_4_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_STD_4_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_4_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_5_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_5_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_STD_5_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_STD_5_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_5_PLC_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_6_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_6_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| CCM_STD_6_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| CCM_STD_6_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| CCM_STD_6_PLC_STATUS | decimal | YES | 18,4 | — |
| EAF_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| EAF_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| EAF_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| EAF_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| Furnace_Combution_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| Furnace_Combution_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| Furnace_Combution_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| Furnace_Combution_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| Furnace_Combution_PLC_STATUS | decimal | YES | 18,4 | — |
| Furnace_Handling_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| Furnace_Handling_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| Furnace_Handling_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| Furnace_Handling_PLC_STATUS | decimal | YES | 18,4 | — |
| Furnace_Handlling_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| EAF_ISAC_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| EAF_ISAC_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| EAF_ISAC_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| EAF_ISAC_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| EAF_ISAC_PLC_STATUS | decimal | YES | 18,4 | — |
| LRF_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| LRF_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| LRF_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| LRF_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| LRF_PLC_STATUS | decimal | YES | 18,4 | — |
| LRF_MHS_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| LRF_MHS_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| LRF_MHS_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| LRF_MHS_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| LRF_MHS_PLC_STATUS | decimal | YES | 18,4 | — |
| EAF_MORE_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| EAF_MORE_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| EAF_MORE_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| EAF_MORE_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| EAF_MORE_PLC_STATUS | decimal | YES | 18,4 | — |
| EAF_PLC_STATUS | decimal | YES | 18,4 | — |
| WRM_CPU_1_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| WRM_CPU_1_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| WRM_CPU_1_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| WRM_CPU_1_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| WRM_CPU_1_PLC_STATUS | decimal | YES | 18,4 | — |
| WRM_CPU_2_PLC_ENABLE_STATUS | decimal | YES | 18,4 | — |
| WRM_CPU_2_PLC_ERROR_CODE | decimal | YES | 18,4 | — |
| WRM_CPU_2_PLC_ERROR_TEXT | varchar | YES | 100 | — |
| WRM_CPU_2_PLC_LICENSED_STATUS | decimal | YES | 18,4 | — |
| WRM_CPU_2_PLC_STATUS | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8DB238EE-7599-4F5A-8DDB-201840400EB6 | NULL | NULL | NULL | NULL | 2026-07-27T08:22:09.5630000 | 2026-09-02T10:48:05.2600000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Communication_System_Data.EquipmentID` -> `XStudio_XBatch.Communication_System_Mst_Tbl.ID` (Many to One)
