#!/usr/bin/env python3
"""Public facade for harness-owned deterministic L2 context delivery."""
from l2_context_delivery_base import *
from l2_context_delivery_assembly import *
from l2_context_delivery_receipts import *

# Preserve a single patchable retriever alias for callers/tests.
import l2_context_delivery_base as _base
import l2_context_delivery_assembly as _assembly
kb = _base.kb

def assemble_stage_context(*args, **kwargs):
    _assembly.kb = kb
    return _assembly.assemble_stage_context(*args, **kwargs)

def assemble_degraded_context(*args, **kwargs):
    return _assembly.assemble_degraded_context(*args, **kwargs)
