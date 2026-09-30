---
type: procedure
title: "XMES_RM_Production_Summary_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Production_Summary_Usp

Parameters: @ReportDate date.

## Writes

- XMES_RM_Production_Summary: ActualWeightTon, ActualYieldPCT, AvgBilletWt, BilletConsumed, CobbleBilletWt, CobblePcs, CreatedOn, DayProduction, EndCutPCT, EndCutTon, Grade, HotChargingPCT, HotChargingTon, HotOutBilletWt, HotOutPcs, MillScale12PCT, NGMMBTU, NGMMBTUTon, NGNm3, PortableWaterm3, PortableWaterm3Ton, PowerKWH, PowerKWHTon, PrimeProduction, ProcessWaterm3, ProcessWaterm3Ton, Product, Rejections, ReportDate, RolledBilletPcs, RolledBilletWTMT, SPWirerodConsKGPerCoil, Section, ShortLengthGeneration, Source, TotalDischargeTon, WireRodCons, yield

## Reads

- Electricity_Meter_Reading: EndDateTime, FeederName, Position, ReportDate, Value
- MES_Logbook_Water_Reading: EntirePlantReadingDifference, RMReadingDifference, ReportDate
- MES_SAP_By_Product_Trn_Tbl: ManufacturingOrder, Material, PostingDate, QuantityInEntryUnit
- MES_SAP_Consumption_Trn_Tbl: BilletNo, FurnaceBilletStatus, ManufacturingOrder, PostingMaterialType, QuantityInEntryUnit, SAPQuantity
- NM3_To_MMBTU_Factor: CreatedOn, RebarCoilTieRodFactor, RebarTieRodFactor, WRMTieRodFactor
- Product_Master: ID, ShortName
- RM_NGConsumption: FromTime, NGCong, NGCons, ReportDate, ToTime
- XBatch_Material_Mst_Tbl: Grade, ID
- XBatch_Work_Order_Mst_Tbl: CampaignId, ID, ItemID, ManufacturingOrderType, Name, WorkOrderNumber
- XMES_Campaign_Plan_Mst: CampaignEndDate, CampaignId, ID, Productname
- XMES_RM_Production_Data: BilletNo, BundleWeightTon, EndProductid, IsDeleted, IsShort, ReportDate, SectionLength, Workorderid
- XMES_Work_Order_Trn_Tbl: CampaignID, EntryDateTime, IsDeleted, ReportDate, WorkOrder
