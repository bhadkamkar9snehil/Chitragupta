"use client";

import {
  ActionBarPrimitive,
  AuiIf,
  ComposerPrimitive,
  ErrorPrimitive,
  MessagePrimitive,
  ThreadPrimitive,
} from "@assistant-ui/react";
import { ArrowUpIcon, CircleAlertIcon, SquareIcon } from "lucide-react";

function UserMessage() {
  return (
    <MessagePrimitive.Root className="flex justify-end px-4 sm:px-6">
      <div className="max-w-2xl break-words rounded-xl bg-primary px-4 py-3 text-base leading-6 text-primary-foreground md:text-sm">
        <MessagePrimitive.Parts />
      </div>
    </MessagePrimitive.Root>
  );
}

function AssistantMessage() {
  return (
    <MessagePrimitive.Root className="px-4 sm:px-6">
      <div className="break-words text-base leading-7 text-foreground md:text-sm md:leading-6">
        <MessagePrimitive.Parts />
        <MessagePrimitive.Error>
          <ErrorPrimitive.Root className="mt-3 flex items-start gap-3 rounded-lg border border-destructive/20 bg-destructive/5 p-3 text-destructive">
            <CircleAlertIcon className="mt-0.5 size-4 shrink-0" aria-hidden="true" />
            <div className="min-w-0 flex-1">
              <ErrorPrimitive.Message>
                I couldn&apos;t complete that reply. Try again.
              </ErrorPrimitive.Message>
            </div>
            <ActionBarPrimitive.Reload className="min-h-11 shrink-0 rounded-md px-3 text-sm font-medium hover:bg-destructive/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
              Retry
            </ActionBarPrimitive.Reload>
          </ErrorPrimitive.Root>
        </MessagePrimitive.Error>
      </div>
    </MessagePrimitive.Root>
  );
}

function Composer() {
  return (
    <ComposerPrimitive.Root className="flex w-full items-end gap-2 rounded-xl border bg-card p-2 focus-within:border-ring focus-within:ring-2 focus-within:ring-ring/20">
      <ComposerPrimitive.Input
        aria-label="Describe your support issue"
        placeholder="Describe what happened…"
        rows={1}
        className="max-h-40 min-h-11 flex-1 resize-none bg-transparent px-3 py-3 text-base leading-6 outline-none placeholder:text-muted-foreground md:text-sm"
      />
      <AuiIf condition={(state) => !state.thread.isRunning}>
        <ComposerPrimitive.Send
          aria-label="Send message"
          className="flex size-11 shrink-0 items-center justify-center rounded-lg bg-primary text-primary-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-40"
        >
          <ArrowUpIcon className="size-4" aria-hidden="true" />
        </ComposerPrimitive.Send>
      </AuiIf>
      <AuiIf condition={(state) => state.thread.isRunning}>
        <ComposerPrimitive.Cancel
          aria-label="Stop response"
          className="flex size-11 shrink-0 items-center justify-center rounded-lg bg-secondary text-secondary-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
        >
          <SquareIcon className="size-4" aria-hidden="true" />
        </ComposerPrimitive.Cancel>
      </AuiIf>
    </ComposerPrimitive.Root>
  );
}

export function L1Thread() {
  return (
    <ThreadPrimitive.Root className="flex h-full flex-col bg-background">
      <header className="border-b bg-card">
        <div className="mx-auto w-full max-w-3xl px-4 py-4 sm:px-6">
          <h1 className="text-base font-semibold tracking-tight">
            Chitragupta Helpdesk
          </h1>
          <p className="mt-1 text-sm text-muted-foreground">
            Describe the symptom and any identifiers you have. We’ll route it
            to the right specialist.
          </p>
        </div>
      </header>

      <ThreadPrimitive.Viewport
        turnAnchor="top"
        className="flex flex-1 flex-col overflow-y-auto"
      >
        <AuiIf condition={(state) => state.thread.isEmpty}>
          <div className="mx-auto flex w-full max-w-3xl flex-1 flex-col justify-center px-6 py-12 text-center">
            <h2 className="text-xl font-semibold tracking-tight sm:text-2xl">
              Describe what happened
            </h2>
            <p className="mx-auto mt-3 max-w-xl text-base leading-7 text-muted-foreground md:text-sm md:leading-6">
              Include the exact error text and any heat, work order, batch, or
              screen name you have. You do not need to know whether the issue
              belongs to SAP, MES, or XStudio.
            </p>
          </div>
        </AuiIf>

        <div className="mx-auto flex w-full max-w-3xl flex-col gap-5 py-6">
          <ThreadPrimitive.Messages>
            {({ message }) =>
              message.role === "user" ? <UserMessage /> : <AssistantMessage />
            }
          </ThreadPrimitive.Messages>

          <AuiIf condition={(state) => state.thread.isRunning}>
            <div
              className="px-4 text-sm text-muted-foreground sm:px-6"
              role="status"
              aria-live="polite"
            >
              Checking your issue…
            </div>
          </AuiIf>
        </div>

        <ThreadPrimitive.ViewportFooter className="sticky bottom-0 mt-auto border-t bg-background px-4 py-4 sm:px-6">
          <div className="mx-auto w-full max-w-3xl">
            <Composer />
          </div>
        </ThreadPrimitive.ViewportFooter>
      </ThreadPrimitive.Viewport>
    </ThreadPrimitive.Root>
  );
}
