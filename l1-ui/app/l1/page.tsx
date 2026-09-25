import { L1RuntimeProvider } from "@/components/assistant-ui/l1-runtime-provider";
import { L1Thread } from "@/components/assistant-ui/l1-thread";

export default function L1Page() {
  return (
    <main className="h-dvh bg-background">
      <L1RuntimeProvider>
        <L1Thread />
      </L1RuntimeProvider>
    </main>
  );
}
