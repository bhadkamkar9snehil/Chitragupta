---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: R part 2

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_Rolling_Plan.Customer -> XBatch_Customer_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Customer-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rolling_Plan.MaterialGrade -> Steel_Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Steel_Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rolling_Plan.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Sales_Order.Customer -> XBatch_Customer_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Customer-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Sales_Order.MaterialGrade -> Steel_Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Steel_Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Sales_Order.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_TC_Grinding_Logbook.CNCOperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CNCOperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_TC_Grinding_Logbook.RingNo -> RM_Ring_No_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: RingNo-RM_Ring_No_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_WRM_Block.EquipmentID -> RM_WRM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_WRM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_WRM_Data.EquipmentID -> RM_WRM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_WRM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_WRM_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_WRM_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_WRM_Tag_Mapping_Tbl.EquipmentID -> RM_WRM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_WRM_Mst_Tbl
Provenance: xstudio_configuration_relationship (2 source row(s))

## RMShiftDelayEntry_CAPA.Agency -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Agency-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.AgencyAfterCAPA -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AgencyAfterCAPA-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.AgencyBeforeCAPA -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AgencyBeforeCAPA-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.DelayTransactionid -> ShiftDelayEntry.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayTransactionid-ShiftDelayEntry
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.Equipment -> Equipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Equipment-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.ID -> CAPA_CorrectiveAction.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-CAPA_CorrectiveAction
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.Photos -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Photos-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.ProposedAction -> CAPA_PreventiveAction.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ProposedAction-CAPA_PreventiveAction
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.Responsibility -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Responsibility-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RMShiftDelayEntry_CAPA.SubEquipment -> SubEquipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SubEquipment-SubEquipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## Roll_History_Card.DeptHead -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DeptHead-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Roll_History_Card.Signature -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Signature-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Round_Bar_Quality_Data.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Round_Bar_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))
