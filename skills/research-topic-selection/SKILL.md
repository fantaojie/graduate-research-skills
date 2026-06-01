---
name: research-topic-selection
description: Use when a graduate researcher wants to choose, narrow, compare, or evaluate possible CS, AI, engineering, thesis, or paper research topics.
---

# Research Topic Selection

## Overview

Turn broad interests into researchable topics with explicit problem boundaries, contribution type, feasibility, risk, and validation path. Use `../../shared/templates/topic-card.md`, `../../shared/rubrics/topic-quality-rubric.md`, and `../../shared/references/cs-ai-research-principles.md` when the user needs a reusable artifact.

## When To Use

- The user has a broad field and wants a thesis, paper, or project direction.
- The user has several candidate topics and needs comparison.
- The user wants to judge whether a topic has research value, novelty, or feasibility.
- The user asks for topic narrowing, research questions, or opening-report direction.

## Do Not Use When

- The user asks for a full proposal draft; use `research-proposal`.
- The user already has a topic and asks for papers; use `research-literature-search`.
- The user asks to classify methods from a paper set; use `research-method-synthesis`.
- The user asks to design experiments for a fixed method; use `research-experiment-design`.

## Workflow

1. Clarify the user's field, degree stage, time budget, available data, compute, coding ability, and expected output if these are not obvious.
2. Convert broad interests into 3 to 5 candidate topic cards.
3. For each candidate, identify the problem, research question, contribution type, evaluation target, required resources, and likely risks.
4. Score candidates using the topic quality rubric: specificity, research value, feasibility, evaluation, and risk visibility.
5. Recommend one primary topic and one backup topic with a short reason.
6. Provide next validation steps, usually including seed literature search, feasibility check, baseline reproduction check, and experiment sketch.

## Required Outputs

- Candidate topic cards following `../../shared/templates/topic-card.md`.
- A comparison table with novelty, feasibility, risk, data access, compute need, and evaluation clarity.
- A recommended topic and backup topic.
- Research question in a testable or arguable form.
- Immediate next steps for validation.

## Quality Checks

- The topic is narrower than a broad theme and stronger than an implementation wish.
- The topic states task, context, limitation, proposed direction, and evaluation target.
- Required data, methods, compute, and evaluation access are explicit.
- The recommendation explains trade-offs instead of only ranking by excitement.
- Research claims are labeled using `../../shared/references/citation-integrity.md`.

## Failure Modes

- If the user's field is too broad, propose scoped candidate directions and ask for the most promising one.
- If data or compute access is unclear, mark feasibility as uncertain and suggest low-resource alternatives.
- If novelty cannot be judged without literature search, label it as a hypothesis requiring validation.
- If all candidate topics are weak, explain why and propose narrower replacements.

