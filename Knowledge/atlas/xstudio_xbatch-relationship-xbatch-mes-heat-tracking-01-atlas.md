---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-mes-heat-tracking part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_MES_Heat_Tracking.CCMWorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CCMWorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.EAFWorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EAFWorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.LFEngineer -> SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.LRFOperator
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LFEngineer-SMS_Shift_Operator_Incharge_Selection_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.LRFWorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LRFWorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.Melter -> SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.EAFOperator
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Melter-SMS_Shift_Operator_Incharge_Selection_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.Sequence -> CCM_Per_Heat.LadleSequence
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Sequence-CCM_Per_Heat
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.ShiftManager -> SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ShiftManager-SMS_Shift_Operator_Incharge_Selection_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.StartTime -> CCM_Per_Heat.StartTime
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StartTime-CCM_Per_Heat
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.SteelGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SteelGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
