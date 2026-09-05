#!/bin/bash
for p in l2-investigator l2-gemma-verifier l2-qwen-verifier l2-eval-investigator; do
  echo "=== $p ==="
  hermes -p "$p" gateway restart
done
