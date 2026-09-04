# XStudio_Xbatch.dbo.XBatch_Tracability_EquipmentDelay_Details_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatNo | int | YES |
| DelayType | varchar | YES |
| AgencyName | varchar | YES |
| Equipment | varchar | YES |
| DelayDuration | decimal | YES |
| Remark | varchar | YES |

## Sample rows (top 5, real live data)

| HeatNo | DelayType | AgencyName | Equipment | DelayDuration | Remark |
|---|---|---|---|---|---|
| 1505633 | Power On | Electrical |  | 4.3000 |  |
| 1505587 | Power On | Electrical |  | 10.0000 |  |
| 1600582 | Power Off | Mechanical |  |  | CCM SIDE VTS MOTOR BASE BOLT SLIPPED |
| 1505633 | Power On | Mechanical |  | 0.0800 |  |
| 1505633 | Power On | Mechanical |  | 0.2500 |  |