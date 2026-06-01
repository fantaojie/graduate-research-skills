---
name: research-proposal
description: Use when a graduate researcher is preparing an opening report, thesis proposal, proposal defense, project proposal, or research plan.
---

# Research Proposal

## Overview

Transform a selected topic into a defensible proposal with problem background, literature basis, objectives, technical route, experiments, milestones, risks, and expected contributions. Use `../../shared/templates/proposal-outline.md`, `../../shared/rubrics/topic-quality-rubric.md`, and `../../shared/references/cs-ai-research-principles.md`.

## When To Use

- The user needs a thesis opening report or proposal defense draft.
- The user has a topic and wants background, significance, objectives, route, and timeline.
- The user needs to turn literature and method ideas into a research plan.
- The user asks whether a proposal is coherent or defensible.

## Do Not Use When

- The user only needs topic choice; use `research-topic-selection`.
- The user only needs paper collection; use `research-literature-search`.
- The user asks for final paper structure; use `research-paper-organization`.
- The user needs detailed experiment protocol only; use `research-experiment-design`.

## Workflow

1. Identify the topic, research question, target domain, expected contribution, available resources, and deadline.
2. Build the proposal outline from problem motivation to method and experiments.
3. Map background and related work into a gap narrative.
4. Define objectives, technical route, deliverables, milestone table, and expected contribution list.
5. Add feasibility analysis: data, method, compute, implementation, supervision, and publication risk.
6. Add risk mitigations and backup plans.
7. Check that each planned contribution has a validation path.

## Required Outputs

- Proposal outline using `../../shared/templates/proposal-outline.md`.
- Background and significance map.
- Research objectives and contribution list.
- Technical route with staged inputs and outputs.
- Work plan and milestone table.
- Feasibility, risks, and mitigation table.

## Quality Checks

- The proposal connects problem, method, experiment, and expected contribution.
- Technical route is specific enough to execute.
- Literature basis supports the gap rather than only listing papers.
- Risks are visible and mitigations are practical.
- Claims and citations follow `../../shared/references/citation-integrity.md`.

## Failure Modes

- If the topic is not fixed, return to topic selection before drafting a full proposal.
- If literature evidence is thin, mark the proposal as preliminary and request a literature search.
- If the technical route is vague, split it into modules, inputs, outputs, and validation points.
- If the expected contribution is overstated, rewrite it as a testable claim.

