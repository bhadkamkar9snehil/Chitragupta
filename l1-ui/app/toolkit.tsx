"use generative";

import { defineToolkit } from "@assistant-ui/react";
import { QuestionFlow } from "@/components/tool-ui/question-flow";
import {
  SerializableQuestionInputFlowSchema,
  safeParseSerializableQuestionInputFlow,
  type SerializableQuestionInputFlow,
} from "@/components/tool-ui/question-flow/schema";

function labelsFor(
  options: ReadonlyArray<{ id: string; label: string }>,
  selected: unknown,
) {
  if (!Array.isArray(selected)) return [];
  return selected.map(String).map(
    (id) => options.find((option) => option.id === id)?.label ?? id,
  );
}

function receiptSummary(
  flow: SerializableQuestionInputFlow,
  result: unknown,
): Array<{ label: string; value: string }> {
  if (!result || typeof result !== "object" || Array.isArray(result)) {
    return [{ label: "Response", value: String(result ?? "Submitted") }];
  }

  const answers = result as Record<string, unknown>;

  if ("steps" in flow) {
    return flow.steps.map((step) => {
      const labels = labelsFor(step.options, answers[step.id]);
      return {
        label: step.title,
        value: labels.length > 0 ? labels.join(", ") : "Not provided",
      };
    });
  }

  const labels = labelsFor(flow.options, answers[flow.id]);
  return [
    {
      label: flow.title,
      value: labels.length > 0 ? labels.join(", ") : "Not provided",
    },
  ];
}

export default defineToolkit({
  collect_intake: {
    type: "human",
    description:
      "Collect missing structured incident context from the Helpdesk user.",
    parameters: SerializableQuestionInputFlowSchema,
    render: ({ args, toolCallId, result, addResult }) => {
      const parsed = safeParseSerializableQuestionInputFlow({
        ...args,
        id:
          typeof args?.id === "string" && args.id.length > 0
            ? args.id
            : `intake-${toolCallId}`,
      });

      if (!parsed) return null;

      if (result !== undefined) {
        return (
          <QuestionFlow
            id={parsed.id}
            role="decision"
            choice={{
              title: "Incident details",
              summary: receiptSummary(parsed, result),
            }}
          />
        );
      }

      if ("steps" in parsed) {
        return (
          <QuestionFlow
            {...parsed}
            onComplete={(answers) => addResult(answers)}
          />
        );
      }

      return (
        <QuestionFlow
          {...parsed}
          onSelect={(optionIds) => addResult({ [parsed.id]: optionIds })}
        />
      );
    },
  },
});
