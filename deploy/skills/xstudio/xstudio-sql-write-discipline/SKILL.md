---
name: xstudio-sql-write-discipline
description: "Follow official-SP-first discipline before any SQL write."
version: 0.1.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, sql, write, stored-procedure, safety]
    related_skills: [xstudio-l2-ticket-workflow]
---

# XStudio SQL Write Discipline Skill

The precedence rule for any SQL mutation against an XStudio/XMES database —
not domain knowledge, applies across every ticket domain. Read-only
investigation doesn't need this skill.

## When to Use

- About to run an `UPDATE`/`INSERT`/`DELETE`, or about to call a stored
  procedure whose write behavior isn't yet confirmed.
- Don't use for: pure `SELECT` investigation with no intent to write.

## Procedure

0. **Verify every table/column name against the real schema before using
   it anywhere** — in a query, in a written response, in reasoning. Never
   trust a name from memory or a plausible-sounding guess, even mid-run:
   ```bash
   python "C:\Users\Admin\Documents\Office\AIHelpdesk\Knowledge\validate_identifiers.py" <table_name> [column1 column2 ...]
   ```
   Exit code 0 = real, verified against the live-exported schema
   (`Knowledge/schema_allowlist.json`, built from `Reference Documents/`).
   Exit code 1 = not real — the tool prints its closest real matches
   ("did you mean"); use one of those or investigate further, never the
   original guess. **This is not optional and not just for writes** — a
   real, documented 2026-09-03 incident had this exact skill's own
   worked model write a full response citing `COMPLAIN_MST_TBL` (doesn't
   exist) and columns like `SourceSystem`/`LastUpdated` on the wrong
   table, entirely from confident-sounding memory, never checked. If the
   allowlist itself looks stale (a column you know was added recently
   shows as unknown), regenerate it before trusting a negative result:
   `python Model_Bench/build_schema_allowlist.py` (rerun
   `SchemaExporter.py` first if the live schema itself has changed since
   the last `Reference Documents/` export).
1. **Resolve the real target database/object** — don't assume; XStudio
   splits config vs. data databases per system (e.g.
   `XStudio_Configuration_Xbatch` vs. `XStudio_Xbatch`).
2. **Search for the official stored procedure/API that owns the
   operation** before writing raw SQL:
   ```sql
   SELECT s.name AS SchemaName, p.name AS ProcedureName
   FROM sys.procedures p JOIN sys.schemas s ON s.schema_id = p.schema_id
   WHERE p.name LIKE '%<feature>%' ORDER BY p.name;

   SELECT OBJECT_SCHEMA_NAME(m.object_id) AS SchemaName,
          OBJECT_NAME(m.object_id) AS ObjectName
   FROM sys.sql_modules m WHERE m.definition LIKE '%<table-or-column>%';
   ```
3. **Inspect the current signature and full definition** — never call a
   procedure because its name looks plausible:
   ```sql
   SELECT OBJECT_NAME(object_id) AS ProcedureName, parameter_id, name,
          TYPE_NAME(user_type_id) AS DataType, max_length, is_output
   FROM sys.parameters WHERE object_id = OBJECT_ID('dbo.<ProcedureName>')
   ORDER BY parameter_id;

   SELECT OBJECT_DEFINITION(OBJECT_ID('dbo.<ProcedureName>'));
   ```
4. **Use the official procedure when it covers the operation.** Inspect
   trigger side effects when relevant — XStudio behavior is often
   implemented by SPs/triggers doing more than a single table update.
5. **For L2 ticket responses specifically, there is no direct-write
   fallback — it is technically blocked, not just discouraged.** As of
   2026-09-03, `approvals.deny` in this profile's `config.yaml`
   unconditionally blocks any `sqlcmd`/`cursor.execute` UPDATE, INSERT, or
   DELETE regardless of target table — a raw write attempt will be
   refused before it reaches the database. `Hermes_L2_Publish_Response_Usp`
   (via `Hermes_Orchestrator.py --publish-response`) is the only write
   path that exists for L2, not merely the recommended one. For other,
   non-L2 XStudio work where no deny rule applies, a direct write remains
   possible when no suitable official path exists, done deliberately and
   recorded: target DB/table, predicate/record IDs, before state, executed
   SQL, after state, result.
6. **Verify the complete affected chain after any write** — a successful
   SQL command is not enough:
   ```
   intended write path -> execution -> target row/state changed as
   expected -> dependent transaction/log/state checked -> ticket response
   written
   ```

## Pitfalls

- **A procedure name containing "Data," "Get," or "View" can still
  write.** `SAP_Posting_Data_ByHeat_Usp` inserts pending
  production/consumption rows despite the read-sounding name — this
  project's own worked example of "inspect before you trust."
- **A header comment can name the wrong operation.**
  `XMES_SAP_WorkOrder_Creation_API_Error_Usp`'s comment says "Movement"
  though the procedure name says "Creation" — trust the body, not the
  comment, when they disagree.
- **Don't invent a new `Source` value** where downstream logic treats
  `Source` as an enum — inspect current data/SP behavior first. Preserve
  existing `CreatedBy`/`ModifiedBy`/`Source`/`ModifiedOn` conventions and
  use a dedicated Hermes service identity where the schema/SP accepts one.

## Verification

- [ ] Every table/column name used in any query, tool call, or written
      response passed `validate_identifiers.py` this run — not assumed
      from memory, not carried over from a prior run.
- [ ] The procedure actually called was the one whose definition was just
      read this run, not one assumed from a prior investigation or from
      this skill's own examples.
- [ ] For a direct write, the full before/SQL/after/result record exists
      in the run's investigation/action evidence.
- [ ] The affected chain (not just the primary row) was re-read after the
      write.
