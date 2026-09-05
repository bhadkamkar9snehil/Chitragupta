#!/bin/bash
# Install + run Qdrant as a systemd user service for Hermes mem0.
#
# Why a server instead of mem0's default embedded/local-path Qdrant:
# embedded mode is SINGLE-PROCESS (a file lock). Kanban workers are separate
# OS processes from their gateway, so with embedded Qdrant every worker's
# mem0 call failed with
#   "Storage folder ... already accessed by another instance of Qdrant client"
# Confirmed from a live worker log: the model DID call mem0_search and got
# that error. Memory was empty for the project's entire life not because
# nothing wrote to it, but because every read and write failed on that lock.
#
# A server is multi-process safe by construction, and lets every profile
# share ONE collection -- restoring the cross-profile learning that the
# earlier per-profile-path workaround had traded away.
#
# No Docker: this is the plain static musl binary from the official release.
#
# Idempotent -- safe to re-run after a `hermes update` or on a fresh box.
set -euo pipefail

DEST="$HOME/.hermes/qdrant"
PORT_HTTP=6333
PORT_GRPC=6334

mkdir -p "$DEST/storage" "$DEST/snapshots" "$HOME/.config/systemd/user"

if [ ! -x "$DEST/qdrant" ]; then
  VER="$(curl -s https://api.github.com/repos/qdrant/qdrant/releases/latest \
        | grep -oP '"tag_name":\s*"\K[^"]+')"
  echo "installing qdrant $VER"
  curl -sL "https://github.com/qdrant/qdrant/releases/download/${VER}/qdrant-x86_64-unknown-linux-musl.tar.gz" \
       -o "$DEST/qdrant.tar.gz"
  tar xzf "$DEST/qdrant.tar.gz" -C "$DEST"
  rm -f "$DEST/qdrant.tar.gz"
  chmod +x "$DEST/qdrant"
else
  echo "qdrant already installed: $("$DEST/qdrant" --version)"
fi

cat > "$HOME/.config/systemd/user/qdrant.service" <<EOF
[Unit]
Description=Qdrant vector store for Hermes mem0 (multi-process safe)
After=network.target

[Service]
Type=simple
Environment=QDRANT__STORAGE__STORAGE_PATH=%h/.hermes/qdrant/storage
Environment=QDRANT__STORAGE__SNAPSHOTS_PATH=%h/.hermes/qdrant/snapshots
Environment=QDRANT__SERVICE__HTTP_PORT=${PORT_HTTP}
Environment=QDRANT__SERVICE__GRPC_PORT=${PORT_GRPC}
Environment=QDRANT__TELEMETRY_DISABLED=true
ExecStart=%h/.hermes/qdrant/qdrant
WorkingDirectory=%h/.hermes/qdrant
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable --now qdrant.service
# Survive logout (WSL: pair with the existing keep-alive session).
loginctl enable-linger "$USER" 2>/dev/null || true

echo "waiting for qdrant to become healthy..."
for _ in $(seq 1 20); do
  if curl -sf "http://127.0.0.1:${PORT_HTTP}/healthz" >/dev/null 2>&1; then
    echo "qdrant healthy on ${PORT_HTTP}"
    exit 0
  fi
  sleep 1
done
echo "ERROR: qdrant did not become healthy in 20s" >&2
systemctl --user status qdrant.service --no-pager | head -20 >&2
exit 1
