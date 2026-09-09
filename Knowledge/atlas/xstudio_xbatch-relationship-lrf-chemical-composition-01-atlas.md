---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: lrf-chemical-composition part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## LRF_Chemical_Composition.Grade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## LRF_Chemical_Composition.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
