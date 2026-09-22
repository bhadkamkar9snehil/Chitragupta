---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rm-roll-turning-job-card part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_Roll_Turning_Job_Card.CNCOperatorName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CNCOperatorName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
