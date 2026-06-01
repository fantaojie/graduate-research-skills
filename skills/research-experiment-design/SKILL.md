---
name: research-experiment-design
description: Use when a graduate researcher needs to design experiments, datasets, metrics, baselines, ablations, controls, or reproducibility plans for CS, AI, or engineering research.
---

# Research Experiment Design

## Overview

Design experiments that test specific research claims with appropriate datasets, metrics, baselines, ablations, controls, and reproducibility details. Use `../../shared/templates/experiment-plan.md`, `../../shared/rubrics/experiment-quality-rubric.md`, and `../../shared/references/cs-ai-research-principles.md`.

## When To Use

- The user has a research idea or method and needs an experiment plan.
- The user asks for datasets, metrics, baselines, ablations, controls, or protocols.
- The user wants to validate a hypothesis or contribution.
- The user needs a reproducibility checklist before implementation.

## Do Not Use When

- The user only needs to compare existing results; use `research-experiment-comparison`.
- The user is still selecting a topic; use `research-topic-selection`.
- The user is still mining ideas; use `research-idea-mining`.
- The user asks for final paper structure; use `research-paper-organization`.

## Workflow

1. Identify the claim, hypothesis, task, target dataset/domain, and constraints.
2. Decompose the claim into experiments: main performance, ablation, robustness, efficiency, generalization, failure analysis, and qualitative analysis when appropriate.
3. Choose datasets, splits, preprocessing, and data access plan.
4. Select metrics that match the claim and list their limitations.
5. Select baselines and fairness requirements.
6. Design ablations that isolate components rather than cosmetic variants.
7. Define controls, confounders, random seeds, hardware, implementation details, and reporting format.
8. Produce a staged experiment plan with minimal first validation before expensive full experiments.

## Required Outputs

- Hypothesis and claim table.
- Dataset and split plan.
- Metric selection with limitations.
- Baseline and fairness checklist.
- Ablation plan.
- Robustness, efficiency, or failure analysis plan when relevant.
- Reproducibility checklist.

## Quality Checks

- Each experiment answers a research question.
- Metrics match claims.
- Baselines are fair and comparable.
- Ablations isolate meaningful components.
- Confounders and failure cases are considered.
- Reproducibility fields follow `../../shared/rubrics/experiment-quality-rubric.md`.

## Failure Modes

- If the claim is vague, rewrite it as a hypothesis before designing experiments.
- If datasets are inaccessible, propose proxy datasets or simulation plans and mark limitations.
- If baselines are unavailable, propose reproduction, official reported numbers with caution, or simpler baselines.
- If compute is limited, recommend staged experiments and smaller validation.

