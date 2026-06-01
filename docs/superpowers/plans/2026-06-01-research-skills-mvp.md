# Research Skills MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a GitHub-ready MVP collection of 10 independently installable CS/AI/engineering graduate research skills with shared templates, rubrics, references, extension space, and validation checks.

**Architecture:** The repository uses a flat `skills/` directory for MVP skills, a `shared/` directory for reusable research templates and integrity rules, and an `extensions/` directory for future skill candidates. A small Python standard-library validator checks structure, frontmatter, required sections, shared resource existence, and unresolved draft markers.

**Tech Stack:** Markdown skills, YAML-like frontmatter, Python 3 standard library validation, `unittest`, Git.

---

## File Structure

Create or modify these files:

- Create: `README.md` - repository overview, installation guidance, and skill index.
- Create: `extensions/README.md` - future skill candidates and graduation criteria.
- Create: `scripts/validate_research_skills.py` - structural validator for this repository.
- Create: `tests/test_validate_research_skills.py` - unit tests for the validator.
- Create: `shared/references/cs-ai-research-principles.md` - reusable CS/AI/engineering research principles.
- Create: `shared/references/citation-integrity.md` - citation and evidence integrity rules.
- Create: `shared/references/venue-and-code-integrity.md` - venue tier, impact factor, CCF, and open-source verification rules.
- Create: `shared/templates/topic-card.md`
- Create: `shared/templates/proposal-outline.md`
- Create: `shared/templates/paper-reading-notes.md`
- Create: `shared/templates/paper-deep-reading-report.md`
- Create: `shared/templates/literature-search-results.md`
- Create: `shared/templates/literature-matrix.md`
- Create: `shared/templates/method-taxonomy.md`
- Create: `shared/templates/idea-gap-analysis.md`
- Create: `shared/templates/experiment-plan.md`
- Create: `shared/templates/experiment-comparison.md`
- Create: `shared/templates/paper-organization.md`
- Create: `shared/rubrics/topic-quality-rubric.md`
- Create: `shared/rubrics/literature-quality-rubric.md`
- Create: `shared/rubrics/experiment-quality-rubric.md`
- Create: `shared/rubrics/paper-structure-rubric.md`
- Create: `skills/research-topic-selection/SKILL.md`
- Create: `skills/research-proposal/SKILL.md`
- Create: `skills/research-literature-search/SKILL.md`
- Create: `skills/research-paper-reading/SKILL.md`
- Create: `skills/research-literature-matrix/SKILL.md`
- Create: `skills/research-method-synthesis/SKILL.md`
- Create: `skills/research-idea-mining/SKILL.md`
- Create: `skills/research-experiment-design/SKILL.md`
- Create: `skills/research-experiment-comparison/SKILL.md`
- Create: `skills/research-paper-organization/SKILL.md`

Each skill file must include these sections exactly:

```markdown
## Overview
## When To Use
## Do Not Use When
## Workflow
## Required Outputs
## Quality Checks
## Failure Modes
```

Each skill should also reference shared resources by relative path when relevant, for example `../../shared/templates/topic-card.md`.

---

### Task 1: Add Validator Tests First

**Files:**
- Create: `tests/test_validate_research_skills.py`

- [ ] **Step 1: Create the tests directory**

Run:

```bash
mkdir -p tests
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Write validator tests**

Create `tests/test_validate_research_skills.py` with:

```python
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
```

- [ ] **Step 3: Run tests to verify the expected failure**

Run:

```bash
python3 -m unittest tests/test_validate_research_skills.py
```

Expected: FAIL with an import error because `scripts/validate_research_skills.py` does not exist yet.

- [ ] **Step 4: Commit the failing validator tests**

Run:

```bash
git add tests/test_validate_research_skills.py
git commit -m "test: add research skill validator tests"
```

Expected: commit succeeds.

---

### Task 2: Implement the Validator

**Files:**
- Create: `scripts/validate_research_skills.py`

- [ ] **Step 1: Create the scripts directory**

Run:

```bash
mkdir -p scripts
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Implement the validator**

Create `scripts/validate_research_skills.py` with:

```python
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
```

- [ ] **Step 3: Run validator unit tests**

Run:

```bash
python3 -m unittest tests/test_validate_research_skills.py
```

Expected: PASS with 4 tests.

- [ ] **Step 4: Run validator against the current repository**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing missing README, shared files, extension README, and MVP skill files. This proves the validator detects the work that remains.

- [ ] **Step 5: Commit validator implementation**

Run:

```bash
git add scripts/validate_research_skills.py
git commit -m "feat: add research skills validator"
```

Expected: commit succeeds.

---

### Task 3: Add Shared References

**Files:**
- Create: `shared/references/cs-ai-research-principles.md`
- Create: `shared/references/citation-integrity.md`
- Create: `shared/references/venue-and-code-integrity.md`

- [ ] **Step 1: Create shared reference directory**

Run:

```bash
mkdir -p shared/references
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Create `cs-ai-research-principles.md`**

Create `shared/references/cs-ai-research-principles.md` with these sections and rules:

```markdown
# CS/AI/Engineering Research Principles

## Research Question

A strong research question states the task, context, limitation, proposed direction, and evaluation target. It is narrower than a broad theme and stronger than an implementation wish.

## Contribution Types

- New problem framing
- New method or architecture
- New training, optimization, or inference strategy
- New dataset, benchmark, protocol, or metric
- New empirical finding, analysis, or failure diagnosis
- New system design or engineering trade-off

## Evidence Expectations

- Claims about performance need metrics, baselines, and settings.
- Claims about efficiency need hardware, input size, implementation details, and measurement method.
- Claims about robustness need stress conditions and failure cases.
- Claims about generality need datasets, domains, or tasks beyond the development setting.

## Common CS/AI Paper Shape

1. Problem and motivation
2. Related work and gap
3. Method or system
4. Experimental setup
5. Results and analysis
6. Limitations and threats to validity

## Reproducibility Signals

- Dataset names, versions, splits, and preprocessing
- Model and baseline configuration
- Hyperparameters and search strategy
- Random seeds and variance reporting
- Hardware and runtime environment
- Code, checkpoints, and artifact availability
```

- [ ] **Step 3: Create `citation-integrity.md`**

Create `shared/references/citation-integrity.md` with:

```markdown
# Citation And Evidence Integrity

## Evidence Labels

Use one label for every research claim:

- Verified from provided source
- Retrieved from current search
- Inferred from available context
- Hypothesis requiring validation
- Unknown or missing

## Non-Negotiable Rules

- Never fabricate citations, venues, years, authors, datasets, metrics, or benchmark rankings.
- Do not treat paper titles, abstracts, blog posts, or leaderboards as interchangeable evidence.
- Distinguish author claims from independent interpretation.
- Mark missing metadata explicitly instead of guessing.
- When search or source access is unavailable, say what cannot be verified.

## Citation Checks

Before using a citation in a final artifact, verify:

- Title
- Authors
- Year
- Venue or preprint source
- DOI, arXiv ID, URL, or repository when available
- The exact claim supported by the citation
```

- [ ] **Step 4: Create `venue-and-code-integrity.md`**

Create `shared/references/venue-and-code-integrity.md` with:

```markdown
# Venue And Code Integrity

## Publication Quality Fields

When a literature skill reports publication quality, include the best available fields:

- Venue or journal name
- Venue type: conference, journal, preprint, workshop, magazine, repository, or unknown
- SCI/JCR quartile for journals when applicable
- CCF class for computer science conferences and journals when applicable
- Impact factor when available
- Metric source and access date

## Verification Rules

- Treat journal quartile, impact factor, and CCF class as time-sensitive metadata.
- Verify current values from authoritative or clearly named sources when browsing is available.
- If a metric cannot be verified, write `Unknown` rather than guessing.
- If the paper is an arXiv preprint with no peer-reviewed venue, mark the venue tier as `Preprint`.
- Prefer top conferences and journals only when the paper is relevant to the user's topic.

## Open-Source Fields

Report code and artifact status as one of:

- Official code available
- Unofficial reproduction available
- Dataset or benchmark available
- Artifact mentioned but unavailable
- No code found
- Not checked

When code is available, include the repository URL and whether it appears official. Prefer links from the paper, project page, author profile, Papers With Code, or the official organization.

## Paper Type Labels

Use one or more labels:

- Survey or review
- Method innovation
- Dataset or benchmark
- System or tool
- Empirical evaluation
- Theory or analysis
- Application study
- Reproducibility or replication
- Position or perspective
```

- [ ] **Step 5: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining missing repository files, shared templates, shared rubrics, and skill files. The three shared references are no longer reported missing.

- [ ] **Step 6: Commit shared references**

Run:

```bash
git add shared/references/cs-ai-research-principles.md shared/references/citation-integrity.md shared/references/venue-and-code-integrity.md
git commit -m "docs: add shared research references"
```

Expected: commit succeeds.

---

### Task 4: Add Shared Templates

**Files:**
- Create all files under `shared/templates/`

- [ ] **Step 1: Create shared templates directory**

Run:

```bash
mkdir -p shared/templates
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Create `topic-card.md`**

Use:

```markdown
# Topic Card

## Candidate Topic

## Research Question

## Problem Context

## Scope Boundary

## Candidate Contribution

## Required Evidence

## Feasibility

| Dimension | Assessment | Evidence | Risk |
| --- | --- | --- | --- |
| Literature access |  |  |  |
| Data access |  |  |  |
| Method feasibility |  |  |  |
| Compute/resources |  |  |  |
| Evaluation path |  |  |  |

## Next Validation Steps
```

- [ ] **Step 3: Create `proposal-outline.md`**

Use:

```markdown
# Proposal Outline

## Title

## Background And Significance

## Research Problem

## Research Objectives

## Related Work Map

## Proposed Method Or Technical Route

## Experiment And Evaluation Plan

## Feasibility Analysis

## Risks And Mitigation

## Work Plan

| Phase | Time | Work | Deliverable |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

## Expected Contributions
```

- [ ] **Step 4: Create `paper-reading-notes.md`**

Use:

```markdown
# Paper Reading Notes

## Metadata

| Field | Value |
| --- | --- |
| Title |  |
| Authors |  |
| Year |  |
| Venue/Source |  |
| Link/ID |  |

## One-Paragraph Summary

## Problem

## Method

## Results

## Claimed Contributions

## Assumptions

## Limitations

## Reproducibility Notes

## Follow-Up Questions

## Evidence Labels
```

- [ ] **Step 5: Create `paper-deep-reading-report.md`**

Use:

```markdown
# Paper Deep Reading Report

## Academic Translation And Chinese Reading

Translate the abstract and user-selected key passages in an academic Chinese style. For copyrighted full papers, provide section-by-section Chinese paraphrase instead of full verbatim translation.

## Plain-Language Overview

## Core Idea

## Code Availability First Check

| Field | Value |
| --- | --- |
| Official code status |  |
| Repository URL |  |
| Artifact URL |  |
| Key entry files |  |
| Key functions/classes |  |
| Code evidence source |  |

## Generated Principle Diagram

Prefer the `imagegen` skill for a large, readable, original teaching diagram when visual explanation helps. Do not copy copyrighted paper figures; cite original figure numbers separately when useful.

| Field | Value |
| --- | --- |
| Diagram purpose |  |
| Imagegen prompt |  |
| Saved image path or inline image |  |
| Original paper figures referenced |  |

If image generation is unavailable, use Mermaid or a compact text diagram and state the fallback.

## Code-Level Explanation

Map the core innovation to repository files, functions, modules, or concise pseudocode. If no code is available, mark `No code found` or `Not checked`.

```text
Input:
Core steps:
Output:
```

## Formula And Algorithm Explanation

| Symbol/Step | Meaning | Intuitive Explanation |
| --- | --- | --- |

## Innovation Points

## Experiment Process

| Experiment | Purpose | Dataset/System | Baseline | Metric | Main Finding |
| --- | --- | --- | --- | --- | --- |

## Experiment Data Tables

| Table/Figure | Dataset | Setting | Compared Methods | Metric | Reported Values | Interpretation | Evidence Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Transferable Ideas For My Research

## Limitations And Open Questions

## Reproducibility Notes

## Follow-Up Reading
```

- [ ] **Step 6: Create remaining templates**

Create these files with the listed headings:

`literature-search-results.md`

```markdown
# Literature Search Results

Default search scope: most recent 3 years and 30 papers unless the user requests another range or count.

## Review-First Search Pass

| Review Paper | Year | Venue/Journal | Tier/Quartile/CCF | Role In Search Expansion | Evidence Status |
| --- | --- | --- | --- | --- | --- |

## Paper Results

| Paper | Year | Venue/Journal | Tier/Quartile/CCF | Impact Factor | Open Source Status | Code URL | Paper Type | Summary <=300 Chinese Characters | Evidence Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Search Log

| Source | Query | Date | Filters | Notes |
| --- | --- | --- | --- | --- |

## Missing Or Unverified Metadata
```

`literature-matrix.md`

```markdown
# Literature Matrix

| Paper | Year | Venue/Journal | Tier/Quartile/CCF | Impact Factor | Open Source Status | Code URL | Paper Type | Problem | Method | Dataset/System | Metrics | Main Result | Limitation | Summary <=300 Chinese Characters | Use In My Work | Evidence Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Theme Clusters

## Chronological Development

## Open-Source Artifact Notes

## Missing Evidence
```

`method-taxonomy.md`

```markdown
# Method Taxonomy

## Method Family Chart

Use Mermaid, a generated diagram, or a compact text tree to show the field-level method taxonomy.

## Method Family Table

| Method Family | Core Mechanism | Assumptions | Strengths | Weaknesses | Representative Papers | Best Use Cases |
| --- | --- | --- | --- | --- | --- | --- |

## Paper-To-Method Mapping

| Paper | Year | Method Family | Specific Technique | Evidence | Notes |
| --- | --- | --- | --- | --- | --- |

## Method Comparison Matrix

| Method Family | Input | Process | Output | Typical Metrics | Data/Compute Needs | Failure Cases |
| --- | --- | --- | --- | --- | --- | --- |

## Selection Guidance

## Open Method Questions
```

`idea-gap-analysis.md`

```markdown
# Idea Gap Analysis

| Gap | Evidence | Candidate Idea | Novelty | Feasibility | Risk | Validation Plan |
| --- | --- | --- | --- | --- | --- | --- |

## Strongest Candidate

## Ideas To Reject

## Evidence Needed Next
```

`experiment-plan.md`

```markdown
# Experiment Plan

## Research Claim

## Hypotheses

| Hypothesis | Experiment | Metric | Expected Evidence |
| --- | --- | --- | --- |

## Dataset Or System Setup

## Baselines

## Metrics

## Ablations

## Controls And Confounders

## Reproducibility Checklist
```

`experiment-comparison.md`

```markdown
# Experiment Comparison

| Method | Setting | Dataset/System | Metric | Result | Fairness Notes | Interpretation |
| --- | --- | --- | --- | --- | --- | --- |

## Baseline Fairness

## Ablation Interpretation

## Threats To Validity

## Result Narrative
```

`paper-organization.md`

```markdown
# Paper Organization

## Core Claim

## Contribution List

## Section Outline

| Section | Purpose | Key Claim | Evidence |
| --- | --- | --- | --- |

## Related Work Structure

## Method Section Skeleton

## Experiment Section Skeleton

## Claim-Evidence Map
```

- [ ] **Step 7: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining missing repository files, shared rubrics, and skill files. The shared templates are no longer reported missing.

- [ ] **Step 8: Commit shared templates**

Run:

```bash
git add shared/templates
git commit -m "docs: add shared research templates"
```

Expected: commit succeeds.

---

### Task 5: Add Shared Rubrics

**Files:**
- Create all files under `shared/rubrics/`

- [ ] **Step 1: Create shared rubrics directory**

Run:

```bash
mkdir -p shared/rubrics
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Create rubric files**

Create `topic-quality-rubric.md`:

```markdown
# Topic Quality Rubric

Score each item 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Specificity | Broad theme | Partly scoped | Clear research question |
| Novelty path | No gap | Plausible gap | Evidence-backed gap |
| Feasibility | Resources unclear | Some resources known | Data, method, and evaluation path known |
| Evaluation | No test | Informal check | Metrics and comparison plan |
| Risk awareness | Hidden risks | Listed risks | Risks and mitigation |
```

Create `literature-quality-rubric.md`:

```markdown
# Literature Quality Rubric

Score each item 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Coverage | Random papers | Partial coverage | Search strategy documented |
| Comparison | Summaries only | Some comparison | Cross-paper dimensions clear |
| Evidence status | Unlabeled | Partly labeled | Missing and verified evidence marked |
| Concept clarity | Paper names only | Some grouping | Method and problem clusters clear |
```

Create `experiment-quality-rubric.md`:

```markdown
# Experiment Quality Rubric

Score each item 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Claim alignment | Experiments disconnected | Partly aligned | Each experiment tests a claim |
| Baseline fairness | Unfair or absent | Partial fairness | Settings and resources comparable |
| Metric fit | Metrics mismatched | Some fit | Metrics directly support claims |
| Ablations | Absent | Minimal | Mechanism-focused ablations |
| Reproducibility | Unclear | Partly documented | Data, seeds, config, hardware noted |
```

Create `paper-structure-rubric.md`:

```markdown
# Paper Structure Rubric

Score each item 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Argument flow | Section list only | Some logic | Clear claim progression |
| Related work | Paper summaries | Partial positioning | Gap and contribution positioning |
| Method clarity | Implementation dump | Partial explanation | Assumptions, mechanism, and complexity clear |
| Experiment narrative | Results listed | Some interpretation | Claims, evidence, and limitations connected |
```

- [ ] **Step 3: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining missing repository files and skill files. The shared rubrics are no longer reported missing.

- [ ] **Step 4: Commit shared rubrics**

Run:

```bash
git add shared/rubrics
git commit -m "docs: add shared research rubrics"
```

Expected: commit succeeds.

---

### Task 6: Add Topic And Proposal Skills

**Files:**
- Create: `skills/research-topic-selection/SKILL.md`
- Create: `skills/research-proposal/SKILL.md`

- [ ] **Step 1: Create skill directories**

Run:

```bash
mkdir -p skills/research-topic-selection skills/research-proposal
```

Expected: directories exist and command exits 0.

- [ ] **Step 2: Create `research-topic-selection/SKILL.md`**

Use this frontmatter and body contract:

```markdown
---
name: research-topic-selection
description: Use when choosing, narrowing, evaluating, or comparing CS, AI, or engineering research topics, thesis directions, research questions, or project ideas
---

# Research Topic Selection

## Overview

Helps turn broad interests into scoped, evaluable research topics. The output should make the problem, boundary, contribution path, feasibility, and next validation steps explicit.

## When To Use

- The user has a broad research area and needs candidate topics.
- The user has several possible directions and needs comparison.
- The user needs to narrow a thesis, paper, or project idea.
- The user wants to judge feasibility before committing to a topic.

## Do Not Use When

- The user already has a fixed topic and needs a proposal; use `research-proposal`.
- The user mainly needs paper search strings; use `research-literature-search`.
- The user asks for fabricated novelty or unsupported claims.

## Workflow

1. Identify the user's field, degree stage, constraints, available data, methods, compute, and timeline.
2. Convert broad interests into 3-5 candidate research questions.
3. For each candidate, state the problem, scope boundary, possible contribution, required evidence, and feasibility risks.
4. Score candidates with `../../shared/rubrics/topic-quality-rubric.md`.
5. Recommend the strongest candidate and list validation steps.

## Required Outputs

- Topic cards using `../../shared/templates/topic-card.md`.
- Candidate comparison table.
- Recommendation with evidence labels.
- Next validation steps.

## Quality Checks

- The topic is narrower than a broad theme.
- The research question can be evaluated or argued.
- Data, method, compute, and evaluation access are explicit.
- Weak topics are rejected with reasons.

## Failure Modes

- If constraints are missing, ask for the degree stage, timeline, data access, and target venue or thesis type.
- If the topic is too broad, produce narrower variants rather than accepting it as-is.
- If novelty cannot be assessed, label it as a hypothesis requiring validation.
```

- [ ] **Step 3: Create `research-proposal/SKILL.md`**

Use this frontmatter and body contract:

```markdown
---
name: research-proposal
description: Use when preparing an opening report, thesis proposal, proposal defense, research plan, technical route, milestone plan, or feasibility analysis for CS, AI, or engineering research
---

# Research Proposal

## Overview

Helps structure a defensible proposal by connecting background, problem, objectives, method, experiment plan, feasibility, risks, milestones, and expected contributions.

## When To Use

- The user needs an opening report or thesis proposal.
- The user has a topic and needs a technical route.
- The user needs milestone planning, feasibility analysis, or proposal defense preparation.

## Do Not Use When

- The user still needs to choose a topic; use `research-topic-selection`.
- The user only needs literature search strategy; use `research-literature-search`.
- The user wants unsupported expected results.

## Workflow

1. Extract topic, target degree/program, constraints, available resources, and deadline.
2. Build the proposal outline using `../../shared/templates/proposal-outline.md`.
3. Connect background to research problem and objectives.
4. Draft the technical route as stages with inputs, methods, outputs, and evaluation.
5. Add feasibility, risks, mitigation, milestones, and expected contributions.
6. Check consistency between problem, method, experiment, and contribution.

## Required Outputs

- Proposal outline.
- Technical route.
- Milestone table.
- Feasibility and risk analysis.
- Expected contribution list with evidence labels.

## Quality Checks

- The method addresses the stated problem.
- The experiment plan can evaluate the objective.
- Risks and mitigation are visible.
- Expected contributions do not overclaim.

## Failure Modes

- If the topic is underspecified, ask for the research direction and intended output.
- If the technical route is vague, rewrite it as ordered stages.
- If evaluation is missing, add candidate datasets, metrics, or system tests.
```

- [ ] **Step 4: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining 8 missing skill files and missing repository files.

- [ ] **Step 5: Commit topic and proposal skills**

Run:

```bash
git add skills/research-topic-selection/SKILL.md skills/research-proposal/SKILL.md
git commit -m "feat: add topic and proposal research skills"
```

Expected: commit succeeds.

---

### Task 7: Add Literature Skills

**Files:**
- Create: `skills/research-literature-search/SKILL.md`
- Create: `skills/research-paper-reading/SKILL.md`
- Create: `skills/research-literature-matrix/SKILL.md`

- [ ] **Step 1: Create skill directories**

Run:

```bash
mkdir -p skills/research-literature-search skills/research-paper-reading skills/research-literature-matrix
```

Expected: directories exist and command exits 0.

- [ ] **Step 2: Create literature search skill**

Create `skills/research-literature-search/SKILL.md` with:

```markdown
---
name: research-literature-search
description: Use when planning literature search, keyword expansion, database selection, inclusion criteria, search logs, seed paper collection, or systematic search for CS, AI, or engineering topics
---

# Research Literature Search

## Overview

Creates a traceable search strategy for exploratory or systematic literature discovery. When the user gives a topic, it defaults to the most recent 3 years and 30 papers unless the user specifies another time range or count.

## When To Use

- The user needs keywords, synonyms, and search strings.
- The user needs databases or sources for CS/AI/engineering literature.
- The user wants inclusion and exclusion criteria.
- The user wants a search log, seed paper collection, or recent-paper table with venue tier and code availability.

## Do Not Use When

- The user asks to deeply read one paper; use `research-paper-reading`.
- The user already has multiple papers and needs organization; use `research-literature-matrix`.
- The user asks for fabricated citations.

## Workflow

1. Clarify research question, field, target venues, time range, paper count, and paper types. Use the most recent 3 years and 30 papers by default.
2. First search for survey or review papers from roughly the most recent year. Use the best recent reviews to identify terminology, subtopics, benchmark datasets, method families, and important primary papers.
3. Build keyword groups: task, method, domain, dataset/system, metric, and synonyms.
4. Create search strings for broad search, targeted search, and backward/forward snowballing from review papers.
5. Define inclusion and exclusion criteria, prioritizing relevant top conferences and journals when possible.
6. If browsing/search tools are available, collect papers and verify metadata, venue tier, impact factor, CCF class, open-source status, and code URL using `../../shared/references/venue-and-code-integrity.md`.
7. Create a search log with source, query, date, filters, and notes.

## Required Outputs

- Search question.
- Keyword groups and synonyms.
- Source/database plan.
- Inclusion and exclusion criteria.
- Search log table.
- Literature search result table using `../../shared/templates/literature-search-results.md`.
- For each paper: year, venue or journal, venue tier, SCI/JCR quartile if applicable, CCF class if applicable, impact factor when available, open-source status, code URL, paper type, and a summary no longer than 300 Chinese characters.
- Seed paper list with evidence labels when sources are available.

## Quality Checks

- Search strings are reproducible.
- Exploratory and systematic searches are not mixed silently.
- Metadata confidence is labeled.
- Missing source access is stated.
- Venue tier, impact factor, CCF class, and open-source links are verified when possible and marked `Unknown` when not verified.
- Review papers guide expansion but do not replace primary-paper verification.
- The result set respects the requested paper count and time range, or explains why fewer papers were found.

## Failure Modes

- If the topic is broad, ask for subfield, task, and target contribution type.
- If no search access exists, provide strings and a log template instead of inventing papers.
- If results are too noisy, split queries by task, method, and application domain.
- If a paper has no identifiable code, mark `No code found`; if code is not checked, mark `Not checked`.
- If the user asks for journal quartile, CCF class, or impact factor without current source access, mark the field `Unknown` and state that it requires verification.
```

- [ ] **Step 3: Create paper reading skill**

Create `skills/research-paper-reading/SKILL.md` with:

```markdown
---
name: research-paper-reading
description: Use when analyzing a single paper, checking open-source code, translating or paraphrasing key content, explaining methods with diagrams, code, and formulas, extracting structured reading notes, critiquing claims, or preparing a deep reading report
---

# Research Paper Reading

## Overview

Turns one paper into a grounded deep-reading report. It first checks whether official code or artifacts exist, then explains the paper in academic Chinese and plain language using diagrams, code or pseudocode, and formula walkthroughs where helpful.

## When To Use

- The user provides a paper, abstract, PDF text, URL, DOI, arXiv ID, or title.
- The user wants academic Chinese translation, section-by-section Chinese reading, method understanding, critique, or reproducibility notes.
- The user wants the core idea explained with a generated principle diagram, code, text, and formulas.
- The user wants notes for later literature review or implementation.

## Do Not Use When

- The user needs a search strategy; use `research-literature-search`.
- The user has many papers to compare; use `research-literature-matrix`.
- The user expects claims beyond the provided or retrieved paper text.
- The user asks for a full verbatim translation of a copyrighted paper; translate short user-provided excerpts or open-licensed text, otherwise provide structured Chinese paraphrase.

## Workflow

1. Verify what paper content is available, what metadata is known, and whether full-text translation is allowed.
2. Before deep explanation, check whether the paper has official code, artifacts, project pages, or reproduction repositories. Use `../../shared/references/venue-and-code-integrity.md` to label code status.
3. If code exists, identify repository URL, artifact URL, key entry files, and key functions or classes. If not, mark `No code found`; if source access is unavailable, mark `Not checked`.
4. Extract metadata and label missing fields.
5. Provide academic Chinese translation for the abstract and user-selected key passages. For copyrighted full papers, provide section-by-section Chinese paraphrase instead of full verbatim translation.
6. Build a deep reading report using `../../shared/templates/paper-deep-reading-report.md`.
7. Explain the paper's core idea with plain-language text and a large, readable generated principle diagram. Prefer the `imagegen` skill for an original teaching diagram when image generation is available; if unavailable, use Mermaid or compact text diagrams and state the fallback.
8. Explain the core innovation through code or pseudocode, mapping concepts to repository files/functions when code is available.
9. Explain formulas, losses, algorithms, or pipelines by defining symbols, stating the technical role, and giving intuitive interpretation.
10. Summarize the problem, method, results, contributions, assumptions, and limitations.
11. Extract experiment process as tables: datasets/systems, settings, baselines, metrics, ablations, reported values, main findings, and threats to validity.
12. Identify transferable ideas for the user's research and separate them from author claims.
13. Generate reproducibility notes, follow-up questions, and related-reading needs.

## Required Outputs

- Reading notes using `../../shared/templates/paper-reading-notes.md`.
- Deep reading report using `../../shared/templates/paper-deep-reading-report.md`.
- Code availability first check with repository URL, artifact URL, key files, and key functions/classes when available.
- Academic translation of abstract and selected key passages, or copyright-safe section-by-section Chinese paraphrase.
- Generated principle diagram plus text explanation of the paper's idea; include the imagegen prompt and image path when an image is generated.
- Code-level explanation or pseudocode for the core innovation.
- Formula and algorithm explanation with symbol definitions and intuitive interpretation.
- Experiment process and reported results in tables.
- Claim-evidence list.
- Core idea, innovation points, experiment process, and transferable ideas.
- Limitation and assumption list.
- Reproducibility notes.
- Follow-up questions.

## Quality Checks

- Every claim is grounded in provided or retrieved text.
- Author claims and reader interpretation are separate.
- Novelty and results are not overstated.
- Unknown metadata is marked.
- Code availability is checked before implementation-level explanation.
- Core innovation is explained through generated diagram, code or pseudocode, and mathematical principle.
- Generated diagrams are original, large, readable, and educational; original paper figures are referenced by figure number and source rather than copied.
- The explanation is accessible to a graduate student outside the narrow subtopic while preserving technical accuracy.
- Formula explanations connect symbols to the paper's research problem.
- Experiment descriptions include purpose, setup, baselines, metrics, reported values, and conclusions in tables.
- Translation respects copyright limits and does not reproduce a full copyrighted paper verbatim.

## Failure Modes

- If only a title is available, ask for abstract, PDF, URL, DOI, or arXiv ID before deep reading.
- If source access is partial, state which sections were not inspected.
- If the paper is outside CS/AI/engineering, adapt the structure but preserve evidence labels.
- If formulas are missing or informal, explain the method as a pipeline instead of inventing equations.
- If `imagegen` is unavailable or inappropriate for the diagram, provide a Mermaid/text fallback and state why.
- If official code exists but cannot be inspected, include the URL and mark implementation details as not inspected.
- If code is unavailable, provide pseudocode and state that it is an interpretation rather than repository-grounded code.
- If experiments are not available in the source, mark the experiment process as missing and avoid guessing results.
- If the user requests full-paper translation of copyrighted text, offer abstract/key-passage translation and full-paper Chinese paraphrase.
```

- [ ] **Step 4: Create literature matrix skill**

Create `skills/research-literature-matrix/SKILL.md` with:

```markdown
---
name: research-literature-matrix
description: Use when organizing multiple papers into a literature matrix, comparing methods, clustering themes, tracking reading status, or preparing related work for CS, AI, or engineering research
---

# Research Literature Matrix

## Overview

Organizes multiple papers into comparison-ready structures for synthesis, related work, gap analysis, and research planning. It preserves publication quality, open-source, paper-type, and concise-summary fields from literature search results.

## When To Use

- The user has several papers and needs a comparison table.
- The user has search results and needs publication tier, open-source status, paper type, and summaries organized in one matrix.
- The user wants theme clusters or chronological development.
- The user is preparing related work or a survey-style summary.

## Do Not Use When

- The user has one paper; use `research-paper-reading`.
- The user needs search strings before collecting papers; use `research-literature-search`.
- The user wants method taxonomy without paper-level organization; use `research-method-synthesis`.

## Workflow

1. List papers and mark available metadata.
2. Choose matrix columns based on the research question.
3. Preserve bibliographic and artifact fields: year, venue or journal, tier, SCI/JCR quartile, CCF class, impact factor, open-source status, code URL, paper type, and evidence status.
4. Fill comparable research fields: problem, method, dataset/system, metrics, result, limitation, concise summary, and relevance.
5. Keep each paper summary no longer than 300 Chinese characters unless the user requests another length.
6. Cluster papers by theme, method family, task, paper type, venue level, or chronology.
7. Identify missing evidence and papers requiring deeper reading.
8. Produce writing-ready related work angles.

## Required Outputs

- Literature matrix using `../../shared/templates/literature-matrix.md`.
- Theme clusters.
- Chronological development map.
- Venue-tier and open-source artifact notes.
- Missing-evidence list.
- Related-work positioning notes.

## Quality Checks

- The output compares papers rather than listing summaries.
- Unknown fields remain visible.
- Columns are stable enough for later writing.
- Evidence status is labeled.
- Publication tier and open-source fields follow `../../shared/references/venue-and-code-integrity.md`.
- Summaries stay within the requested length limit.

## Failure Modes

- If paper metadata is incomplete, create the matrix and mark missing fields.
- If papers are too diverse, split them into clusters before comparison.
- If the user asks for conclusions unsupported by the papers, label them as hypotheses.
- If venue tier, impact factor, CCF class, or code status cannot be verified, mark it `Unknown` rather than guessing.
```

- [ ] **Step 5: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining 5 missing skill files and missing repository files.

- [ ] **Step 6: Commit literature skills**

Run:

```bash
git add skills/research-literature-search/SKILL.md skills/research-paper-reading/SKILL.md skills/research-literature-matrix/SKILL.md
git commit -m "feat: add literature research skills"
```

Expected: commit succeeds.

---

### Task 8: Add Method And Idea Skills

**Files:**
- Create: `skills/research-method-synthesis/SKILL.md`
- Create: `skills/research-idea-mining/SKILL.md`

- [ ] **Step 1: Create skill directories**

Run:

```bash
mkdir -p skills/research-method-synthesis skills/research-idea-mining
```

Expected: directories exist and command exits 0.

- [ ] **Step 2: Create method synthesis skill**

Create `skills/research-method-synthesis/SKILL.md` with:

```markdown
---
name: research-method-synthesis
description: Use when organizing surveyed papers into method families, method taxonomies, technical-route charts, paper-to-method mapping tables, or method comparison tables across CS, AI, or engineering research
---

# Research Method Synthesis

## Overview

Synthesizes methods from a surveyed literature set by mechanism, assumptions, strengths, weaknesses, representative papers, and applicable scenarios. The output should make the field's method landscape visible through charts and tables.

## When To Use

- The user wants to understand a family of methods.
- The user needs a taxonomy of models, algorithms, systems, or pipelines.
- The user has a literature list or matrix and wants method categories.
- The user wants papers organized by technical route.
- The user needs method selection guidance for a research problem.

## Do Not Use When

- The user needs paper-level comparison first; use `research-literature-matrix`.
- The user needs experiment planning; use `research-experiment-design`.
- The user asks for unsupported superiority claims.

## Workflow

1. Identify the target problem, surveyed paper set, and method scope.
2. Extract each paper's core method, inputs, outputs, evaluation target, and claimed contribution.
3. Group methods by core mechanism, assumption, pipeline stage, or technical route.
4. Build a method family chart using `../../shared/templates/method-taxonomy.md`; use Mermaid, a generated diagram, or a compact text tree.
5. Create a paper-to-method mapping table linking each paper to method family, specific technique, and evidence.
6. For each method family, summarize mechanism, assumptions, strengths, weaknesses, representative papers, and applicable scenarios.
7. Compare method families across input, process, output, metrics, data/compute needs, and failure cases.
8. Produce method selection guidance and open technical questions.

## Required Outputs

- Method taxonomy using `../../shared/templates/method-taxonomy.md`.
- Method family chart or taxonomy diagram.
- Paper-to-method mapping table.
- Method comparison matrix.
- Mechanism and assumption table.
- Strength and weakness comparison.
- Representative papers for each method family.
- Use-case guidance.
- Open method questions.

## Quality Checks

- Method families are grouped by principle.
- Every major method family cites representative papers from the surveyed literature.
- The output uses charts and tables rather than prose-only summaries.
- Mechanism, implementation detail, and empirical effect are separate.
- Evidence source and inference are labeled.
- Selection guidance includes constraints.

## Failure Modes

- If methods are mixed across unrelated tasks, split the taxonomy by task.
- If the user has not provided papers, ask for a literature list or use `research-literature-search` first.
- If a paper fits multiple families, mark primary and secondary families.
- If evidence is thin, state which comparisons are inferred.
- If the user wants implementation details, identify which papers or codebases need inspection.
```

- [ ] **Step 3: Create idea mining skill**

Create `skills/research-idea-mining/SKILL.md` with:

```markdown
---
name: research-idea-mining
description: Use when finding innovation points, research gaps, thesis ideas, contribution candidates, improvement directions, or novelty-feasibility trade-offs from literature and methods
---

# Research Idea Mining

## Overview

Turns literature, limitations, method comparisons, and experimental gaps into candidate research ideas with novelty, feasibility, risk, and validation paths.

## When To Use

- The user wants innovation points for a thesis, paper, or project.
- The user has literature notes and needs gap analysis.
- The user wants to compare candidate contributions.

## Do Not Use When

- The user has not gathered enough context for any evidence-backed gap; use `research-literature-search` or `research-literature-matrix`.
- The user needs experiment details for an existing idea; use `research-experiment-design`.
- The user asks for guaranteed novelty.

## Workflow

1. Identify the evidence base: papers, methods, datasets, experiments, and limitations.
2. Extract gaps in problem framing, method, data, evaluation, system constraints, or theory.
3. Generate candidate ideas tied to specific gaps.
4. Score novelty, feasibility, risk, and validation cost.
5. Reject weak ideas with reasons.
6. Recommend the strongest idea and first validation experiment.

## Required Outputs

- Gap analysis using `../../shared/templates/idea-gap-analysis.md`.
- Candidate innovation matrix.
- Strongest candidate recommendation.
- Rejected idea list.
- Validation plan.

## Quality Checks

- Each idea maps to a concrete gap.
- Each idea has an evaluation route.
- Claims about novelty are labeled as verified, inferred, or requiring validation.
- Vague improvements are rewritten as mechanism-level hypotheses.

## Failure Modes

- If the evidence base is weak, produce a gap inventory and reading plan first.
- If ideas are too broad, narrow them by task, data, metric, or constraint.
- If an idea cannot be evaluated, mark it as weak and explain why.
```

- [ ] **Step 4: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining 3 missing skill files and missing repository files.

- [ ] **Step 5: Commit method and idea skills**

Run:

```bash
git add skills/research-method-synthesis/SKILL.md skills/research-idea-mining/SKILL.md
git commit -m "feat: add method and idea research skills"
```

Expected: commit succeeds.

---

### Task 9: Add Experiment Skills

**Files:**
- Create: `skills/research-experiment-design/SKILL.md`
- Create: `skills/research-experiment-comparison/SKILL.md`

- [ ] **Step 1: Create skill directories**

Run:

```bash
mkdir -p skills/research-experiment-design skills/research-experiment-comparison
```

Expected: directories exist and command exits 0.

- [ ] **Step 2: Create experiment design skill**

Create `skills/research-experiment-design/SKILL.md` with:

```markdown
---
name: research-experiment-design
description: Use when designing CS, AI, or engineering experiments, hypotheses, datasets, metrics, protocols, baselines, controls, ablations, or reproducibility plans
---

# Research Experiment Design

## Overview

Designs experiments that test research claims with aligned hypotheses, data, baselines, metrics, ablations, controls, and reproducibility details.

## When To Use

- The user has a method or idea and needs an experiment plan.
- The user needs datasets, metrics, baselines, controls, or ablations.
- The user wants to check whether experiments support specific claims.

## Do Not Use When

- The user is comparing completed results; use `research-experiment-comparison`.
- The user still needs an idea; use `research-idea-mining`.
- The user asks for invented results.

## Workflow

1. State the research claim and hypotheses.
2. Map each hypothesis to experiments, metrics, and expected evidence.
3. Define datasets, systems, splits, preprocessing, or workloads.
4. Choose fair baselines and controls.
5. Design ablations around mechanisms.
6. Add reproducibility details and failure-case analysis.

## Required Outputs

- Experiment plan using `../../shared/templates/experiment-plan.md`.
- Hypothesis-experiment-metric table.
- Baseline and ablation plan.
- Confounder and failure-case list.
- Reproducibility checklist.

## Quality Checks

- Each experiment answers a research question.
- Metrics match claims.
- Baselines are fair and justified.
- Reproducibility details are explicit.

## Failure Modes

- If the claim is unclear, rewrite it before designing experiments.
- If baselines are missing, propose categories and required implementation details.
- If data access is uncertain, list alternative datasets or synthetic/system tests.
```

- [ ] **Step 3: Create experiment comparison skill**

Create `skills/research-experiment-comparison/SKILL.md` with:

```markdown
---
name: research-experiment-comparison
description: Use when comparing experiments, baselines, ablations, metrics, tables, completed results, fairness, significance, or result narratives in CS, AI, or engineering research
---

# Research Experiment Comparison

## Overview

Compares completed or planned experimental results with attention to fairness, settings, metrics, statistical meaning, practical meaning, and narrative claims.

## When To Use

- The user has result tables and needs interpretation.
- The user wants baseline fairness checks.
- The user needs ablation analysis or result narrative.
- The user is preparing an experiment section.

## Do Not Use When

- The user needs to design experiments before results exist; use `research-experiment-design`.
- The user needs paper-level literature comparison; use `research-literature-matrix`.
- The user wants results strengthened beyond the data.

## Workflow

1. Extract methods, settings, datasets or systems, metrics, and results.
2. Check whether comparisons are fair under shared settings.
3. Separate statistical, practical, and narrative significance.
4. Interpret ablations by mechanism.
5. Identify threats to validity and missing controls.
6. Draft a restrained result narrative.

## Required Outputs

- Comparison table using `../../shared/templates/experiment-comparison.md`.
- Baseline fairness checklist.
- Ablation interpretation.
- Threats-to-validity notes.
- Result narrative.

## Quality Checks

- Comparisons use consistent settings where possible.
- Missing controls are flagged.
- Metric differences are not overclaimed.
- Result narrative matches the table.

## Failure Modes

- If settings differ, compare cautiously and state the mismatch.
- If variance or statistical evidence is missing, mark significance as unknown.
- If a baseline is unfair, explain the direction of bias.
```

- [ ] **Step 4: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing the remaining paper organization skill file and missing repository files.

- [ ] **Step 5: Commit experiment skills**

Run:

```bash
git add skills/research-experiment-design/SKILL.md skills/research-experiment-comparison/SKILL.md
git commit -m "feat: add experiment research skills"
```

Expected: commit succeeds.

---

### Task 10: Add Paper Organization Skill

**Files:**
- Create: `skills/research-paper-organization/SKILL.md`

- [ ] **Step 1: Create skill directory**

Run:

```bash
mkdir -p skills/research-paper-organization
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Create paper organization skill**

Create `skills/research-paper-organization/SKILL.md` with:

```markdown
---
name: research-paper-organization
description: Use when organizing a paper, thesis chapter, related work, method section, experiment section, contribution narrative, claim-evidence map, or article structure
---

# Research Paper Organization

## Overview

Builds a paper or chapter structure around argument flow, contribution positioning, method clarity, experiment evidence, and claim-evidence alignment.

## When To Use

- The user needs a paper or thesis chapter outline.
- The user wants to organize Related Work, Method, or Experiments.
- The user needs a contribution narrative or claim-evidence map.

## Do Not Use When

- The user needs experiment design before writing; use `research-experiment-design`.
- The user needs reviewer response or submission formatting; reserve that for future extension skills.
- The user wants unsupported claims inserted into the paper.

## Workflow

1. Identify target artifact: conference paper, journal paper, thesis chapter, or report.
2. State the core claim and contribution list.
3. Build section-level argument flow.
4. Structure related work around gaps and positioning.
5. Structure method around assumptions, mechanism, and implementation.
6. Structure experiments around claims, evidence, and limitations.
7. Check the outline with `../../shared/rubrics/paper-structure-rubric.md`.

## Required Outputs

- Paper organization template using `../../shared/templates/paper-organization.md`.
- Section outline.
- Related Work structure.
- Method section skeleton.
- Experiment section skeleton.
- Claim-evidence map.

## Quality Checks

- The structure follows the argument.
- Each claim has planned evidence.
- Related work positions the contribution.
- Limitations and threats to validity are visible.

## Failure Modes

- If the contribution is unclear, ask for the problem, method, and strongest evidence.
- If the outline is generic, rewrite sections around claims and evidence.
- If evidence is missing, mark the claim as unsupported and list what experiment or citation is needed.
```

- [ ] **Step 3: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: FAIL listing missing repository files only.

- [ ] **Step 4: Commit paper organization skill**

Run:

```bash
git add skills/research-paper-organization/SKILL.md
git commit -m "feat: add paper organization research skill"
```

Expected: commit succeeds.

---

### Task 11: Add Repository README And Extensions Documentation

**Files:**
- Create: `README.md`
- Create: `extensions/README.md`

- [ ] **Step 1: Create extension directory**

Run:

```bash
mkdir -p extensions/future-skills
```

Expected: directory exists and command exits 0.

- [ ] **Step 2: Create `README.md`**

Create `README.md` with:

```markdown
# Research Skills

A GitHub-ready collection of independent skills for CS, AI, and engineering graduate research.

## MVP Skills

| Skill | Use When |
| --- | --- |
| `research-topic-selection` | Choosing, narrowing, or comparing research topics |
| `research-proposal` | Preparing opening reports, proposal defenses, or research plans |
| `research-literature-search` | Finding recent papers, search logs, venue tiers, code links, and concise summaries |
| `research-paper-reading` | Deep reading a single paper with translation, generated diagrams, code, formulas, experiment tables, and takeaways |
| `research-literature-matrix` | Organizing papers with methods, venue tiers, code availability, paper types, and summaries |
| `research-method-synthesis` | Classifying surveyed papers into method families with charts and comparison tables |
| `research-idea-mining` | Finding gaps, innovation points, and candidate contributions |
| `research-experiment-design` | Designing experiments, baselines, metrics, and ablations |
| `research-experiment-comparison` | Comparing results, baselines, ablations, and claims |
| `research-paper-organization` | Organizing paper sections and claim-evidence flow |

## Structure

```text
skills/      Independent installable skills
shared/      Templates, rubrics, and reusable references
extensions/  Future skill candidates
scripts/     Repository validation tools
tests/       Validator tests
```

## Installation

Copy any directory under `skills/` into your agent's skills directory. Each skill is independent. Shared templates and rubrics are included in this repository so users can reuse the Markdown artifacts directly.

## Integrity

These skills are designed to support research judgment, not replace it. They require evidence labels for research claims and prohibit fabricated citations, datasets, metrics, and results.

## Validation

Run:

```bash
python3 -m unittest tests/test_validate_research_skills.py
python3 scripts/validate_research_skills.py
```
```

- [ ] **Step 3: Create `extensions/README.md`**

Create `extensions/README.md` with:

```markdown
# Extensions

This directory reserves space for future research skills after the MVP stabilizes.

## Candidate Skills

| Candidate | Purpose |
| --- | --- |
| `research-review-response` | Reviewer comments and response letters |
| `research-submission-check` | Submission checklists and venue formatting |
| `research-thesis-writing` | Thesis chapter planning and long-form structure |
| `research-reproducibility` | Code, environment, seed, and artifact checks |
| `research-figure-planning` | Figure/table narrative and visual argument design |
| `research-poster-slides` | Posters and defense slide planning |
| `research-grant-proposal` | Funding proposal and project application writing |

## Graduation Criteria

A candidate skill moves to `skills/` only when it has:

- Clear trigger conditions.
- A focused workflow.
- Required outputs.
- Quality checks.
- Failure modes.
- A validation scenario.
```

- [ ] **Step 4: Run validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: PASS with `Validation passed.`

- [ ] **Step 5: Commit repository docs**

Run:

```bash
git add README.md extensions/README.md
git commit -m "docs: add repository guide and extensions"
```

Expected: commit succeeds.

---

### Task 12: Final Verification And Cleanup

**Files:**
- Modify only files that fail validation or contain clear consistency errors.

- [ ] **Step 1: Run unit tests**

Run:

```bash
python3 -m unittest tests/test_validate_research_skills.py
```

Expected: PASS with 4 tests.

- [ ] **Step 2: Run repository validator**

Run:

```bash
python3 scripts/validate_research_skills.py
```

Expected: PASS with `Validation passed.`

- [ ] **Step 3: Scan for unresolved draft markers**

Run:

```bash
rg -n "T.?BD|TO.?DO|FIX.?ME|implement[[:space:]]+later|fill[[:space:]]+in[[:space:]]+details|\x{5f85}\x{5b9a}|\x{5360}\x{4f4d}" README.md extensions skills shared docs
```

Expected: no output and exit code 1.

- [ ] **Step 4: Check Git status**

Run:

```bash
git status --short
```

Expected: no output.

- [ ] **Step 5: Review spec coverage**

Check that the implementation satisfies these spec requirements:

- 10 independently installable skills exist under `skills/`.
- Shared templates, rubrics, and references exist under `shared/`.
- Future skill candidates are documented under `extensions/`.
- Research integrity rules are documented.
- Each skill has trigger-focused frontmatter and the required sections.
- Validation commands pass.

- [ ] **Step 6: Commit final fixes only if needed**

If Step 1-5 required corrections, run:

```bash
git add README.md extensions skills shared scripts tests docs
git commit -m "chore: finish research skills mvp validation"
```

Expected: commit succeeds when corrections exist. If no corrections exist, skip this step.

---

## Self-Review Checklist

- Spec coverage: Tasks 1-2 cover validation, Tasks 3-5 cover shared resources, Tasks 6-10 cover all 10 MVP skills, Task 11 covers README and extensions, Task 12 covers final verification.
- Required MVP skills: all 10 approved skill names are included.
- Required shared files: every file named in the design spec is included.
- Trigger descriptions: every skill description starts with `Use when`.
- Validation: unit tests, repository validator, unresolved marker scan, and Git status are included.
