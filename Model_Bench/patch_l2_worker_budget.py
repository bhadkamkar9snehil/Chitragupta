"""Apply bounded worker settings without rewriting unrelated config/comments."""
from pathlib import Path
import sys
from patch_profile_config import _find_key_line, _block_end


# One completion path per role: investigators finish with xstudio_submit_proposal,
# reviewers with kanban_complete/kanban_block. Reviewers seeing the submit tool made
# 22 replacement-proposal attempts in 6h, so it lives in its own plugin toolset.
SUBMIT_TOOLSET = "l2_submit"
EXPLORE_TOOLSET = "xstudio_explore"


def _mark_known_plugin_toolset(lines: list[str], toolset: str) -> None:
    """A plugin toolset listed as known-but-absent stays off (hermes tools_config)."""
    parent = _find_key_line(lines, "known_plugin_toolsets", 0, len(lines), 0)
    if parent < 0:
        lines += ["known_plugin_toolsets:", "  cli:", f"    - {toolset}"]
        return
    index = _find_key_line(lines, "cli", parent + 1, _block_end(lines, parent), 2)
    if index < 0:
        lines.insert(parent + 1, "  cli:")
        index = parent + 1
    end = _block_end(lines, index)
    if f"    - {toolset}" not in lines[index + 1:end]:
        lines.insert(index + 1, f"    - {toolset}")


def off_domain_skills(skills_dir: Path) -> list[str]:
    """Every installed skill outside skills/xstudio.

    Hermes lists all enabled skills in each request's system prompt with a "you MUST
    load" nudge; for the 9B worker that was ~7K chars of claude-code/email/media
    entries per request. Disabling them keeps the index to the XStudio skills.
    """
    names = []
    for skill in sorted(skills_dir.glob("*/**/SKILL.md")):
        if skill.relative_to(skills_dir).parts[0] == "xstudio":
            continue
        head = skill.read_text(encoding="utf-8", errors="replace").split("\n", 12)
        name = next((l.split(":", 1)[1].strip().strip("'\"") for l in head if l.startswith("name:")),
                    skill.parent.name)
        names.append(name)
    return sorted(set(names))


def _set_disabled_skills(lines: list[str], disabled: list[str]) -> None:
    parent = _find_key_line(lines, "skills", 0, len(lines), 0)
    block = [f"    - {name}" for name in disabled]
    if parent < 0:
        lines += ["skills:", "  disabled:"] + block
        return
    index = _find_key_line(lines, "disabled", parent + 1, _block_end(lines, parent), 2)
    if index < 0:
        lines[parent + 1:parent + 1] = ["  disabled:"] + block
    else:
        lines[index:_block_end(lines, index)] = ["  disabled:"] + block


def configure(text: str, reviewer: bool = False, disabled_skills: list[str] | None = None) -> str:
    lines = text.splitlines()
    # Match the verified loaded Qwen context, rather than advertising a larger
    # window Hermes can never actually send to LM Studio.
    for section, key, value in [("model", "context_length", "65792"),
                                ("model", "max_tokens", "8192"),
                                ("agent", "reasoning_effort", "none"),
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
    # Exact worker toolset. l2_learning carries l2_recall (on-demand GBrain); this list
    # used to omit it and silently undo patch_profile_config on every deploy.
    toolsets = ["file", "kanban", "skills", "xstudio_l2", "l2_learning"] + ([] if reviewer else [SUBMIT_TOOLSET])
    lines[index:_block_end(lines, index)] = ["  cli:"] + [f"    - {t}" for t in toolsets]
    # Known-but-unlisted keeps a plugin toolset off: the exploration tools for every
    # worker, the submit tool for reviewers.
    _mark_known_plugin_toolset(lines, EXPLORE_TOOLSET)
    if reviewer:
        _mark_known_plugin_toolset(lines, SUBMIT_TOOLSET)
    if disabled_skills:
        _set_disabled_skills(lines, disabled_skills)
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    path = Path(sys.argv[1])
    original = path.read_text(encoding="utf-8")
    updated = configure(original, reviewer="reviewer" in path.parent.name,
                        disabled_skills=off_domain_skills(path.parent / "skills"))
    if updated != original:
        path.write_text(updated, encoding="utf-8")
    print(f"Worker budgets configured: {path.parent.name}")
