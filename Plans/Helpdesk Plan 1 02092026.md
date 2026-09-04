The revised split is cleaner:

> **XStudio = L1 interaction layer**  
> **Hermes = autonomous L2 investigator**  
> **Human engineers = L3**

Hermes should not behave like another chatbot. It should behave like an **automated support engineer working a queue of unresolved L2 tickets**.

Your drawing maps well to this model.

## 1. Target flow

```text
                    XSTUDIO HELPDESK
                           │
                L1 handled in XStudio
                           │
                 unresolved / L2 needed
                           ▼
                Helpdesk Ticket Table
                           │
                           │ SQL
                           ▼
               ┌───────────────────────┐
               │       HERMES L2       │
               │                       │
               │ Scheduler / Worker    │
               └───────────┬───────────┘
                           │
                    claim next ticket
                           │
                           ▼
                 Understand Problem
                           │
                           ▼
                  Investigation Plan
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
           Bot A         Bot B         Bot C
        MES state       SAP/API       Logs/config
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                     Collate Evidence
                           │
                           ▼
                       Reasoning
                           │
          ┌────────────────┼─────────────────┐
          │                │                 │
          ▼                ▼                 ▼
      Resolved        Need user info      Need L3
          │                │                 │
          ▼                ▼                 ▼
     L2 reply table   L2 reply table     L3 escalation
     + close ticket   ask question       + investigation
                           │                 package
                           ▼
                    wait for response
                           │
                           └──────► Hermes resumes
```

That is the architecture I would build.

---

# 2. Hermes's job

Hermes gets five responsibilities.

### A. Queue management

Continuously identify tickets that:

```text
Status = Open
SupportLevel = L2
AIProcessingStatus != Running
```

or whatever equivalent fields exist in XStudio.

### B. Understand the ticket

Turn free-text ticket information into a structured problem statement.

For example:

```json
{
  "ticketId": 38291,
  "area": "SMS",
  "module": "CCM",
  "problemType": "SAP_PRODUCTION_POSTING",
  "entities": {
    "heatNo": "H26090241",
    "workOrder": null,
    "transactionId": null
  },
  "symptom": "Billet production is visible in MES but SAP posting failed"
}
```

### C. Investigate

Hermes determines what information it needs and launches appropriate investigation bots/tools.

### D. Decide

Hermes concludes one of:

```text
RESOLVED
NEED_USER_INFORMATION
CONTINUE_INVESTIGATION
ESCALATE_L3
```

### E. Respond

Insert a structured L2 response into the XStudio Helpdesk database.

---

# 3. Do not make the cron job itself the investigator

Your note says:

> Hermes cron job reads unresolved tickets.

Conceptually yes, but I would separate these internally:

```text
Scheduler
    ↓
Ticket Dispatcher
    ↓
Ticket Worker
    ↓
Investigation Orchestrator
```

The scheduler should only wake Hermes up.

It should **not** process every unresolved ticket serially inside one cron invocation.

Otherwise one ticket taking 10 minutes blocks everything behind it.

---

# 4. SQL queue / claim mechanism

Even if you don't introduce RabbitMQ/Kafka/etc., SQL Server itself can safely act as the queue.

Hermes should atomically **claim** a ticket.

Conceptually:

```sql
BEGIN TRANSACTION;

SELECT TOP 1 ...
FROM HelpdeskTicket WITH (UPDLOCK, READPAST, ROWLOCK)
WHERE
    SupportLevel = 'L2'
    AND Status IN ('OPEN', 'REOPENED')
    AND (
        AIProcessingStatus IS NULL
        OR AIProcessingStatus IN ('READY', 'RETRY')
    )
ORDER BY Priority DESC, CreatedOn ASC;

UPDATE ...
SET
    AIProcessingStatus = 'RUNNING',
    AIClaimedBy = @WorkerID,
    AIClaimedOn = SYSUTCDATETIME();

COMMIT;
```

This becomes important once you run multiple Hermes workers.

Without claiming, two workers can investigate and reply to the same ticket.

---

# 5. Hermes should have an investigation orchestrator

This is the central piece.

Do **not** build one giant prompt saying:

> Here is a support ticket. Investigate it.

Instead:

```text
Ticket
   ↓
Problem Classifier
   ↓
Investigation Planner
   ↓
Specialized diagnostic tools/bots
   ↓
Evidence Collector
   ↓
Reasoner
```

The investigation planner decides what needs to be checked.

Example:

```text
Ticket:
"Heat 12124 production not posted to SAP"

Planner decides:

1. Find Heat 12124
2. Determine CCM production record
3. Determine associated WO
4. Check production quantity
5. Check SAP transaction creation
6. Check API request
7. Check API response
8. Check retry status
9. Check if SAP document number exists
10. Search application exceptions around transaction time
```

It then executes those steps.

---

# 6. Bots should represent investigation domains

I would not create arbitrary agents everywhere.

Create a relatively small set of domain investigators.

For LMEL MES, something like:

| Investigator | Responsibility |
|---|---|
| `TicketContextBot` | Understand ticket history, replies, user, timestamps |
| `OrderBot` | Sales order, work order, job state |
| `SMSBot` | EAF/LRF/VD/CCM and heat state |
| `BFBot` | Cast, consumption, production state |
| `WRMBot` | billet → furnace → coil execution |
| `BMBot` | billet → bloom execution |
| `InventoryBot` | material state/location/movements |
| `QualityBot` | sample/results/release state |
| `SAPBot` | requests, responses, posting state, document IDs |
| `IntegrationBot` | L2/interface/API connectivity |
| `UserAccessBot` | permissions/security configuration |
| `ApplicationBot` | application errors/services/logs |
| `ConfigurationBot` | XStudio/MES configuration and masters |
| `KnowledgeBot` | documentation/known issues when useful |

These aren't necessarily separate processes.

They can simply be **tool groups / agent definitions inside Hermes**.

---

# 7. Read-only DB access should be powerful

For Hermes L2, I would now favour giving it considerably more freedom than a typical end-user AI.

It needs to behave like an engineer.

Give Hermes a SQL identity that can:

```text
SELECT
execute approved read-only SPs
read views
read system configuration tables where appropriate
```

and cannot:

```text
INSERT MES data
UPDATE MES data
DELETE MES data
execute operational write SPs
DDL
```

The restriction should come from the SQL account itself.

Then Hermes can generate investigative SQL dynamically.

Example:

```sql
SELECT
    HeatNo,
    ProductionOrder,
    ProducedQty,
    SAPPostingStatus,
    CreatedOn
FROM ...
WHERE HeatNo = @HeatNo;
```

This is much more useful than trying to anticipate every possible L2 troubleshooting query.

---

# 8. Hermes should understand the database

This is what the **DOC** section of your drawing becomes.

Hermes needs structured engineering context about:

```text
1. Database schemas
2. Tables/views
3. Stored procedures
4. Relationships
5. Column meanings
6. Status/state meanings
7. Screen → table/SP relationships
8. MES processes
9. Integration flows
10. Known system behaviour
11. As-built configuration
12. Error codes
13. Deployment topology
```

For example:

```text
CCM Production Screen
    ↓
production records
    ↓
Heat No
    ↓
Production Transaction
    ↓
SAP API transaction
    ↓
SAP response
```

This information should help the planner know **where to investigate**.

It doesn't necessarily require embeddings/RAG.

---

# 9. Investigation should be evidence-driven

Every bot should return evidence, not prose.

Example:

```json
{
  "check": "SAP production posting",
  "status": "FAILED",
  "source": "SAP_API_TRANSACTION",
  "recordId": 872811,
  "observedAt": "2026-09-02T09:41:32",
  "facts": {
    "transactionId": "GR_20260902_00128",
    "httpStatus": 500,
    "sapDocumentNo": null,
    "retryCount": 2
  }
}
```

Another investigator:

```json
{
  "check": "CCM production",
  "status": "OK",
  "source": "CCM_PRODUCTION",
  "facts": {
    "heatNo": "H26090241",
    "billetCount": 18,
    "weight": 39.82,
    "productionCompleted": true
  }
}
```

Then Hermes reasons over structured findings.

This makes debugging Hermes itself much easier.

---

# 10. L2 reply table

I agree with your drawing: **don't dump Hermes output directly into arbitrary ticket columns.**

Create a dedicated transactional table joined through Ticket ID.

Something like:

```sql
Helpdesk_L2_Reply_Trn
---------------------

ID
TicketID
RunID

ReplyType
-- ANSWER
-- QUESTION
-- INVESTIGATION_UPDATE
-- RESOLUTION
-- L3_ESCALATION

ReplyText

RootCause
Resolution
EvidenceSummary

RequiresUserResponse
IsResolution
EscalateToL3

CreatedOn
CreatedBy
```

XStudio Helpdesk then simply displays these records in the normal ticket thread.

---

# 11. Keep detailed investigation separately

Do not put all the internal investigation into the user-visible reply.

Have another table:

```sql
Helpdesk_L2_Run_Trn
-------------------

RunID
TicketID
RunNo
Status
StartedOn
CompletedOn
ProblemCategory
ProblemSubCategory
InvestigationSummary
RootCause
Outcome
Model
PromptVersion
```

And:

```sql
Helpdesk_L2_Evidence_Trn
------------------------

ID
RunID
Investigator
CheckType
SourceSystem
SourceTable
SourceRecordID
Finding
ObservedValue
ObservedOn
QueryReference
```

This gives you full explainability later:

> Why did Hermes close INC-38291?

You can reconstruct the complete investigation.

---

# 12. Questions to the user

The loop in your drawing is important.

Hermes should absolutely be able to ask questions.

Example:

> The system shows two possible heats matching the reported time. Please confirm whether the affected heat is H26090241 or H26090242.

Then:

```text
Ticket state:
WAITING_USER

Hermes:
stop processing
```

When the user replies:

```text
XStudio inserts ticket reply
        ↓
Ticket becomes READY_L2
        ↓
Hermes sees it
        ↓
Loads complete previous investigation
        ↓
Continues from where it stopped
```

Do **not** start the whole investigation from scratch each time.

Persist the investigation state.

---

# 13. Closing tickets

Hermes should be able to close tickets directly.

Example:

```text
Investigation completed
       ↓
Root cause identified
       ↓
Resolution communicated
       ↓
Issue demonstrably no longer exists
       ↓
INSERT resolution reply
       ↓
UPDATE helpdesk ticket
SET Status = 'RESOLVED'
```

Whether XStudio subsequently moves `RESOLVED → CLOSED` immediately or after a defined period is an operational decision.

No special AI confidence mechanism is required.

Hermes simply makes an engineering decision:

```text
Can I explain the problem?
Can I provide a valid resolution?
Do current observations support that conclusion?
```

If yes, resolve.

---

# 14. L3 escalation

L3 should receive something much better than the original user ticket.

Hermes should prepare an **L3 investigation package**.

Example:

```text
L3 ESCALATION
────────────────────────────────

Ticket
INC-038291

Area
SMS / CCM

Issue
Billet production not reaching SAP

Entity
Heat H26090241

User symptom
"Production posting failed."

Hermes findings

✓ Heat exists
✓ CCM production complete
✓ 18 billets created
✓ MES production transaction created
✓ SAP request generated
✗ SAP transaction failed
✗ No material document generated

Failure started
09:41:32

Last successful posting
09:38:06

Affected transactions
5

SAP response
...

Application exception
...

Database inconsistency found
None

Similar known issue
None

Probable fault boundary
SAP integration / response processing

Investigations already completed
1...
2...
3...
4...

Reason for L3 escalation
Unexpected SAP response not covered by known
integration behaviour.

Useful IDs
...
```

That could save a developer 30–60 minutes before they even touch the case.

---

# 15. L3 should itself be a ticket state

You probably do not need a completely separate ticketing system.

Something like:

```text
SupportLevel

L1
L2
L3
```

and:

```text
Status

OPEN
WAITING_USER
AI_INVESTIGATING
RESOLVED
CLOSED
ESCALATED_L3
```

is enough.

Humans filter:

```text
SupportLevel = L3
AND Status = ESCALATED_L3
```

in XStudio.

---

# 16. Priority handling

Your notebook says:

> pick highest priority question

Correct, but add ageing.

Otherwise low-priority tickets can starve indefinitely.

Use something like:

```text
EffectivePriority =
    BasePriority
    + SLA urgency
    + waiting time
```

Also allow parallel investigations.

There is no reason Hermes should work only one ticket at a time.

---

# 17. Hermes should support investigation branches

A useful pattern is:

```text
                         Ticket
                            │
                  "SAP posting failed"
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
       MES production     SAP txn      Integration
          branch          branch          branch
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                       synthesis
```

This is what I interpret your **“bots”** note to mean.

Parallel investigative branches are a good fit.

But all bots should report back to one **lead investigator/orchestrator**.

You don't want bots conversing freely amongst themselves forever.

---

# 18. Avoid a rigid decision tree

Don't encode:

```text
IF problem = SAP
    run queries A,B,C
ELSE IF problem = Inventory
    run D,E,F
```

as the core design.

MES incidents cross domains.

Example:

```text
"Billet missing in WRM"
```

could involve:

```text
CCM production
quality
inventory
SAP GR
transfer
WRM allocation
```

Let Hermes construct the investigation plan dynamically using its knowledge of the system.

Deterministic diagnostic functions remain available, but the **sequence should be agent-driven**.

---

# 19. What I would build first

### Hermes V1

Implement only:

```text
Ticket poll / claim
Ticket context loading
SQL read tool
Schema/system documentation
Investigation planner
Evidence collection
Structured reply generation
Question-to-user handling
Ticket resolve
L3 escalation
Audit tables
```

That's enough to make a genuinely useful L2 system.

Do **not** initially build:

```text
Vector database
FAISS
complex RAG pipeline
support-ticket learning loop
dozens of specialist agents
external message broker
AI confidence scoring
```

Those can come later if the actual support data proves they're useful.

---

# 20. Initial Hermes architecture

I would therefore freeze this architecture:

```text
┌─────────────────────────────────────────────────┐
│                 XSTUDIO HELPDESK                 │
│                                                 │
│ L1                                               │
│ Ticket UI                                        │
│ Ticket replies                                   │
│ L3 engineer UI                                   │
└──────────────────────┬──────────────────────────┘
                       │ SQL
                       ▼
┌─────────────────────────────────────────────────┐
│                    HERMES L2                     │
│                                                 │
│  Scheduler                                      │
│      ↓                                          │
│  Ticket Dispatcher                              │
│      ↓                                          │
│  Lead Investigator                              │
│      │                                          │
│      ├── Problem understanding                  │
│      ├── Investigation planning                 │
│      ├── Launch diagnostic bots/tools           │
│      ├── Collect evidence                       │
│      ├── Cross-check findings                   │
│      └── Decide outcome                         │
│                                                 │
│         ↓              ↓               ↓        │
│       Reply        Ask User        Escalate L3  │
└─────────┬──────────────┬───────────────┬────────┘
          │              │               │
          └──────────────┼───────────────┘
                         ▼
                  SQL Helpdesk tables


Hermes Investigation Sources
─────────────────────────────────────────────────

       MES DB             Application
      READ ONLY             logs

       SAP/API             XStudio
     transactions         configuration

         L2                 System
    integration data     documentation
```

The main design problem now is **not LLM selection or RAG**.

It is building a sufficiently good **Hermes investigation environment**:

> **What can Hermes inspect, how does it know where to look, how does it preserve evidence, and when does it decide it has enough information to resolve versus escalate?**

That is where I would spend the design effort next.