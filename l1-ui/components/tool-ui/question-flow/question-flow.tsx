"use client";

import {
  Fragment,
  useCallback,
  useMemo,
  useRef,
  useState,
} from "react";
import type { KeyboardEvent } from "react";
import { Check, ChevronLeft } from "lucide-react";
import { cn, Button, Separator } from "./_adapter";
import type {
  QuestionFlowOption,
  QuestionFlowProgressiveProps,
  QuestionFlowProps,
  QuestionFlowReceiptProps,
  QuestionFlowUpfrontProps,
} from "./schema";

function SelectionIndicator({
  mode,
  isSelected,
  disabled,
}: {
  mode: "single" | "multi";
  isSelected: boolean;
  disabled?: boolean;
}) {
  return (
    <div
      className={cn(
        "flex size-4 shrink-0 items-center justify-center border-2",
        "motion-safe:transition-colors motion-safe:duration-200",
        mode === "single" ? "rounded-full" : "rounded",
        isSelected &&
          "border-primary bg-primary text-primary-foreground",
        !isSelected && "border-muted-foreground/50",
        disabled && "opacity-50",
      )}
    >
      {mode === "multi" && isSelected ? (
        <Check className="size-3" strokeWidth={3} />
      ) : null}
      {mode === "single" && isSelected ? (
        <span className="size-2 rounded-full bg-current" />
      ) : null}
    </div>
  );
}

function ProgressBar({ current, total }: { current: number; total: number }) {
  return (
    <div
      className="flex h-1.5 gap-1"
      role="progressbar"
      aria-label="Question progress"
      aria-valuenow={current}
      aria-valuemin={1}
      aria-valuemax={total}
    >
      {Array.from({ length: total }).map((_, index) => (
        <div
          key={index}
          className="relative flex-1 overflow-hidden rounded-full bg-muted"
        >
          <div
            className={cn(
              "absolute inset-0 origin-left rounded-full bg-primary motion-safe:transition-transform",
              index < current ? "scale-x-100" : "scale-x-0",
            )}
          />
        </div>
      ))}
    </div>
  );
}

function OptionList({
  options,
  selectedIds,
  selectionMode,
  onToggle,
  ariaLabel,
  disabled,
}: {
  options: QuestionFlowOption[];
  selectedIds: Set<string>;
  selectionMode: "single" | "multi";
  onToggle: (id: string) => void;
  ariaLabel: string;
  disabled?: boolean;
}) {
  const optionRefs = useRef<Array<HTMLButtonElement | null>>([]);
  const firstEnabled = options.findIndex((option) => !option.disabled);
  const [activeIndex, setActiveIndex] = useState(
    firstEnabled >= 0 ? firstEnabled : 0,
  );

  const focusEnabled = useCallback(
    (start: number, direction: 1 | -1) => {
      if (options.length === 0) return;
      for (let offset = 1; offset <= options.length; offset += 1) {
        const index =
          (start + direction * offset + options.length) % options.length;
        if (!options[index]?.disabled) {
          setActiveIndex(index);
          optionRefs.current[index]?.focus();
          return;
        }
      }
    },
    [options],
  );

  const onKeyDown = useCallback(
    (event: KeyboardEvent<HTMLDivElement>) => {
      if (disabled || options.length === 0) return;
      if (event.key === "ArrowDown") {
        event.preventDefault();
        focusEnabled(activeIndex, 1);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        focusEnabled(activeIndex, -1);
      } else if (event.key === "Home") {
        event.preventDefault();
        const index = options.findIndex((option) => !option.disabled);
        if (index >= 0) {
          setActiveIndex(index);
          optionRefs.current[index]?.focus();
        }
      } else if (event.key === "End") {
        event.preventDefault();
        for (let index = options.length - 1; index >= 0; index -= 1) {
          if (!options[index]?.disabled) {
            setActiveIndex(index);
            optionRefs.current[index]?.focus();
            break;
          }
        }
      }
    },
    [activeIndex, disabled, focusEnabled, options],
  );

  return (
    <div
      className="flex flex-col"
      role="listbox"
      aria-label={ariaLabel}
      aria-multiselectable={selectionMode === "multi"}
      onKeyDown={onKeyDown}
    >
      {options.map((option, index) => {
        const selected = selectedIds.has(option.id);
        return (
          <Fragment key={option.id}>
            {index > 0 ? <Separator /> : null}
            <Button
              ref={(element) => {
                optionRefs.current[index] = element;
              }}
              type="button"
              variant="ghost"
              size="lg"
              role="option"
              aria-selected={selected}
              disabled={disabled || option.disabled}
              tabIndex={index === activeIndex ? 0 : -1}
              onFocus={() => setActiveIndex(index)}
              onClick={() => onToggle(option.id)}
              className="h-auto min-h-12 w-full justify-start rounded-none px-1 py-3 text-left text-base md:text-sm"
            >
              <span className="flex items-start gap-3">
                <span className="flex h-6 items-center">
                  <SelectionIndicator
                    mode={selectionMode}
                    isSelected={selected}
                    disabled={disabled || option.disabled}
                  />
                </span>
                <span className="flex flex-col">
                  <span className="leading-6">{option.label}</span>
                  {option.description ? (
                    <span className="text-sm font-normal text-muted-foreground">
                      {option.description}
                    </span>
                  ) : null}
                </span>
              </span>
            </Button>
          </Fragment>
        );
      })}
    </div>
  );
}

function StepCard({
  id,
  step,
  totalSteps,
  title,
  description,
  options,
  selectionMode,
  selectedIds,
  onToggle,
  onBack,
  onNext,
  isLastStep,
  className,
}: {
  id: string;
  step: number;
  totalSteps?: number;
  title: string;
  description?: string;
  options: QuestionFlowOption[];
  selectionMode: "single" | "multi";
  selectedIds: Set<string>;
  onToggle: (id: string) => void;
  onBack?: () => void;
  onNext: () => void;
  isLastStep: boolean;
  className?: string;
}) {
  const canProceed = selectedIds.size > 0;
  return (
    <div
      className={cn(
        "@container/question-flow flex w-full min-w-0 max-w-lg flex-col text-foreground",
        className,
      )}
      data-slot="question-flow"
      data-tool-ui-id={id}
      role="form"
      aria-label={title}
    >
      <div className="flex w-full flex-col gap-4 rounded-xl border bg-card p-5">
        <div className="flex flex-col gap-2">
          <span className="text-xs font-medium uppercase tracking-wide text-muted-foreground">
            {totalSteps ? `Step ${step} of ${totalSteps}` : `Step ${step}`}
          </span>
          {totalSteps ? <ProgressBar current={step} total={totalSteps} /> : null}
          <div className="mt-1">
            <h3 className="text-base font-semibold">{title}</h3>
            {description ? (
              <p className="mt-1 text-sm text-muted-foreground">{description}</p>
            ) : null}
          </div>
        </div>

        <OptionList
          key={`${id}-${step}`}
          options={options}
          selectedIds={selectedIds}
          selectionMode={selectionMode}
          onToggle={onToggle}
          ariaLabel={title}
        />

        <div className="flex items-center justify-between pt-1">
          {onBack ? (
            <Button type="button" variant="ghost" onClick={onBack}>
              <ChevronLeft className="size-4" />
              Back
            </Button>
          ) : (
            <span />
          )}
          <Button type="button" onClick={onNext} disabled={!canProceed}>
            {isLastStep ? "Continue" : "Next"}
          </Button>
        </div>
      </div>
    </div>
  );
}

function QuestionFlowReceipt({
  id,
  choice,
  className,
}: QuestionFlowReceiptProps) {
  return (
    <div
      className={cn("w-full max-w-lg", className)}
      data-slot="question-flow"
      data-tool-ui-id={id}
      data-receipt="true"
      role="status"
      aria-label={choice.title}
    >
      <div className="rounded-xl border bg-card p-5">
        <div className="flex items-center justify-between gap-3">
          <span className="font-medium">{choice.title}</span>
          <span className="flex items-center gap-1.5 text-xs font-medium text-primary">
            <Check className="size-3.5" />
            Added
          </span>
        </div>
        <div className="mt-3 flex flex-col">
          {choice.summary.map((item, index) => (
            <Fragment key={`${item.label}-${index}`}>
              {index > 0 ? <Separator className="my-2" /> : null}
              <div className="flex flex-col gap-0.5 text-sm">
                <span className="text-muted-foreground">{item.label}</span>
                <span className="break-words font-medium">{item.value}</span>
              </div>
            </Fragment>
          ))}
        </div>
      </div>
    </div>
  );
}

function QuestionFlowProgressive({
  id,
  step,
  title,
  description,
  options,
  selectionMode = "single",
  defaultValue,
  onSelect,
  onBack,
  className,
}: QuestionFlowProgressiveProps) {
  const [selectedIds, setSelectedIds] = useState(
    () => new Set(defaultValue ?? []),
  );

  const toggle = useCallback(
    (optionId: string) => {
      setSelectedIds((current) => {
        const next = new Set(current);
        if (selectionMode === "single") {
          next.clear();
          next.add(optionId);
        } else if (next.has(optionId)) {
          next.delete(optionId);
        } else {
          next.add(optionId);
        }
        return next;
      });
    },
    [selectionMode],
  );

  return (
    <StepCard
      id={id}
      step={step}
      title={title}
      description={description}
      options={options}
      selectionMode={selectionMode}
      selectedIds={selectedIds}
      onToggle={toggle}
      onBack={step > 1 ? onBack : undefined}
      onNext={() => onSelect?.(Array.from(selectedIds))}
      isLastStep
      className={className}
    />
  );
}

function QuestionFlowUpfront({
  id,
  steps,
  onStepChange,
  onComplete,
  className,
}: QuestionFlowUpfrontProps) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string[]>>({});

  const currentStep = steps[currentStepIndex];
  const currentSelection = useMemo(
    () => new Set(answers[currentStep.id] ?? []),
    [answers, currentStep.id],
  );

  const toggle = useCallback(
    (optionId: string) => {
      setAnswers((current) => {
        const existing = current[currentStep.id] ?? [];
        const selectionMode = currentStep.selectionMode ?? "single";
        const next =
          selectionMode === "single"
            ? [optionId]
            : existing.includes(optionId)
              ? existing.filter((id) => id !== optionId)
              : [...existing, optionId];
        return { ...current, [currentStep.id]: next };
      });
    },
    [currentStep.id, currentStep.selectionMode],
  );

  const goBack = useCallback(() => {
    const nextIndex = Math.max(0, currentStepIndex - 1);
    setCurrentStepIndex(nextIndex);
    onStepChange?.(steps[nextIndex].id);
  }, [currentStepIndex, onStepChange, steps]);

  const goNext = useCallback(() => {
    if (currentSelection.size === 0) return;
    if (currentStepIndex === steps.length - 1) {
      onComplete?.(answers);
      return;
    }
    const nextIndex = currentStepIndex + 1;
    setCurrentStepIndex(nextIndex);
    onStepChange?.(steps[nextIndex].id);
  }, [
    answers,
    currentSelection.size,
    currentStepIndex,
    onComplete,
    onStepChange,
    steps,
  ]);

  return (
    <StepCard
      id={id}
      step={currentStepIndex + 1}
      totalSteps={steps.length}
      title={currentStep.title}
      description={currentStep.description}
      options={currentStep.options}
      selectionMode={currentStep.selectionMode ?? "single"}
      selectedIds={currentSelection}
      onToggle={toggle}
      onBack={currentStepIndex > 0 ? goBack : undefined}
      onNext={goNext}
      isLastStep={currentStepIndex === steps.length - 1}
      className={className}
    />
  );
}

export function QuestionFlow(props: QuestionFlowProps) {
  if ("choice" in props && props.choice !== undefined) {
    return <QuestionFlowReceipt {...props} />;
  }
  if ("steps" in props && props.steps !== undefined) {
    return <QuestionFlowUpfront {...props} />;
  }
  return <QuestionFlowProgressive {...props} />;
}
