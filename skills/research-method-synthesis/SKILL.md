---
name: research-method-synthesis
description: Use when a graduate researcher needs to classify methods, model families, algorithms, pipelines, or technical approaches from surveyed papers.
---

# Research Method Synthesis

## Overview

Turn a literature matrix or paper set into a method-level landscape. Group methods by principle, explain each family, map papers to families, and present the result with charts and tables. Use `../../shared/templates/method-taxonomy.md`, `../../shared/templates/literature-matrix.md`, `../../shared/references/cs-ai-research-principles.md`, and `../../shared/references/citation-integrity.md`.

## When To Use

- The user has surveyed papers and wants method classification.
- The user asks for method families, technical routes, model taxonomy, algorithm comparison, or pipeline comparison.
- The user wants charts and tables summarizing a field.
- The user needs material for related work, proposal method section, or innovation mining.

## Do Not Use When

- The user still needs to collect papers; use `research-literature-search`.
- The user needs a matrix before synthesis; use `research-literature-matrix`.
- The user asks for a single paper explanation; use `research-paper-reading`.
- The user wants new ideas from the synthesis; use `research-idea-mining` after this skill.

## Workflow

1. Read the available literature matrix, paper summaries, or user-provided paper list.
2. Identify grouping dimensions: learning paradigm, architecture, supervision signal, data requirement, objective function, pipeline stage, threat model, or deployment scenario.
3. Group methods by underlying principle, not only by paper name or publication year.
4. Produce a method family chart. Use Mermaid, a generated diagram, or a compact taxonomy table.
5. For each method family, explain representative papers, core mechanism, key assumptions, strengths, weaknesses, and best-fit scenarios.
6. Build a paper-to-method mapping table.
7. Build a method comparison matrix across inputs, training cost, inference cost, robustness, interpretability, and reproducibility.
8. Add selection guidance: when to choose each method family and what evidence is still missing.

## Required Outputs

- Method taxonomy or family chart.
- Method family explanation table.
- Paper-to-method mapping table.
- Method comparison matrix.
- Strengths, weaknesses, assumptions, and applicable scenarios.
- Evidence notes distinguishing literature facts from inference.

## Quality Checks

- Methods are grouped by mechanism or assumption, not only labels.
- Every major method family lists representative papers.
- Charts and tables make the landscape easy to scan.
- Mechanism, implementation detail, and empirical effect are separated.
- Evidence status follows `../../shared/references/citation-integrity.md`.
- The synthesis can feed idea mining or paper organization.

## Failure Modes

- If the paper set is too small, label the taxonomy as preliminary.
- If method families overlap, create a cross-cutting dimension table instead of forcing one hierarchy.
- If a paper lacks method detail, map it with low confidence and explain why.
- If the user asks for novelty claims, mark them as requiring literature validation unless evidence is available.

