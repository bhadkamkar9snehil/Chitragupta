# XStudio_Xbatch.dbo.Temp_Rebar_Coil_Quality_Data_14_46_45_01_09_2026

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference agt, camp, charging, error, grade, isvalid, line, message, rebend, remarks, rra, sample.

**Primary Key:** —  
**Row Count:** 9,662  
**Date Range (Sample Recieving Time):** 1899-12-31T00:00:00.0000000 to 2026-09-01T01:50:00.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| Entry Date | nvarchar | YES | -1 | — |
| Camp | bigint | YES | 19,0 | — |
| Heat No | bigint | YES | 19,0 | — |
| C | float | YES | 53 | — |
| Mn | float | YES | 53 | — |
| Sample | bigint | YES | 19,0 | — |
| Sample Recieving Time | datetime | YES | — | — |
| Testing Time | datetime | YES | — | — |
| Line | nvarchar | YES | -1 | — |
| Nom d mm | bigint | YES | 19,0 | — |
| ACSA mm2 | float | YES | 53 | — |
| Nominal CSA mm2 | float | YES | 53 | — |
| Wt per Mtr | float | YES | 53 | — |
| Tol | float | YES | 53 | — |
| Rib less mm | nvarchar | YES | -1 | — |
| Rib Spacing C mm | nvarchar | YES | -1 | — |
| Tran Rib ht mm | nvarchar | YES | -1 | — |
| Long Rib ht mm | nvarchar | YES | -1 | — |
| RRA | float | YES | 53 | — |
| Rib Inclination | nvarchar | YES | -1 | — |
| Rib Flank Inclination | nvarchar | YES | -1 | — |
| Roots of Transverse Rib | nvarchar | YES | -1 | — |
| YS MPa | bigint | YES | 19,0 | — |
| UTS MPa | bigint | YES | 19,0 | — |
| UTS_YS Ratio | float | YES | 53 | — |
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
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 40 | 1899-12-31T02:30:00.0000000 | 1899-12-31T02:44:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 25 | 1899-12-31T02:10:00.0000000 | 1899-12-31T02:24:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 25 | 1899-12-31T02:10:00.0000000 | 1899-12-31T02:24:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 5 | 1899-12-31T01:50:00.0000000 | 1899-12-31T02:04:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 5 | 1899-12-31T01:50:00.0000000 | 1899-12-31T02:04:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 40 | 1899-12-31T01:30:00.0000000 | 1899-12-31T01:44:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 40 | 1899-12-31T01:30:00.0000000 | 1899-12-31T01:44:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 25 | 1899-12-31T01:00:00.0000000 | 1899-12-31T01:14:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 25 | 1899-12-31T01:00:00.0000000 | 1899-12-31T01:14:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 5 | 1899-12-31T00:45:00.0000000 | 1899-12-31T00:59:24.0000000 | Back | 12 |

### Bottom 10 Records

| Entry Date | Camp | Heat No | C | Mn | Sample | Sample Recieving Time | Testing Time | Line | Nom d mm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 40 | 1899-12-31T02:30:00.0000000 | 1899-12-31T02:44:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 25 | 1899-12-31T02:10:00.0000000 | 1899-12-31T02:24:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 25 | 1899-12-31T02:10:00.0000000 | 1899-12-31T02:24:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 5 | 1899-12-31T01:50:00.0000000 | 1899-12-31T02:04:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503427 | 0.23 | 0.72 | 5 | 1899-12-31T01:50:00.0000000 | 1899-12-31T02:04:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 40 | 1899-12-31T01:30:00.0000000 | 1899-12-31T01:44:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 40 | 1899-12-31T01:30:00.0000000 | 1899-12-31T01:44:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 25 | 1899-12-31T01:00:00.0000000 | 1899-12-31T01:14:24.0000000 | Back | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 25 | 1899-12-31T01:00:00.0000000 | 1899-12-31T01:14:24.0000000 | Front | 12 |
| 10.06.2025 | 1 | 1503428 | 0.24 | 0.72 | 5 | 1899-12-31T00:45:00.0000000 | 1899-12-31T00:59:24.0000000 | Back | 12 |

---
