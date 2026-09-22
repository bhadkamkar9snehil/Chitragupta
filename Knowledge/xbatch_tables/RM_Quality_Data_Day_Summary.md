# XStudio_Xbatch.dbo.RM_Quality_Data_Day_Summary

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference dot, back, front, agt, max, min, utsysratio, one, three, two, qty, utsmax.

**Primary Key:** ID  
**Row Count:** 449  
**Date Range (ModifiedOn):** 2026-09-02T08:10:42.2470000 to 2026-09-02T08:10:42.7000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Product | varchar | YES | 100 | — |
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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Campaign | varchar | YES | 100 | — |
| SectionRolled | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| NoOfBilletsDischarged | decimal | YES | 18,3 | — |
| NoOfBilletsCobbled | decimal | YES | 18,3 | — |
| NoOfBilletsHotOut | decimal | YES | 18,3 | — |
| NoOfBilletsRolled | decimal | YES | 18,3 | — |
| NoOfSamplesTaken | int | YES | 10,0 | — |
| Abnormality | varchar | YES | 100 | — |
| NegativeRollingNoDot | decimal | YES | 18,4 | — |
| NegativeRollingOneDot | decimal | YES | 18,4 | — |
| NegativeRollingTwoDot | decimal | YES | 18,4 | — |
| NegativeRollingThreeDot | decimal | YES | 18,4 | — |
| YSMinNoDot | decimal | YES | 18,2 | — |
| YSMinOneDot | decimal | YES | 18,2 | — |
| YSMinTwoDot | decimal | YES | 18,2 | — |
| YSMinThreeDot | decimal | YES | 18,2 | — |
| YSMaxNoDot | decimal | YES | 18,2 | — |
| YSMaxOneDot | decimal | YES | 18,2 | — |
| YSMaxTwoDot | decimal | YES | 18,2 | — |
| YSMaxThreeDot | decimal | YES | 18,2 | — |
| YSStdevNoDot | decimal | YES | 18,2 | — |
| YSStdevOneDot | decimal | YES | 18,2 | — |
| YSStdevTwoDot | decimal | YES | 18,2 | — |
| YSStdevThreeDot | decimal | YES | 18,2 | — |
| UTSMinNoDot | decimal | YES | 18,2 | — |
| UTSMinOneDot | decimal | YES | 18,2 | — |
| UTSMinTwoDot | decimal | YES | 18,2 | — |
| UTSMinThreeDot | decimal | YES | 18,2 | — |
| UTSMaxNoDot | decimal | YES | 18,2 | — |
| UTSMaxOneDot | decimal | YES | 18,2 | — |
| UTSMaxTwoDot | decimal | YES | 18,2 | — |
| UTSMaxThreeDot | decimal | YES | 18,2 | — |
| UTSStdevNoDot | decimal | YES | 18,2 | — |
| UTSStdevOneDot | decimal | YES | 18,2 | — |
| UTSStdevTwoDot | decimal | YES | 18,2 | — |
| UTSStdevThreeDot | decimal | YES | 18,2 | — |
| AgtMinNoDot | decimal | YES | 18,2 | — |
| AgtMinOneDot | decimal | YES | 18,2 | — |
| AgtMinTwoDot | decimal | YES | 18,2 | — |
| AgtMinThreeDot | decimal | YES | 18,2 | — |
| AgtMaxNoDot | decimal | YES | 18,2 | — |
| AgtMaxOneDot | decimal | YES | 18,2 | — |
| AgtMaxTwoDot | decimal | YES | 18,2 | — |
| AgtMaxThreeDot | decimal | YES | 18,2 | — |
| UTSYSRatioMinNoDot | decimal | YES | 18,2 | — |
| UTSYSRatioMinOneDot | decimal | YES | 18,2 | — |
| UTSYSRatioMinTwoDot | decimal | YES | 18,2 | — |
| UTSYSRatioMinThreeDot | decimal | YES | 18,2 | — |
| UTSYSRatioMaxNoDot | decimal | YES | 18,2 | — |
| UTSYSRatioMaxOneDot | decimal | YES | 18,2 | — |
| UTSYSRatioMaxTwoDot | decimal | YES | 18,2 | — |
| UTSYSRatioMaxThreeDot | decimal | YES | 18,2 | — |
| BundleHoldReason | varchar | YES | 1000 | — |
| BundleDefectiveReason | varchar | YES | 1000 | — |
| BilletGrade | varchar | YES | 100 | — |
| ScrapBucketStatus | varchar | YES | 100 | — |
| DelayMinutes | decimal | YES | 18,2 | — |
| DelayReason | varchar | YES | 1000 | — |
| AcceptedWithDeviation | varchar | YES | 1000 | — |
| SAPProductionQty | decimal | YES | 18,3 | — |
| SAPPrimeQty | decimal | YES | 18,3 | — |
| SAPRejQty | decimal | YES | 18,3 | — |
| SAPPostingPendingQty | decimal | YES | 18,3 | — |
| SAPHoldQty | decimal | YES | 18,3 | — |
| ShortBarBundleSAPRejQty | decimal | YES | 18,3 | — |
| YSMinFront | decimal | YES | 18,2 | — |
| YSMinBack | decimal | YES | 18,2 | — |
| YSMaxFront | decimal | YES | 18,2 | — |
| YSMaxBack | decimal | YES | 18,2 | — |
| YSStdevFront | decimal | YES | 18,2 | — |
| YSStdevBack | decimal | YES | 18,2 | — |
| UTSMinFront | decimal | YES | 18,2 | — |
| UTSMinBack | decimal | YES | 18,2 | — |
| UTSMaxFront | decimal | YES | 18,2 | — |
| UTSMaxBack | decimal | YES | 18,2 | — |
| UTSStdevFront | decimal | YES | 18,2 | — |
| UTSStdevBack | decimal | YES | 18,2 | — |
| AgtMinFront | decimal | YES | 18,2 | — |
| AgtMinBack | decimal | YES | 18,2 | — |
| AgtMaxFront | decimal | YES | 18,2 | — |
| AgtMaxBack | decimal | YES | 18,2 | — |
| UTSYSRatioMinFront | decimal | YES | 18,2 | — |
| UTSYSRatioMinBack | decimal | YES | 18,2 | — |
| UTSYSRatioMaxFront | decimal | YES | 18,2 | — |
| UTSYSRatioMaxBack | decimal | YES | 18,2 | — |
| ActualCrossSectionalAreaFront | decimal | YES | 18,2 | — |
| ActualCrossSectionalAreaBack | decimal | YES | 18,2 | — |
| NominalCrossSectionAreaFront | decimal | YES | 18,2 | — |
| NominalCrossSectionAreaBack | decimal | YES | 18,2 | — |
| WtMtrFront | decimal | YES | 18,3 | — |
| WtMtrBack | decimal | YES | 18,3 | — |
| ToleranceFront | decimal | YES | 18,4 | — |
| ToleranceBack | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Product | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 06635AA9-7A19-459F-89BE-D66950F4A3A4 | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:38.8500000 | NULL | False | False | NULL |
| 056B6B08-56F6-41E1-8845-742A168F7B37 | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:42.0270000 | NULL | False | False | NULL |
| 0528D171-4D43-494F-A4BD-897D286F02CB | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:42.2200000 | NULL | False | False | NULL |
| 04E71D59-1F44-4AF1-88D7-8CFAEBEE21AF | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:42.1600000 | NULL | False | False | NULL |
| 04633EFF-FAF1-4D30-8EAC-F1E52F74B57B | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:39.4730000 | NULL | False | False | NULL |
| 0448F6A7-F3E1-4C99-8BB6-ACEA07B9561F | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:39.7830000 | NULL | False | False | NULL |
| 03993D6B-1DA1-444C-957A-F76062B03DA7 | Rebar Coil | NULL | NULL | NULL | 2026-09-02T08:10:40.0530000 | NULL | False | False | NULL |
| 0256E908-6917-4273-893C-BD37853AEE6E | Rebar Coil | NULL | NULL | NULL | 2026-09-02T08:10:37.9400000 | NULL | False | False | NULL |
| 018A7257-2887-40B6-8DD0-9CBA27962FD5 | Rebar | NULL | NULL | NULL | 2026-09-02T08:10:39.4370000 | NULL | False | False | NULL |
| 00B8C020-D854-4055-BB0A-114D9D3E3840 | Rebar Coil | NULL | NULL | NULL | 2026-09-02T08:10:38.4400000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Product | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3CD42F36-2AC5-42AB-B72C-F41FD7286990 | Rebar Coil | NULL | NULL | NULL | 2026-09-01T16:10:48.9730000 | 2026-09-02T08:10:42.7000000 | False | False | NULL |
| 3872B83B-1A4C-42BA-890B-683995568D66 | Rebar Coil | NULL | NULL | NULL | 2026-09-01T16:10:48.9600000 | 2026-09-02T08:10:42.6830000 | False | False | NULL |
| 94A6E7EA-D8C0-4067-8CEE-3B68D292F60D | Rebar Coil | NULL | NULL | NULL | 2026-09-01T16:10:48.9400000 | 2026-09-02T08:10:42.6630000 | False | False | NULL |
| AC927E53-CE9A-4537-AD06-73D60FEB6678 | Rebar Coil | NULL | NULL | NULL | 2026-09-01T16:10:48.9400000 | 2026-09-02T08:10:42.6630000 | False | False | NULL |
| 0BB21AAD-1F8B-415C-B268-5E14610342FE | Rebar Coil | NULL | NULL | NULL | 2026-09-01T16:10:48.9200000 | 2026-09-02T08:10:42.6400000 | False | False | NULL |
| A0DF278E-2126-4E46-AAF5-C5690FA0A3D5 | Rebar | NULL | NULL | NULL | 2026-09-01T16:10:48.9200000 | 2026-09-02T08:10:42.6400000 | False | False | NULL |
| 618F7F39-8F00-4220-84A6-450506BC301D | Rebar | NULL | NULL | NULL | 2026-09-01T16:10:48.8930000 | 2026-09-02T08:10:42.6100000 | False | False | NULL |
| 40E4CD17-F782-4BE8-BE19-9A21E76C7D0F | Rebar | NULL | NULL | NULL | 2026-09-01T16:10:48.8800000 | 2026-09-02T08:10:42.5930000 | False | False | NULL |
| 4F170EBD-D22D-44B9-9E29-F645AB976D8D | Rebar | NULL | NULL | NULL | 2026-09-01T11:39:24.4770000 | 2026-09-02T08:10:42.5830000 | False | False | NULL |
| 789F0444-5913-4A0F-9EB4-04EBEC27BF6B | Rebar | NULL | NULL | NULL | 2026-09-01T11:39:24.4770000 | 2026-09-02T08:10:42.5830000 | False | False | NULL |

---
