---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-sms-grade-protocol-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_SMS_Grade_Protocol_Mst_Tbl.ChemistryID -> XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ChemistryID-XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.GradeID -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.ID -> XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.SectionID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SectionID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
