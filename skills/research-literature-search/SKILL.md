---
name: research-literature-search
description: Use when a graduate researcher needs literature search, recent paper collection, keyword expansion, source planning, or a paper list for a CS, AI, or engineering topic.
---

# Research Literature Search

## Overview

Collect and organize recent literature with transparent search strategy, source traceability, venue and code checks, and concise paper summaries. Use `../../shared/templates/literature-search-results.md`, `../../shared/references/citation-integrity.md`, `../../shared/references/venue-and-code-integrity.md`, and `../../shared/rubrics/literature-quality-rubric.md`.

## When To Use

- The user gives a topic and asks for recent papers.
- The user requests a literature search strategy, keywords, databases, or paper set.
- The user specifies a count such as 10, 30, or 50 papers.
- The user asks for venue tier, SCI/JCR quartile, CCF class, impact factor, code availability, or paper type.
- The user wants a seed paper list before literature matrix or method synthesis.

## Do Not Use When

- The user provides one paper and wants deep reading; use `research-paper-reading`.
- The user already has a paper set and wants comparison columns; use `research-literature-matrix`.
- The user wants innovation points after reading papers; use `research-idea-mining`.
- Search access is unavailable and the user needs current metadata; explain what cannot be verified.

## Workflow

1. Parse topic, field, time range, paper count, language, and preferred sources. Default to the most recent 3 years and 30 papers when the user does not specify.
2. Build keyword groups: core concept, synonyms, task names, method names, application domain, and exclusion terms.
3. Search first for recent survey or review papers from roughly the most recent year. Use them to identify subtopics, terminology, representative methods, benchmarks, and cited primary papers.
4. Expand to primary papers from the requested time range. Prefer top conferences and journals when relevance is comparable.
5. Deduplicate papers by title, DOI, arXiv ID, and venue version.
6. For each included paper, verify title, year, venue, venue type, SCI/JCR quartile when applicable, CCF class when applicable, impact factor when available, and metric source/access date when possible.
7. Check open-source status using paper links, project pages, author pages, Papers With Code, GitHub, Zenodo, or official organization pages. Record official versus unofficial status.
8. Assign paper type labels: survey or review, method innovation, dataset or benchmark, system or tool, empirical evaluation, theory or analysis, application study, reproducibility or replication, position or perspective.
9. Produce the result table and a short search narrative. Each paper summary must be no more than 300 Chinese characters unless the user requests another length.

## Required Outputs

- Search scope: topic, date range, target count, sources, search date.
- Search strategy table with queries, sources, and purpose.
- Literature result table with title, year, venue, venue tier, SCI/JCR, CCF, impact factor, open-source status, code URL, paper type, and concise summary.
- Excluded paper list when useful.
- Unverified metadata list with reasons.
- Suggested next steps: matrix, paper reading, or method synthesis.

## Quality Checks

- Recent survey-first strategy is visible.
- Search strings and source databases are recorded.
- Venue tier, impact factor, CCF class, and code URL are verified from current sources when possible.
- Unknown metadata is written as `Unknown`; do not guess.
- Top venues are prioritized only when relevant.
- Summaries are concise and do not exceed the requested length.
- Evidence labels follow `../../shared/references/citation-integrity.md`.

## Failure Modes

- If browsing/search tools are unavailable, provide a search plan and mark current metadata as not verified.
- If fewer papers exist in the requested range, report the actual count and explain the shortage.
- If venue tier or impact factor cannot be verified, write `Unknown` and keep the paper if it is relevant.
- If code links are ambiguous, label them unofficial unless the paper or authors clearly link them.
- If a topic is too broad, split it into subtopics before collecting the full paper set.

