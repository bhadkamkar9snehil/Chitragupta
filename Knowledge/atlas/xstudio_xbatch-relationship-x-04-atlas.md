---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: X part 4

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Unit_Mst_Tbl.ParentID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_UpdateStackLocation.StackID -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StackID-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.CampaignId -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignId-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.Equipment -> Equipment.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Equipment-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.ItemID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ItemID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.ManufacturingOrderType -> Order_Type_MST.OrderType
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ManufacturingOrderType-Order_Type_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.ProductionPlant -> Plant_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProductionPlant-Plant_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.SalesOrder -> XBatch_Sales_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrder-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.SalesOrderItem -> XBatch_Sales_Order_Mst_Tbl.ItemID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrderItem-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.Status -> XBatch_Status_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Status-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.StorageLocation -> Storage_Location_MST.StorageLocation
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_ActiveLife_Element_Mst_Tbl.ElementNameID -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementNameID-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.ChargingBedBilletNo -> XMES_Live_Billet_Charging_Bed.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ChargingBedBilletNo-XMES_Live_Billet_Charging_Bed
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.Section1BilletNo -> XMES_Live_Charging_SECT1.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section1BilletNo-XMES_Live_Charging_SECT1
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.Section2BilletNo -> XMES_Live_Charging_SECT2.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section2BilletNo-XMES_Live_Charging_SECT2
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.ZonewiseBilletNo -> XMES_RM_Furnace_Billet_Trn_Tbl.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ZonewiseBilletNo-XMES_RM_Furnace_Billet_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Strand_tracking.EndProduct -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndProduct-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Strand_tracking.ParentID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: ParentID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.ProcessStage -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessStage-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.Qualitygradeid -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Qualitygradeid-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.StatePosition -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatePosition-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.BilletGrade -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.EndproductGrade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndproductGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.GLSGrade -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GLSGrade-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Campaign_Plan_Mst.ID -> XMES_RM_Campaign_Plan_Trn.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_RM_Campaign_Plan_Trn
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Campaign_Plan_Mst.Productname -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Productname-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.ProcessStage -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessStage-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.Qualitygradeid -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Qualitygradeid-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.StatePosition -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatePosition-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Counter_Trn_Tbl.ElementNameID -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementNameID-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Type_Mapping_Mst_Tbl.ElementType -> XMES_Life_Element_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementType-XMES_Life_Element_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Type_Mapping_Mst_Tbl.ParentID -> XMES_Life_Tracker_Register_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Life_Tracker_Register_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_CCM_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_CCM_Remarks_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Grade -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
