---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: sms-shift-operator-incharge-selection-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

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
