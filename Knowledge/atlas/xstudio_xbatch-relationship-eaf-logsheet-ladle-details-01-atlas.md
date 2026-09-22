---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: eaf-logsheet-ladle-details part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## EAF_LogSheet_Ladle_Details.LaddleNumber -> LRF_Ladle_Number_Master.LadleNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LaddleNumber-LRF_Ladle_Number_Master
Provenance: xstudio_configuration_relationship (1 source row(s))
