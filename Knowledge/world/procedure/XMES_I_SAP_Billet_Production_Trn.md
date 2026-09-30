---
type: procedure
title: "XMES_I_SAP_Billet_Production_Trn"
built: "2026-09-24T11:36:36"
---

# XMES_I_SAP_Billet_Production_Trn

Parameters: @UserId varchar, @SystemId varchar, @RecordIds varchar, @Status varchar, @DataCollection nvarchar.

## Writes

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, BilletType1, BilletType2, BilletType3, BilletType4, CalcBilletsWeight1, CalcBilletsWeight2, CalcBilletsWeight3, CalcBilletsWeight4, Customer, CutLenght1, CutLenght2, CutLenght3, CutLenght4, EndCutMeter, Grade, LaunderLossTon, Material, ModifiedOn, NoofBillets1, NoofBillets2, NoofBillets3, NoofBillets4, OtherLossesTon, PostToSAP1, PostToSAP2, PostToSAP3, PostToSAP4, ProductionPlant, RemainingPostedBilletCount, RemainingPostedBilletWeightTon, SAPPostingDate, SAPWorkflowStatus, SalesOrder, Source, TotalPostedBilletCount, TotalPostedBilletWeightTon, TundishlossTon, WorkOrder
- LRF_Per_Heat: Grade, WorkOrder
- MES_SAP_Production_Trn_Tbl: Batch, BilletNo, Cutlength, EntryUnit, GoodsMovementType, Grade, HeatNo, IsAutoPost, ManufacturingOrder, Material, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation
- XBatch_Material_Item_Prod_Trn_Tbl: CreatedOn, GradeID, HeatNo, ID, LotNumber, MaterialID, Quantity, Source, SublotNumber, UOMID
- XBatch_Work_Order_Mst_Tbl: CreatedBy, CreatedOn, Equipment, ID, ItemID, ManufacturingOrderType, MaterialName, MfgOrderPlannedEndDate, MfgOrderPlannedStartDate, ProductionPlant, Quantity, ReleasedDate, SalesOrder, SalesOrderItem, Source, StartTime, Status, UnitID
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, IsDeleted, ManufacturingOrder, Materialid, ModifiedOn, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_SAP_Batch_Characteristic_Trn_Tbl: ActualGrade, BatchNo, ClassNumber, ClassType, ColourCode, CreatedBy, ExternalGrade, HeatNo, HeatSequenceNumber, InspectionAgency, Length, Material, NoOfPieces, Pieces, Plant, ProcessRoute, Product, ProductionSectionalWeight, SAPPostingStatus, SectionalWeight, Source, TDCRefNo, Thickness, TonsPerPiece, Width
- XMES_SAP_CreateBatch_Mst_Tbl: Batch, CreatedBy, HeatNo, Material, ModifiedBy, ModifiedOn, SAPPostingStatus, Source
- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: Batch, CreatedOn, Customer, EntryUnit, GoodsMovementType, HeatNo, IssgOrRcvgBatch, IssgOrRcvgMaterial, IssuingOrReceivingPlant, IssuingOrReceivingStorageLoc, ManufacturingOrder, Material, Plant, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, SalesOrder, SalesOrderItem, Source, StorageLocation, Supplier
- Xbatch_Material_Inventory_Trn_Tbl: CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- CCM_Per_Heat: CrossSection, EndTime, HeatID, HeatReportDate, ID, IsDeleted, LadleSequence, SetWeightTon
- LRF_Per_Heat: HeatID, IsDeleted
- MES_SAP_Production_Trn_Tbl: Batch, BilletNo, Cutlength, Grade, HeatNo, IsDeleted, ManufacturingOrder, Material, Plant, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, StorageLocation
- XBatch_Customer_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name, SAPColorCode
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, ProductionPlant, SalesOrder, SalesOrderItem, StorageLocation, WorkOrderNumber
- XMES_Billet_Tracking_Per_Strand: BilletNo, HeatNo
- XMES_Billet_Tracking_Trn_Tbl: BilletNo, HeatNo, ID, PostingMaterialType
- XMES_Billet_VS_GLS_Grade_Mapping: BilletGrade, GLSGrade, IsDeleted
- XMES_SAP_CreateBatch_Mst_Tbl: ID
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber

## Writes (named in its SQL text)

- XBatch_Material_Inventory_Mst_Tbl
- XMES_Log_Trn_Tbl

## Calls

- XMES_AUTO_WO_AND_SO_CALCULATION
- XMES_BackCalculation_GLS_Usp
- XMES_I_ByProduct_Trn_Usp
- XMES_I_SAP_GLS_LS_Consumption_Trn_Usp
- XMES_I_SAP_GLS_LS_Production_Trn_Usp

## What its own log shows

360 log rows, 2026-06-23 13:45 to 2026-06-27 08:54.

Steps:
- 1. update billetno for current heat in billetno of previous heat when billet count is more that total billet count of previous heat
- 2. update billetno for previous heat in billetno of current heat when billet count is less that total billet count of previous heat and update current heat billet count after complete previous heat billet count is same as total billet of previous heat
- 3. update other details for heat no 1603642 and 1603641
- 3. update other details for heat no 1603661 and 1603660
- 3. update other details for heat no 1603680 and 1603679
- 3. update other details for heat no 1603701 and 1603700
- 3. update other details for heat no 1603702 and 1603701
- 3. update other details for heat no 1603703 and 1603702
- 3. update other details for heat no 1603704 and 1603703
- 3. update other details for heat no 1603705 and 1603704
- 3. update other details for heat no 1603706 and 1603705
- 3. update other details for heat no 1603707 and 1603706
- 3. update other details for heat no 1603708 and 1603707
- 3. update other details for heat no 1603709 and 1603708
- 3. update other details for heat no 1603710 and 1603709
- 3. update other details for heat no 1603711 and 1603710
- 3. update other details for heat no 1603712 and 1603711
- 3. update other details for heat no 1603713 and 1603712
- 3. update other details for heat no 1603714 and 1603713
- 3. update other details for heat no 1603715 and 1603714
- 3. update other details for heat no 1603716 and 1603715
- 3. update other details for heat no 1603717 and 1603716
- 3. update other details for heat no 1603718 and 1603717
- 3. update other details for heat no 1603719 and 1603718
- 3. update other details for heat no 1603720 and 1603719
- 3. update other details for heat no 1603721 and 1603720
- 3. update other details for heat no 1603722 and 1603721
- 3. update other details for heat no 1603723 and 1603722
- 3. update other details for heat no 1603724 and 1603723
- 3. update other details for heat no 1603725 and 1603724

Example call: `EXEC XStudio_Xbatch.dbo.XMES_I_SAP_Billet_Production_Trn @UserID = 'CF587DA9-0FDF-494E-8044-7620D00418AE', @SystemID = 'A0E0934F-B370-4374-819B-A60CF61E71AF', @RecordID = 'FC8C7442-2994-41A1-AD34-0C8C9D964EB0', @Status = 'Posted', @DataCollection = '[{"Key":"HeatID","Value":"1603731"},{"Key":"SalesO`
