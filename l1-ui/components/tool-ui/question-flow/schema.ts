import type { ReactNode } from "react";
import { z } from "zod";

const ToolUIRoleSchema = z.enum([
  "information",
  "decision",
  "control",
  "state",
  "composite",
]);

export const QuestionFlowOptionSchema = z.object({
  id: z.string().min(1),
  label: z.string().min(1),
  description: z.string().optional(),
  icon: z.custom<ReactNode>().optional(),
  disabled: z.boolean().optional(),
});

export type QuestionFlowOption = z.infer<typeof QuestionFlowOptionSchema>;

export const QuestionFlowStepDefinitionSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  description: z.string().optional(),
  options: z.array(QuestionFlowOptionSchema.omit({ icon: true })).min(1),
  selectionMode: z.enum(["single", "multi"]).optional(),
});

export type QuestionFlowStepDefinition = z.infer<
  typeof QuestionFlowStepDefinitionSchema
>;

export const QuestionFlowSummaryItemSchema = z.object({
  label: z.string().min(1),
  value: z.string().min(1),
});

export const QuestionFlowChoiceSchema = z.object({
  title: z.string().min(1),
  summary: z.array(QuestionFlowSummaryItemSchema).min(1),
});

const BaseSchema = z.object({
  id: z.string().min(1),
  role: ToolUIRoleSchema.optional(),
});

export const SerializableProgressiveModeSchema = BaseSchema.extend({
  step: z.number().min(1),
  title: z.string().min(1),
  description: z.string().optional(),
  options: z.array(QuestionFlowOptionSchema.omit({ icon: true })).min(1),
  selectionMode: z.enum(["single", "multi"]).optional(),
});

export const SerializableUpfrontModeSchema = BaseSchema.extend({
  steps: z.array(QuestionFlowStepDefinitionSchema).min(1),
});

export const SerializableReceiptModeSchema = BaseSchema.extend({
  choice: QuestionFlowChoiceSchema,
});

export const SerializableQuestionInputFlowSchema = z.union([
  SerializableProgressiveModeSchema,
  SerializableUpfrontModeSchema,
]);

export type SerializableQuestionInputFlow = z.infer<
  typeof SerializableQuestionInputFlowSchema
>;

export function safeParseSerializableQuestionInputFlow(input: unknown) {
  const parsed = SerializableQuestionInputFlowSchema.safeParse(input);
  return parsed.success ? parsed.data : null;
}

interface BaseRuntimeProps {
  className?: string;
}

export interface QuestionFlowProgressiveProps
  extends BaseRuntimeProps,
    Omit<z.infer<typeof SerializableProgressiveModeSchema>, "options"> {
  options: Array<z.infer<typeof QuestionFlowOptionSchema>>;
  defaultValue?: string[];
  onSelect?: (optionIds: string[]) => void | Promise<void>;
  onBack?: () => void;
  steps?: never;
  choice?: never;
}

export interface QuestionFlowUpfrontProps
  extends BaseRuntimeProps,
    z.infer<typeof SerializableUpfrontModeSchema> {
  onStepChange?: (stepId: string) => void;
  onComplete?: (answers: Record<string, string[]>) => void | Promise<void>;
  step?: never;
  choice?: never;
}

export interface QuestionFlowReceiptProps
  extends BaseRuntimeProps,
    z.infer<typeof SerializableReceiptModeSchema> {
  step?: never;
  steps?: never;
}

export type QuestionFlowProps =
  | QuestionFlowProgressiveProps
  | QuestionFlowUpfrontProps
  | QuestionFlowReceiptProps;
