"use client";

import * as React from "react";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import * as MenuPrimitive from "@radix-ui/react-dropdown-menu";
import * as TooltipPrimitive from "@radix-ui/react-tooltip";
import * as SwitchPrimitive from "@radix-ui/react-switch";
import { Search, X } from "lucide-react";
import type { Tone } from "@/lib/api";
import { initials } from "@/lib/format";
import { cn } from "@/lib/utils";

export function Input({ className, ...props }: React.ComponentProps<"input">) {
  return (
    <input
      className={cn(
        "h-10 w-full rounded-md border bg-surface px-3 text-base outline-none placeholder:text-subtle-foreground focus:border-border-strong focus:ring-2 focus:ring-ring sm:text-sm",
        className,
      )}
      {...props}
    />
  );
}

export function SearchInput({ className, size = "default", ...props }: Omit<React.ComponentProps<"input">, "size"> & { size?: "default" | "lg" }) {
  return (
    <div className={cn("relative", className)}>
      <Search className="pointer-events-none absolute left-3 top-1/2 size-4 -translate-y-1/2 text-subtle-foreground" aria-hidden />
      <input
        type="search"
        className={cn(
          "w-full rounded-md border bg-surface pl-9 pr-3 text-base outline-none placeholder:text-subtle-foreground focus:border-border-strong focus:ring-2 focus:ring-ring sm:text-sm",
          size === "lg" ? "h-11" : "h-9",
        )}
        {...props}
      />
    </div>
  );
}

export function Textarea({ className, ...props }: React.ComponentProps<"textarea">) {
  return (
    <textarea
      className={cn(
        "w-full resize-y rounded-md border bg-surface px-3 py-2.5 text-base leading-relaxed outline-none placeholder:text-subtle-foreground focus:border-border-strong focus:ring-2 focus:ring-ring sm:text-sm",
        className,
      )}
      {...props}
    />
  );
}

export function Label({ className, ...props }: React.ComponentProps<"label">) {
  return <label className={cn("text-meta font-medium text-foreground", className)} {...props} />;
}

const TONE: Record<Tone, string> = {
  attention: "bg-warning-soft text-warning [&>i]:bg-warning",
  progress: "bg-info-soft text-info [&>i]:bg-info",
  pending: "bg-surface-3 text-muted-foreground [&>i]:bg-subtle-foreground",
  done: "bg-success-soft text-success [&>i]:bg-success",
};

export function StatePill({ tone, children, className }: { tone: Tone; children: React.ReactNode; className?: string }) {
  return (
    <span className={cn("inline-flex h-6 items-center gap-1.5 whitespace-nowrap rounded-full px-2.5 text-xs font-medium", TONE[tone], className)}>
      <i className={cn("size-1.5 rounded-full", tone === "attention" && "motion-safe:animate-pulse")} aria-hidden />
      {children}
    </span>
  );
}

export function Tag({ children, className, mono, variant = "default" }: { children: React.ReactNode; className?: string; mono?: boolean; variant?: "default" | "error" }) {
  return <span className={cn("inline-flex h-6 items-center rounded-md border bg-surface-2 px-2 text-xs text-muted-foreground", variant === "error" && "text-destructive", mono && "font-mono", className)}>{children}</span>;
}

export function Avatar({ name, className }: { name: string; className?: string }) {
  // Stable hue per person so lists scan quickly.
  const hue = [...name].reduce((h, c) => (h * 31 + c.charCodeAt(0)) % 360, 7);
  return (
    <span
      aria-hidden
      data-hue={hue}
      className={cn("grid size-8 shrink-0 place-items-center rounded-full text-2xs font-semibold tracking-wide text-white", className)}
      ref={(el) => {
        el?.style.setProperty("background", `oklch(0.58 0.11 ${hue})`);
      }}
    >
      {initials(name)}
    </span>
  );
}

export function Kbd({ children }: { children: React.ReactNode }) {
  return <kbd className="inline-flex h-5 min-w-5 items-center justify-center rounded border bg-surface-2 px-1 font-mono text-2xs text-muted-foreground">{children}</kbd>;
}

export function Skeleton({ className }: { className?: string }) {
  return <div className={cn("rounded-md bg-surface-3 motion-safe:animate-pulse", className)} />;
}

export function Empty({ icon, title, children, className }: { icon: React.ReactNode; title: string; children?: React.ReactNode; className?: string }) {
  return (
    <div className={cn("flex flex-col items-center px-6 py-14 text-center", className)}>
      <div className="grid size-11 place-items-center rounded-xl border bg-surface text-muted-foreground shadow-lift">{icon}</div>
      <p className="mt-4 text-sm font-medium">{title}</p>
      {children && <div className="mt-1 max-w-xs text-sm text-muted-foreground">{children}</div>}
    </div>
  );
}

export function Switch({ className, ...props }: React.ComponentProps<typeof SwitchPrimitive.Root>) {
  return (
    <SwitchPrimitive.Root
      className={cn(
        "peer inline-flex h-6 w-10 shrink-0 cursor-pointer items-center rounded-full border border-transparent bg-surface-3 transition-colors data-[state=checked]:bg-primary",
        className,
      )}
      {...props}
    >
      <SwitchPrimitive.Thumb className="block size-5 translate-x-0.5 rounded-full bg-white shadow-lift transition-transform data-[state=checked]:translate-x-4" />
    </SwitchPrimitive.Root>
  );
}

export const TooltipProvider = TooltipPrimitive.Provider;

export function Tip({ label, children, side = "top" }: { label: string; children: React.ReactNode; side?: "top" | "bottom" | "left" | "right" }) {
  return (
    <TooltipPrimitive.Root delayDuration={300}>
      <TooltipPrimitive.Trigger asChild>{children}</TooltipPrimitive.Trigger>
      <TooltipPrimitive.Portal>
        <TooltipPrimitive.Content side={side} sideOffset={6} className="z-50 rounded-md bg-foreground px-2 py-1 text-xs text-background animate-fade">
          {label}
        </TooltipPrimitive.Content>
      </TooltipPrimitive.Portal>
    </TooltipPrimitive.Root>
  );
}

export const Menu = MenuPrimitive.Root;
export const MenuTrigger = MenuPrimitive.Trigger;

export function MenuContent({ className, ...props }: React.ComponentProps<typeof MenuPrimitive.Content>) {
  return (
    <MenuPrimitive.Portal>
      <MenuPrimitive.Content
        sideOffset={6}
        align="end"
        className={cn("z-50 min-w-44 rounded-lg border bg-surface p-1 shadow-pop animate-fade", className)}
        {...props}
      />
    </MenuPrimitive.Portal>
  );
}

export function MenuItem({ className, destructive, ...props }: React.ComponentProps<typeof MenuPrimitive.Item> & { destructive?: boolean }) {
  return (
    <MenuPrimitive.Item
      className={cn(
        "flex h-9 cursor-default select-none items-center gap-2 rounded-md px-2.5 text-sm outline-none data-[highlighted]:bg-surface-2 [&_svg]:size-4 [&_svg]:text-muted-foreground",
        destructive && "text-destructive [&_svg]:text-destructive",
        className,
      )}
      {...props}
    />
  );
}

export function MenuSeparator() {
  return <MenuPrimitive.Separator className="my-1 h-px bg-border" />;
}

export function Dialog({
  open,
  onOpenChange,
  title,
  description,
  children,
  className,
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  title: string;
  description?: string;
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay className="fixed inset-0 z-50 bg-black/40 animate-fade" />
        <DialogPrimitive.Content
          className={cn(
            "fixed left-1/2 top-1/2 z-50 w-[calc(100%-2rem)] max-w-md -translate-x-1/2 -translate-y-1/2 rounded-xl border bg-surface p-5 shadow-pop animate-rise",
            className,
          )}
        >
          <DialogPrimitive.Title className="text-base font-semibold">{title}</DialogPrimitive.Title>
          {description ? (
            <DialogPrimitive.Description className="mt-1 text-sm text-muted-foreground">{description}</DialogPrimitive.Description>
          ) : (
            <DialogPrimitive.Description className="sr-only">{title}</DialogPrimitive.Description>
          )}
          <div className="mt-4">{children}</div>
          <DialogPrimitive.Close className="absolute right-3 top-3 grid size-8 place-items-center rounded-md text-muted-foreground hover:bg-surface-2" aria-label="Close">
            <X className="size-4" />
          </DialogPrimitive.Close>
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  );
}
