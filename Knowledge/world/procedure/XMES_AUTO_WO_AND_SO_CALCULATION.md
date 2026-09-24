---
type: procedure
title: "XMES_AUTO_WO_AND_SO_CALCULATION"
built: "2026-09-24T11:36:36"
---

# XMES_AUTO_WO_AND_SO_CALCULATION

Parameters: @Plant varchar, @WorkOrder varchar.

## Writes

- XBatch_Sales_Order_Mst_Tbl: ProgressTonnage
- XBatch_Work_Order_Mst_Tbl: ActualCompletionDate, Description, ModifiedBy, ModifiedOn, ProgressTonnage, Source, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Per_Heat: ActualBilletWeightTon, TotalProduction, WorkOrder
- EAF_PER_HEAT: CalcLiquidMetalWeight, LiquidMetalWeight, WorkOrder
- LRF_Per_Heat: CalcLiquidMetalWeight, LiquidMetalWeight, WorkOrder
- XBatch_Sales_Order_Mst_Tbl: ID
- XBatch_Work_Order_Mst_Tbl: Equipment, ID, IsDeleted, MfgOrderScheduledStartDate, RemainingTonnage, SalesOrder

## What its own log shows

31,190 log rows, 2026-05-21 09:23 to 2026-07-08 23:43.

Steps:
- 1 Entered
- 2 Set WO number for EAF, LRF and CCM Start
- 3 Set WO number for EAF (MES_2026062413_LS), LRF (MES_2026062413_GLS) and CCM (MES_2026062413_BL) End
- 3 Set WO number for EAF (MES_2026062414_LS), LRF (MES_2026062414_GLS) and CCM (MES_2026062414_BL) End
- 3 Set WO number for EAF (MES_2026062415_LS), LRF (MES_2026062415_GLS) and CCM (MES_2026062415_BL) End
- 3 Set WO number for EAF (MES_2026062416_LS), LRF (MES_2026062416_GLS) and CCM (MES_2026062416_BL) End
- 3 Set WO number for EAF (MES_2026062417_LS), LRF (MES_2026062417_GLS) and CCM (MES_2026062417_BL) End
- 3 Set WO number for EAF (MES_2026062418_LS), LRF (MES_2026062418_GLS) and CCM (MES_2026062418_BL) End
- 3 Set WO number for EAF (MES_2026062419_LS), LRF (MES_2026062419_GLS) and CCM (MES_2026062419_BL) End
- 3 Set WO number for EAF (MES_2026062420_LS), LRF (MES_2026062420_GLS) and CCM (MES_2026062420_BL) End
- 3 Set WO number for EAF (MES_2026062421_LS), LRF (MES_2026062421_GLS) and CCM (MES_2026062421_BL) End
- 3 Set WO number for EAF (MES_2026062422_LS), LRF (MES_2026062422_GLS) and CCM (MES_2026062422_BL) End
- 3 Set WO number for EAF (MES_2026062423_LS), LRF (MES_2026062423_GLS) and CCM (MES_2026062423_BL) End
- 3 Set WO number for EAF (MES_2026062500_LS), LRF (MES_2026062500_GLS) and CCM (MES_2026062500_BL) End
- 3 Set WO number for EAF (MES_2026062503_LS), LRF (MES_2026062503_GLS) and CCM (MES_2026062503_BL) End
- 3 Set WO number for EAF (MES_2026062505_LS), LRF (MES_2026062505_GLS) and CCM (MES_2026062505_BL) End
- 3 Set WO number for EAF (MES_2026062506_LS), LRF (MES_2026062506_GLS) and CCM (MES_2026062506_BL) End
- 3 Set WO number for EAF (MES_2026062507_LS), LRF (MES_2026062507_GLS) and CCM (MES_2026062507_BL) End
- 3 Set WO number for EAF (MES_2026062508_LS), LRF (MES_2026062508_GLS) and CCM (MES_2026062508_BL) End
- 3 Set WO number for EAF (MES_2026062509_LS), LRF (MES_2026062509_GLS) and CCM (MES_2026062509_BL) End
- 3 Set WO number for EAF (MES_2026062510_LS), LRF (MES_2026062510_GLS) and CCM (MES_2026062510_BL) End
- 3 Set WO number for EAF (MES_2026062511_LS), LRF (MES_2026062511_GLS) and CCM (MES_2026062511_BL) End
- 3 Set WO number for EAF (MES_2026062512_LS), LRF (MES_2026062512_GLS) and CCM (MES_2026062512_BL) End
- 3 Set WO number for EAF (MES_2026062513_LS), LRF (MES_2026062513_GLS) and CCM (MES_2026062513_BL) End
- 3 Set WO number for EAF (MES_2026062514_LS), LRF (MES_2026062514_GLS) and CCM (MES_2026062514_BL) End
- 3 Set WO number for EAF (MES_2026062515_LS), LRF (MES_2026062515_GLS) and CCM (MES_2026062515_BL) End
- 3 Set WO number for EAF (MES_2026062516_LS), LRF (MES_2026062516_GLS) and CCM (MES_2026062516_BL) End
- 3 Set WO number for EAF (MES_2026062517_LS), LRF (MES_2026062517_GLS) and CCM (MES_2026062517_BL) End
- 3 Set WO number for EAF (MES_2026062518_LS), LRF (MES_2026062518_GLS) and CCM (MES_2026062518_BL) End
- 3 Set WO number for EAF (MES_2026062519_LS), LRF (MES_2026062519_GLS) and CCM (MES_2026062519_BL) End

Example call: `EXEC XStudio_Xbatch.dbo.XMES_AUTO_WO_AND_SO_CALCULATION @Plant='LRF', @WorkOrder='FF56F036-19A6-4808-8F29-E500C8D878AE'`
