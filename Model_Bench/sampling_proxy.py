#!/usr/bin/env python3
"""Sampling-injection proxy for LM Studio.

Problem this fixes: LM Studio's OpenAI-compatible server only applies
sampling parameters (temperature, repeat_penalty, etc.) from whatever
preset is currently GUI-selected for the loaded model. Hermes itself sends
no sampling overrides in its requests (confirmed by reading hermes_cli's
source -- no temperature/repeat_penalty/top_p field anywhere), so every
`hermes -z` call silently runs on whatever the GUI happens to have selected
-- which has already drifted back to "no preset" once in this project
despite being fixed. That's not something a one-time GUI click reliably
prevents.

Fix: sit between Hermes and LM Studio. Forward everything, but for
/v1/chat/completions and /v1/completions requests, inject the known-good
sampling fields (see Knowledge/70_local_inference_setup.md,
"OptimisedPreset 1" -- the real fix for a genuine repetition-loop outage on
qwen3.5-9b: repeat_penalty=1.5, min_p disabled, top_k=20) UNLESS the caller
already specified that field, so a deliberate per-call override (e.g. from
hermes_cli_bench.py testing a different preset) still wins.

Run on the desktop, pointed at the real LM Studio server:

    python sampling_proxy.py --upstream http://localhost:1235 --port 1236

Then point the profile's config.yaml base_url at
http://100.111.69.102:1236/v1 instead of :1235/v1 -- everything else about
the setup (model identifier, provider name) stays the same, this is a pure
passthrough for every other endpoint (/v1/models, /v1/embeddings, etc).
"""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import urllib.request
import urllib.error

# The verified fix from Knowledge/70_local_inference_setup.md's
# "OptimisedPreset 1" -- do not change without updating that doc too.
DEFAULT_SAMPLING = {
    "repeat_penalty": 1.5,
    "min_p": 0,
    "top_k": 20,
}

INJECT_PATHS = {"/v1/chat/completions", "/v1/completions"}


class ProxyHandler(BaseHTTPRequestHandler):
    upstream = "http://localhost:1235"
    sampling = DEFAULT_SAMPLING

    def log_message(self, fmt, *args):
        print(f"[proxy] {self.address_string()} {fmt % args}")

    def _forward(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        body = self.rfile.read(length) if length else b""

        if self.path in INJECT_PATHS and body:
            try:
                payload = json.loads(body)
                injected = []
                for k, v in self.sampling.items():
                    if k not in payload:
                        payload[k] = v
                        injected.append(k)
                if injected:
                    print(f"[proxy] injected {injected} into {self.path}")
                body = json.dumps(payload).encode("utf-8")
            except (json.JSONDecodeError, TypeError):
                pass  # not JSON, or not a dict -- forward as-is

        url = self.upstream.rstrip("/") + self.path
        req = urllib.request.Request(url, data=body or None, method=self.command)
        for h, v in self.headers.items():
            if h.lower() not in ("host", "content-length"):
                req.add_header(h, v)
        if body:
            req.add_header("Content-Length", str(len(body)))

        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                self.send_response(resp.status)
                for h, v in resp.getheaders():
                    if h.lower() not in ("transfer-encoding", "connection"):
                        self.send_header(h, v)
                self.end_headers()
                self.wfile.write(resp.read())
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_GET(self):
        self._forward()

    def do_POST(self):
        self._forward()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--upstream", default="http://localhost:1235")
    ap.add_argument("--port", type=int, default=1236)
    args = ap.parse_args()

    ProxyHandler.upstream = args.upstream
    server = ThreadingHTTPServer(("0.0.0.0", args.port), ProxyHandler)
    print(f"Sampling proxy on 0.0.0.0:{args.port} -> {args.upstream}")
    print(f"Always-injected sampling fields (unless caller overrides): {DEFAULT_SAMPLING}")
    print("Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
