---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: eaf-per-heat part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

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
