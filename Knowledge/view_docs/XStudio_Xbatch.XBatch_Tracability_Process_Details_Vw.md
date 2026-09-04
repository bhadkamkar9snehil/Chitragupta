# XStudio_Xbatch.dbo.XBatch_Tracability_Process_Details_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatID | decimal | YES |
| StateSequence | int | YES |
| Status | varchar | YES |
| StartTime | nvarchar | YES |
| EndTime | nvarchar | YES |
| Duration | decimal | YES |

## Sample rows (top 5, real live data)

| HeatID | StateSequence | Status | StartTime | EndTime | Duration |
|---|---|---|---|---|---|
| 1600299.0000 | 14 | Billets Production | 13-01-2026 | 13-01-2026 | 62.5000 |
| 1601065.0000 | 8 | LRF Arcing | 14-02-2026 | 14-02-2026 | 20.4833 |
| 1602284.0000 | 11 | Ladle At CCM Arm 2 Rest Position | 08-04-2026 | 08-04-2026 | 11.2333 |
| 1600780.0000 | 5 | Ladle Car Move From EAF To LRF | 03-02-2026 | 03-02-2026 | 1.0833 |
|  |  | LRF Process Start | 05-08-2025 | 05-08-2025 | 34.8333 |