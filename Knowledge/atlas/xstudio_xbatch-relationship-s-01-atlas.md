---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: S part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## SAP_Posting_Tbl.CreatedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CreatedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.MaterialCode -> XBatch_Material_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialCode-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.StorageLocation -> XBatch_Store_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-XBatch_Store_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.WorkOrderNo -> XBatch_Work_Order_Mst_Tbl.WorkOrderNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrderNo-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Shift_Operator_Incharge_Selection_Trn_Tbl.CP1Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CP1Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Shift_Operator_Incharge_Selection_Trn_Tbl.CP2Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CP2Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Shift_Operator_Incharge_Selection_Trn_Tbl.CP3Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CP3Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Shift_Operator_Incharge_Selection_Trn_Tbl.CP4Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CP4Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ShiftInCharge-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Shift_Operator_Incharge_Selection_Trn_Tbl.YardOperator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: YardOperator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.AreaName -> DelayAgency_Master.AreaName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaName-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.DelayAgency -> DelayAgency_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayAgency-DelayAgency_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.DelaySubtypeid -> DelaySubType_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelaySubtypeid-DelaySubType_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.DelayType -> DelayTypeMST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayType-DelayTypeMST
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.EquipmentName -> Equipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentName-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.ID -> RMShiftDelayEntry_CAPA.DelayTransactionid
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ID-RMShiftDelayEntry_CAPA
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.OperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: OperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.ShiftManager -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ShiftManager-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry.SubEquipmentName -> SubEquipment.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SubEquipmentName-SubEquipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry_Transaction_Operator.Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## ShiftDelayEntry_Transaction_Operator.ShiftManager -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ShiftManager-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Size_Nominal_Wt_Value_Master.Product -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_DelayEntry_CAPA.DelayTransactionid -> ShiftDelayEntry.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelayTransactionid-ShiftDelayEntry
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_DelayEntry_CAPA.Responsibility -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: Responsibility-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Production_Summary.Particulars -> Particulars_Masters.Particulars
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Particulars-Particulars_Masters
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Production_Summary.Type -> Particulars_Masters.Type
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Type-Particulars_Masters
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Production_Summary.UOM -> Particulars_Masters.UOM
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOM-Particulars_Masters
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.CCMOperator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CCMOperator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.EAFOperator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: EAFOperator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.LRFOperator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: LRFOperator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator1 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperator1-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator2 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperator2-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator3 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperator3-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.MouldOperator4 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperator4-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ScrapYardSupervision -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ScrapYardSupervision-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.Shift -> XStudio_Shift_Dtl_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Shift-XStudio_Shift_Dtl_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ShiftInCharge-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SSM_Shift_Operator_Incharge_Selection_Trn_Tbl.CP4Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CP4Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
