#!/usr/bin/env python3
"""Public facade for governed deterministic Chitragupta L2 retrieval."""
from kb_retrieval_routing import *
from kb_retrieval_base import *
from kb_retrieval_corpus import *
from kb_retrieval_cli import *
import kb_retrieval_routing as _routing
import kb_retrieval_base as _base
import kb_retrieval_corpus as _corpus

# Keep monkey-patching at this public boundary effective for tests/diagnostics.
MANIFEST_PATH = _routing.MANIFEST_PATH
DEPLOYED_MANIFEST_PATH = _routing.DEPLOYED_MANIFEST_PATH
gbrain_scope_search = _base.gbrain_scope_search

def load_manifest(path=None):
    _routing.MANIFEST_PATH = MANIFEST_PATH
    _routing.DEPLOYED_MANIFEST_PATH = DEPLOYED_MANIFEST_PATH
    return _routing.load_manifest(path)

def retrieve(*args, **kwargs):
    _corpus.gbrain_scope_search = gbrain_scope_search
    _corpus.load_manifest = load_manifest
    return _corpus.retrieve(*args, **kwargs)

if __name__ == "__main__":
    raise SystemExit(main())
