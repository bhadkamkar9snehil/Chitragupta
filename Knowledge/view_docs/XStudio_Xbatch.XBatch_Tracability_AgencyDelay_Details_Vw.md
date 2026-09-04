# XStudio_Xbatch.dbo.XBatch_Tracability_AgencyDelay_Details_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatNo | int | YES |
| DelayType | varchar | YES |
| AgencyName | varchar | YES |
| DelayDuration | decimal | YES |
| Remark | varchar | YES |

## Sample rows (top 5, real live data)

| HeatNo | DelayType | AgencyName | DelayDuration | Remark |
|---|---|---|---|---|
| 1506719 | Power On | Electrical | 6.28 | Test SSM |
| 1600109 | Setup Delay | Electrical | 3.83 | SVC motor tripped |
| 1505587 | Power On | Operation | 20.00 |  |
| 1505659 | Power Off | Electrical | 1.00 |  |
| 1505587 | Power On | Refractory | 22.33 |  |