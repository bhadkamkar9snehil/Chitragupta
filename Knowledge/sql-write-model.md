---
type: "Write Model"
title: "Hermes SQL Write Model"
description: "Defines how Hermes performs SQL-backed L2 fixes while following XKB's official-SP-first and live-verification principles."
status: draft
tags:
  - hermes
  - sql
  - write
  - stored-procedure
---

# Hermes SQL Write Model

## Hermes is allowed to write

Hermes is not constrained to read-only diagnosis.

It may write:

```text
XStudio_Helpdesk
XStudio_Xbatch / related project data databases
XStudio project configuration databases when the routed L2 fix requires it
```

The exact write is determined by the ticket and by the current installed XStudio/XMES
surface.

## Write-path precedence

Adopt the XKB rule:

```text
1. resolve the real target database/object
2. search for the official stored procedure/API that owns the operation
3. inspect the current signature/definition
4. use it when it covers the required operation
5. inspect trigger side effects when relevant
6. if no suitable official path exists, use a direct SQL write deliberately
7. verify the complete affected chain
```

This rule exists because XStudio behaviour is often implemented by SPs/triggers that do
more than a single table update. It is not a prohibition on SQL writes.

## Procedure discovery before a fix

Hermes can perform the discovery itself:

```sql
SELECT s.name AS SchemaName, p.name AS ProcedureName
FROM sys.procedures p
JOIN sys.schemas s ON s.schema_id = p.schema_id
WHERE p.name LIKE '%<feature>%'
ORDER BY p.name;

SELECT OBJECT_SCHEMA_NAME(m.object_id) AS SchemaName,
       OBJECT_NAME(m.object_id) AS ObjectName
FROM sys.sql_modules m
WHERE m.definition LIKE '%<target table or column>%';

SELECT OBJECT_NAME(object_id) AS ProcedureName,
       parameter_id, name,
       TYPE_NAME(user_type_id) AS DataType,
       max_length, is_output
FROM sys.parameters
WHERE object_id = OBJECT_ID('dbo.<ProcedureName>')
ORDER BY parameter_id;

SELECT OBJECT_DEFINITION(OBJECT_ID('dbo.<ProcedureName>'));
```

Search the relevant shared configuration, system configuration and data databases rather
than assuming the procedure is in one fixed database.

## Why the SP-first rule matters in this project

The supplied XBatch snapshot already demonstrates that procedures can:

- generate or transform posting rows;
- perform SAP posting sequence logic;
- populate API error summaries;
- log execution to `XMES_Log_Trn_Tbl`;
- update linked domain states;
- validate billet/heat/quantity conditions;
- recalculate summaries.

For example, `SAP_Posting_Data_ByHeat_Usp` is not a read procedure despite the word
"Data" in its name: the supplied definition inserts pending production/consumption rows
into `SAP_Posting_Tbl`.

Therefore Hermes must inspect definitions, not infer mutability from names.

## Direct writes

Direct writes are valid L2 actions when the current system has no suitable official operation.

Hermes should still record:

```text
ticket ID
target DB/table
predicate/record IDs
before state
executed SQL
after state
result
```

This can live in the structured L2 response's investigation/action JSON rather than requiring
a second audit subsystem.

## Audit identity

Use a dedicated Hermes service/user identity where the schema/SP accepts a user ID.
Preserve the platform's existing `CreatedBy`, `ModifiedBy`, `Source`, `ModifiedOn` conventions.

Do not invent a new `Source` value where downstream logic treats `Source` as an enum; inspect
the current data/SP behaviour first.

## Postflight

After a mutation, re-read the primary row and its dependent chain.

Examples:

### SAP posting fix

```text
domain production/consumption row
-> SAP transaction ID/status
-> API summary/error
-> material/inspection document response where applicable
-> execution log
```

### Heat correction

```text
source per-heat row
-> integrated heat tracking
-> production/summary consumer
-> any SAP transaction derived from it
```

### Helpdesk resolution

```text
Hermes L2 response inserted
-> existing ticket status/solution updated through current workflow path
-> ticket re-read
```

Hermes can close the ticket when the technical result and Helpdesk write both succeed.
