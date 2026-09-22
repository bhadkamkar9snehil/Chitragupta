---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: lrf-per-heat part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

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
