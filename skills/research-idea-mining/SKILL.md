---
name: research-idea-mining
description: Use when a graduate researcher wants research gaps, innovation points, contribution ideas, thesis directions, or improvement opportunities from literature and methods.
---

# Research Idea Mining

## Overview

Mine feasible innovation points from literature gaps, method limitations, dataset weaknesses, evaluation blind spots, and deployment constraints. Use `../../shared/templates/idea-gap-analysis.md`, `../../shared/templates/method-taxonomy.md`, `../../shared/rubrics/topic-quality-rubric.md`, and `../../shared/references/citation-integrity.md`.

## When To Use

- The user asks for innovation points or research gaps.
- The user has a literature matrix or method synthesis and wants contribution directions.
- The user needs thesis or paper ideas with novelty, feasibility, risk, and validation plan.
- The user wants to reject weak ideas before spending time.

## Do Not Use When

- The user needs literature collection first; use `research-literature-search`.
- The user needs method classification first; use `research-method-synthesis`.
- The user needs a full proposal; use `research-proposal`.
- The user needs experiment protocol for a selected idea; use `research-experiment-design`.

## Workflow

1. Extract gaps from papers and method synthesis: assumptions, failure cases, missing datasets, weak metrics, limited domains, high cost, privacy risk, robustness gaps, or reproducibility gaps.
2. Convert gaps into candidate innovation points with a mechanism, not only a desired outcome.
3. Score each idea by novelty, feasibility, risk, evaluation clarity, resource need, and expected contribution.
4. Reject weak ideas with explicit reasons.
5. For promising ideas, define hypothesis, method sketch, required data, baselines, metrics, and first validation experiment.
6. Recommend one primary idea and one backup idea.

## Required Outputs

- Gap analysis table.
- Candidate innovation point matrix.
- Novelty-feasibility-risk assessment.
- Validation plan for each strong idea.
- Rejection reasons for weak ideas.
- Recommended direction and next actions.

## Quality Checks

- Each innovation point is tied to a concrete gap or limitation.
- Each idea has a mechanism and evaluation path.
- Vague claims such as "improve accuracy" are rewritten or rejected.
- Risks and resource requirements are visible.
- Evidence labels follow `../../shared/references/citation-integrity.md`.

## Failure Modes

- If literature evidence is missing, produce hypotheses and request literature validation.
- If ideas are too broad, split them into smaller testable variants.
- If ideas are too incremental, identify stronger mechanism changes or reject them.
- If feasibility is low, propose lower-cost experiments or simulation-first validation.

