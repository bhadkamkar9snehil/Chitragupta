# XStudio_Xbatch.dbo.LRF_Manual_Entry

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference per, consumption, time, electrode, temperature, addition, alloy, caster, consuption, dololime, end, gas.

**Primary Key:** ID  
**Row Count:** 28  
**Date Range (ModifiedOn):** 2025-08-02T10:49:49.0000000 to 2026-02-15T17:42:39.0000000  

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
| IsProcessed | bit | YES | — | — |
| ElectrodeConsumption1Kg | decimal | YES | 18,4 | — |
| LaddleHoldTime | int | YES | 10,0 | — |
| LRFTreatmentEndTime | datetime | YES | — | — |
| LFInTime | datetime | YES | — | — |
| LimeConsuption | decimal | YES | 18,4 | — |
| AlloyAdditionPerTonOfSteel | int | YES | 10,0 | — |
| TemperatureLifting | decimal | YES | 18,4 | — |
| Temperature2 | decimal | YES | 18,4 | — |
| LFProcessTime | int | YES | 10,0 | — |
| HeatNo | int | YES | 10,0 | — |
| Name | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| CasterStartTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| Temperature1 | decimal | YES | 18,4 | — |
| LFOutTime | datetime | YES | — | — |
| NitrogenGasConsumption | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |
| DololimeConsumption | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 100 | — |
| Sample | varchar | YES | 100 | — |
| Temperature | int | YES | 10,0 | — |
| PerC | decimal | YES | 18,4 | — |
| PerMn | decimal | YES | 18,4 | — |
| PerSi | decimal | YES | 18,4 | — |
| PerS | decimal | YES | 18,4 | — |
| PerP | decimal | YES | 18,4 | — |
| PerCr | decimal | YES | 18,4 | — |
| PerNi | decimal | YES | 18,4 | — |
| PerMo | decimal | YES | 18,4 | — |
| PerCu | decimal | YES | 18,4 | — |
| PerSn | decimal | YES | 18,4 | — |
| PerAl | decimal | YES | 18,4 | — |
| PerN2 | decimal | YES | 18,4 | — |
| ElectrodeConsumption2Kg | decimal | YES | 18,4 | — |
| ElectrodeConsumption3Kg | decimal | YES | 18,4 | — |
| TotalElectrodeConsumption | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 26A6EE43-56F8-456C-B953-AEB3F29D36E9 | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| 1B864B14-2809-403E-80EE-D80DEB611114 | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| 0AA2F0D8-05BB-4C47-8CBA-606AA0347DC6 | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| 999977DD-A948-4086-928E-0BF400FF5E06 | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| B7C20CD5-0C82-4FC5-92C0-009028F84F33 | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| C1CF33C7-194E-43BB-9AFD-ECFBF4D6A85E | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| FF0D6713-C0CF-4C6F-87CE-6FE49411FFAA | NULL | NULL | 2025-07-24T17:21:48.3230000 | NULL | False | False | NULL | NULL |  |
| B990766D-B27E-4C5D-9049-50281B8369FF | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T17:21:48.3230000 | 2025-08-02T10:49:49.0000000 | False | False | NULL |  |  |
| BF033DAE-AC94-4512-8C84-5749E99BABD7 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-27T14:32:12.6700000 | 2025-11-27T14:32:12.0000000 | False | False | NULL |  |  |
| F771575A-C606-4D28-BBD1-F07C2F27E00E | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-11-28T15:02:29.1500000 | 2025-11-28T15:02:29.0000000 | False | False | NULL |  |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1E23830D-A688-4112-9F8E-2561A3AF1AC1 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-15T17:42:39.5130000 | 2026-02-15T17:42:39.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| E6EC2A64-C9E5-480E-A33B-C816C83E9E8E | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-15T15:47:38.8900000 | 2026-02-15T15:47:38.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| 4EB2AEA1-04C4-41A3-A31F-6787218F09CF | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-15T15:33:47.2130000 | 2026-02-15T15:33:47.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| 7535F76B-D306-4F18-94CF-849D8F422A7F | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-15T15:21:10.4930000 | 2026-02-15T15:21:10.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| 93636CC6-1808-4BDF-BB02-491B80BC28EE | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-15T14:58:26.7270000 | 2026-02-15T14:58:26.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| 856A4127-79A3-4BF1-B9BA-F6AD1186F2AE | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-14T14:52:27.0930000 | 2026-02-14T14:52:27.0000000 | False | False | NULL |  | NULL |
| 356E52C1-12F6-45B8-B8A3-F9FC56F329C4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-12T04:59:56.2730000 | 2026-02-12T04:59:56.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| A3C92B36-1EAD-42B2-AE70-2D175717F9C1 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-12T04:17:08.2570000 | 2026-02-12T04:17:08.0000000 | False | False | NULL |  | NULL |
| 2CD4C09B-92BD-4245-A35D-BD02171D5616 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | AB916AAC-C6FE-49B2-8308-D482E3A71BF4 | 2026-02-12T03:20:06.6470000 | 2026-02-12T03:20:06.0000000 | False | False | NULL | 172.16.4.72 | NULL |
| 6738839B-B378-4F18-999B-0908AF10DA83 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-08T17:42:18.7500000 | 2026-02-08T17:42:18.0000000 | False | False | NULL |  | NULL |

---
