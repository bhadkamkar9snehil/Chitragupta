"""Apply bounded worker settings without rewriting unrelated config/comments."""
from pathlib import Path
import sys
from patch_profile_config import _find_key_line, _block_end


def configure(text: str) -> str:
    lines = text.splitlines()
    for section, key, value in [("model", "context_length", "75776"),
                                ("model", "max_tokens", "8192"),
                                ("agent", "max_turns", "20")]:
        parent = _find_key_line(lines, section, 0, len(lines), 0)
        if parent < 0:
            raise ValueError(f"Missing config section {section}")
        index = _find_key_line(lines, key, parent + 1, _block_end(lines, parent), 2)
        if index < 0:
            lines.insert(parent + 1, f"  {key}: {value}")
        else:
            lines[index] = f"  {key}: {value}"
    parent = _find_key_line(lines, "platform_toolsets", 0, len(lines), 0)
    if parent < 0:
        raise ValueError("Missing platform_toolsets")
    index = _find_key_line(lines, "cli", parent + 1, _block_end(lines, parent), 2)
    if index < 0:
        raise ValueError("Missing platform_toolsets.cli")
    lines[index:_block_end(lines, index)] = ["  cli:", "    - file", "    - kanban",
                                           "    - skills", "    - xstudio_l2"]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    path = Path(sys.argv[1])
    original = path.read_text(encoding="utf-8")
    updated = configure(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
    print(f"Worker budgets configured: {path.parent.name}")
