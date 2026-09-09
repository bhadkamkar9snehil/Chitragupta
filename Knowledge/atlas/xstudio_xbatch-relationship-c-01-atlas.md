---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: C part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## CAPA_CorrectiveAction.CAPANO -> RMShiftDelayEntry_CAPA.CAPANO
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CAPANO-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## CAPA_CorrectiveAction.ParentID -> RMShiftDelayEntry_CAPA.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## CAPA_PreventiveAction.ParentID -> RMShiftDelayEntry_CAPA.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## CAPA_ProblemSolvingTeam.Name -> XStudio_User_Mst_Tbl.FullName
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Name-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CAPA_ProblemSolvingTeam.ParentID -> RMShiftDelayEntry_CAPA.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_5.EquipmentID -> CCM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Block.EquipmentID -> CCM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Data.CastingTimeHHMMSS -> CCM_Per_Heat.CastingStartTime
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CastingTimeHHMMSS-CCM_Per_Heat
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Data.EquipmentID -> CCM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.SalesOrder -> XBatch_Sales_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrder-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.SuperHeat -> CCM_Section_Strands.SuperHeat
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SuperHeat-CCM_Section_Strands
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_PER_SHIFT.EquipmentID -> CCM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand1 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand1-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand2 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand2-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand3 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand3-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand4 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand4-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand5 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand5-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand6 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand6-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_SMS_Block.EquipmentID -> CCM_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_SMS_Data.EquipmentID -> CCM_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_SMS_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_SMS_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_SMS_Tag_Mapping_Tbl.EquipmentID -> CCM_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Tag_Mapping_Tbl.EquipmentID -> CCM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-CCM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Chemistry_Deviation_Quality_Data.Grade -> XMES_SMS_Grade_Protocol_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Chemistry_Deviation_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## Chemistry_Deviation_Quality_Data.ShiftIncharge -> XStudio_User_Mst_Tbl.FullName
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ShiftIncharge-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Communication_System_Block.EquipmentID -> Communication_System_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-Communication_System_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Communication_System_Data.EquipmentID -> Communication_System_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-Communication_System_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Communication_System_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Communication_System_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Communication_System_Tag_Mapping_Tbl.EquipmentID -> Communication_System_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-Communication_System_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Control_and_Relay_Panels.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Control_and_Relay_Panels.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
