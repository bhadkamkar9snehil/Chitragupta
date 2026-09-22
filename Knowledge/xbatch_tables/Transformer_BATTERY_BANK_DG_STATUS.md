# XStudio_Xbatch.dbo.Transformer_BATTERY_BANK_DG_STATUS

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference charger, ecr, auto, man, voltage, battery, oper, pcurrent, pvoltage, wtpdg, opcurrent, opvoltage.

**Primary Key:** ID  
**Row Count:** 209  
**Date Range (ModifiedOn):** 2025-08-04T10:22:54.0000000 to 2026-07-08T13:50:23.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| ECR1OperPVoltage | decimal | YES | 18,4 | — |
| ECR1OperPCurrent | decimal | YES | 18,4 | — |
| ECR4OperPCurrent | decimal | YES | 18,4 | — |
| ECR4OperPVoltage | decimal | YES | 18,4 | — |
| MRSSOperPVoltage | decimal | YES | 18,4 | — |
| MRSSOperPCurrent | decimal | YES | 18,4 | — |
| ECR5AOperPCurrent | decimal | YES | 18,4 | — |
| ECR5AOperPVoltage | decimal | YES | 18,4 | — |
| DG1Voltage | decimal | YES | 18,4 | — |
| DG1AutoMan | bit | YES | — | — |
| DG2Voltage | decimal | YES | 18,4 | — |
| DG3Voltage | decimal | YES | 18,4 | — |
| DG2AutoMan | bit | YES | — | — |
| DG3AutoMan | bit | YES | — | — |
| WTPDG1Voltage | decimal | YES | 18,4 | — |
| WTPDG1AutoMan | bit | YES | — | — |
| WTPDG2Voltage | decimal | YES | 18,4 | — |
| WTPDG2AutoMan | bit | YES | — | — |
| Remarks | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| BatteryCharger1OPVoltage | decimal | YES | 18,4 | — |
| BatteryCharger1OPCurrent | decimal | YES | 18,4 | — |
| BatteryCharger2OPCurrent | decimal | YES | 18,4 | — |
| BatteryCharger2OPVoltage | decimal | YES | 18,4 | — |
| SVCBatteryChargerOPVoltage | decimal | YES | 18,4 | — |
| SVCBatteryChargerOPCurrent | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7439A401-A791-4B36-9026-BCFC92503C31 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T15:06:53.1070000 | 2025-08-04T10:22:54.0000000 | False | False | NULL |
| AE6F289E-D808-46CA-B3B7-74E144EE8EFF | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-29T16:57:01.8770000 | 2025-10-29T16:57:01.0000000 | False | False | NULL |
| 8528FED7-7022-4E08-8418-220120FBBBC8 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-31T08:41:28.6800000 | 2025-10-31T08:41:28.0000000 | False | False | NULL |
| 9B7150B9-0424-47F0-A3F3-6D9C3BA17930 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-01T09:16:42.7270000 | 2025-11-01T09:16:42.0000000 | False | False | NULL |
| EA94D1FF-C45F-45A6-9A80-74A00BF98728 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-02T09:26:59.4730000 | 2025-11-02T09:26:59.0000000 | False | False | NULL |
| FB2CF0D3-8B9B-4FB5-8C9A-207C4535A5DB | NULL | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-11-04T11:08:40.9070000 | 2025-11-04T11:08:40.0000000 | False | False | NULL |
| 8C7761F8-FEA5-4881-9C14-27932E37D090 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-06T12:54:58.9300000 | 2025-11-06T12:54:58.0000000 | False | False | NULL |
| 7A0D9C71-0E65-4024-9994-D0B9980942BA | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-07T16:04:58.6400000 | 2025-11-07T16:04:58.0000000 | False | False | NULL |
| 3CB54E86-8600-4B0C-A5A8-11B1ED9ED06C | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-05T13:13:19.3600000 | 2025-11-07T16:05:27.0000000 | False | False | NULL |
| EE19F24C-E281-495D-9C34-A4EEF56D6FA9 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-08T11:22:48.9430000 | 2025-11-08T11:22:48.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6AC903BC-A1EF-44D5-B8EA-1135AE1A2D5B | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T13:50:23.6670000 | 2026-07-08T13:50:23.0000000 | False | False | NULL |
| 35D38C0A-41EF-465C-BF04-B86E1BCEF382 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T08:48:15.8800000 | 2026-07-07T08:48:15.0000000 | False | False | NULL |
| 2EA9174A-102F-4687-B63B-BE70518BABDE | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T09:20:38.9330000 | 2026-07-06T09:20:38.0000000 | False | False | NULL |
| B823A33E-8CB7-4620-AA4D-3BC9C09E01CF | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-04T10:10:01.2800000 | 2026-07-04T10:10:01.0000000 | False | False | NULL |
| ED08826B-5AFB-491F-B705-B51ABEFFB190 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-03T08:51:28.7100000 | 2026-07-03T08:51:28.0000000 | False | False | NULL |
| 24D55144-888E-4790-AD6C-C63A07FAB0EE | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-02T09:42:38.9000000 | 2026-07-02T09:42:38.0000000 | False | False | NULL |
| 8A2FDD43-EA64-4F51-A341-9C6F4E81E28F | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-07-01T09:38:47.5230000 | 2026-07-01T09:38:47.0000000 | False | False | NULL |
| 59D3CD2C-68F0-4944-A2E7-C0D799584F67 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-06-30T08:46:03.6530000 | 2026-06-30T08:46:03.0000000 | False | False | NULL |
| 1D7E678D-D66E-48D8-88F5-3C421BD546AD | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-06-29T09:38:50.8570000 | 2026-06-29T09:38:50.0000000 | False | False | NULL |
| BCC09F51-5120-41A0-AE54-7BDF4CA61CF5 | NULL | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-06-28T15:49:07.3200000 | 2026-06-28T15:49:07.0000000 | False | False | NULL |

---
