// The browser talks only to this route; the L1 API (and every credential behind it) stays server-side.
import { NextResponse } from "next/server";

export const runtime = "nodejs";

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
      signal: AbortSignal.timeout(240_000),
    });
    return new NextResponse(await res.text(), {
      status: res.status,
      headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
    });
  } catch {
    return NextResponse.json({ error: "The Helpdesk service is unavailable." }, { status: 502 });
  }
}

export { forward as GET, forward as POST, forward as PATCH, forward as DELETE };
