# XStudio_Xbatch.dbo.XBatch_Delay_Analysis_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatNo | int | YES |
| DelayType | varchar | YES |
| AgencyName | varchar | YES |
| Equipment | varchar | YES |
| TotalDelayStartTime | nvarchar | YES |
| TotalDelayEndTime | nvarchar | YES |
| TotalDelayReason | varchar | YES |
| TotalDelayInMinutes | decimal | YES |
| AgencyDelayDuration | decimal | YES |
| AgencyRemark | varchar | YES |
| EquipmentDuration | decimal | YES |
| EquipmentRemark | varchar | YES |

## Sample rows (top 5, real live data)

| HeatNo | DelayType | AgencyName | Equipment | TotalDelayStartTime | TotalDelayEndTime | TotalDelayReason | TotalDelayInMinutes | AgencyDelayDuration | AgencyRemark | EquipmentDuration | EquipmentRemark |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1601048 | Tapping Delay | Process Requirement |  | 13-02-2026 18:39:16 | 13-02-2026 18:39:35 |  | 0.3200 |  |  |  |  |
| 1601048 | Tapping Delay | TRM |  | 13-02-2026 18:39:16 | 13-02-2026 18:39:35 |  | 0.3200 |  |  |  |  |
| 1601048 | Tapping Delay | Operation |  | 13-02-2026 18:39:16 | 13-02-2026 18:39:35 |  | 0.3200 |  |  |  |  |
| 1601048 | Tapping Delay | Other |  | 13-02-2026 18:39:16 | 13-02-2026 18:39:35 |  | 0.3200 |  |  |  |  |
| 1601048 | Tapping Delay | Std Delay |  | 13-02-2026 18:39:16 | 13-02-2026 18:39:35 |  | 0.3200 |  |  |  |  |