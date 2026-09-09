---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: E part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## EAF_Custom.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_LogSheet_Ladle_Details.LaddleNumber -> LRF_Ladle_Number_Master.LadleNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LaddleNumber-LRF_Ladle_Number_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_LogSheet_Quantity.Grade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_LogSheet_Quantity.HeatNo -> EAF_PER_HEAT.HeatID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_LogSheet_Quantity.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_PER_HEAT.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_PER_HEAT.SteelGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SteelGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_PER_HEAT.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_ProcessTime.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_SMS_5.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_SMS_Block.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_SMS_Data.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_SMS_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_SMS_Tag_Mapping_Tbl.DataSourceID -> XStudio_DataSource_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: DatasourceID-XStudio_DataSource_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_SMS_Tag_Mapping_Tbl.EquipmentID -> EAF_SMS_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-EAF_SMS_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_Transformer.Attendant -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Attendant-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## EAF_Transformer_Reactor.Attendant -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Attendant-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Earthing_Transfomer.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Earthing_Transfomer.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_A_Shift_Check_List.ContractManpower -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ContractManpower-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_A_Shift_Check_List.NameGElectricians -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameGElectricians-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_A_Shift_Check_List.NameGEngineers -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameGEngineers-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_A_Shift_Check_List.NameofShiftELectricians -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameofShiftELectricians-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_A_Shift_Check_List.NameofShiftEngineers -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameofShiftEngineers-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_Shift_B_Check_List.ContractManpower -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ContractManpower-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_Shift_B_Check_List.NameofElectrician -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameofElectrician-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_Shift_B_Check_List.NameofEngineers -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameofEngineers-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Electricity_Bill_Details.TimeOfUse -> Rate_Band_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TimeOfUse-Rate_Band_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Electricity_Rate_Tbl_Mst.Months -> Month_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Months-Month_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Electricity_Rate_Tbl_Mst.Year -> Year_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Year-Year_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.AllFIleUpload -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: AllFIleUpload-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUpload132KVIC1 -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUpload132KVIC1-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUpload132KVIC2 -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUpload132KVIC2-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUpload15MVA -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUpload15MVA-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUpload24MVA -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUpload24MVA-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUpload33KVIC1 -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUpload33KVIC1-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUpload33KVIC2 -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUpload33KVIC2-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUploadEAF -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUploadEAF-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUploadLRF -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUploadLRF-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electricity_Meter_Reading_Upload.FIleUploadROLLINGMILL -> XStudio_Notes_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: FIleUploadROLLINGMILL-XStudio_Notes_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
