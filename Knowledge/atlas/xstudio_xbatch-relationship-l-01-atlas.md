---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: L part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Laddle_Life_for_Each_Heat.LaddleNumber -> LRF_Ladle_Number_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LaddleNumber-LRF_Ladle_Number_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Life_Tracking.Area -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Area-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Life_Tracking.LifeName -> LifeName_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LifeName-LifeName_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Lightning_Arrestor_Counter_Reading.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Lightning_Arrestor_Counter_Reading.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.BilletGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## List_Rebar_Coil_Quality_Data_Histroy.ShiftInChargeOperation -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ShiftInChargeOperation-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Chemical_Composition.Grade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Chemical_Composition.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Ladle_No_Per_Heat.ActiveLadle -> LRF_Ladle_Number_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ActiveLadle-LRF_Ladle_Number_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Per_Heat.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Per_Heat.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Per_Heat.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_ProcessTime.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_5.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_Block.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_Data.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_SMS_Tag_Mapping_Tbl.EquipmentID -> LRF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-LRF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
