---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-grade-protocol-eaf-parameters-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Grade -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Section -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
