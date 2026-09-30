---
type: procedure
title: "XMES_I_Billets_Tracking_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_Billets_Tracking_Usp

Parameters: @HeatNo int, @seqNo int.

## Writes

- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Per_Heat: EndTime, HeatID, IsDeleted, TotalBilletsCount, TotalProduction, WorkOrder
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, ProductionPlant, StorageLocation, WorkOrderNumber
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber

## What its own log shows

13,904 log rows, 2026-05-25 10:09 to 2026-07-08 19:30.

Steps:
- 1 Entered
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603162 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603163 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603164 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603165 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603166 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603167 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603168 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603169 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603170 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603171 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603172 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603173 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603174 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603175 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603176 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603177 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603178 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603179 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603180 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603181 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603182 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603183 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603184 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603185 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603186 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603187 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603188 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603189 Start
- 2 Get Work Order ID, Total Billet Count, total production and endtime from CCM PER HEAT for heat no 1603190 Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_I_Billets_Tracking_Usp @HeatNo='1604014', @seqNo='1'`
