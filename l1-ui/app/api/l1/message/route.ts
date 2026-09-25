import { NextResponse } from "next/server";
import {
  L1MessageRequestSchema,
  L1MessageResponseSchema,
} from "@/lib/l1-contract";

export const runtime = "nodejs";

function upstreamMessagesUrl() {
  const value = process.env.CHITRAGUPTA_L1_MESSAGES_URL?.trim();
  if (!value) return null;

  try {
    return new URL(value);
  } catch {
    return null;
  }
}

export async function POST(request: Request) {
  const target = upstreamMessagesUrl();
  if (!target) {
    return NextResponse.json(
      {
        error:
          "CHITRAGUPTA_L1_MESSAGES_URL is missing or invalid on the L1 UI server.",
      },
      { status: 503 },
    );
  }

  const requestBody = await request.json().catch(() => null);
  const parsedRequest = L1MessageRequestSchema.safeParse(requestBody);
  if (!parsedRequest.success) {
    return NextResponse.json(
      { error: "Invalid L1 chat request." },
      { status: 400 },
    );
  }

  const headers = new Headers({ "Content-Type": "application/json" });
  const token = process.env.CHITRAGUPTA_L1_API_TOKEN?.trim();
  if (token) headers.set("Authorization", `Bearer ${token}`);

  let upstream: Response;
  try {
    upstream = await fetch(target, {
      method: "POST",
      headers,
      body: JSON.stringify(parsedRequest.data),
      cache: "no-store",
      signal: request.signal,
    });
  } catch {
    return NextResponse.json(
      { error: "Chitragupta L1 is temporarily unavailable." },
      { status: 502 },
    );
  }

  if (!upstream.ok) {
    return NextResponse.json(
      {
        error: "Chitragupta L1 could not complete the request.",
        upstreamStatus: upstream.status,
      },
      { status: 502 },
    );
  }

  const responseBody = await upstream.json().catch(() => null);
  const parsedResponse = L1MessageResponseSchema.safeParse(responseBody);
  if (!parsedResponse.success) {
    return NextResponse.json(
      { error: "Chitragupta L1 returned an invalid response." },
      { status: 502 },
    );
  }

  return NextResponse.json(parsedResponse.data);
}
