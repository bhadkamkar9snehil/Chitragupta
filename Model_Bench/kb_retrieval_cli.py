#!/usr/bin/env python3
"""CLI/WSL transport for governed L2 retrieval."""
from __future__ import annotations
from kb_retrieval_base import *
from kb_retrieval_corpus import retrieve

def _wsl_path(path: Path) -> str:
    value = str(path.resolve()); m = re.match(r"^([A-Za-z]):\\(.*)$", value)
    return value.replace("\\", "/") if not m else f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92), '/')}"


def _proxy_to_wsl(args: argparse.Namespace) -> dict[str, Any] | None:
    if os.name != "nt" or args.wsl_inner: return None
    cmd = ["wsl", "-d", os.environ.get("CHITRAGUPTA_WSL_DISTRO", "Ubuntu"), "--", "python3", _wsl_path(Path(__file__)),
           "--query", args.query, "--top", str(args.top), "--wsl-inner"]
    try: proc = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired): return None
    if proc.returncode != 0: return None
    try: value = json.loads(proc.stdout)
    except json.JSONDecodeError: return None
    return value if isinstance(value, dict) else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    for flag in ("server", "database", "username", "password"): ap.add_argument(f"--{flag}", default=None)
    ap.add_argument("--query", required=True); ap.add_argument("--top", type=int, default=3); ap.add_argument("--wsl-inner", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    proxied = _proxy_to_wsl(args)
    if proxied is not None:
        result = proxied
    else:
        result = retrieve(args.query, top=args.top)
        if os.name == "nt" and not args.wsl_inner:
            result["retrieval_degraded"] = True
            result.setdefault("degradation_reasons", []).append("WSL retrieval proxy unavailable")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str)); return 0


if __name__ == "__main__": raise SystemExit(main())

__all__=[name for name in globals() if not name.startswith("__")]
