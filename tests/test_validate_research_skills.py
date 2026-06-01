import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_research_skills as validator


MINIMAL_BODY = """## Overview
Brief overview.

## When To Use
- Use for a concrete research workflow.

## Do Not Use When
- Do not use for unrelated tasks.

## Workflow
1. Clarify inputs.
2. Produce structured output.

## Required Outputs
- Structured artifact.

## Quality Checks
- Evidence is labeled.

## Failure Modes
- Missing inputs are made visible.
"""


def write_valid_repo(root: Path) -> None:
    (root / "README.md").write_text("# Research Skills\n", encoding="utf-8")
    (root / "extensions").mkdir(parents=True)
    (root / "extensions" / "README.md").write_text("# Extensions\n", encoding="utf-8")

    for relpath in validator.SHARED_FILES:
        path = root / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {path.stem}\n\nReusable research resource.\n", encoding="utf-8")

    for skill in validator.EXPECTED_SKILLS:
        skill_dir = root / "skills" / skill
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_text = (
            "---\n"
            f"name: {skill}\n"
            "description: Use when a graduate researcher needs this specific research workflow.\n"
            "---\n\n"
            f"# {skill}\n\n"
            f"{MINIMAL_BODY}"
        )
        (skill_dir / "SKILL.md").write_text(skill_text, encoding="utf-8")


class ValidatorTests(unittest.TestCase):
    def test_valid_minimal_repo_has_no_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_repo(root)
            errors = validator.validate_repo(root)
            self.assertEqual([], errors)

    def test_missing_skill_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_repo(root)
            target = root / "skills" / validator.EXPECTED_SKILLS[0] / "SKILL.md"
            target.unlink()
            errors = validator.validate_repo(root)
            self.assertTrue(any(str(target.relative_to(root)) in error for error in errors))

    def test_description_must_start_with_use_when(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_repo(root)
            skill = validator.EXPECTED_SKILLS[0]
            path = root / "skills" / skill / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("description: Use when", "description: Helps when"), encoding="utf-8")
            errors = validator.validate_repo(root)
            self.assertTrue(any("description must start with 'Use when'" in error for error in errors))

    def test_unresolved_draft_marker_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_repo(root)
            skill = validator.EXPECTED_SKILLS[0]
            path = root / "skills" / skill / "SKILL.md"
            path.write_text(path.read_text(encoding="utf-8") + "\n" + ("TO" + "DO") + "\n", encoding="utf-8")
            errors = validator.validate_repo(root)
            self.assertTrue(any("unresolved draft marker" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
