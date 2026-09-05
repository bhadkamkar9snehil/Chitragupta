# XS Builder integration for Chitragupta (2026-09-05)

## Hard scope

Chitragupta's investigation tooling reads only two SQL databases:

- `XStudio_Helpdesk`
- `XStudio_Xbatch`

The XS Builder product remains generic. The Chitragupta bridge is deliberately
not generic: any third database is rejected before compilation or execution.

## Responsibility split

```text
Conductor / Qwopus
  decides which evidence is needed
          |
          v
Chitragupta MCP `query_table`
  structured intent only
          |
          v
XS Builder `xsb compile-read-query`
  live table/view discovery
  live column validation
  structured filter/order validation
  deterministic bounded SELECT compilation
  DOES NOT execute the final SELECT
          |
          v
Chitragupta Hermes_L2_Execute_SQL_Usp
  executes the compiled read ONCE
  records it against the ticket RunID
          |
          v
rows returned to investigator
```

This boundary is intentional:

- XS Builder is the one XStudio/SQL schema compiler.
- Chitragupta remains the one owner of ticket/run/evidence state.
- There is no Python query-builder fallback. XS Builder failure is explicit.
- The model cannot provide raw `WHERE` or `ORDER BY` fragments on the normal
  path.
- `execute_sql` remains only a read-only JOIN/aggregate escape hatch.

## XS Builder contract

Feature branch: `bhadkamkar9snehil/XS_Builder:feature/chitragupta-helpdesk`

New CLI operation:

```powershell
xsb compile-read-query `
  --connection <saved-connection-name-or-id> `
  --request-json '{"database":"XStudio_Xbatch","table":"SAP_Posting_Tbl","columns":["ID","Status"],"filters":[{"column":"Status","operator":"eq","value":"Pending"}],"orderBy":[{"column":"ID","direction":"DESC"}],"top":20}'
```

The request supports only structured operators:

- `eq`, `ne`
- `gt`, `gte`, `lt`, `lte`
- `contains`, `starts_with`, `ends_with`
- `in`
- `is_null`, `is_not_null`

`Top` is bounded to 1..1000. Every projected/filter/order column is resolved
against the live SQL Server object contract. Both user tables and views are
supported.

## Chitragupta runtime configuration

The MCP process needs:

```text
XSBUILDER_CONNECTION=<saved XS Builder connection profile name or ID>
XSBUILDER_CLI=<optional full path to xsb/xsb.exe; defaults to xsb>
```

`Model_Bench/xsbuilder_query_bridge.py` invokes the CLI and has no local
compiler fallback.

## MCP tool policy

### `suggest_tables`

Retrieval/ranking only. It searches the existing Chitragupta domain index but
now merges candidates only from Helpdesk and Xbatch. A suggestion is not
trusted until XS Builder live-validates it.

### `query_table`

Default data tool. Input is structured intent. XS Builder compiles it and
Chitragupta executes it once through the audited run path.

### `execute_sql`

Read-only fallback only when a real JOIN/aggregate cannot be expressed with
`query_table`. The same two-database boundary still applies.

## Fix included: audited reads no longer run twice in this MCP path

The older helper first called `Hermes_L2_Execute_SQL_Usp` for audit and then
executed the same SELECT directly again to obtain rows. `query_table` and the
fallback read path now obtain the first result set from the audited SP execution
itself, so the evidence query runs once.

## LM Studio / structured output

The active `qwopus3.5-9b-coder` LM Studio preset now has Structured Output
(Valid JSON) enabled. Conductor already declares the investigator output schema,
so no regex parser or parallel JSON-repair layer should be added.

The interactive LM Studio preset currently shows temperature `0.8`; the
Conductor workflow intentionally continues to request `0.2` for repeatable
support investigation. Change that from outcome benchmarks, not merely to match
the UI preset.

## Helpdesk BOM

Artifact: `Chitragupta_Helpdesk_XSBuilder_BOM.xlsx`.

The BOM owns the XStudio side of the Chitragupta Helpdesk extension:

- 12 Chitragupta operational entities (runs, SQL evidence, L3 queue, activity,
  taxonomy, solution KB, problem management, feedback, escalation rules,
  agent trace)
- their business attributes and relations
- L2/L3/knowledge/admin/observability list views
- human-edit surfaces
- pages and menu navigation
- L3 workflow (`Open -> Assigned -> InProgress -> Resolved/Rejected`)
- Helpdesk L2 / L3 / Admin roles and functional rights
- reporting/summaries sourced from the runtime metric views

Base Helpdesk objects (`Complaint_Mst_Tbl`, `priority_mst`, `Area_Mst_Tbl`,
`ComplaintType_Mst_Tbl`, `CommonErrors`, `systemreferencedocuments`) remain
pre-existing prerequisites; this extension BOM does not fabricate a partial
replacement for the core Helpdesk product.

## Why the runtime SQL package still exists

The current generic XS Builder BOM can author XStudio entities/attributes and UI
objects, but it does not fully express all runtime-only SQL contracts used here:

- filtered/unique indexes
- check constraints
- exact SQL defaults
- stored procedures
- reporting views
- seed taxonomy rows

Those remain authoritative in `Knowledge/*.sql`. The correct fresh deployment
sequence is therefore:

1. validate + plan the BOM;
2. deploy XStudio objects through XS Builder;
3. apply the Chitragupta runtime SQL reconciliation/procedure/view package;
4. run `Knowledge/99_postflight.sql`;
5. re-plan with XS Builder and require no unexplained drift.

This is one deployment design, not two independent schema engines: the BOM owns
XStudio metadata/UI; the repository SQL owns operational SQL Server artifacts
that XStudio BOM cannot currently represent.

## Fresh-install drift found while building the BOM

The current repository SQL has at least two model-vs-installer drifts that the
BOM makes explicit and that must be reconciled before calling a fresh deployment
fully reproducible:

1. `Hermes_Log_Agent_Trace_Usp` and `Hermes_L2_Compute_Per_Ticket_Vw` depend on
   `Hermes_Agent_Trace_Trn_Tbl`, but `00_tables_and_indexes.sql` does not create
   that table.
2. current publish logic writes `Hermes_L3_Escalation_Trn_Tbl.EscalationCategory`
   (`UNRESOLVED` / `NEEDS_HUMAN_ACTION`), while the base L3 table DDL in
   `00_tables_and_indexes.sql` does not declare that column.

The BOM intentionally includes both target objects so this mismatch is visible
rather than silently perpetuated.
