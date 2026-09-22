# XStudio_Xbatch.dbo.Temp_Rebar_Coil_Quality_Data_09_12_55_02_09_2026

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference agt, camp, charging, error, grade, isvalid, line, message, rebend, remarks, rra, sample.

**Primary Key:** —  
**Row Count:** 9,662  
**Date Range (Sample Recieving Time):** 1899-12-31T00:00:00.0000000 to 2026-09-02T01:50:00.0000000  

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
| 15.01.2026 | 1 | 1600328 | 0.2 | 0.71 | 1 | 1899-12-31T11:30:00.0000000 | 1899-12-31T11:44:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 30 | 1899-12-31T23:15:00.0000000 | 1899-12-31T23:29:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 30 | 1899-12-31T23:15:00.0000000 | 1899-12-31T23:29:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 15 | 1899-12-31T22:10:00.0000000 | 1899-12-31T22:24:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 15 | 1899-12-31T22:10:00.0000000 | 1899-12-31T22:24:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 3 | 1899-12-31T09:45:00.0000000 | 1899-12-31T09:59:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 3 | 1899-12-31T09:45:00.0000000 | 1899-12-31T09:59:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 2 | 1899-12-31T09:30:00.0000000 | 1899-12-31T09:44:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 2 | 1899-12-31T09:30:00.0000000 | 1899-12-31T09:44:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 1 | 1899-12-31T09:10:00.0000000 | 1899-12-31T09:24:24.0000000 | Back | 10 |

### Bottom 10 Records

| Entry Date | Camp | Heat No | C | Mn | Sample | Sample Recieving Time | Testing Time | Line | Nom d mm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.01.2026 | 1 | 1600328 | 0.2 | 0.71 | 1 | 1899-12-31T11:30:00.0000000 | 1899-12-31T11:44:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 30 | 1899-12-31T23:15:00.0000000 | 1899-12-31T23:29:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 30 | 1899-12-31T23:15:00.0000000 | 1899-12-31T23:29:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 15 | 1899-12-31T22:10:00.0000000 | 1899-12-31T22:24:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600327 | 0.21 | 0.71 | 15 | 1899-12-31T22:10:00.0000000 | 1899-12-31T22:24:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 3 | 1899-12-31T09:45:00.0000000 | 1899-12-31T09:59:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 3 | 1899-12-31T09:45:00.0000000 | 1899-12-31T09:59:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 2 | 1899-12-31T09:30:00.0000000 | 1899-12-31T09:44:24.0000000 | Back | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 2 | 1899-12-31T09:30:00.0000000 | 1899-12-31T09:44:24.0000000 | Front | 10 |
| 15.01.2026 | 1 | 1600326 | 0.2 | 0.72 | 1 | 1899-12-31T09:10:00.0000000 | 1899-12-31T09:24:24.0000000 | Back | 10 |

---
