import type { ReactNode } from "react";
import { z } from "zod";

const IdSchema = z.string().trim().min(1).max(128);
const TitleSchema = z.string().trim().min(1).max(240);
const LabelSchema = z.string().trim().min(1).max(200);
const DescriptionSchema = z.string().trim().min(1).max(600);

const ToolUIRoleSchema = z.enum([
  "information",
  "decision",
  "control",
  "state",
  "composite",
]);

export const QuestionFlowOptionSchema = z.object({
  id: IdSchema,
  label: LabelSchema,
  description: DescriptionSchema.optional(),
  icon: z.custom<ReactNode>().optional(),
  disabled: z.boolean().optional(),
});

export type QuestionFlowOption = z.infer<typeof QuestionFlowOptionSchema>;

const SerializableOptionsSchema = z
  .array(QuestionFlowOptionSchema.omit({ icon: true }))
  .min(1)
  .max(20)
  .refine(
    (options) =>
      new Set(options.map((option) => option.id)).size === options.length,
    { message: "Question option IDs must be unique." },
  )
  .refine((options) => options.some((option) => !option.disabled), {
    message: "Question must contain at least one enabled option.",
  });

export const QuestionFlowStepDefinitionSchema = z.object({
  id: IdSchema,
  title: TitleSchema,
  description: DescriptionSchema.optional(),
  options: SerializableOptionsSchema,
  selectionMode: z.enum(["single", "multi"]).optional(),
});

export type QuestionFlowStepDefinition = z.infer<
  typeof QuestionFlowStepDefinitionSchema
>;

export const QuestionFlowSummaryItemSchema = z.object({
  label: LabelSchema,
  value: z.string().trim().min(1).max(600),
});

export const QuestionFlowChoiceSchema = z.object({
  title: TitleSchema,
  summary: z.array(QuestionFlowSummaryItemSchema).min(1).max(20),
});

const BaseSchema = z.object({
  id: IdSchema,
  role: ToolUIRoleSchema.optional(),
});

export const SerializableProgressiveModeSchema = BaseSchema.extend({
  step: z.number().int().min(1).max(8),
  title: TitleSchema,
  description: DescriptionSchema.optional(),
  options: SerializableOptionsSchema,
  selectionMode: z.enum(["single", "multi"]).optional(),
});

export const SerializableUpfrontModeSchema = BaseSchema.extend({
  steps: z
    .array(QuestionFlowStepDefinitionSchema)
    .min(1)
    .max(8)
    .refine(
      (steps) => new Set(steps.map((step) => step.id)).size === steps.length,
      { message: "Question step IDs must be unique." },
    ),
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
