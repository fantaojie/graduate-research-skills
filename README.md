# Graduate Research Skills

[English](README.md) | [简体中文](README.zh-CN.md)

This repository contains a GitHub-ready collection of modular research skills for Chinese-speaking graduate students and research assistants in computer science, AI, engineering, computer application, and related majors.

The skill set is built for the real graduation workflow of many Mainland China computer-related graduate programs, where students often need two smaller research papers plus a main thesis or dissertation. It covers the path from topic selection and proposal writing to literature search, paper reading, method synthesis, experiment design, result comparison, and paper organization, helping protect your graduation journey one research step at a time.

This is not a one-click paper generator. It is an interactive research companion: it asks, guides, checks, organizes, and helps you think through computer-related research. The project will keep improving over time. Everyone is welcome to use it, follow it, and contribute ideas.

Each skill is an independent `SKILL.md` directory under `skills/`. Shared templates, rubrics, and integrity references live under `shared/` so the skills stay compact while still producing structured research artifacts.

## Skill Index

| Skill | Use Case |
| --- | --- |
| `research-topic-selection` | Choose, narrow, and evaluate a research topic. |
| `research-proposal` | Draft an opening report, thesis proposal, or project proposal. |
| `research-literature-search` | Search and collect recent literature with venue, code, and metadata checks. |
| `research-paper-reading` | Deep-read a single paper with code, diagrams, math, and experiments. |
| `research-literature-matrix` | Organize multiple papers into a comparison matrix. |
| `research-method-synthesis` | Classify methods from surveyed papers and explain method families. |
| `research-idea-mining` | Mine gaps, innovation points, and feasible contribution directions. |
| `research-experiment-design` | Design datasets, metrics, baselines, ablations, and protocols. |
| `research-experiment-comparison` | Compare experiments, baselines, ablations, and result claims. |
| `research-paper-organization` | Organize a paper, thesis chapter, or related work narrative. |

## Installation

Copy one or more skill directories from `skills/` into your Codex skills directory, or install this repository as a source of reusable skill folders if your Codex setup supports repository-based skill installation.

Typical local copy shape:

```text
~/.codex/skills/research-literature-search/SKILL.md
~/.codex/skills/research-paper-reading/SKILL.md
```

Keep the `shared/` directory beside the repository during development. When copying a skill elsewhere, also copy the shared files it references or adapt the paths.

## Validation

Run the structural checks before publishing:

```bash
python3 -m unittest tests/test_validate_research_skills.py
python3 scripts/validate_research_skills.py
```

The validator checks required files, skill frontmatter, required skill sections, and unresolved draft markers.

## Integrity Rules

These skills are designed to be research assistants, not citation generators. They must:

- Never fabricate papers, venues, code links, metrics, or experimental results.
- Mark unknown metadata explicitly.
- Separate verified evidence from inference.
- Prefer current source checks for recent literature, venue tiers, impact factors, CCF class, and open-source status.
