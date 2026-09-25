import type { NextConfig } from "next";

// The dev server blocks script requests from other origins; allow Tailscale devices (phones) to test it.
const config: NextConfig = { devIndicators: false, allowedDevOrigins: ["100.*.*.*", "*.ts.net"] };

export default config;
