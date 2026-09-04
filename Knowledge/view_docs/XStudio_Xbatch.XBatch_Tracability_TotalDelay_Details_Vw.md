# XStudio_Xbatch.dbo.XBatch_Tracability_TotalDelay_Details_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatNo | int | YES |
| DelayType | varchar | YES |
| DelayStartTime | nvarchar | YES |
| DelayEndTime | nvarchar | YES |
| DelayReason | varchar | YES |
| DelayInMinutes | decimal | YES |

## Sample rows (top 5, real live data)

| HeatNo | DelayType | DelayStartTime | DelayEndTime | DelayReason | DelayInMinutes |
|---|---|---|---|---|---|
| 1601048 | Tapping Delay | 13-02-2026 18:39:16 | 13-02-2026 18:39:35 |  | 0.3200 |
| 1603480 | Tapping Delay | 12-06-2026 09:30:10 | 12-06-2026 09:31:36 |  | 1.4300 |
| 1600518 | Power On | 24-01-2026 12:12:18 | 24-01-2026 12:17:09 | More power on time Due to low grade metallics | 4.8500 |
| 1603090 | Power Off | 21-05-2026 16:38:04 | 21-05-2026 16:40:42 |  | 2.6300 |
| 1601757 | Power On | 14-03-2026 01:37:00 | 14-03-2026 01:40:00 | More power on time Due to low grade metallics | 3.0000 |