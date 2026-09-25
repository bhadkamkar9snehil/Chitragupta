import { clsx, type ClassValue } from "clsx";
import { extendTailwindMerge } from "tailwind-merge";

// The app's own type scale (globals.css @theme) must merge as font sizes, not colours.
const twMerge = extendTailwindMerge({
  extend: { theme: { text: ["2xs", "meta", "body", "title", "heading", "display"] } },
});

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
