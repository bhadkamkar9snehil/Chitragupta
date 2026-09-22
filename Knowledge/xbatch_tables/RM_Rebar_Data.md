# XStudio_Xbatch.dbo.RM_Rebar_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference rebar, speed, cbapprt, cbrit, current, mps, rpm, torque, tmt, bar, lpm, waterflow.

**Primary Key:** ID  
**Row Count:** 1  

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
| RebarPostprCurrentA | decimal | YES | 18,4 | — |
| RebarPostprSpeedRpm | decimal | YES | 18,4 | — |
| RebarPostprTorqueNm | decimal | YES | 18,4 | — |
| RebarPostprSpeedMps | decimal | YES | 18,4 | — |
| RebarTmtWaterflowLine1Lpm | decimal | YES | 18,4 | — |
| RebarTmtWaterflow2Line2Lpm | decimal | YES | 18,4 | — |
| RebarTmtWaterflow3Line3Lpm | decimal | YES | 18,4 | — |
| RebarTmtWaterflow4Line4Lpm | decimal | YES | 18,4 | — |
| RebarTmtMainWaterflowOutLpm | decimal | YES | 18,4 | — |
| RebarTmtWaterpressBar | decimal | YES | 18,4 | — |
| RebarTmtWatertempC | decimal | YES | 18,4 | — |
| RebarDividingShear1CurrentA | decimal | YES | 18,4 | — |
| RebarDividingShear1SpeedRpm | decimal | YES | 18,4 | — |
| RebarDividingShear1TorqueNm | decimal | YES | 18,4 | — |
| RebarDividingShear1SpeedMps | decimal | YES | 18,4 | — |
| RebarFinishbyprtCurrentA | decimal | YES | 18,4 | — |
| RebarFinishbyprtSpeedRpm | decimal | YES | 18,4 | — |
| RebarFinishbyprtTorqueNm | decimal | YES | 18,4 | — |
| RebarFinishbyprtSpeedMps | decimal | YES | 18,4 | — |
| RebarTmtextCurrentA | decimal | YES | 18,4 | — |
| RebarTmtextSpeedRpm | decimal | YES | 18,4 | — |
| RebarTmtextTorqueNm | decimal | YES | 18,4 | — |
| RebarTmtextSpeedMps | decimal | YES | 18,4 | — |
| RebarShortBarDivCurrentA | decimal | YES | 18,4 | — |
| RebarShortBarDivSpeedRpm | decimal | YES | 18,4 | — |
| RebarShortBarDivTorqueNm | decimal | YES | 18,4 | — |
| RebarShortBarDivSpeedMps | decimal | YES | 18,4 | — |
| RebarCbapprt1CurrentA | decimal | YES | 18,4 | — |
| RebarCbapprt1SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbapprt1TorqueNm | decimal | YES | 18,4 | — |
| RebarCbapprt1SpeedMps | decimal | YES | 18,4 | — |
| RebarCbapprt2CurrentA | decimal | YES | 18,4 | — |
| RebarCbapprt2SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbapprt2TorqueNm | decimal | YES | 18,4 | — |
| RebarCbapprt2SpeedMps | decimal | YES | 18,4 | — |
| RebarCbapprt3CurrentA | decimal | YES | 18,4 | — |
| RebarCbapprt3SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbapprt3TorqueNm | decimal | YES | 18,4 | — |
| RebarCbapprt3SpeedMps | decimal | YES | 18,4 | — |
| RebarCbapprt4CurrentA | decimal | YES | 18,4 | — |
| RebarCbapprt4SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbapprt4TorqueNm | decimal | YES | 18,4 | — |
| RebarCbapprt4SpeedMps | decimal | YES | 18,4 | — |
| RebarCbapprt5CurrentA | decimal | YES | 18,4 | — |
| RebarCbapprt5SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbapprt5TorqueNm | decimal | YES | 18,4 | — |
| RebarCbapprt5SpeedMps | decimal | YES | 18,4 | — |
| RebarCbapprt6CurrentA | decimal | YES | 18,4 | — |
| RebarCbapprt6SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbapprt6TorqueNm | decimal | YES | 18,4 | — |
| RebarCbapprt6SpeedMps | decimal | YES | 18,4 | — |
| RebarCbrit1CurrentA | decimal | YES | 18,4 | — |
| RebarCbrit1SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbrit1TorqueNm | decimal | YES | 18,4 | — |
| RebarCbrit1SpeedMps | decimal | YES | 18,4 | — |
| RebarCbrit2CurrentA | decimal | YES | 18,4 | — |
| RebarCbrit2SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbrit2TorqueNm | decimal | YES | 18,4 | — |
| RebarCbrit2SpeedMps | decimal | YES | 18,4 | — |
| RebarCbrit3CurrentA | decimal | YES | 18,4 | — |
| RebarCbrit3SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbrit3TorqueNm | decimal | YES | 18,4 | — |
| RebarCbrit3SpeedMps | decimal | YES | 18,4 | — |
| RebarCbrit4CurrentA | decimal | YES | 18,4 | — |
| RebarCbrit4SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbrit4TorqueNm | decimal | YES | 18,4 | — |
| RebarCbrit4SpeedMps | decimal | YES | 18,4 | — |
| RebarCbrit5CurrentA | decimal | YES | 18,4 | — |
| RebarCbrit5SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbrit5TorqueNm | decimal | YES | 18,4 | — |
| RebarCbrit5SpeedMps | decimal | YES | 18,4 | — |
| RebarCbrit6CurrentA | decimal | YES | 18,4 | — |
| RebarCbrit6SpeedRpm | decimal | YES | 18,4 | — |
| RebarCbrit6TorqueNm | decimal | YES | 18,4 | — |
| RebarCbrit6SpeedMps | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5E645CA3-9CF6-448E-B2AC-32B46F7B50B8 | NULL | NULL | NULL | NULL | 2025-11-26T09:53:26.7430000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Rebar_Data.EquipmentID` -> `XStudio_XBatch.RM_Rebar_Mst_Tbl.ID` (Many to One)
