#!/bin/bash
set -e
for p in l2-investigator l2-eval-investigator l2-gemma-verifier l2-qwen-verifier; do
  sed -i 's/^  default: qwopus3.5-9b-coder/  default: qwen\/qwen3.5-9b/' ~/.hermes/profiles/$p/config.yaml
  echo "$p:"; grep "default:" ~/.hermes/profiles/$p/config.yaml
done
