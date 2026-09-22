---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: procedure-steps-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Procedure_Steps_Mst_Tbl.ProcedureID -> Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcedureID-Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
