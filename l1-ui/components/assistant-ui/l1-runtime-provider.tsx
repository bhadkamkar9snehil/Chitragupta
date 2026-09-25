"use client";

import { useMemo, useRef, type ReactNode } from "react";
import {
  AssistantRuntimeProvider,
  AuiConfig,
  Tools,
  useLocalRuntime,
  type ChatModelAdapter,
  type ThreadAssistantMessagePart,
} from "@assistant-ui/react";
import l1Toolkit from "@/app/toolkit";
import {
  L1HumanToolNameSchema,
  L1MessageResponseSchema,
} from "@/lib/l1-contract";

type ToolCallPart = Extract<
  ThreadAssistantMessagePart,
  { type: "tool-call" }
>;

function assertNever(_value: never): never {
  throw new Error("Unsupported L1 response type.");
}

function displayToolCall(
  toolName: string,
  toolCallId: string,
  result: unknown,
): ToolCallPart {
  return {
    type: "tool-call",
    toolCallId,
    toolName,
    args: {},
    argsText: "{}",
    result,
  };
}

function humanToolCall(
  toolName: string,
  toolCallId: string,
  args: unknown,
): ToolCallPart {
  const argsText = JSON.stringify(args);
  return {
    type: "tool-call",
    toolCallId,
    toolName,
    args: JSON.parse(argsText),
    argsText,
  };
}

function displayToolCallId(prefix: string, turn: number) {
  return `${prefix}-${turn}`;
}

export function L1RuntimeProvider({
  children,
}: Readonly<{ children: ReactNode }>) {
  const conversationIdRef = useRef<string | null>(null);

  const modelAdapter = useMemo<ChatModelAdapter>(
    () => ({
      async run({ messages, abortSignal, unstable_getMessage }) {
        if (!conversationIdRef.current) {
          conversationIdRef.current = crypto.randomUUID();
        }

        const toolResults = unstable_getMessage().content.flatMap((part) => {
          if (part.type !== "tool-call" || part.result === undefined) return [];

          const parsedName = L1HumanToolNameSchema.safeParse(part.toolName);
          if (!parsedName.success) return [];

          return [
            {
              toolCallId: part.toolCallId,
              toolName: parsedName.data,
              result: part.result,
            },
          ];
        });

        const response = await fetch("/api/l1/message", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            conversationId: conversationIdRef.current,
            messages,
            toolResults,
          }),
          signal: abortSignal,
        });

        if (!response.ok) {
          throw new Error("The Helpdesk request could not be completed.");
        }

        const parsed = L1MessageResponseSchema.safeParse(await response.json());
        if (!parsed.success) {
          throw new Error("The Helpdesk response was invalid.");
        }

        const turn = messages.length;

        switch (parsed.data.type) {
          case "message": {
            const content: ThreadAssistantMessagePart[] = [
              { type: "text", text: parsed.data.text },
            ];

            if (parsed.data.sources) {
              content.push(
                displayToolCall(
                  "show_knowledge_sources",
                  displayToolCallId("knowledge", turn),
                  { sources: parsed.data.sources },
                ),
              );
            }

            return { content };
          }

          case "collect_intake":
            return {
              content: [
                humanToolCall(
                  "collect_intake",
                  parsed.data.toolCallId,
                  parsed.data.flow,
                ),
              ],
              status: { type: "requires-action", reason: "tool-calls" },
            };

          case "ticket":
            return {
              content: [
                displayToolCall(
                  "show_ticket",
                  displayToolCallId("ticket", turn),
                  parsed.data.ticket,
                ),
              ],
            };

          case "tickets":
            return {
              content: [
                displayToolCall(
                  "show_tickets",
                  displayToolCallId("tickets", turn),
                  { tickets: parsed.data.tickets },
                ),
              ],
            };

          case "l2_reply":
            return {
              content: [
                displayToolCall(
                  "show_l2_reply",
                  displayToolCallId("l2-reply", turn),
                  parsed.data.reply,
                ),
              ],
            };

          case "l2_question":
            return {
              content: [
                humanToolCall(
                  "answer_l2_question",
                  parsed.data.toolCallId,
                  parsed.data.prompt,
                ),
              ],
              status: { type: "requires-action", reason: "tool-calls" },
            };

          default:
            return assertNever(parsed.data);
        }
      },
    }),
    [],
  );

  const runtime = useLocalRuntime(modelAdapter, {
    unstable_humanToolNames: ["collect_intake", "answer_l2_question"],
  });
  const config = AuiConfig({ tools: Tools({ toolkit: l1Toolkit }) });

  return (
    <AssistantRuntimeProvider runtime={runtime} config={config}>
      {children}
    </AssistantRuntimeProvider>
  );
}
