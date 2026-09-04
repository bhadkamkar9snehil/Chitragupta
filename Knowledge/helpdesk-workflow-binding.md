---
type: "Reference"
title: "Helpdesk Workflow Binding for Hermes"
description: "Explains how Hermes uses the existing Complaint_Mst_Tbl workflow without creating a second ticket lifecycle."
tags:
  - "hermes"
  - "helpdesk"
  - "workflow"
status: draft
---

# Helpdesk Workflow Binding for Hermes

## What is known from the supplied snapshot

`dbo.Complaint_Mst_Tbl` contains:

```text
Status
Solution
SupportExecutiveRemarks
AskRemarks
ReplyRemarks
AskStatus
messages
ssmmessage
Soharmessage
AssignedUserID
Priority
```

The supplied Helpdesk stored-procedure export contains ticket-number and assignment
procedures and a UAT procedure that inserts complaints, but it does not show a generic
close/reply procedure.

That does not prove one does not exist in the current installed configuration/system
databases.

## First deployment action

Run:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

It returns:

1. distinct current `Status` / `AskStatus` / `messages` combinations;
2. priority IDs;
3. complaint types;
4. current SQL modules that touch `Complaint_Mst_Tbl` or reply fields;
5. current triggers on the ticket table;
6. recent ticket rows with the workflow/reply fields.

Review those results before binding Hermes.

## Hermes does not invent status names

The stored-procedure package deliberately avoids assumptions such as:

```text
Status = Open
Status = L2
Status = Closed
Status = L3
```

The actual values come from the current Helpdesk.

The runtime supplies:

```text
EligibleStatusCsv       statuses Hermes should poll as unresolved L2
ResolvedTicketStatus    existing Helpdesk state representing resolved/closed
L3TicketStatus          existing Helpdesk state shown to humans
NewAskStatus            existing question/waiting state, if the current workflow uses one
```

## L2 reply storage

The detailed L2 response is stored in:

```text
Hermes_L2_Response_Trn_Tbl
```

joined by:

```text
Complaint_Mst_Tbl.ID = Hermes_L2_Response_Trn_Tbl.TicketID
```

This is the structured reply surface XStudio should display.

The existing single-value fields such as `SupportExecutiveRemarks` and `AskRemarks` are not
required to become the history store.

`Hermes_L2_Publish_Response_Usp` can optionally mirror the reply into those existing fields
during transition, but the default is not to overwrite them.

## User follow-up

When Hermes asks a question:

```text
Hermes response row = QUESTION
RequiresUserInput = 1
TicketModifiedOnSeen = ticket ModifiedOn after Hermes publication
```

The candidate query does not pick the ticket again until the Helpdesk row changes after that
timestamp.

When the user replies through the existing Helpdesk mechanism, the ticket's `ModifiedOn`
changes. Hermes sees it again and starts the next attempt with the previous Hermes response
history loaded.

## Resolve and L3

Resolution:

```sql
EXEC dbo.Hermes_L2_Resolve_Ticket_Usp
    @RunID = ...,
    @ReplyText = ...,
    @Resolution = ...,
    @ResolvedTicketStatus = '<LIVE STATUS>';
```

L3:

```sql
EXEC dbo.Hermes_L2_Escalate_L3_Usp
    @RunID = ...,
    @ReplyText = ...,
    @L3TicketStatus = '<LIVE STATUS>';
```

The Helpdesk remains the workflow engine; Hermes merely drives the already-valid transition
state through SQL.
