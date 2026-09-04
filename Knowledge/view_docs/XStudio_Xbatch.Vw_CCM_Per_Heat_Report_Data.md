# XStudio_Xbatch.dbo.Vw_CCM_Per_Heat_Report_Data

## Columns

| Column | Type | Nullable |
|---|---|---|
| HeatID | int | YES |
| HeatReportDate | date | YES |
| Grade | varchar | YES |
| LadleSequenceText | varchar | YES |
| ActualBilletCount | int | YES |
| Status | varchar | YES |
| CastingStartTime | varchar | YES |
| Shift | varchar | YES |
| MouldWaterFlowLMinSTD1 | decimal | NO |
| MouldWaterFlowLMinSTD2 | decimal | NO |
| MouldWaterFlowLMinSTD3 | decimal | NO |
| MouldWaterFlowLMinSTD4 | decimal | NO |
| MouldWaterFlowLMinSTD5 | decimal | NO |
| MouldWaterFlowLMinSTD6 | decimal | NO |
| InletPressureSTD1 | decimal | YES |
| OutletPressureSTD1 | decimal | YES |
| OutletPressureSTD2 | decimal | YES |
| OutletPressureSTD3 | decimal | YES |
| OutletPressureSTD4 | decimal | YES |
| OutletPressureSTD5 | decimal | YES |
| OutletPressureSTD6 | decimal | YES |
| InletTempT1STD1 | decimal | YES |
| OutletTempT2STD1 | decimal | YES |
| OutletTempT2STD2 | decimal | YES |
| OutletTempT2STD3 | decimal | YES |
| OutletTempT2STD4 | decimal | YES |
| OutletTempT2STD5 | decimal | YES |
| OutletTempT2STD6 | decimal | YES |
| Strand1CastingSpeed | decimal | YES |
| Strand2CastingSpeed | decimal | YES |
| Strand3CastingSpeed | decimal | YES |
| Strand4CastingSpeed | decimal | YES |
| Strand5CastingSpeed | decimal | YES |
| Strand6CastingSpeed | decimal | YES |
| FlowZ1LtMinSTD1 | decimal | YES |
| FlowZ1LtMinSTD2 | decimal | YES |
| FlowZ1LtMinSTD3 | decimal | YES |
| FlowZ1LtMinSTD4 | decimal | YES |
| FlowZ1LtMinSTD5 | decimal | YES |
| FlowZ1LtMinSTD6 | decimal | YES |
| FlowZ2LtMinSTD1 | decimal | YES |
| FlowZ2LtMinSTD2 | decimal | YES |
| FlowZ2LtMinSTD3 | decimal | YES |
| FlowZ2LtMinSTD4 | decimal | YES |
| FlowZ2LtMinSTD5 | decimal | YES |
| FlowZ2LtMinSTD6 | decimal | YES |
| FlowZ3LtMinSTD1 | decimal | YES |
| FlowZ3LtMinSTD2 | decimal | YES |
| FlowZ3LtMinSTD3 | decimal | YES |
| FlowZ3LtMinSTD4 | decimal | YES |
| FlowZ3LtMinSTD5 | decimal | YES |
| FlowZ3LtMinSTD6 | decimal | YES |
| TotalFlowLtMinSTD1 | decimal | NO |
| TotalFlowLtMinSTD2 | decimal | NO |
| TotalFlowLtMinSTD3 | decimal | NO |
| TotalFlowLtMinSTD4 | decimal | NO |
| TotalFlowLtMinSTD5 | decimal | NO |
| TotalFlowLtMinSTD6 | decimal | NO |
| Strand1StraightnerPressure | decimal | YES |
| Strand2StraightnerPressure | decimal | YES |
| Strand3StraightnerPressure | decimal | YES |
| Strand4StraightnerPressure | decimal | YES |
| Strand5StraightnerPressure | decimal | YES |
| Strand6StraightnerPressure | decimal | YES |
| Strand1WithdrawalPressure | decimal | YES |
| Strand2WithdrawalPressure | decimal | YES |
| Strand3WithdrawalPressure | decimal | YES |
| Strand4WithdrawalPressure | decimal | YES |
| Strand5WithdrawalPressure | decimal | YES |
| Strand6WithdrawalPressure | decimal | YES |
| Delta T1 | decimal | YES |
| Delta T2 | decimal | YES |
| Delta T3 | decimal | YES |
| Delta T4 | decimal | YES |
| Delta T5 | decimal | YES |
| Delta T6 | decimal | YES |
| MouldJacketNoStrand1 | int | NO |
| MouldJacketNoStrand2 | int | NO |
| MouldJacketNoStrand3 | int | NO |
| MouldJacketNoStrand4 | int | NO |
| MouldJacketNoStrand5 | int | NO |
| MouldJacketNoStrand6 | int | NO |
| SectionSizemmStrand1 | varchar | NO |
| SectionSizemmStrand2 | varchar | NO |
| SectionSizemmStrand3 | varchar | NO |
| SectionSizemmStrand4 | varchar | NO |
| SectionSizemmStrand5 | varchar | NO |
| SectionSizemmStrand6 | varchar | NO |
| MouldTubeNoStrand1 | varchar | NO |
| MouldTubeNoStrand2 | varchar | NO |
| MouldTubeNoStrand3 | varchar | NO |
| MouldTubeNoStrand4 | varchar | NO |
| MouldTubeNoStrand5 | varchar | NO |
| MouldTubeNoStrand6 | varchar | NO |
| MouldLifeStrand1 | int | NO |
| MouldLifeStrand2 | int | NO |
| MouldLifeStrand3 | int | NO |
| MouldLifeStrand4 | int | NO |
| MouldLifeStrand5 | int | NO |
| MouldLifeStrand6 | int | NO |
| TundishTemp1 | decimal | NO |
| TundishTemp2 | decimal | NO |
| TundishTemp3 | decimal | NO |
| MouldOperatorStrand1 | varchar | NO |
| MouldOperatorStrand2 | varchar | NO |
| MouldOperatorStrand3 | varchar | NO |
| MouldOperatorStrand4 | varchar | NO |
| MouldOperatorStrand5 | varchar | NO |
| MouldOperatorStrand6 | varchar | NO |
| LadleNo | int | NO |
| LadleLife | int | NO |
| LadleLiftingTempC | decimal | NO |
| LRFLMWeightmT | decimal | NO |
| LadleGrossWeightmT | decimal | NO |
| EmptyLadleWeightmT | decimal | NO |
| LadleShrouldLife | int | NO |
| LadleNuzzalOpening | xml | YES |
| TeemingStartTime | datetime | NO |
| TeemingEndTime | datetime | NO |
| TotalTime | int | NO |
| TundishNumber | int | NO |

## Sample rows (top 5, real live data)

| HeatID | HeatReportDate | Grade | LadleSequenceText | ActualBilletCount | Status | CastingStartTime | Shift | MouldWaterFlowLMinSTD1 | MouldWaterFlowLMinSTD2 | MouldWaterFlowLMinSTD3 | MouldWaterFlowLMinSTD4 | MouldWaterFlowLMinSTD5 | MouldWaterFlowLMinSTD6 | InletPressureSTD1 | OutletPressureSTD1 | OutletPressureSTD2 | OutletPressureSTD3 | OutletPressureSTD4 | OutletPressureSTD5 | OutletPressureSTD6 | InletTempT1STD1 | OutletTempT2STD1 | OutletTempT2STD2 | OutletTempT2STD3 | OutletTempT2STD4 | OutletTempT2STD5 | OutletTempT2STD6 | Strand1CastingSpeed | Strand2CastingSpeed | Strand3CastingSpeed | Strand4CastingSpeed | Strand5CastingSpeed | Strand6CastingSpeed | FlowZ1LtMinSTD1 | FlowZ1LtMinSTD2 | FlowZ1LtMinSTD3 | FlowZ1LtMinSTD4 | FlowZ1LtMinSTD5 | FlowZ1LtMinSTD6 | FlowZ2LtMinSTD1 | FlowZ2LtMinSTD2 | FlowZ2LtMinSTD3 | FlowZ2LtMinSTD4 | FlowZ2LtMinSTD5 | FlowZ2LtMinSTD6 | FlowZ3LtMinSTD1 | FlowZ3LtMinSTD2 | FlowZ3LtMinSTD3 | FlowZ3LtMinSTD4 | FlowZ3LtMinSTD5 | FlowZ3LtMinSTD6 | TotalFlowLtMinSTD1 | TotalFlowLtMinSTD2 | TotalFlowLtMinSTD3 | TotalFlowLtMinSTD4 | TotalFlowLtMinSTD5 | TotalFlowLtMinSTD6 | Strand1StraightnerPressure | Strand2StraightnerPressure | Strand3StraightnerPressure | Strand4StraightnerPressure | Strand5StraightnerPressure | Strand6StraightnerPressure | Strand1WithdrawalPressure | Strand2WithdrawalPressure | Strand3WithdrawalPressure | Strand4WithdrawalPressure | Strand5WithdrawalPressure | Strand6WithdrawalPressure | Delta T1 | Delta T2 | Delta T3 | Delta T4 | Delta T5 | Delta T6 | MouldJacketNoStrand1 | MouldJacketNoStrand2 | MouldJacketNoStrand3 | MouldJacketNoStrand4 | MouldJacketNoStrand5 | MouldJacketNoStrand6 | SectionSizemmStrand1 | SectionSizemmStrand2 | SectionSizemmStrand3 | SectionSizemmStrand4 | SectionSizemmStrand5 | SectionSizemmStrand6 | MouldTubeNoStrand1 | MouldTubeNoStrand2 | MouldTubeNoStrand3 | MouldTubeNoStrand4 | MouldTubeNoStrand5 | MouldTubeNoStrand6 | MouldLifeStrand1 | MouldLifeStrand2 | MouldLifeStrand3 | MouldLifeStrand4 | MouldLifeStrand5 | MouldLifeStrand6 | TundishTemp1 | TundishTemp2 | TundishTemp3 | MouldOperatorStrand1 | MouldOperatorStrand2 | MouldOperatorStrand3 | MouldOperatorStrand4 | MouldOperatorStrand5 | MouldOperatorStrand6 | LadleNo | LadleLife | LadleLiftingTempC | LRFLMWeightmT | LadleGrossWeightmT | EmptyLadleWeightmT | LadleShrouldLife | LadleNuzzalOpening | TeemingStartTime | TeemingEndTime | TotalTime | TundishNumber |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1505673 | 2025-10-02 | 3SP/PS | L +  | 36 | Arm 2 | 11:10:55 | A | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 7.7100 | 3.0500 | 2.7900 | 3.8400 | 3.0200 | 3.0800 | 2.7900 | 34.8000 | 35.1500 | 41.4100 | 41.3000 | 41.4600 | 41.3100 | 35.1400 | 0.0000 | 1.8900 | 1.8600 | 1.8400 | 1.9500 | 0.0000 | 0.0000 | 160.7000 | 157.6900 | 156.2000 | 165.8300 | 0.1000 | 0.0000 | 179.6400 | 176.2500 | 174.5300 | 185.8000 | 11.7000 | 0.0200 | 65.2600 | 63.0300 | 62.6900 | 66.1500 | 0.1900 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  |  |  |  |  |  |  |  | 0.3500 | 6.6100 | 6.5000 | 6.6600 | 6.5100 | 0.3400 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |  | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 0 | 0 |
| 1505933 | 2025-10-12 | 3SP/PS | L + 25 | 36 | Arm 1 | 20:44:51 | B | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 7.7800 | 3.1300 | 2.8800 | 3.9000 | 3.1100 | 3.1500 | 2.8600 | 31.4100 | 31.7700 | 37.9100 | 38.1400 | 31.6300 | 37.6900 | 38.3600 | 0.0000 | 1.9300 | 2.0000 | 0.0000 | 1.8800 | 1.9800 | 0.0000 | 163.6900 | 161.9300 | 0.0000 | 160.2100 | 167.5700 | 0.0000 | 182.9800 | 190.3200 | 5.9800 | 178.9600 | 187.8700 | 0.0300 | 66.4200 | 66.2400 | 0.0000 | 63.5000 | 68.4000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 39.6500 | 19.6300 | 19.5300 | 40.3100 | 19.8200 | 19.3900 | 40.0100 | 18.9600 | 18.9600 | 40.0000 | 18.9600 | 19.0200 | 0.3600 | 6.5000 | 6.7300 | 0.2200 | 6.2800 | 6.9500 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |  | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 0 | 0 |
| 1504890 | 1900-01-01 |  | L +  |  | Arm 2 | 07:58:13 | A | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  |  |  |  |  |  |  |  | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |  | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 0 | 0 |
| 1601493 | 2026-03-03 | B500BLMNHC | L + 23 | 37 | Arm 2 | 12:50:02 | A | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 7.9400 | 2.4600 | 2.0800 | 3.1300 | 2.3600 | 2.3600 | 2.1200 | 34.7600 | 37.7400 | 41.2500 | 40.5700 | 35.0300 | 41.6100 | 41.5200 | 1.1300 | 1.7100 | 1.5700 | 0.0000 | 1.7000 | 1.5600 | 71.8700 | 145.4100 | 134.2800 | 0.0000 | 144.7800 | 132.6900 | 74.5100 | 162.5600 | 149.2600 | 0.0000 | 161.8800 | 148.4100 | 27.9600 | 59.0400 | 53.1400 | 0.0000 | 58.3300 | 53.7800 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 27.2700 | 19.2600 | 19.1700 | 39.4000 | 19.6100 | 19.3400 | 27.1600 | 19.0500 | 18.9900 | 40.0100 | 19.0700 | 19.0800 | 2.9800 | 6.4900 | 5.8100 | 0.2700 | 6.8500 | 6.7600 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |  | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 0 | 0 |
| 1602374 | 2026-04-12 | B500BLMNHC | L + 26 | 37 | Arm 1 | 21:18:12 | B | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 7.9700 | 2.4300 | 2.0900 | 3.3200 | 2.3500 | 2.3800 | 2.1300 | 30.8800 | 37.0100 | 36.6100 | 36.4500 | 37.5100 | 31.0300 | 31.2100 | 1.7300 | 1.5500 | 1.7400 | 1.6900 | 0.0000 | 0.0000 | 147.3400 | 131.4900 | 148.3800 | 143.9000 | 0.2900 | 0.0900 | 164.6800 | 146.8000 | 165.7100 | 160.8100 | 1.1700 | 10.7500 | 59.7600 | 53.1200 | 59.0800 | 58.3300 | 11.1600 | 0.1900 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 19.9100 | 19.3900 | 19.0900 | 18.9900 | 40.2900 | 39.9200 | 17.9500 | 17.9900 | 19.0000 | 17.9900 | 40.0000 | 40.0000 | 6.1300 | 5.7300 | 5.5700 | 6.6300 | 0.1500 | 0.3300 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |  | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 0 | 0 |