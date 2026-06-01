---
name: research-paper-reading
description: Use when a graduate researcher provides or names a single paper and needs deep reading, academic Chinese explanation, code inspection, formulas, diagrams, experiments, or transferable ideas.
---

# Research Paper Reading

## Overview

Produce a deep reading report for one paper. The report should explain the paper in academic Chinese, check code availability first, and connect the core idea through an original principle diagram, code or pseudocode, mathematical explanation, experiment tables, innovation points, limitations, and transferable ideas. Use `../../shared/templates/paper-deep-reading-report.md`, `../../shared/templates/paper-reading-notes.md`, `../../shared/references/citation-integrity.md`, and `../../shared/references/venue-and-code-integrity.md`.

## When To Use

- The user gives one paper title, PDF, URL, DOI, arXiv ID, or citation.
- The user asks to "read", "deep-read", "explain", "translate", "精读", or "复现" one paper.
- The user asks for formulas, method diagrams, code-level explanation, innovation points, experiments, or lessons to borrow.
- The user asks whether the paper has official code or how the method maps to implementation.

## Do Not Use When

- The user asks for many papers; use `research-literature-search` or `research-literature-matrix`.
- The user asks to classify methods across a paper set; use `research-method-synthesis`.
- The user requests full verbatim translation of a copyrighted paper. Provide short excerpt translation or structured paraphrase instead.
- The user asks for experiment design for their own work; use `research-experiment-design`.

## Workflow

1. Identify the exact paper version. Verify title, authors, year, venue, paper URL, and PDF/source when available.
2. Before deep reading, search for official code, artifact, project page, dataset, checkpoint, or reproduction. Prefer links from the paper, project page, authors, venue artifact pages, GitHub, Zenodo, or Papers With Code.
3. Record code status: official code available, unofficial reproduction available, artifact mentioned but unavailable, no code found, or not checked. If code exists, list repository URL, key entry files, key functions/classes, and license or artifact notes when visible.
4. Provide academic Chinese translation of the abstract and user-selected short passages. For copyrighted full papers, provide section-by-section Chinese paraphrase rather than full verbatim translation.
5. Explain the paper in this order: problem, motivation, core idea, method pipeline, formulas, algorithm, experiments, results, limitations, and transferable ideas.
6. Use an original large, readable principle diagram by preference. If `$imagegen` or an image generation tool is available, use it to generate the core concept diagram. If unavailable, use Mermaid or text diagrams. Reference original paper figures by figure number and source instead of copying them.
7. Connect the diagram to code or pseudocode and to mathematical principles. Explain symbols, operations, and intuition.
8. Present experiment data as tables: datasets, settings, baselines, metrics, main results, ablations, and conclusions. Mark unverified values.
9. End with innovation points, what can be borrowed, limitations, and follow-up reading questions.

## Required Outputs

- Paper metadata table.
- Code availability first check with repository URL, key files, and key functions/classes when available.
- Academic Chinese translation or copyright-safe Chinese paraphrase.
- One-paragraph summary.
- Original principle diagram or fallback diagram.
- Mathematical principle table and formula explanation.
- Code-level explanation using real code pointers or concise pseudocode.
- Innovation points, experiment process, limitations, and transferable ideas.
- Experiment result tables.
- Evidence status for claims and missing information.

## Quality Checks

- Code search happens before implementation explanation.
- `No code found` or `Not checked` is used instead of guessing.
- The core innovation is explained through diagram, code or pseudocode, and math.
- Generated diagrams are original, readable, and large enough for study notes.
- Experimental data is presented in tables.
- Author claims are separated from reader interpretation.
- Copyright limits are respected for translation.
- Claims follow `../../shared/references/citation-integrity.md`.

## Failure Modes

- If the paper title is ambiguous, ask for the exact URL, DOI, arXiv ID, or author/year.
- If code is found but is large, inspect only the core files needed to explain the method.
- If code cannot be accessed, provide pseudocode and mark repository details as unavailable.
- If formulas are missing in the paper, explain the algorithmic principle and mark the derivation as inferred.
- If image generation fails, provide Mermaid or a text diagram and state that it is a fallback.

