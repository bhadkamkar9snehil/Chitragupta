---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: quality-spectro-result part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Quality_Spectro_Result.SampleID -> Quality_Spectro_Sample.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SampleID-Quality_Spectro_Sample
Provenance: xstudio_configuration_relationship (1 source row(s))
