"""The call trace must record exceptions without keeping them (or their frames) alive."""
import gc
import json
import sys
import tempfile
import unittest
import weakref
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import l2_calltrace  # noqa: E402


class Resource:
    """Stands in for a pyodbc cursor with pending results."""


def l2_calltrace_probe_fails(resource):
    raise RuntimeError(f"audit failed for {type(resource).__name__}")


def l2_calltrace_probe_caller():
    resource = Resource()
    ref = weakref.ref(resource)
    try:
        l2_calltrace_probe_fails(resource)
    except RuntimeError:
        pass
    del resource
    return ref


class CallTraceTests(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def test_caught_exception_is_logged_but_not_retained(self):
        # Live 2026-09-23: holding the exception kept a failed cursor alive, the connection
        # stayed "busy with results", and every claim failed for ~50 minutes.
        with patch.dict("os.environ", {"L2_CALLTRACE_DIR": self.dir}), \
                patch.object(l2_calltrace, "_OWN", ("test_l2_calltrace",)):
            l2_calltrace._current = None
            sys.settrace(l2_calltrace._trace)
            try:
                ref = l2_calltrace_probe_caller()
            finally:
                sys.settrace(None)
        gc.collect()
        self.assertIsNone(ref(), "traced exception kept the failed resource alive")
        records = [json.loads(line) for f in Path(self.dir).glob("*.jsonl") for line in f.open()]
        failed = [r for r in records if r["fn"] == "l2_calltrace_probe_fails" and r["event"] == "exception"]
        self.assertEqual(failed[0]["error_type"], "RuntimeError")
        self.assertIn("audit failed for Resource", failed[0]["error"])

    def test_only_today_and_yesterday_are_kept(self):
        for name in ("2020-01-01.jsonl", "2020-01-02.jsonl"):
            (Path(self.dir) / name).write_text("{}\n")
        with patch.dict("os.environ", {"L2_CALLTRACE_DIR": self.dir}):
            l2_calltrace._current = None
            l2_calltrace._path()
        self.assertEqual(list(Path(self.dir).glob("2020-*.jsonl")), [])


if __name__ == "__main__":
    unittest.main()
