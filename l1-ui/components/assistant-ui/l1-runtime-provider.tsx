"use client";

import type { ReactNode } from "react";
import {
  AssistantRuntimeProvider,
  AuiConfig,
  Tools,
  useLocalRuntime,
  type ChatModelAdapter,
} from "@assistant-ui/react";
import l1Toolkit from "@/app/toolkit";
import { L1MessageResponseSchema } from "@/lib/l1-contract";

const L1ModelAdapter: ChatModelAdapter = {
  async run({ messages, abortSignal, unstable_getMessage }) {
    const toolResults = unstable_getMessage().content.flatMap((part) =>
      part.type === "tool-call" && part.result !== undefined
        ? [{ toolCallId: part.toolCallId, result: part.result }]
        : [],
    );

    const response = await fetch("/api/l1/message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages, toolResults }),
      signal: abortSignal,
    });

    if (!response.ok) {
      const payload = (await response.json().catch(() => null)) as
        | { error?: string }
        | null;
      throw new Error(payload?.error ?? "L1 request failed.");
    }

    const parsed = L1MessageResponseSchema.safeParse(await response.json());
    if (!parsed.success) {
      throw new Error("L1 response did not match the UI contract.");
    }

    if (parsed.data.type === "collect_intake") {
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
    }

    return {
      content: [{ type: "text", text: parsed.data.text }],
    };
  },
};

export function L1RuntimeProvider({
  children,
}: Readonly<{ children: ReactNode }>) {
  const runtime = useLocalRuntime(L1ModelAdapter, {
    unstable_humanToolNames: ["collect_intake"],
  });
  const config = AuiConfig({ tools: Tools({ toolkit: l1Toolkit }) });

  return (
    <AssistantRuntimeProvider runtime={runtime} config={config}>
      {children}
    </AssistantRuntimeProvider>
  );
}
