import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

export const buttonVariants = cva(
  "inline-flex shrink-0 select-none items-center justify-center gap-2 whitespace-nowrap rounded-lg text-sm font-medium outline-none disabled:pointer-events-none disabled:opacity-60 focus-visible:ring-2 focus-visible:ring-ring motion-safe:transition-[background-color,color,box-shadow,transform] motion-safe:active:scale-[0.98] [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
  {
    variants: {
      variant: {
        default: "bg-foreground text-background hover:opacity-90 disabled:bg-surface-3 disabled:text-subtle-foreground",
        soft: "border border-signal/40 bg-signal-soft text-signal hover:border-signal",
        outline: "border border-border-strong bg-canvas text-foreground hover:bg-surface-3",
        ghost: "text-muted-foreground hover:bg-surface-2 hover:text-foreground",
        destructive: "bg-destructive-soft text-destructive hover:brightness-110",
        link: "h-auto px-0 text-signal underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4",
        sm: "h-10 rounded-lg px-3 text-meta sm:h-8",
        lg: "h-11 px-5",
        icon: "size-10",
        "icon-sm": "size-10 sm:size-8",
      },
    },
    defaultVariants: { variant: "default", size: "default" },
  },
);

export function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> & VariantProps<typeof buttonVariants> & { asChild?: boolean }) {
  const Comp = asChild ? Slot : "button";
  return <Comp data-slot="button" className={cn(buttonVariants({ variant, size, className }))} {...props} />;
}
