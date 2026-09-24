---
type: procedure
title: "XMES_SAP_Posting_Sequence_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_Posting_Sequence_Usp

Parameters: @ID varchar, @APIPostingType varchar.

## Writes

- CCM_Per_Heat: RemainingPostedBilletCount, RemainingPostedBilletWeightTon, TotalPostedBilletCount, TotalPostedBilletWeightTon
- Heat_Chemistry_Quality_Data: InspectionLot, IsUDStatus, ModifiedOn, SAPStatus, Source
- MES_Raw_Material_Consumptions_Trn_Tbl: SAPWorkflowStatus
- MES_SAP_By_Product_Trn_Tbl: ModifiedBy, ModifiedOn, SAPPostingStatus, Source
- MES_SAP_Consumption_Trn_Tbl: ModifiedBy, ModifiedOn, SAPPostingStatus, Source
- MES_SAP_Production_Trn_Tbl: Batch, BilletNo, CreatedBy, CreatedByUser, CreationDate, CreationTime, CtrlPostForWhseMgmtSyst, Cutlength, DocumentDate, EntryUnit, GoodsMovementCode, GoodsMovementType, Grade, HeatNo, InventoryTransactionType, IsReversal, ManualPrintLsTriggered, ManufacturingOrder, Material, MaterialDocument, MaterialDocumentHeaderText, MaterialDocumentYear, ModifiedBy, ModifiedOn, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, ReferenceDocument, SAPPostingStatus, Source, StorageLocation, VersionForPrintingSlip
- MES_SAP_UsageDecision_Trn_Tbl: HeatNo, InspectionLot, MaterialType, ModifiedBy, ModifiedOn, SAPPostingStatus, Source, UsgDecCode
- MES_SAP_WorkOrder_Movements_Trn_Tbl: Batch, CreatedOn, DebitCreditindication, ID, MaterialDocument, MovementType, NoOfItem, ParentID, PostingDate, Quantity, QuantityinCount, Source, StorageLocation
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- XMES_SAP_Batch_Characteristic_Trn_Tbl: Length, ModifiedBy, ModifiedOn, NoOfPieces, Pieces, SAPPostingStatus, Source, TonsPerPiece
- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: ModifiedBy, ModifiedOn, SAPPostingStatus, Source
- Xbatch_Material_Inventory_Trn_Tbl: CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, HeatID, IsDeleted
- Heat_Chemistry_Quality_Data: HeatNo, ID, InspectionLot, IsDeleted, IsLatestSample, Message, ModifiedBy
- MES_Raw_Material_Consumptions_Trn_Tbl: ID
- MES_SAP_By_Product_Trn_Tbl: Batch, GoodsMovementType, HeatNo, ID, InspectionLot, ManufacturingOrder, MaterialDocument, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, Saptransactionid, StorageLocation
- MES_SAP_Consumption_Trn_Tbl: Batch, GoodsMovementType, HeatNo, ID, InspectionLot, ManufacturingOrder, MaterialDocument, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, RawMaterialRecordID, StorageLocation
- MES_SAP_Production_Trn_Tbl: Batch, BilletNo, Cutlength, EntryUnit, GoodsMovementType, Grade, HeatNo, ID, InspectionLot, IsAutoPost, IsDeleted, ManufacturingOrder, Material, MaterialDocument, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, StorageLocation
- MES_SAP_UsageDecision_Trn_Tbl: HeatNo, ID, InspectionLot, MaterialType
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, WorkOrderNumber
- XMES_SAP_Batch_Characteristic_Trn_Tbl: BatchNo, ID
- XMES_SAP_CreateBatch_Mst_Tbl: Batch, ID, ModifiedBy, SAPPostingStatus
- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: Batch, CreatedBy, EntryUnit, GoodsMovementType, HeatNo, ID, IsDeleted, IssgOrRcvgMaterial, IssuingOrReceivingPlant, IssuingOrReceivingStorageLoc, ManufacturingOrder, Material, Plant, PostingMaterialType, QuantityInEntryUnit, StorageLocation

## What its own log shows

232,556 log rows, 2026-03-20 00:40 to 2026-07-08 23:45.
Error steps: Error; Set Posted In Batch characteristics for Hot or Cold Billet which are Posted but not enetered, reversal failed or post in Production process End; Set Posted In Batch characteristics for Hot or Cold Billet which are Posted but not enetered, reversal failed or post in Production process Start

Steps:
- Completed
- Cursor byprodcur on By Product table to set Posted state of Entered By Products process End
- Cursor byprodcur on By Product table to set Posted state of Entered By Products process Start
- Enable UD status in quality Having inspection Lot process End
- Enable UD status in quality Having inspection Lot process Start
- Entered
- Error
- Insert in inventory Transaction from Source plant and storage location  End
- Insert in inventory Transaction from Source plant and storage location  Start
- Insert in inventory Transaction from destination plant and storage location  Start
- Set Entered state for posted in Raw Material Consumption When Raw Material ID is entered in Consumption process End
- Set Entered state for posted in Raw Material Consumption When Raw Material ID is entered in Consumption process Start
- Set Post state In Production for Cold Billet process End
- Set Post state In Production for Cold Billet process Start
- Set Post state for Cold billet which are in Entered state in Production for Created Batch Process Start
- Set Post state for Cold billet which are in Entered state in Production for created batch Process End
- Set Post state for hot billet which are in Entered state in Production for Created Batch Process Start
- Set Post state for hot billet which are in Entered state in Production for created batch Process End
- Set Posted In Batch characteristics for Hot or Cold Billet which are Posted but not enetered, reversal failed or post in Production process End
- Set Posted In Batch characteristics for Hot or Cold Billet which are Posted but not enetered, reversal failed or post in Production process Start
- Set Posted In Production for GLS which is enetered in Production process End
- Set Posted In Production for GLS which is enetered in Production process Start
- Set Posted Quality is entered and having inspection lot when hot billet already posted in production process End
- Set Posted Quality is entered and having inspection lot when hot billet already posted in production process Start
- Set Posted UD of GLS is entered after successfully RR of GLS process End
- Set Posted UD of GLS is entered after successfully RR of GLS process Start
- Set Posted UD of Hot Billet is entered after RR of GLS process End
- Set Posted UD of Hot Billet is entered after RR of GLS process Start
- Set Posted plant to plant transfer of Hot Billet is entered after UD Process End
- Set Posted plant to plant transfer of Hot Billet is entered after UD Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_SAP_Posting_Sequence_Usp @ID='FFFFBA99-C1E3-4D74-B779-77BF0DAFECDB', @APIPostingType='Consumption'`
