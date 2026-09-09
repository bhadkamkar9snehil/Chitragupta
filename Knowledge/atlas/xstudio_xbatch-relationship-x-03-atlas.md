---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: X part 3

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

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

## XMES_Work_Order_Trn_Tbl.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xstudio_Xbatch_ChargingPlan_Mst_Tbl.Stackid -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Stackid-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
