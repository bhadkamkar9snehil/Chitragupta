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

function assertNever(value: never): never {
  throw new Error(`Unsupported L1 response type: ${String(value)}`);
}

function toolCallId(prefix: string, value: string, turn: number) {
  return `${prefix}-${value}-${turn}`;
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

            if (parsed.data.sources && parsed.data.sources.length > 0) {
              content.push({
                type: "tool-call",
                toolCallId: toolCallId(
                  "knowledge",
                  parsed.data.sources[0].id,
                  turn,
                ),
                toolName: "show_knowledge_sources",
                args: {},
                argsText: "{}",
                result: { sources: parsed.data.sources },
              });
            }

            return { content };
          }

          case "collect_intake":
            return {
              content: [
                {
                  type: "tool-call",
                  toolCallId: parsed.data.toolCallId,
                  toolName: "collect_intake",
                  args: parsed.data.flow,
                  argsText: JSON.stringify(parsed.data.flow),
                },
              ],
              status: { type: "requires-action", reason: "tool-calls" },
            };

          case "ticket":
            return {
              content: [
                {
                  type: "tool-call",
                  toolCallId: toolCallId(
                    "ticket",
                    parsed.data.ticket.ticketId,
                    turn,
                  ),
                  toolName: "show_ticket",
                  args: {},
                  argsText: "{}",
                  result: parsed.data.ticket,
                },
              ],
            };

          case "tickets":
            return {
              content: [
                {
                  type: "tool-call",
                  toolCallId: toolCallId("tickets", "current", turn),
                  toolName: "show_tickets",
                  args: {},
                  argsText: "{}",
                  result: { tickets: parsed.data.tickets },
                },
              ],
            };

          case "l2_reply":
            return {
              content: [
                {
                  type: "tool-call",
                  toolCallId: toolCallId(
                    "l2-reply",
                    parsed.data.reply.replyId,
                    turn,
                  ),
                  toolName: "show_l2_reply",
                  args: {},
                  argsText: "{}",
                  result: parsed.data.reply,
                },
              ],
            };

          case "l2_question":
            return {
              content: [
                {
                  type: "tool-call",
                  toolCallId: parsed.data.toolCallId,
                  toolName: "answer_l2_question",
                  args: parsed.data.prompt,
                  argsText: JSON.stringify(parsed.data.prompt),
                },
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
