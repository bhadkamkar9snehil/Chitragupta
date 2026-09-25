"use client";

import { useId, useState } from "react";
import { Button } from "@/components/ui/button";
import type {
  KnowledgeSource,
  L2QuestionAnswerResult,
  L2QuestionPrompt,
  L2Reply,
  TicketSnapshot,
} from "@/lib/l1-contract";

function formatWhen(value?: string) {
  if (!value) return null;
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;

  return new Intl.DateTimeFormat(undefined, {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date);
}

export function KnowledgeSources({
  sources,
}: Readonly<{ sources: KnowledgeSource[] }>) {
  return (
    <section className="mt-4 border-t pt-3" aria-label="Sources used">
      <div className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">
        Sources used
      </div>
      <ul className="mt-2 space-y-3">
        {sources.map((source) => (
          <li key={source.id} className="min-w-0">
            <div className="break-words text-sm font-medium">{source.title}</div>
            {source.section ? (
              <div className="mt-0.5 break-words text-xs text-muted-foreground">
                {source.section}
              </div>
            ) : null}
            {source.excerpt ? (
              <p className="mt-1 break-words text-sm leading-6 text-muted-foreground">
                {source.excerpt}
              </p>
            ) : null}
          </li>
        ))}
      </ul>
    </section>
  );
}

export function TicketCard({
  ticket,
}: Readonly<{ ticket: TicketSnapshot }>) {
  const when = formatWhen(ticket.updatedOn ?? ticket.createdOn);

  return (
    <section
      className="mt-2 w-full max-w-lg rounded-xl border bg-card p-4"
      aria-label={`Helpdesk ticket ${ticket.ticketNo}`}
    >
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <div className="text-xs font-medium text-muted-foreground">
            Helpdesk ticket
          </div>
          <div className="mt-0.5 text-base font-semibold tabular-nums">
            {ticket.ticketNo}
          </div>
        </div>
        <div className="rounded-md bg-secondary px-2 py-1 text-xs font-medium text-secondary-foreground">
          {ticket.statusLabel}
        </div>
      </div>

      <p className="mt-3 break-words text-sm leading-6">{ticket.summary}</p>

      {ticket.domain || ticket.area || when ? (
        <dl className="mt-3 grid gap-2 border-t pt-3 text-sm sm:grid-cols-3">
          {ticket.domain ? (
            <div>
              <dt className="text-xs text-muted-foreground">System</dt>
              <dd className="mt-0.5 break-words font-medium">{ticket.domain}</dd>
            </div>
          ) : null}
          {ticket.area ? (
            <div>
              <dt className="text-xs text-muted-foreground">Area</dt>
              <dd className="mt-0.5 break-words font-medium">{ticket.area}</dd>
            </div>
          ) : null}
          {when ? (
            <div>
              <dt className="text-xs text-muted-foreground">Updated</dt>
              <dd className="mt-0.5 break-words font-medium">{when}</dd>
            </div>
          ) : null}
        </dl>
      ) : null}

      {ticket.attentionRequired ? (
        <p className="mt-3 border-t pt-3 text-sm font-medium text-destructive">
          Your reply is needed before support can continue.
        </p>
      ) : null}
    </section>
  );
}

export function TicketList({
  tickets,
}: Readonly<{ tickets: TicketSnapshot[] }>) {
  return (
    <section
      className="mt-2 w-full max-w-2xl border-t pt-3"
      aria-label="Your Helpdesk tickets"
    >
      <h3 className="text-sm font-semibold">Your Helpdesk tickets</h3>
      {tickets.length === 0 ? (
        <p className="mt-2 text-sm text-muted-foreground">
          No Helpdesk tickets are available for this account.
        </p>
      ) : (
        <ul className="mt-2">
          {tickets.map((ticket, index) => {
            const when = formatWhen(ticket.updatedOn ?? ticket.createdOn);
            return (
              <li
                key={ticket.ticketId}
                className={index > 0 ? "border-t py-3" : "pb-3"}
              >
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <span className="text-sm font-semibold tabular-nums">
                    {ticket.ticketNo}
                  </span>
                  <span className="rounded-md bg-secondary px-2 py-1 text-xs font-medium text-secondary-foreground">
                    {ticket.statusLabel}
                  </span>
                </div>
                <p className="mt-1 break-words text-sm leading-6">
                  {ticket.summary}
                </p>
                <div className="mt-1 flex flex-wrap gap-x-3 gap-y-1 text-xs text-muted-foreground">
                  {ticket.domain ? <span>{ticket.domain}</span> : null}
                  {ticket.area ? <span>{ticket.area}</span> : null}
                  {when ? <span>{when}</span> : null}
                  {ticket.attentionRequired ? (
                    <span className="font-medium text-destructive">
                      Reply needed
                    </span>
                  ) : null}
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}

const replyLabels: Record<L2Reply["kind"], string> = {
  UPDATE: "Support update",
  RESOLUTION: "Resolution",
  L3_ESCALATION: "Escalated",
  NEEDS_HUMAN_ACTION: "Manual action required",
};

export function L2ReplySurface({ reply }: Readonly<{ reply: L2Reply }>) {
  const when = formatWhen(reply.publishedOn);

  return (
    <section
      className="mt-2 w-full max-w-2xl border-t pt-3"
      aria-label={`${replyLabels[reply.kind]} for ticket ${reply.ticketNo}`}
    >
      <div className="flex flex-wrap items-center gap-x-2 gap-y-1 text-xs text-muted-foreground">
        <span className="font-semibold text-foreground">
          {replyLabels[reply.kind]}
        </span>
        <span aria-hidden="true">·</span>
        <span className="tabular-nums">{reply.ticketNo}</span>
        {when ? (
          <>
            <span aria-hidden="true">·</span>
            <span>{when}</span>
          </>
        ) : null}
      </div>
      <p className="mt-2 break-words whitespace-pre-wrap text-sm leading-6">
        {reply.text}
      </p>
    </section>
  );
}

export function L2QuestionSurface({
  prompt,
  answer,
  onSubmit,
}: Readonly<{
  prompt: L2QuestionPrompt;
  answer?: L2QuestionAnswerResult;
  onSubmit?: (answer: L2QuestionAnswerResult) => Promise<void> | void;
}>) {
  const answerFieldId = useId();
  const [value, setValue] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (answer) {
    return (
      <section
        className="mt-2 w-full max-w-lg rounded-xl border bg-card p-4"
        aria-label={`Answered support question for ticket ${prompt.ticketNo}`}
      >
        <div className="text-xs font-medium text-muted-foreground">
          Ticket {prompt.ticketNo}
        </div>
        <p className="mt-2 break-words text-sm font-medium leading-6">
          {prompt.question}
        </p>
        <div className="mt-3 border-t pt-3">
          <div className="text-xs text-muted-foreground">Your answer</div>
          <p className="mt-1 break-words whitespace-pre-wrap text-sm leading-6">
            {answer.answer}
          </p>
          <div className="mt-2 text-xs font-medium text-primary">
            Answer sent
          </div>
        </div>
      </section>
    );
  }

  async function submit() {
    const trimmed = value.trim();
    if (!trimmed || !onSubmit || submitting) return;

    setSubmitting(true);
    setError(null);
    try {
      await onSubmit({
        questionId: prompt.questionId,
        ticketId: prompt.ticketId,
        answer: trimmed,
      });
    } catch {
      setError("Your answer could not be sent. Try again.");
      setSubmitting(false);
    }
  }

  return (
    <form
      className="mt-2 w-full max-w-lg rounded-xl border bg-card p-4"
      aria-label={`Support question for ticket ${prompt.ticketNo}`}
      onSubmit={(event) => {
        event.preventDefault();
        void submit();
      }}
    >
      <div className="text-xs font-medium text-muted-foreground">
        Ticket {prompt.ticketNo}
      </div>
      <h3 className="mt-2 text-base font-semibold">Support needs more detail</h3>
      <p className="mt-1 break-words text-sm leading-6">{prompt.question}</p>

      <label
        className="mt-4 block text-sm font-medium"
        htmlFor={answerFieldId}
      >
        Your answer
      </label>
      <textarea
        id={answerFieldId}
        value={value}
        onChange={(event) => setValue(event.target.value)}
        maxLength={4_000}
        rows={4}
        disabled={submitting}
        className="mt-2 min-h-28 w-full resize-y rounded-lg border bg-background px-3 py-2 text-base leading-6 outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring/20 disabled:opacity-60 md:text-sm"
        placeholder="Add the detail support asked for…"
      />

      {error ? (
        <p className="mt-2 text-sm text-destructive" role="alert">
          {error}
        </p>
      ) : null}

      <div className="mt-3 flex justify-end">
        <Button
          type="submit"
          disabled={!value.trim() || submitting}
          className="w-full sm:w-auto"
        >
          {submitting ? "Sending…" : "Send answer"}
        </Button>
      </div>
    </form>
  );
}
