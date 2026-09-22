# XStudio_Xbatch.dbo.CCM_SMS_Block

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference std, flow, min, pressure, inlet, outlet, strand, temp, production, total, count, billet.

**Primary Key:** ID  
**Row Count:** 0  

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
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| CCMHeatID | decimal | YES | 18,4 | — |
| STD1BilletCount | decimal | YES | 18,4 | — |
| STD2BilletCount | decimal | YES | 18,4 | — |
| STD3BilletCount | decimal | YES | 18,4 | — |
| STD4BilletCount | decimal | YES | 18,4 | — |
| STD5BilletCount | decimal | YES | 18,4 | — |
| STD6BilletCount | decimal | YES | 18,4 | — |
| STD1CastingSpeed | decimal | YES | 18,4 | — |
| STD2CastingSpeed | decimal | YES | 18,4 | — |
| STD4CastingSpeed | decimal | YES | 18,4 | — |
| STD5CastingSpeed | decimal | YES | 18,4 | — |
| STD6CastingSpeed | decimal | YES | 18,4 | — |
| STD1OSCSpeed | decimal | YES | 18,4 | — |
| STD2OSCSpeed | decimal | YES | 18,4 | — |
| STD3OSCSpeed | decimal | YES | 18,4 | — |
| STD4OSCSpeed | decimal | YES | 18,4 | — |
| STD5OSCSpeed | decimal | YES | 18,4 | — |
| STD6OSCSpeed | decimal | YES | 18,4 | — |
| STD3CastingSpeed | decimal | YES | 18,4 | — |
| TotalBilletsCount | decimal | YES | 18,4 | — |
| STD1BLTSpecificWeight | decimal | YES | 18,4 | — |
| STD2BLTSpecificWeight | decimal | YES | 18,4 | — |
| STD3BLTSpecificWeight | decimal | YES | 18,4 | — |
| STD4BLTSpecificWeight | decimal | YES | 18,4 | — |
| STD5BLTSpecificWeight | decimal | YES | 18,4 | — |
| STD6BLTSpecificWeight | decimal | YES | 18,4 | — |
| STD1Production | decimal | YES | 18,4 | — |
| STD2Production | decimal | YES | 18,4 | — |
| STD3Production | decimal | YES | 18,4 | — |
| STD4Production | decimal | YES | 18,4 | — |
| STD5Production | decimal | YES | 18,4 | — |
| STD6Production | decimal | YES | 18,4 | — |
| TotalProduction | decimal | YES | 18,4 | — |
| CrossSection | decimal | YES | 18,4 | — |
| MonthlyTarget | decimal | YES | 18,4 | — |
| MTDPlannedTon | decimal | YES | 18,4 | — |
| TodayPlannedProduction | decimal | YES | 18,4 | — |
| AskingRate | decimal | YES | 18,4 | — |
| Month | varchar | YES | 100 | — |
| MTDAchievedpercentage | decimal | YES | 18,4 | — |
| RunningRate | decimal | YES | 18,4 | — |
| TodayAchievedpercentage | decimal | YES | 18,4 | — |
| Year | decimal | YES | 18,4 | — |
| YesterdayAchievedpercentage | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD1 | decimal | YES | 18,4 | — |
| InletPressureSTD1 | decimal | YES | 18,4 | — |
| OutletPressureSTD1 | decimal | YES | 18,4 | — |
| InletTempT1STD1 | decimal | YES | 18,4 | — |
| OutletTempT2STD1 | decimal | YES | 18,4 | — |
| DeltaTSTD1 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD1 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD1 | decimal | YES | 18,4 | — |
| WeeklyTarget | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD1 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD1 | decimal | YES | 18,4 | — |
| WeeklyAchievedProduction | decimal | YES | 18,4 | — |
| WeeklyAchievedpercentage | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD2 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD2 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD2 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD3 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD4 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD5 | decimal | YES | 18,4 | — |
| FlowZ1LtMinSTD6 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD3 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD4 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD5 | decimal | YES | 18,4 | — |
| FlowZ2LtMinSTD6 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD3 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD4 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD5 | decimal | YES | 18,4 | — |
| FlowZ3LtMinSTD6 | decimal | YES | 18,4 | — |
| DeltaTSTD2 | decimal | YES | 18,4 | — |
| DeltaTSTD3 | decimal | YES | 18,4 | — |
| DeltaTSTD4 | decimal | YES | 18,4 | — |
| DeltaTSTD5 | decimal | YES | 18,4 | — |
| DeltaTSTD6 | decimal | YES | 18,4 | — |
| InletPressureSTD2 | decimal | YES | 18,4 | — |
| InletPressureSTD3 | decimal | YES | 18,4 | — |
| InletPressureSTD4 | decimal | YES | 18,4 | — |
| InletPressureSTD6 | decimal | YES | 18,4 | — |
| InletPressureSTD5 | decimal | YES | 18,4 | — |
| OutletPressureSTD2 | decimal | YES | 18,4 | — |
| OutletPressureSTD3 | decimal | YES | 18,4 | — |
| OutletPressureSTD4 | decimal | YES | 18,4 | — |
| OutletPressureSTD5 | decimal | YES | 18,4 | — |
| OutletPressureSTD6 | decimal | YES | 18,4 | — |
| InletTempT1STD2 | decimal | YES | 18,4 | — |
| InletTempT1STD3 | decimal | YES | 18,4 | — |
| InletTempT1STD4 | decimal | YES | 18,4 | — |
| InletTempT1STD5 | decimal | YES | 18,4 | — |
| InletTempT1STD6 | decimal | YES | 18,4 | — |
| OutletTempT2STD2 | decimal | YES | 18,4 | — |
| OutletTempT2STD3 | decimal | YES | 18,4 | — |
| OutletTempT2STD4 | decimal | YES | 18,4 | — |
| OutletTempT2STD5 | decimal | YES | 18,4 | — |
| OutletTempT2STD6 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD2 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD3 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD4 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD5 | decimal | YES | 18,4 | — |
| TotalFlowLtMinSTD6 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD2 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD3 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD4 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD5 | decimal | YES | 18,4 | — |
| MouldWaterFlowLMinSTD6 | decimal | YES | 18,4 | — |
| YearlyTarget | decimal | YES | 18,4 | — |
| TPH | decimal | YES | 18,4 | — |
| Strand1WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand2WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand3WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand4WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand5WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand6WithdrawalPressure | decimal | YES | 18,4 | — |
| Strand1StraightnerPressure | decimal | YES | 18,4 | — |
| Strand2StraightnerPressure | decimal | YES | 18,4 | — |
| Strand3StraightnerPressure | decimal | YES | 18,4 | — |
| Strand4StraightnerPressure | decimal | YES | 18,4 | — |
| Strand5StraightnerPressure | decimal | YES | 18,4 | — |
| Strand6StraightnerPressure | decimal | YES | 18,4 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_SMS_Block.EquipmentID` -> `XStudio_XBatch.CCM_SMS_Mst_Tbl.ID` (Many to One)
