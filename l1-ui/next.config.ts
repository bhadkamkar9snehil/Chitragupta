import type { NextConfig } from "next";

// The dev server blocks script requests from other origins; allow Tailscale devices (phones) to test it.
// Production is a static export served by the API on one origin (see docs/plans/no-hermes-architecture.md, D5).
const config: NextConfig = { output: "export", devIndicators: false, allowedDevOrigins: ["100.*.*.*", "*.ts.net"] };

export default config;
