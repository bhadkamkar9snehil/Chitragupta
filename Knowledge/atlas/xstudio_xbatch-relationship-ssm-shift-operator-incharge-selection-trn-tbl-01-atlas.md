---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: ssm-shift-operator-incharge-selection-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## SSM_Shift_Operator_Incharge_Selection_Trn_Tbl.CP4Operator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CP4Operator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SSM_Shift_Operator_Incharge_Selection_Trn_Tbl.YardOperator -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: YardOperator-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
