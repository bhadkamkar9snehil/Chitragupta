import { plugin as shadcn } from "@shadcn/lint";
import tsParser from "@typescript-eslint/parser";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    ignores: [".next/**", "node_modules/**"],
  },
  {
    files: ["**/*.{js,jsx,ts,tsx}"],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaFeatures: { jsx: true },
        sourceType: "module",
      },
    },
    plugins: { shadcn },
    settings: {
      shadcn: {
        ui: "@/components/ui",
        note: "L1 UI uses shadcn/ui and copied Tool UI components. Keep app code token-based.",
      },
    },
    rules: {
      "shadcn/no-restyle": ["error", { allow: ["layout"] }],
      "shadcn/no-raw-colors": "error",
      "shadcn/no-arbitrary-values": "error",
      "shadcn/no-inline-styles": "error",
      "shadcn/require-static-classes": "error",
      "shadcn/no-unknown-classes": "error",
    },
  },
  {
    files: ["components/ui/**", "components/tool-ui/**"],
    rules: {
      "shadcn/no-restyle": "off",
      "shadcn/no-arbitrary-values": "off",
      "shadcn/no-inline-styles": "off",
      "shadcn/require-static-classes": "off",
      "shadcn/no-unknown-classes": "off",
    },
  },
]);
