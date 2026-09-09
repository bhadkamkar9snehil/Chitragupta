---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: X part 5

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Section -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Remarks_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_LRF_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_LRF_Remarks_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_Super_Heat_Speed_Nozzle_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_Tapping_Additions_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Life_Element_Mst_Tbl.ParentID -> XMES_Life_Element_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Life_Element_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Billet_Charging_Bed.ID -> XMES_Billet_Tracking_Trn_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ID-XMES_Billet_Tracking_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Billet_Charging_Bed.ParentID -> RM_Operator_HeatSelection.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RM_Operator_HeatSelection
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT1.ParentID -> XMES_Live_Billet_Charging_Bed.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Billet_Charging_Bed
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT2.ID -> XMES_RM_Furnace_Billet_Trn_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_RM_Furnace_Billet_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT2.ParentID -> XMES_Live_Charging_SECT1.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Charging_SECT1
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Production_Campaign_Tracking.CampaignId -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignId-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Production_Campaign_Tracking.Work_Order -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Work_Order-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.Customer -> XBatch_Customer_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Customer-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.MaterialNo -> XBatch_Material_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialNo-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.ParentID -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.SONumber -> XBatch_Sales_Order_Mst_Tbl.SalesOrderNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SONumber-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.WorkorderNo -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkorderNo-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Furnace_Billet_Trn_Tbl.HeatNo -> XBatch_Material_Inventory_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-XBatch_Material_Inventory_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Furnace_Billet_Trn_Tbl.ParentID -> XMES_Live_Charging_SECT2.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Charging_SECT2
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.Campaignid -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Campaignid-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.ProductType -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProductType-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.Workorderid -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Workorderid-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Production_Data.EndProductid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndProductid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Production_Data.Workorderid -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Workorderid-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_MST.Product -> Product_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_TRN.Campaignid -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Campaignid-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_TRN.Product -> Product_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SAP_Batch_Characteristic_Trn_Tbl.Saptransactionid -> XMES_SAP_API_Batch_Characteristics_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Saptransactionid-XMES_SAP_API_Batch_Characteristics_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SAP_CreateBatch_Mst_Tbl.SAPTransactionID -> XMES_SAP_API_Batch_Creation_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: SAPTransactionID-XMES_SAP_API_Batch_Creation_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.ChemistryID -> XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ChemistryID-XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.GradeID -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.ID -> XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.SectionID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SectionID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Stage_Position_Mapping_Mst_Tbl.PositionType -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PositionType-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Stage_Position_Mapping_Mst_Tbl.StageCode -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StageCode-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Work_Order_Trn_Tbl.CampaignID -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignID-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))
