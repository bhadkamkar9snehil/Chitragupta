import { NextResponse } from "next/server";
import {
  L1MessageRequestSchema,
  L1MessageResponseSchema,
} from "@/lib/l1-contract";

export const runtime = "nodejs";

const MAX_REQUEST_BYTES = 512 * 1024;
const MAX_RESPONSE_BYTES = 512 * 1024;

function byteLength(value: string) {
  return new TextEncoder().encode(value).byteLength;
}

function upstreamMessagesUrl() {
  const value = process.env.CHITRAGUPTA_L1_MESSAGES_URL?.trim();
  if (!value) return null;

  try {
    return new URL(value);
  } catch {
    return null;
  }
}

function jsonError(error: string, status: number) {
  return NextResponse.json({ error }, { status });
}

export async function POST(request: Request) {
  const target = upstreamMessagesUrl();
  if (!target) {
    return jsonError("The Helpdesk service is not configured.", 503);
  }

  const declaredLength = Number(request.headers.get("content-length") ?? "0");
  if (
    Number.isFinite(declaredLength) &&
    declaredLength > MAX_REQUEST_BYTES
  ) {
    return jsonError("The Helpdesk request is too large.", 413);
  }

  const rawRequest = await request.text().catch(() => "");
  if (!rawRequest || byteLength(rawRequest) > MAX_REQUEST_BYTES) {
    return jsonError(
      rawRequest ? "The Helpdesk request is too large." : "Invalid Helpdesk request.",
      rawRequest ? 413 : 400,
    );
  }

  let requestBody: unknown;
  try {
    requestBody = JSON.parse(rawRequest);
  } catch {
    return jsonError("Invalid Helpdesk request.", 400);
  }

  const parsedRequest = L1MessageRequestSchema.safeParse(requestBody);
  if (!parsedRequest.success) {
    return jsonError("Invalid Helpdesk request.", 400);
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
    return jsonError("The Helpdesk service is temporarily unavailable.", 502);
  }

  if (!upstream.ok) {
    return jsonError("The Helpdesk service could not complete the request.", 502);
  }

  const declaredResponseLength = Number(
    upstream.headers.get("content-length") ?? "0",
  );
  if (
    Number.isFinite(declaredResponseLength) &&
    declaredResponseLength > MAX_RESPONSE_BYTES
  ) {
    return jsonError("The Helpdesk service returned an invalid response.", 502);
  }

  const rawResponse = await upstream.text().catch(() => "");
  if (!rawResponse || byteLength(rawResponse) > MAX_RESPONSE_BYTES) {
    return jsonError("The Helpdesk service returned an invalid response.", 502);
  }

  let responseBody: unknown;
  try {
    responseBody = JSON.parse(rawResponse);
  } catch {
    return jsonError("The Helpdesk service returned an invalid response.", 502);
  }

  const parsedResponse = L1MessageResponseSchema.safeParse(responseBody);
  if (!parsedResponse.success) {
    return jsonError("The Helpdesk service returned an invalid response.", 502);
  }

  return NextResponse.json(parsedResponse.data);
}
