---
name: research-literature-matrix
description: Use when a graduate researcher has multiple papers and needs a literature matrix, comparison table, clustering, chronology, or reading-management structure.
---

# Research Literature Matrix

## Overview

Convert a paper list into a structured comparison matrix that supports later related work writing, method synthesis, and idea mining. Use `../../shared/templates/literature-matrix.md`, `../../shared/templates/literature-search-results.md`, `../../shared/references/citation-integrity.md`, `../../shared/references/venue-and-code-integrity.md`, and `../../shared/rubrics/literature-quality-rubric.md`.

## When To Use

- The user already has papers from search, reading notes, PDFs, or citations.
- The user wants to organize papers by method, dataset, metric, venue, code, or limitations.
- The user asks for a literature table, matrix, comparison, timeline, or clustering.
- The user wants an artifact that can feed method synthesis or related work writing.

## Do Not Use When

- The user still needs to find papers; use `research-literature-search`.
- The user gives one paper; use `research-paper-reading`.
- The user asks for method taxonomy and explanation; use `research-method-synthesis`.
- The user asks for final paper outline; use `research-paper-organization`.

## Workflow

1. Normalize paper metadata: title, year, venue, venue tier, SCI/JCR, CCF, impact factor, paper type, code status, and URL.
2. Extract comparable fields: problem, method, dataset, metrics, main result, limitations, and evidence status.
3. Keep each paper summary under 300 Chinese characters unless the user requests another limit.
4. Cluster papers by theme, method family, data type, application scenario, or chronology.
5. Build a timeline showing how the field has developed.
6. Identify missing evidence and fields requiring verification.
7. Recommend which papers deserve deep reading.

## Required Outputs

- Literature matrix following `../../shared/templates/literature-matrix.md`.
- Theme clusters.
- Method, dataset, and metric comparison.
- Chronological development map.
- Missing-evidence list.
- Recommended priority list for paper reading.

## Quality Checks

- The matrix compares across papers rather than only summarizing them.
- Stable columns support later writing and method synthesis.
- Unknown metadata is visible.
- Venue and code fields follow `../../shared/references/venue-and-code-integrity.md`.
- Paper summaries stay within the requested length.
- Evidence labels follow `../../shared/references/citation-integrity.md`.

## Failure Modes

- If metadata is incomplete, include the paper but mark unknown fields.
- If papers cover unrelated subtopics, split the matrix into separate clusters.
- If summaries are too long, compress them into problem-method-result-limitation form.
- If there are too many papers, prioritize by relevance, recency, and venue quality.

