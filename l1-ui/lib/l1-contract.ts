import { z } from "zod";
import { SerializableQuestionInputFlowSchema } from "@/components/tool-ui/question-flow/schema";

const IdSchema = z.string().trim().min(1).max(128);
const ShortTextSchema = z.string().trim().min(1).max(240);
const LongTextSchema = z.string().trim().min(1).max(12_000);
const DateTextSchema = z.string().trim().min(1).max(64);

export const L1HumanToolNameSchema = z.enum([
  "collect_intake",
  "answer_l2_question",
]);

export const L1ToolResultSchema = z.object({
  toolCallId: IdSchema,
  toolName: L1HumanToolNameSchema,
  result: z.unknown(),
});

export const KnowledgeSourceSchema = z.object({
  id: IdSchema,
  title: ShortTextSchema,
  section: z.string().trim().min(1).max(160).optional(),
  excerpt: z.string().trim().min(1).max(600).optional(),
});

export const KnowledgeSourcesResultSchema = z.object({
  sources: z.array(KnowledgeSourceSchema).min(1).max(8),
});

export const TicketSnapshotSchema = z.object({
  ticketId: IdSchema,
  ticketNo: ShortTextSchema,
  summary: z.string().trim().min(1).max(1_200),
  statusLabel: z.string().trim().min(1).max(80),
  attentionRequired: z.boolean().default(false),
  domain: z.string().trim().min(1).max(80).optional(),
  area: z.string().trim().min(1).max(80).optional(),
  createdOn: DateTextSchema.optional(),
  updatedOn: DateTextSchema.optional(),
});

export const L2ReplySchema = z.object({
  replyId: IdSchema,
  ticketId: IdSchema,
  ticketNo: ShortTextSchema,
  kind: z.enum([
    "UPDATE",
    "RESOLUTION",
    "L3_ESCALATION",
    "NEEDS_HUMAN_ACTION",
  ]),
  text: LongTextSchema,
  publishedOn: DateTextSchema.optional(),
});

export const L2QuestionPromptSchema = z.object({
  questionId: IdSchema,
  ticketId: IdSchema,
  ticketNo: ShortTextSchema,
  question: z.string().trim().min(1).max(4_000),
});

export const L2QuestionAnswerResultSchema = z.object({
  questionId: IdSchema,
  ticketId: IdSchema,
  answer: z.string().trim().min(1).max(4_000),
});

export const L1MessageRequestSchema = z.object({
  conversationId: z.string().uuid(),
  messages: z.array(z.unknown()).min(1).max(100),
  toolResults: z.array(L1ToolResultSchema).max(4).default([]),
});

export const L1MessageResponseSchema = z.discriminatedUnion("type", [
  z.object({
    type: z.literal("message"),
    text: LongTextSchema,
    sources: z.array(KnowledgeSourceSchema).max(8).optional(),
  }),
  z.object({
    type: z.literal("collect_intake"),
    toolCallId: IdSchema,
    flow: SerializableQuestionInputFlowSchema,
  }),
  z.object({
    type: z.literal("ticket"),
    ticket: TicketSnapshotSchema,
  }),
  z.object({
    type: z.literal("l2_reply"),
    reply: L2ReplySchema,
  }),
  z.object({
    type: z.literal("l2_question"),
    toolCallId: IdSchema,
    prompt: L2QuestionPromptSchema,
  }),
]);

export type KnowledgeSource = z.infer<typeof KnowledgeSourceSchema>;
export type TicketSnapshot = z.infer<typeof TicketSnapshotSchema>;
export type L2Reply = z.infer<typeof L2ReplySchema>;
export type L2QuestionPrompt = z.infer<typeof L2QuestionPromptSchema>;
export type L2QuestionAnswerResult = z.infer<
  typeof L2QuestionAnswerResultSchema
>;
export type L1MessageResponse = z.infer<typeof L1MessageResponseSchema>;
