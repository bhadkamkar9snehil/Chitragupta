"use generative";

import { defineToolkit } from "@assistant-ui/react";
import {
  KnowledgeSources,
  L2QuestionSurface,
  L2ReplySurface,
  TicketCard,
} from "@/components/helpdesk/helpdesk-surfaces";
import { QuestionFlow } from "@/components/tool-ui/question-flow";
import {
  SerializableQuestionInputFlowSchema,
  safeParseSerializableQuestionInputFlow,
  type SerializableQuestionInputFlow,
} from "@/components/tool-ui/question-flow/schema";
import {
  KnowledgeSourcesResultSchema,
  L2QuestionAnswerResultSchema,
  L2QuestionPromptSchema,
  L2ReplySchema,
  TicketSnapshotSchema,
} from "@/lib/l1-contract";

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

  show_knowledge_sources: {
    type: "backend",
    description:
      "Show the approved governed knowledge sources that support an L1 answer.",
    render: ({ result }) => {
      const parsed = KnowledgeSourcesResultSchema.safeParse(result);
      if (!parsed.success) return null;
      return <KnowledgeSources sources={parsed.data.sources} />;
    },
  },

  show_ticket: {
    type: "backend",
    description:
      "Show the authoritative Helpdesk ticket snapshot returned by Chitragupta.",
    render: ({ result }) => {
      const parsed = TicketSnapshotSchema.safeParse(result);
      if (!parsed.success) return null;
      return <TicketCard ticket={parsed.data} />;
    },
  },

  show_l2_reply: {
    type: "backend",
    description:
      "Show a user-visible L2 publication for an existing Helpdesk ticket.",
    render: ({ result }) => {
      const parsed = L2ReplySchema.safeParse(result);
      if (!parsed.success) return null;
      return <L2ReplySurface reply={parsed.data} />;
    },
  },

  answer_l2_question: {
    type: "human",
    description:
      "Collect the requester's free-text answer to a specific L2 QUESTION.",
    parameters: L2QuestionPromptSchema,
    render: ({ args, result, addResult }) => {
      const parsedPrompt = L2QuestionPromptSchema.safeParse(args);
      if (!parsedPrompt.success) return null;

      const parsedAnswer =
        result === undefined
          ? null
          : L2QuestionAnswerResultSchema.safeParse(result);

      if (parsedAnswer && !parsedAnswer.success) return null;

      return (
        <L2QuestionSurface
          prompt={parsedPrompt.data}
          answer={parsedAnswer?.data}
          onSubmit={
            result === undefined
              ? async (answer) => {
                  await addResult(answer);
                }
              : undefined
          }
        />
      );
    },
  },
});
