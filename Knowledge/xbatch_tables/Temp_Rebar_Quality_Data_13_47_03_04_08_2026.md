# XStudio_Xbatch.dbo.Temp_Rebar_Quality_Data_13_47_03_04_08_2026

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference null, agt, camp, charging, error, grade, isvalid, line, message, rebend, remarks, rra.

**Primary Key:** —  
**Row Count:** 214  
**Date Range (Sample Recieving Time):** 1899-12-31T00:05:00.0000000 to 1899-12-31T23:55:00.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | nvarchar | YES | -1 | — |
| Entry Date | nvarchar | YES | -1 | — |
| Shift | nvarchar | YES | -1 | — |
| Camp | nvarchar | YES | -1 | — |
| Heat No | bigint | YES | 19,0 | — |
| C | float | YES | 53 | — |
| Mn | float | YES | 53 | — |
| Sample | bigint | YES | 19,0 | — |
| Sample Recieving Time | datetime | YES | — | — |
| Testing Time | datetime | YES | — | — |
| Line | nvarchar | YES | -1 | — |
| Nom d mm | bigint | YES | 19,0 | — |
| ACSA mm2 | float | YES | 53 | — |
| Nominal CSA mm2 | bigint | YES | 19,0 | — |
| Wt per Mtr | float | YES | 53 | — |
| Tol | float | YES | 53 | — |
| Rib less mm | float | YES | 53 | — |
| Rib Spacing C mm | float | YES | 53 | — |
| Tran Rib ht mm | float | YES | 53 | — |
| Long Rib ht mm | float | YES | 53 | — |
| RRA | float | YES | 53 | — |
| Rib Inclination | bigint | YES | 19,0 | — |
| Rib Flank Inclination | bigint | YES | 19,0 | — |
| Roots of Transverse Rib | nvarchar | YES | -1 | — |
| YS MPa | bigint | YES | 19,0 | — |
| UTS MPa | bigint | YES | 19,0 | — |
| UTS_YS Ratio | float | YES | 53 | — |
| Agt | float | YES | 53 | — |
| Rebend | nvarchar | YES | -1 | — |
| Grade | nvarchar | YES | -1 | — |
| Remarks | nvarchar | YES | -1 | — |
| Charging | nvarchar | YES | -1 | — |
| Initial of Testing Person | nvarchar | YES | -1 | — |
| Shift InCharge Operation | nvarchar | YES | -1 | — |
| Billet Grade | nvarchar | YES | -1 | — |
| ISValid | bit | YES | — | — |
| ErrorMessage | nvarchar | YES | -1 | — |

### Top 10 Records

| ID | Entry Date | Shift | Camp | Heat No | C | Mn | Sample | Sample Recieving Time | Testing Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NULL | 02.08.2026 | NULL | WS | 1260757 | 0.2 | 0.64 | 30 | 1899-12-31T09:10:00.0000000 | 1899-12-31T09:12:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260757 | 0.2 | 0.64 | 15 | 1899-12-31T08:55:00.0000000 | 1899-12-31T08:57:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260757 | 0.2 | 0.64 | 5 | 1899-12-31T08:35:00.0000000 | 1899-12-31T08:37:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 45 | 1899-12-31T08:25:00.0000000 | 1899-12-31T08:27:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 30 | 1899-12-31T08:00:00.0000000 | 1899-12-31T08:02:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 15 | 1899-12-31T07:35:00.0000000 | 1899-12-31T07:37:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 5 | 1899-12-31T07:15:00.0000000 | 1899-12-31T07:17:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260785 | 0.2 | 0.69 | 45 | 1899-12-31T07:00:00.0000000 | 1899-12-31T07:02:52.8000000 |
| NULL | 02.08.2026 | NULL | 1 | 1260785 | 0.2 | 0.69 | 30 | 1899-12-31T06:45:00.0000000 | 1899-12-31T06:47:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260785 | 0.2 | 0.69 | 15 | 1899-12-31T06:30:00.0000000 | 1899-12-31T06:32:52.8000000 |

### Bottom 10 Records

| ID | Entry Date | Shift | Camp | Heat No | C | Mn | Sample | Sample Recieving Time | Testing Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NULL | 02.08.2026 | NULL | WS | 1260757 | 0.2 | 0.64 | 30 | 1899-12-31T09:10:00.0000000 | 1899-12-31T09:12:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260757 | 0.2 | 0.64 | 15 | 1899-12-31T08:55:00.0000000 | 1899-12-31T08:57:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260757 | 0.2 | 0.64 | 5 | 1899-12-31T08:35:00.0000000 | 1899-12-31T08:37:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 45 | 1899-12-31T08:25:00.0000000 | 1899-12-31T08:27:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 30 | 1899-12-31T08:00:00.0000000 | 1899-12-31T08:02:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 15 | 1899-12-31T07:35:00.0000000 | 1899-12-31T07:37:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260776 | 0.2 | 0.68 | 5 | 1899-12-31T07:15:00.0000000 | 1899-12-31T07:17:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260785 | 0.2 | 0.69 | 45 | 1899-12-31T07:00:00.0000000 | 1899-12-31T07:02:52.8000000 |
| NULL | 02.08.2026 | NULL | 1 | 1260785 | 0.2 | 0.69 | 30 | 1899-12-31T06:45:00.0000000 | 1899-12-31T06:47:52.8000000 |
| NULL | 02.08.2026 | NULL | WS | 1260785 | 0.2 | 0.69 | 15 | 1899-12-31T06:30:00.0000000 | 1899-12-31T06:32:52.8000000 |

---
