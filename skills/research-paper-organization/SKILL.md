---
name: research-paper-organization
description: Use when a graduate researcher needs to organize a paper, thesis chapter, related work, method section, experiment section, or contribution narrative.
---

# Research Paper Organization

## Overview

Turn research materials into a coherent paper or thesis chapter structure with section-level argument flow, contribution claims, related work positioning, method skeleton, experiment skeleton, and claim-evidence map. Use `../../shared/templates/paper-organization.md`, `../../shared/rubrics/paper-structure-rubric.md`, and `../../shared/references/cs-ai-research-principles.md`.

## When To Use

- The user needs a paper outline or thesis chapter outline.
- The user asks how to write related work, method, experiments, or contribution narrative.
- The user has methods and experiments but needs structure.
- The user wants to map claims to figures, tables, and evidence.

## Do Not Use When

- The user needs literature search; use `research-literature-search`.
- The user needs method taxonomy first; use `research-method-synthesis`.
- The user needs experiment design first; use `research-experiment-design`.
- The user asks for a full proposal rather than paper structure; use `research-proposal`.

## Workflow

1. Identify paper type, target venue or thesis requirement, audience, central claim, contribution list, and available evidence.
2. Build the argument path: problem, gap, insight, method, evidence, limitations, and conclusion.
3. Draft section outline with each section's purpose, key claims, and required evidence.
4. Organize related work by themes and gaps, not by one-paper-one-paragraph summaries.
5. Create method section skeleton with inputs, assumptions, modules, algorithms, and complexity when relevant.
6. Create experiment section skeleton with research questions, datasets, metrics, baselines, main results, ablations, and limitations.
7. Build a claim-evidence map linking claims to figures, tables, experiments, or citations.

## Required Outputs

- Paper or chapter outline using `../../shared/templates/paper-organization.md`.
- Section-level argument flow.
- Related work structure.
- Method section skeleton.
- Experiment section skeleton.
- Claim-evidence map.
- Writing risks and missing evidence list.

## Quality Checks

- Structure follows the argument rather than a generic template.
- Each major claim has planned evidence.
- Related work positions the contribution.
- Contributions are specific and not overstated.
- The outline can be used directly as a writing plan.

## Failure Modes

- If the central claim is unclear, ask for or infer candidate claims before outlining.
- If evidence is missing, mark the section as blocked by evidence rather than filling unsupported text.
- If related work is a list, regroup it by themes and gaps.
- If the target venue has strict format requirements, request or verify those requirements before final formatting.

