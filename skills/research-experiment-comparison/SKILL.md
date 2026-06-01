---
name: research-experiment-comparison
description: Use when a graduate researcher needs to compare experiments, baselines, ablations, metrics, result tables, or empirical claims across methods.
---

# Research Experiment Comparison

## Overview

Compare results fairly across methods by aligning datasets, protocols, metrics, compute, baselines, and evidence status. Use `../../shared/templates/experiment-comparison.md`, `../../shared/rubrics/experiment-quality-rubric.md`, and `../../shared/references/citation-integrity.md`.

## When To Use

- The user has experimental results and wants comparison tables or interpretation.
- The user asks whether baselines are fair.
- The user wants to compare ablations, metrics, or reported claims across papers.
- The user needs a result narrative for a paper or thesis.

## Do Not Use When

- The user needs to design experiments from scratch; use `research-experiment-design`.
- The user needs to collect papers first; use `research-literature-search`.
- The user asks to organize all paper sections; use `research-paper-organization`.
- The user asks for method taxonomy; use `research-method-synthesis`.

## Workflow

1. Gather methods, datasets, protocols, metrics, result values, and source evidence.
2. Normalize comparison units: same split, same metric definition, same preprocessing, comparable training data, and comparable compute when possible.
3. Build comparison tables with a setting-match column.
4. Interpret main results, ablations, efficiency, robustness, and failure cases.
5. Flag unfair or missing baselines.
6. Separate statistical significance, practical significance, and narrative significance.
7. Draft a concise result narrative and threats-to-validity notes.

## Required Outputs

- Result comparison table using `../../shared/templates/experiment-comparison.md`.
- Baseline fairness checklist.
- Ablation interpretation table.
- Result narrative.
- Threats-to-validity notes.
- Missing evidence or verification list.

## Quality Checks

- Comparisons use consistent settings where possible.
- Unmatched settings are visible.
- The narrative does not overstate small or unsupported gains.
- Missing controls and unfair baselines are flagged.
- Claims follow `../../shared/references/citation-integrity.md`.

## Failure Modes

- If settings differ, compare cautiously and explain the mismatch.
- If result values are unverified, mark them as unverified rather than treating them as final.
- If metrics conflict, explain metric definitions before ranking methods.
- If no fair comparison is possible, provide a qualitative comparison and list required evidence.

