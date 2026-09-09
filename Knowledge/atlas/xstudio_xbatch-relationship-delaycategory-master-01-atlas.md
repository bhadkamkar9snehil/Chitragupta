---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: delaycategory-master part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## DelayCategory_Master.DelaySubCategoryid -> DelaySubType_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: DelaySubCategoryid-DelaySubType_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
