# AI-Embedded Helpdesk: Hermes L2 Implementation Summary

Based on: Helpdesk Plan 1 02092026.md

## Architecture Overview

The implementation follows the XStudio Helpdesk model mapped to Hermes L2:

```
XSTUDIO HELPDESK (L1)
    │
    └─→ Unresolved tickets → HERMES L2 (automated investigation)
                        │
                        ├─→ Queue/claim mechanism (SQL UPDLOCK/READPAST)
                        ├─→ Problem structuring
                        ├─→ Investigation orchestrator (this module)
                        │    ├─→ Specialized domain bots
                        │    ├─→ Evidence collection (structured, not prose)
                        │    └─→ Reasoning over findings
                        ├─→ Decision: RESOLVED / NEED_USER_INFORMATION / 
                        │     CONTINUE_INVESTIGATION / ESCALATE_L3
                        └─→ Structured L2 reply table

                SQL Helpdesk tables
```

## Components Built

### 1. Database Schema (Helpdesk_L2_Schema.sql)

Three new tables per plan sections 10-11:

- **Helpdesk_L2_Run_Trn**: Tracks each investigation run per ticket
  - RunID, TicketID, RunNo, Status, StartedOn, CompletedOn
  - ProblemCategory, ProblemSubCategory, InvestigationSummary, RootCause, Outcome
  - Model, PromptVersion for auditability

- **Helpdesk_L2_Reply_Trn**: Structured L2 replies in ticket thread
  - ReplyType (ANSWER/QUESTION/INVESTIGATION_UPDATE/RESOLUTION/L3_ESCALATION)
  - ReplyText, RootCause, Resolution, EvidenceSummary
  - RequiresUserResponse, IsResolution, EscalateToL3 flags
  - Joined through Ticket ID (not arbitrary columns)

- **Helpdesk_L2_Evidence_Trn**: Evidence collected during investigation
  - One row per check/finding from each bot
  - Investigator, CheckType, SourceSystem, SourceRecordID
  - Finding, ObservedValue, ObservedOn, QueryReference
  - Enables full explainability: "Why did Hermes close INC-38291?"

- Indexes and view `vw_Hermes_InvestigationStatus` for progress tracking

- **sp_Hermes_ClaimTicket**: Atomic ticket claiming with UPDLOCK/READPAST/ROWLOCK
  - Prevents two workers investigating same ticket
  - Marks AIProcessingStatus = 'RUNNING', sets AIClaimedBy/AIClaimedOn

- **sp_Hermes_ResolveTicket**: Update ticket after L2 resolution/decision

### 2. Hermes Investigation Orchestrator (Hermes_Orchestrator.py)

Python implementation of the core Hermes L2 workflow per the plan:

#### Workflow Phases (per plan sections):

1. **Claim Ticket** (Section 4): Atomic SQL SELECT with UPDLOCK/READPAST/ROWLOCK
   - One ticket per worker; serializes via SQL Server

2. **Load Context** (Section 8): Structured ticket state from DB
   - Ticket basics + previous replies + investigation runs + evidence history

3. **Structure Problem** (Sections 87-100): Free-text → structured problem statement
   - problem_type (SAP_PRODUCTION_POSTING, MES_PRODUCTION_STATE, etc.)
   - entities (heat_no, work_order, transaction_id)
   - symptom (extracted from description)

4. **Investigate** (Sections 5-7): Launch appropriate domain bots
   - Bots defined in INVESTIGATION_BOTS dict (Section 6):
     - TicketContextBot, SAPBot, SMSBot, QualityBot, IntegrationBot,
       ConfigurationBot, KnowledgeBot
   - Each bot performs domain-specific checks via SQL queries
   - Returns structured evidence (not prose) per Section 9

5. **Reason Over Findings** (Section 9): Hermes reasons over structured evidence
   - Evidence-driven (not prose-based)
   - Returns: RESOLVED / ESCALATE_L3 / CONTINUE_INVESTIGATION / 
     NEED_USER_INFORMATION
   - Critical failures → L3 escalation
   - Partial results → continue investigation

6. **Decide Outcome** (Sections 55-59): Hermes engineering decision
   - Can I explain the problem? → Yes/No
   - Can I provide valid resolution? → Yes/No
   - Do observations support conclusion? → Yes/No
   - Final outcome per above 4 options

7. **Generate Structured Reply** (Sections 10-11): Insert into Helpdesk_L2_Reply_Trn
   - ReplyType, ReplyText, RootCause, Resolution, EvidenceSummary
   - RequiresUserResponse, IsResolution, EscalateToL3 flags
   - Dedicated transactional table, not arbitrary columns

8. **Update Ticket Status** (Section 13): Direct ticket closure/escalation
   - STATUS mapping: RESOLVED → RESOLVED, ESCALATE_L3 → ESCALATED_L3,
     NEED_USER_INFORMATION → WAITING_USER, CONTINUE_INVESTIGATION → AI_INVESTIGATING
   - AIProcessingStatus = COMPLETED, ResolvedOn = GETUTCDATE()

#### Key Design Decisions from the Plan:

- **Section 3**: Cron job only wakes Hermes up; does NOT process every ticket serially
- **Section 4**: Ticket claiming with atomic SQL transaction (implemented)
- **Section 5**: Investigation planner decides WHAT to check, not one giant prompt
- **Section 6**: Small set of domain investigators (7 bots defined, extensible)
- **Section 7**: Read-only SQL identity for Hermes (SELECT approved SPs, views, config)
- **Section 8**: Structured engineering context about schemas, relationships, meanings
- **Section 9**: Evidence-driven (each bot returns structured JSON, not prose)
- **Section 10**: Dedicated L2 reply table joined through Ticket ID
- **Section 11**: Separate Run_Trn + Evidence_Trn for full explainability later
- **Section 12**: Hermes can ask user questions (RequiresUserResponse flag)
- **Section 13**: Hermes can close tickets directly
- **Section 14**: L3 escalation package prepared with complete investigation history

### 3. Bot Definitions (Section 6)

The orchestrator includes 7 domain investigators matching the plan's specification:

| Investigator | Responsibility |
|---|---|
| TicketContextBot | Understand ticket history, replies, user, timestamps |
| SAPBot | requests, responses, posting state, document IDs |
| SMSBot | EAF/LRF/VD/CCM and heat state |
| QualityBot | sample/results/release state |
| IntegrationBot | L2/interface/API connectivity |
| ConfigurationBot | XStudio/MES configuration and masters |
| KnowledgeBot | documentation/known issues when useful |

These are "tool groups / agent definitions inside Hermes" per Section 6 - not separate processes.

## Usage

```python
from Hermes_Orchestrator import HermesOrchestrator

# Initialize with worker ID
orch = HermesOrchestrator(worker_id="HERMES_WORKER_001")

# Run one complete investigation cycle
result = orch.run_investigation_cycle()

print(f"Outcome: {result['outcome']}")
if result.get('reply', {}).get('reply_id'):
    print(f"Reply inserted: {result['reply']['reply_id']}")
    print(f"Requires user: {result['reply']['requires_user_response']}")
    print(f"Is resolution: {result['reply']['is_resolution']}")
    print(f"Escalate L3: {result['reply']['escalate_to_l3']}")
```

## Migration Path from Plan to Implementation

| Plan Section | Implemented As |
|---|---|
| 1-2 | Target flow diagram → SQL queue + Hermes responsibilities |
| 3 | Scheduler → Dispatcher → Worker → Orchestrator pattern |
| 4 | SQL UPDLOCK/READPAST/ROWLOCK claiming → `sp_Hermes_ClaimTicket` |
| 5 | Investigation planner → `investigate()` method with bot dispatch |
| 6 | Domain investigators → `INVESTIGATION_BOTS` dict (7 bots) |
| 7 | Read-only SQL identity → GRANT SELECT on views/tables, DENY DML on MES |
| 8 | Engineering context → Schema docs + `load_ticket_context()` |
| 9 | Evidence-driven → Structured JSON evidence from each bot |
| 10 | L2 reply table → `Helpdesk_L2_Reply_Trn` |
| 11 | Separate investigation persistence → `Helpdesk_L2_Run_Trn` + `Helpdesk_L2_Evidence_Trn` |
| 12 | User questioning → `RequiresUserResponse` flag + QUESTION reply type |
| 13 | Close tickets directly → `update_ticket_status()` |
| 14 | L3 escalation package → `ESCALATE_L3` outcome + evidence summary |

## Next Steps / enhancements per the Plan

The plan deliberately keeps V1 simple (Section 19-20):

**DO NOT initially build:**
- Vector database / FAISS / complex RAG pipeline
- Support-ticket learning loop
- Dozens of specialist agents
- External message broker
- AI confidence scoring

**V1 implements only (Section 788-804):**
- Ticket poll / claim ✓ (implemented)
- Ticket context loading ✓ (implemented)
- SQL read tool ✓ (implemented)
- Schema/system documentation ✓ (implemented)
- Investigation planner ✓ (implemented)
- Evidence collection ✓ (implemented)
- Structured reply generation ✓ (implemented)
- Question-to-user handling ✓ (implemented)
- Ticket resolve ✓ (implemented)
- L3 escalation ✓ (implemented)
- Audit tables ✓ (implemented)

**Later additions if data proves useful:**
- Vector database for semantic ticket search
- RAG pipeline for knowledge bot
- Additional specialist agents
- External message broker (RabbitMQ/Kafka)
- AI confidence scoring