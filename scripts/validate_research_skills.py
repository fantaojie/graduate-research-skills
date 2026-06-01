#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_SKILLS = [
    "research-topic-selection",
    "research-proposal",
    "research-literature-search",
    "research-paper-reading",
    "research-literature-matrix",
    "research-method-synthesis",
    "research-idea-mining",
    "research-experiment-design",
    "research-experiment-comparison",
    "research-paper-organization",
]

SHARED_FILES = [
    "shared/references/cs-ai-research-principles.md",
    "shared/references/citation-integrity.md",
    "shared/references/venue-and-code-integrity.md",
    "shared/templates/topic-card.md",
    "shared/templates/proposal-outline.md",
    "shared/templates/paper-reading-notes.md",
    "shared/templates/paper-deep-reading-report.md",
    "shared/templates/literature-search-results.md",
    "shared/templates/literature-matrix.md",
    "shared/templates/method-taxonomy.md",
    "shared/templates/idea-gap-analysis.md",
    "shared/templates/experiment-plan.md",
    "shared/templates/experiment-comparison.md",
    "shared/templates/paper-organization.md",
    "shared/rubrics/topic-quality-rubric.md",
    "shared/rubrics/literature-quality-rubric.md",
    "shared/rubrics/experiment-quality-rubric.md",
    "shared/rubrics/paper-structure-rubric.md",
]

REQUIRED_SKILL_SECTIONS = [
    "## Overview",
    "## When To Use",
    "## Do Not Use When",
    "## Workflow",
    "## Required Outputs",
    "## Quality Checks",
    "## Failure Modes",
]

BANNED_MARKERS = [
    "T" + "BD",
    "TO" + "DO",
    "FIX" + "ME",
    "implement " + "later",
    "fill in " + "details",
    "\u5f85\u5b9a",
    "\u5360\u4f4d",
]

NAME_RE = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def has_unresolved_marker(text: str) -> str | None:
    lowered = text.lower()
    for marker in BANNED_MARKERS:
        if marker.lower() in lowered:
            return marker
    return None


def validate_skill(root: Path, skill: str) -> list[str]:
    errors: list[str] = []
    path = root / "skills" / skill / "SKILL.md"
    rel = path.relative_to(root)

    if not path.exists():
        return [f"Missing skill file: {rel}"]

    text = path.read_text(encoding="utf-8")
    marker = has_unresolved_marker(text)
    if marker:
        errors.append(f"{rel}: unresolved draft marker '{marker}'")

    frontmatter, body = parse_frontmatter(text)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if name != skill:
        errors.append(f"{rel}: frontmatter name must equal folder name '{skill}'")
    if not NAME_RE.match(name):
        errors.append(f"{rel}: name must use lowercase letters, digits, and hyphens")
    if not description:
        errors.append(f"{rel}: missing description")
    elif not description.startswith("Use when"):
        errors.append(f"{rel}: description must start with 'Use when'")

    for section in REQUIRED_SKILL_SECTIONS:
        if section not in body:
            errors.append(f"{rel}: missing section {section}")

    return errors


def validate_repo(root: Path) -> list[str]:
    errors: list[str] = []

    for relpath in ["README.md", "extensions/README.md"]:
        if not (root / relpath).exists():
            errors.append(f"Missing repository file: {relpath}")

    for relpath in SHARED_FILES:
        path = root / relpath
        if not path.exists():
            errors.append(f"Missing shared file: {relpath}")
            continue
        marker = has_unresolved_marker(path.read_text(encoding="utf-8"))
        if marker:
            errors.append(f"{relpath}: unresolved draft marker '{marker}'")

    for skill in EXPECTED_SKILLS:
        errors.extend(validate_skill(root, skill))

    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path.cwd()
    errors = validate_repo(root)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
