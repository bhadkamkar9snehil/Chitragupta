# Memory, Knowledge and Retrieval Re-evaluation

Status: design checkpoint before changing autonomous-worker memory/skill permissions.

## Goal

Chitragupta must run an autonomous L2 support cycle reliably on a small local model. The harness owns identity, lifecycle, transport, workflow mutations, evidence provenance and retrieval assembly. The model reasons over context and selects read-only evidence operations; it must not become the authority for durable truth.

## Confirmed principles

1. Durable current-ticket truth comes from live Helpdesk/XBatch evidence and deterministic run state.
2. Canonical reusable reference belongs in Git Knowledge/ and explicitly governed Solution exports.
3. GBrain is a derivative retrieval/index/graph substrate, not an authority class by itself.
4. Redacted sessions and mined lessons may be recorded automatically, but remain unverified until promoted by a separate control-plane process.
5. Retrieval that the harness can derive from the assigned ticket should be assembled by the harness before model reasoning rather than depending on the model to remember to search.
6. Similarity is never proof; retrieved material must carry provenance/trust and current-ticket facts still require live verification.
7. The small model must never be responsible for exact incident identity, SQL transport, or durable workflow state.

## Open decision deliberately not frozen yet

Do not globally disable Hermes memory, session-search or skill capabilities merely because model-written durable state is risky. Evaluate each capability by its read/write semantics and role in the full L2 cycle. The preferred pattern may be read-only or harness-mediated access rather than total removal.

Likewise, do not disable Mem0 or skill machinery until the exact Hermes behavior, automatic write paths, prefetch behavior, and configuration boundaries are verified against the deployed/current Hermes implementation.

## Retrieval direction to evaluate

The desired normal path is a deterministic context envelope assembled from requester-grounded ticket text and harness-known route/identity. Candidate sources include:

- canonical route-specific Git Knowledge content;
- promoted reviewed operational facts;
- governed semantic-hash-pinned Solution exports;
- bounded GBrain trusted-source retrieval;
- current ticket/run context and prior same-ticket ledger where applicable.

Raw sessions, unverified candidates and historical outcome cases may still be useful, but should be injected only under explicit policy with their trust class preserved. The correct question is not simply automatic vs manual retrieval; it is which authority classes are safe to inject at which lifecycle stage.

## Write direction to evaluate

Potential durable writes must be split by producer and trust transition:

- harness session recorder -> unverified episodic history;
- deterministic reviewer/publisher outcome materialization -> outcome-labelled cases;
- deterministic miners -> unverified candidates;
- human/controlled curator -> promoted operational facts / governed solutions;
- small model -> ideally no direct authority transition, though model suggestions may be captured as unverified evidence if bounded and provenance-preserving.

This file is intentionally a checkpoint, not the final architecture decision.