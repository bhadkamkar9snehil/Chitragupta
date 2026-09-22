# XStudio_Xbatch.dbo.Temp_Rebar_Quality_Data_15_25_59_11_09_2026

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference agt, camp, charging, error, grade, isvalid, line, message, rebend, remarks, rra, sample.

**Primary Key:** —  
**Row Count:** 32,595  
**Date Range (Entry Date):** 2025-01-09T00:00:00.0000000 to 2026-08-24T00:00:00.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| Entry Date | datetime | YES | — | — |
| Camp | nvarchar | YES | -1 | — |
| Heat No | nvarchar | YES | -1 | — |
| C | float | YES | 53 | — |
| Mn | float | YES | 53 | — |
| Sample | bigint | YES | 19,0 | — |
| Sample Recieving Time | nvarchar | YES | -1 | — |
| Testing Time | nvarchar | YES | -1 | — |
| Line | nvarchar | YES | -1 | — |
| Nom d mm | nvarchar | YES | -1 | — |
| Nominal CSA mm2 | float | YES | 53 | — |
| ACSA mm2 | float | YES | 53 | — |
| Wt per Mtr | float | YES | 53 | — |
| Tolerance | float | YES | 53 | — |
| Rib less Spacing mm | nvarchar | YES | -1 | — |
| Centre Rib Spacing C mm | nvarchar | YES | -1 | — |
| Tran Rib ht mm | nvarchar | YES | -1 | — |
| Long Rib ht mm | nvarchar | YES | -1 | — |
| RRA | nvarchar | YES | -1 | — |
| Rib Inclination | nvarchar | YES | -1 | — |
| Rib Flank Inclination | nvarchar | YES | -1 | — |
| Roots of Transverse Rib | nvarchar | YES | -1 | — |
| YS MPa | float | YES | 53 | — |
| UTS MPa | bigint | YES | 19,0 | — |
| UTS_YS Ratio | nvarchar | YES | -1 | — |
| Agt | float | YES | 53 | — |
| Rebend | nvarchar | YES | -1 | — |
| Grade | nvarchar | YES | -1 | — |
| Charging | nvarchar | YES | -1 | — |
| Remarks | nvarchar | YES | -1 | — |
| Initial of Testing Person | nvarchar | YES | -1 | — |
| Shift InCharge Operation | nvarchar | YES | -1 | — |
| Billet Grade | nvarchar | YES | -1 | — |
| ID | nvarchar | YES | -1 | — |
| ISValid | bit | YES | — | — |
| ErrorMessage | nvarchar | YES | -1 | — |

### Top 10 Records

| Entry Date | Camp | Heat No | C | Mn | Sample | Sample Recieving Time | Testing Time | Line | Nom d mm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-15T00:00:00.0000000 | 2 | 1602423 | 0.19 | 0.52 | 4 | 11:05:00 | 11:19:24 | No dot | 10 |
| 2026-06-25T00:00:00.0000000 | 2 | 1603752 | 0.2 | 0.55 | 28 | 21:29:00 | 21:33:19 | One dot | 8 |
| 2026-02-12T00:00:00.0000000 | 1 | 1601018 | 0.23 | 0.51 | 4 | 18:10:00 | 18:17:12 | one dot | 14 |
| 2026-02-19T00:00:00.0000000 | 1 | 1601195 | 0.23 | 0.49 | 5 | 19:10:00 | 19:14:19 | No dot | 16 |
| 2026-07-21T00:00:00.0000000 | 2 | 1260611 | 0.2 | 0.63 | 1 | 18:33:00 | 18:37:19 | No dot | 10 |
| 2026-03-03T00:00:00.0000000 | 1 | 1601506 | 0.23 | 0.51 | 15 | 04:10:00 | 04:17:12 | No dot | 14 |
| 2026-06-17T00:00:00.0000000 | 1 | 1260103 | 0.2 | 0.68 | 22 | 23:15:00 | 23:29:24 | Two dot | 10 |
| 2026-05-14T00:00:00.0000000 | 1 | 1602810 | 0.22 | 0.72 | 1 | 19:36:00 | 19:40:19 | One dot | 16 |
| 2026-01-29T00:00:00.0000000 | 1 | 1600643 | 0.24 | 0.52 | 18 | 19:30:00 | 19:34:19 | No dot | 16 |
| 2026-04-29T00:00:00.0000000 | 3 | 1602714 | 0.2 | 0.54 | 22 | 18:15:00 | 18:29:24 | One dot | 10 |

### Bottom 10 Records

| Entry Date | Camp | Heat No | C | Mn | Sample | Sample Recieving Time | Testing Time | Line | Nom d mm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-02T00:00:00.0000000 | 1 | 2602331 | 0.22 | 0.72 | 2 | 04:35:00 | 04:39:19 | No dot | 32 |
| 2026-06-17T00:00:00.0000000 | 1 | 1260096 | 0.2 | 0.69 | 45 | 11:48:00 | 12:02:24 | One dot | 10 |
| 2026-08-07T00:00:00.0000000 | 1 | 2605973 | 0.23 | 0.67 | 39 | 23:30:00 | 23:34:19 | No dot | 32 |
| 2026-07-19T00:00:00.0000000 | 2 | 1603984 | 0.18 | 0.61 | 30 | 03:00:00 | 03:14:24 | One dot | 10 |
| 2026-02-20T00:00:00.0000000 | 1 | 1601216 | 0.22 | 0.5 | 7 | 14:20:00 | 14:24:19 | No dot | 16 |
| 2026-07-21T00:00:00.0000000 | 2 | 1260707 | 0.19 | 0.65 | 5 | 15:52:00 | 15:56:19 | Three Dot | 10 |
| 2026-01-07T00:00:00.0000000 | 1 | 1600167 | 0.23 | 0.53 | 36 | 19:40:00 | 19:47:12 | No dot | 14 |
| 2026-03-31T00:00:00.0000000 | 2 | 1602122 | 0.19 | 0.53 | 26 | 00:45:00 | 00:59:24 | One dot | 10 |
| 2026-03-15T00:00:00.0000000 | 2 | 1601805 | 0.19 | 0.52 | 4 | 05:30:00 | 05:44:24 | One dot | 8 |
| 2026-07-22T00:00:00.0000000 | 2 | 1260543 | 0.19 | 0.68 | 36 | 23:30:00 | 23:34:19 | Three Dot | 10 |

---
