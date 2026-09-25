import { NextResponse } from "next/server";
import {
  L1MessageRequestSchema,
  L1MessageResponseSchema,
} from "@/lib/l1-contract";

export const runtime = "nodejs";

const MAX_REQUEST_BYTES = 512 * 1024;
const MAX_RESPONSE_BYTES = 512 * 1024;
const UPSTREAM_TIMEOUT_MS = 120_000;

class BodyTooLargeError extends Error {}

async function readBoundedText(
  body: ReadableStream<Uint8Array> | null,
  maxBytes: number,
) {
  if (!body) return "";

  const reader = body.getReader();
  const decoder = new TextDecoder("utf-8", { fatal: true });
  let totalBytes = 0;
  let text = "";

  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      if (!value) continue;

      totalBytes += value.byteLength;
      if (totalBytes > maxBytes) {
        await reader.cancel().catch(() => undefined);
        throw new BodyTooLargeError();
      }

      text += decoder.decode(value, { stream: true });
    }

    text += decoder.decode();
    return text;
  } finally {
    reader.releaseLock();
  }
}

function upstreamMessagesUrl() {
  const value = process.env.CHITRAGUPTA_L1_MESSAGES_URL?.trim();
  if (!value) return null;

  try {
    const url = new URL(value);
    if (!["http:", "https:"].includes(url.protocol)) return null;
    if (url.username || url.password) return null;
    return url;
  } catch {
    return null;
  }
}

const RESPONSE_HEADERS = {
  "Cache-Control": "no-store",
} as const;

function jsonError(error: string, status: number) {
  return NextResponse.json({ error }, { status, headers: RESPONSE_HEADERS });
}

function declaredBodyTooLarge(value: string | null, maxBytes: number) {
  if (!value) return false;
  const length = Number(value);
  return Number.isFinite(length) && length > maxBytes;
}

export async function POST(request: Request) {
  const target = upstreamMessagesUrl();
  if (!target) {
    return jsonError("The Helpdesk service is not configured.", 503);
  }

  const contentType = request.headers.get("content-type")?.toLowerCase();
  if (!contentType?.startsWith("application/json")) {
    return jsonError("Unsupported Helpdesk request.", 415);
  }

  if (
    declaredBodyTooLarge(
      request.headers.get("content-length"),
      MAX_REQUEST_BYTES,
    )
  ) {
    return jsonError("The Helpdesk request is too large.", 413);
  }

  let rawRequest: string;
  try {
    rawRequest = await readBoundedText(request.body, MAX_REQUEST_BYTES);
  } catch (error) {
    return error instanceof BodyTooLargeError
      ? jsonError("The Helpdesk request is too large.", 413)
      : jsonError("Invalid Helpdesk request.", 400);
  }

  if (!rawRequest) {
    return jsonError("Invalid Helpdesk request.", 400);
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

  const headers = new Headers({
    Accept: "application/json",
    "Content-Type": "application/json",
  });
  const token = process.env.CHITRAGUPTA_L1_API_TOKEN?.trim();
  if (token) headers.set("Authorization", `Bearer ${token}`);

  let upstream: Response;
  try {
    upstream = await fetch(target, {
      method: "POST",
      headers,
      body: JSON.stringify(parsedRequest.data),
      cache: "no-store",
      signal: AbortSignal.any([
        request.signal,
        AbortSignal.timeout(UPSTREAM_TIMEOUT_MS),
      ]),
    });
  } catch {
    return jsonError("The Helpdesk service is temporarily unavailable.", 502);
  }

  if (!upstream.ok) {
    return jsonError("The Helpdesk service could not complete the request.", 502);
  }

  if (
    declaredBodyTooLarge(
      upstream.headers.get("content-length"),
      MAX_RESPONSE_BYTES,
    )
  ) {
    return jsonError("The Helpdesk service returned an invalid response.", 502);
  }

  let rawResponse: string;
  try {
    rawResponse = await readBoundedText(upstream.body, MAX_RESPONSE_BYTES);
  } catch {
    return jsonError("The Helpdesk service returned an invalid response.", 502);
  }

  if (!rawResponse) {
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

  return NextResponse.json(parsedResponse.data, {
    headers: RESPONSE_HEADERS,
  });
}
