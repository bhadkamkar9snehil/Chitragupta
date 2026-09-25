// The browser talks only to this route; the L1 API (and every credential behind it) stays server-side.
// Bodies are piped, so chat turns stream through as server-sent events.
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const upstream = (process.env.L1_API_URL ?? "http://127.0.0.1:5116").replace(/\/$/, "");

async function forward(request: Request, { params }: { params: Promise<{ path: string[] }> }) {
  const { path } = await params;
  const url = `${upstream}/api/${path.map(encodeURIComponent).join("/")}${new URL(request.url).search}`;
  try {
    const res = await fetch(url, {
      method: request.method,
      headers: { "Content-Type": "application/json" },
      body: ["GET", "DELETE"].includes(request.method) ? undefined : await request.text(),
      cache: "no-store",
      signal: request.signal,
    });
    return new Response(res.body, {
      status: res.status,
      headers: {
        "Content-Type": res.headers.get("Content-Type") ?? "application/json",
        "Cache-Control": "no-store",
        "X-Accel-Buffering": "no",
      },
    });
  } catch {
    return Response.json({ error: "The Helpdesk service is unavailable." }, { status: 502 });
  }
}

export { forward as GET, forward as POST, forward as PUT, forward as PATCH, forward as DELETE };
