import Markdown from "react-markdown";

// Replies arrive as light Markdown (bold, lists, code); render it, never raw HTML.
export function RichText({ children }: { children: string }) {
  return (
    <div className="space-y-3 break-words text-base leading-relaxed">
      <Markdown
        skipHtml
        components={{
          ul: (p) => <ul className="list-disc space-y-1 pl-5" {...p} />,
          ol: (p) => <ol className="list-decimal space-y-1 pl-5" {...p} />,
          strong: (p) => <strong className="font-semibold" {...p} />,
          code: (p) => <code className="rounded bg-muted px-1 py-0.5 font-mono text-sm" {...p} />,
          a: (p) => <a className="text-primary underline underline-offset-2" target="_blank" rel="noreferrer" {...p} />,
        }}
      >
        {children}
      </Markdown>
    </div>
  );
}
