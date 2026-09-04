# XStudio_Xbatch.dbo.Vw_XBatch_Tracability_SMS_Process_Time

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatID | decimal | YES |
| StateSequence | int | YES |
| Status | varchar | YES |
| StartTime | datetime | YES |
| EndTime | datetime | YES |
| Duration | decimal | YES |

## Sample rows (top 5, real live data)

| HeatID | StateSequence | Status | StartTime | EndTime | Duration |
|---|---|---|---|---|---|
| 1600299.0000 | 14 | Billets Production | 2026-01-13 22:16:06.563000 | 2026-01-13 23:18:36.507000 | 62.5000 |
| 1601065.0000 | 8 | LRF Arcing | 2026-02-14 09:24:08.097000 | 2026-02-14 09:44:37.833000 | 20.4833 |
| 1602284.0000 | 11 | Ladle At CCM Arm 2 Rest Position | 2026-04-08 17:57:35.513000 | 2026-04-08 18:08:49.703000 | 11.2333 |
| 1600780.0000 | 5 | Ladle Car Move From EAF To LRF | 2026-02-03 20:09:17.567000 | 2026-02-03 20:10:22.910000 | 1.0833 |
|  |  | LRF Process Start | 2025-08-05 04:22:16.157000 | 2025-08-05 04:57:06.710000 | 34.8333 |