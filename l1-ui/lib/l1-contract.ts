import { z } from "zod";
import { SerializableQuestionInputFlowSchema } from "@/components/tool-ui/question-flow/schema";

export const L1ToolResultSchema = z.object({
  toolCallId: z.string().min(1),
  result: z.unknown(),
});

export const L1MessageRequestSchema = z.object({
  messages: z.array(z.unknown()).min(1),
  toolResults: z.array(L1ToolResultSchema).default([]),
});

export const L1MessageResponseSchema = z.discriminatedUnion("type", [
  z.object({
    type: z.literal("message"),
    text: z.string(),
  }),
  z.object({
    type: z.literal("collect_intake"),
    toolCallId: z.string().min(1),
    flow: SerializableQuestionInputFlowSchema,
  }),
]);
