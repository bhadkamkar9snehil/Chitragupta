# Qwen L2 harness validation — 2026-09-19

The target is the reusable Xbatch L2 investigation system. Tickets are synthetic test inputs. Editing an answer does not count as model success.

## Measured baseline

Ticket_212, attempt 8, run `BFB4CCC2-C8C1-4972-9DCE-444AAC8272C6`, exported from SQL and scored with `l2_harness_eval.py`:

| Measure | Observed |
|---|---:|
| Investigator / reviewer model turns | 16 / 10 |
| Investigator / reviewer tool calls | 22 / 13 |
| Cumulative reported tokens | 832,775 |
| Claim-to-completion duration | 12m 36.74s |
| Summed model API duration | 221.16s |
| Peak GPU memory | 7,760 / 8,188 MB |
| Material claims grounded in live evidence | No |
| Persisted outcome | UPDATE, approved |
| Expected outcome for missing occurrence identifier | QUESTION |

Token totals sum every API request, including repeated input context; they are not unique text tokens. The evaluator found 12 failed or unmatched tool calls; unmatched trace events alone do not establish execution failure. Tool-choice checks without required-tool assertions are not evidence of correct investigation. This run fails the outcome test despite completing publication.

The trace demonstrates `xstudio_get_definition(object_name="dbo.LRF_Per_Heat")` and `dbo.LRF_Manual_Entry` failing because the bridge passed a qualified name as the SQL object's unqualified name. Subsequent calls guessed columns and trigger names. The bridge now accepts plain, qualified and bracketed qualified object names, and rejects conflicting explicit schemas.

## Changes under test

- Existing outcome gates require a verified resolution, a concrete continuation for incomplete UPDATE, or a specific requester QUESTION.
- Investigator and reviewer completion instructions are separated; reviewers cannot replace the frozen proposal.
- The existing evaluator checks expected response type against persisted SQL first and rejects evidence references to failed SQL actions.
- The definition bridge normalizes the demonstrated argument shape. No new transport, scheduler or benchmark framework was added.

Regression checks on this continuation: 73 typed-tool checks and 10 evaluator tests pass. These checks do not establish improved model performance.

## Live verification boundary

The loaded model was verified as `qwen/qwen3.5-9b`, context 65,792, parallelism 1. The normal two-minute scout was resumed after the deployment pause. Fresh Windows MCP reads succeeded, but repeated native runtime ODBC reads failed during SQL prelogin/login; one runtime status read succeeded between failures. The resumed scout also failed before claiming work. No network root cause has been established.

Ticket_145 run `96EC62DE-913A-4E69-AA69-34B9C40FD073` remains active in SQL with its investigator task `t_fa3b3020` done. Its summary claims database rows establish resolution; this is not proof that the reported UI issue is resolved. The run must pass normalization, independent review and persisted publication checks. It must not be recovered merely because it is old.

Fixtures Ticket_229–231 are defined in `harness_20260918.json`. No successful post-change end-to-end result for those fixtures has been demonstrated. After stable runtime SQL connectivity returns, let the scout finish existing WIP, export the resulting runs, and compare outcomes and costs against this baseline. Do not bypass WIP with raw polling or count regression tests as model proof.
