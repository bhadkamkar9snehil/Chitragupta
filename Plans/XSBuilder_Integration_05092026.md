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

The Conductor workflow explicitly forwards those variables into the MCP child
process using `${VAR}` / `${VAR:-default}` interpolation.

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

The BOM models the XStudio side of the Chitragupta Helpdesk extension:

- 12 Chitragupta operational entities (runs, SQL evidence, L3 queue, activity,
  taxonomy, solution KB, problem management, feedback, escalation rules,
  agent trace)
- their business attributes
- L2/L3/knowledge/admin/observability list views
- human-edit surfaces for knowledge/problem/admin/feedback
- pages and menu navigation
- a native XStudio Approval workflow on `Hermes_L3_Escalation_Trn_Tbl.L3Status`
  with primary sequence `Open -> Assigned -> InProgress -> Resolved` and
  `Rejected` as a branch state
- workflow gate forms for assignment, resolution summary and rejection remarks
- Helpdesk L2 / L3 / Admin roles and functional rights
- reporting/summaries sourced from the runtime metric views

### Why the operational IDs are not XStudio Relations

`TicketID`, `RunID`, `SolutionID`, `ProblemID`, etc. are deliberately *not*
declared as XStudio dropdown relations in this BOM. The live/runtime contract
stores these as `varchar(36)`. XS Builder interprets a populated `Reference
Entity / Object` as Dropdown intent, and its relation compiler requires a
Dropdown attribute. Adding those relations would therefore change the datatype
and renderer contract instead of merely documenting correlation.

Correlation remains explicit in the runtime SQL, query tools, indexes and UI
columns. If the underlying Helpdesk schema is later migrated to genuine XStudio
Dropdown/Guid relations, that should be a separate intentional migration.

Base Helpdesk objects (`Complaint_Mst_Tbl`, `priority_mst`, `Area_Mst_Tbl`,
`ComplaintType_Mst_Tbl`, `CommonErrors`, `systemreferencedocuments`) remain
pre-existing prerequisites; this extension BOM does not fabricate a partial
replacement for the core Helpdesk product.

## Fresh-install boundary: workbook alone is not yet the whole SQL installer

The current XS Builder BOM can author XStudio entities/attributes and the
associated XStudio UI/workflow objects, but it does not express every runtime
SQL Server invariant in Chitragupta's custom support schema:

- exact physical string lengths
- custom SQL DEFAULT constraints
- filtered/unique indexes
- CHECK constraints
- stored procedures
- reporting views
- seed taxonomy rows

Those contracts currently live in `Knowledge/*.sql`.

**Important:** the existing `Knowledge/00_tables_and_indexes.sql` was originally
written as a create-if-absent installer. If XS Builder creates a table first,
that script will not automatically retrofit every table-level DEFAULT/CHECK
inside the skipped `CREATE TABLE` block. Therefore the final fresh-install path
must not be declared complete until one of these is implemented and tested:

1. preferred: make the Chitragupta SQL package a true idempotent reconciliation
   layer for XS Builder-created entities (verify columns, add missing defaults /
   checks / indexes, fail closed on incompatible physical types); or
2. add a certified XS Builder "adopt existing runtime table" path and run the
   exact Chitragupta table installer first.

The feature branch intentionally does **not** hide this gap with arbitrary raw
SQL embedded in workbook cells.

The intended end state is still one deployment design:

1. validate/plan the BOM;
2. establish exact runtime table invariants through the chosen certified path;
3. deploy/verify XStudio UI/workflow metadata through XS Builder;
4. apply discovery/dispatch/investigation/response/reporting SQL objects;
5. run `Knowledge/99_postflight.sql`;
6. re-plan with XS Builder and require no unexplained drift.

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

## Validation status

No live ticket was claimed and no target database was mutated while building
this branch. The new XS Builder C# tests and Conductor YAML still need to be run
in the real workstation checkout before merge/cutover; the branch is a reviewable
implementation, not a production cutover.
