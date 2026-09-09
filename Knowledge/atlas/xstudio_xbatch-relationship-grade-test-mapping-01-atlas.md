---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: grade-test-mapping part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Grade_Test_Mapping.GradeName -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeName-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Grade_Test_Mapping.TestName -> Grade_Test_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TestName-Grade_Test_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
