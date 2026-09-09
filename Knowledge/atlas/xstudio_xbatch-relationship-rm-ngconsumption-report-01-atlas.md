---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rm-ngconsumption-report part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_NGConsumption_Report.EquipmentID -> RM_Reheating_Furnace_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentID-RM_Reheating_Furnace_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
