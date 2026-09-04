# XStudio_Xbatch.dbo.XBatch_Tracability_Heat_Details_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatNo | int | YES |
| TotalChargeWeight | decimal | NO |
| SequenceNo | int | NO |
| LiquidMetalYield | float | YES |
| SteelGrade | varchar | YES |
| LiquidMetalWeight | decimal | NO |
| ArmNo | varchar | YES |
| CasterYield | float | YES |
| CrossSection | int | NO |
| BilletProduction | decimal | NO |
| LadleSequence | int | YES |
| LadleNo | varchar | YES |
| ChargeToBilletYield | float | YES |
| PowerOnTime | varchar | NO |
| PowerOffTime | varchar | NO |
| TapToTapTime | varchar | NO |
| TapTimeMinute | decimal | NO |
| LRFArcingTime | decimal | NO |
| LRFTreatmentTime | decimal | NO |
| CastingDuration | int | YES |
| HeatStartDateTime | nvarchar | YES |
| Tapping Start DateTime | nvarchar | YES |
| LRFTreatmentStartDatetime | nvarchar | YES |
| CastingStartDatetime | nvarchar | YES |
| HMS1 | decimal | NO |
| HMS1+2 | decimal | NO |
| MSBundle | decimal | NO |
| Shredded | decimal | NO |
| RMSEndCut | decimal | NO |
| Copex Scrap | decimal | NO |
| Skull | decimal | NO |
| BRQ | decimal | NO |
| Cold-DRI | decimal | YES |
| HBI | decimal | NO |
| EAFLIME | decimal | NO |
| LRFLIME | decimal | NO |
| EAFDolo | decimal | NO |
| LRFDolo | decimal | NO |
| EAFSiMnn | decimal | NO |
| LRFSiMnn | decimal | NO |
| EAFFeSi | decimal | NO |
| LRFFeSi | decimal | NO |
| EAFSiMn | decimal | NO |
| SiMn | decimal | NO |
| Oxygen | decimal | NO |
| NG | decimal | NO |
| Carbon | decimal | NO |
| Argon | decimal | NO |
| EAF_Power | decimal | NO |
| LRF_Power | decimal | NO |
| TotalBiilletProduced | decimal | NO |
| BilletProducedWeight | decimal | NO |

## Sample rows (top 5, real live data)

| HeatNo | TotalChargeWeight | SequenceNo | LiquidMetalYield | SteelGrade | LiquidMetalWeight | ArmNo | CasterYield | CrossSection | BilletProduction | LadleSequence | LadleNo | ChargeToBilletYield | PowerOnTime | PowerOffTime | TapToTapTime | TapTimeMinute | LRFArcingTime | LRFTreatmentTime | CastingDuration | HeatStartDateTime | Tapping Start DateTime | LRFTreatmentStartDatetime | CastingStartDatetime | HMS1 | HMS1+2 | MSBundle | Shredded | RMSEndCut | Copex Scrap | Skull | BRQ | Cold-DRI | HBI | EAFLIME | LRFLIME | EAFDolo | LRFDolo | EAFSiMnn | LRFSiMnn | EAFFeSi | LRFFeSi | EAFSiMn | SiMn | Oxygen | NG | Carbon | Argon | EAF_Power | LRF_Power | TotalBiilletProduced | BilletProducedWeight |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1505673 | 92.2000 | 0 | 76.33492407809109 | 3SP/PS | 70.3808 | Arm 2  | 107.41565881604073 | 150 | 75.6000 |  |  | 81.99566160520607 | 49:53 | 8:15 | 58:08 | 2.2833 | 17.0000 | 28.0000 | 66 | 02-10-2025 09:34:13 | 02-10-2025 10:30:06 | 02-10-2025 10:34:55 | 02-10-2025 11:10:55 | 0.0000 | 7.9000 | 0.0000 | 0.0000 | 8.7000 | 10.6000 | 4.4000 | 2.3000 | 56.9000 | 1.3000 | 0.0000 | 180.0000 | 0.0000 | 0.0000 | 600.0000 | 0.0000 | 110.0000 | 25.0000 | 600.0000 | 105.0000 | 2387.0000 | 195.0000 | 1431.0000 | 6.1100 | 47.8000 | 2.2400 | 36.0000 | 75.6000 |
| 1505933 | 93.1500 | 25 | 72.22952227589909 | 3SP/PS | 67.2818 | Arm 1  | 112.3632245272867 | 150 | 75.6000 | 25 |  | 81.15942028985506 | 48:29 | 6:50 | 55:19 | 2.7833 | 17.0000 | 21.0000 | 58 | 12-10-2025 19:14:24 | 12-10-2025 20:07:03 | 12-10-2025 20:12:08 | 12-10-2025 20:44:51 | 0.0000 | 10.2000 | 0.0000 | 0.0000 | 4.2000 | 13.6000 | 5.6000 | 1.7000 | 57.8500 | 0.0000 | 0.0000 | 188.0000 | 0.0000 | 0.0000 | 600.0000 | 0.0000 | 110.0000 | 0.0000 | 600.0000 | 80.0000 | 2127.0000 | 245.0000 | 1306.0000 | 4.8000 | 47.2200 | 2.7100 | 36.0000 | 75.6000 |
| 1504890 | 93.5000 | 0 | 82.1233155080214 | 3SP/PS | 76.7853 | Arm 2  | 0.0 | 150 | 0.0000 |  |  | 0.0 | 51:8 | 7:14 | 58:22 | 7.8000 | 22.0000 | 38.0000 | 54 | 01-01-1900 06:05:13 | 30-08-2025 06:59:27 | 01-01-1900 07:06:00 | 30-08-2025 07:58:13 | 0.0000 | 5.2000 | 2.5000 | 0.0000 | 5.8000 | 6.2000 | 5.6000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2154.0000 | 122.0000 | 0.0000 | 6498.7998 | 50.7500 | 3.1000 | 0.0000 | 0.0000 |
| 1601493 | 92.1300 | 23 | 75.2716813198741 | B500B | 69.3478 | Arm 2  | 112.04392929552198 | 150 | 77.7000 | 23 |  | 84.33734939759037 | 49:48 | 6:19 | 56:07 | 3.6000 | 19.0000 | 23.0000 | 55 | 03-03-2026 11:18:21 | 03-03-2026 12:10:52 | 03-03-2026 12:17:35 | 03-03-2026 12:50:02 | 0.0000 | 9.0000 | 0.0000 | 0.0000 | 5.2000 | 6.5000 | 7.8000 | 0.0000 | 63.6300 | 0.0000 | 0.0000 | 1080.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 120.0000 | 40.0000 | 600.0000 | 410.0000 | 2298.0000 | 161.0000 | 1069.0000 | 8.6700 | 49.6800 | 2.8500 | 37.0000 | 77.7000 |
| 1602374 | 103.7300 | 26 | 67.45165333076257 | 1008 | 69.9676 | Arm 1  | 112.32055980196547 | 150 | 78.5880 | 26 |  | 75.7620746167936 | 60:14 | 9:20 | 69:34 | 3.5500 | 20.0000 | 27.0000 | 63 | 12-04-2026 19:32:15 | 12-04-2026 20:38:20 | 12-04-2026 20:44:21 | 12-04-2026 21:18:12 | 0.0000 | 30.7000 | 0.0000 | 0.0000 | 3.2000 | 6.0000 | 6.8000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 800.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 100.0000 | 100.0000 | 600.0000 | 231.0000 | 2352.0000 | 166.0000 | 1491.0000 | 9.0200 | 59.3000 | 2.6500 | 37.0000 | 78.5880 |