---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: R part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Rebar_Coil_Quality_Data.BilletGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Coil_Quality_Data.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Coil_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Coil_Quality_Data.ShiftInChargeOperation -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ShiftInChargeOperation-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.BilletGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## Rebar_Quality_Data.ShiftInChargeOperation -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ShiftInChargeOperation-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Billet_Weight_Block.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Charging_Plan.MaterialId -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialId-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Combustion_5.EquipmentID -> RM_Furnace_Combustion_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Furnace_Combustion_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Combustion_Data.EquipmentID -> RM_Furnace_Combustion_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Furnace_Combustion_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Combustion_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Combustion_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Combustion_Tag_Mapping_Tbl.EquipmentID -> RM_Furnace_Combustion_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Furnace_Combustion_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Logbook.EquipmentID -> RM_Mill_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Mill_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Logbook_Block.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Logbook_Block.OperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: OperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Furnace_Parameter.OperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: OperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Mill_Block.EquipmentID -> RM_Mill_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Mill_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Mill_Data.EquipmentID -> RM_Mill_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Mill_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Mill_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Mill_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Mill_Tag_Mapping_Tbl.EquipmentID -> RM_Mill_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Mill_Mst_Tbl
Provenance: xstudio_configuration_relationship (3 source row(s))

## RM_NGConsumption.CP1Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CP1Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_NGConsumption_Report.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Operator_HeatSelection.CampaignId -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignId-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Operator_HeatSelection.length -> XBatch_Work_Order_Mst_Tbl.Length
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: length-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Operator_HeatSelection.workorder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: workorder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rebar_Block.EquipmentID -> RM_Rebar_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Rebar_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rebar_Data.EquipmentID -> RM_Rebar_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Rebar_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rebar_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rebar_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Rebar_Tag_Mapping_Tbl.EquipmentID -> RM_Rebar_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Rebar_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Reheating_Furnace_Block.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Reheating_Furnace_Data.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Reheating_Furnace_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Reheating_Furnace_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Reheating_Furnace_Tag_Mapping_Tbl.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Roll_Turning_Job_Card.CNCOperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CNCOperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
