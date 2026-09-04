# XStudio_Xbatch.dbo.XStudio_List_XBatch_Billets_Transfer_History_Tbl_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| RecievedDate | datetime | YES |
| MaterialGrade | varchar | YES |
| HeatNo | varchar | YES |
| BilletNo | varchar | YES |
| ID | varchar | NO |
| BilletStatus | varchar | YES |
| FromLocation | varchar | YES |
| Stack | varchar | YES |
| InventoryID | varchar | YES |
| StackLayer | varchar | YES |
| ActionDate | datetime | YES |
| Details | varchar | NO |
| ActionBy | varchar | YES |

## Sample rows (top 5, real live data)

| RecievedDate | MaterialGrade | HeatNo | BilletNo | ID | BilletStatus | FromLocation | Stack | InventoryID | StackLayer | ActionDate | Details | ActionBy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2025-11-13 14:50:55.003000 | 3SP/PS | 1505575 | 1505575_10 | 522FB82E-2450-464D-AE1E-DEAD9AA19E82 | Outward | Furnace | Furnace | 9F12EB40-408B-4DB2-A28C-8BEE55097739 | Furnace | 2025-11-13 14:50:55.003000 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"13542905-D50D-4502-A9 |  |
| 2025-11-06 09:03:45.063000 | 3SP/PS | 1506511 | 1506511_20 | 522FD315-1D47-46A3-9FA2-FC1DD461EDF6 | Received | CCM |  | 0112E509-3B15-4490-9F1B-96017E69D798 |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"13542905-D50D-4502-A9 |  |
| 2026-01-27 22:14:15.590000 | 3SP/P | 1600603 | 1600603_21 | 522FEBC3-E5CD-43CE-AF1B-8886820533B8 | Received | CCM |  | 9B549CE0-C86E-4E7A-B5E5-61F2C035DAA2 |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"13542905-D50D-4502-A9 |  |
| 2026-03-23 12:15:14.870000 | B500BLMNHC | 1601954 | 1601954_09 | 5230098C-FEBF-40CF-986E-682850D393DE | Received | CCM |  | 65FC3DC8-5398-4F26-BA1B-0F5E90BD1FF9 |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"13542905-D50D-4502-A9 |  |
| 2026-04-05 02:06:03.723000 | HHMNB500B | 1602204 | 1602204_05 | 5230BA62-FEDB-4114-8450-513CC012375B | Received | CCM |  | 4FE7462F-C720-4489-A63A-A3388C1C3FB6 |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"13542905-D50D-4502-A9 |  |