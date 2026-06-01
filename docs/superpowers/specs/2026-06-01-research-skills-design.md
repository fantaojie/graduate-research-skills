# Research Skills Design

## Context

This repository will provide a GitHub-ready collection of independent research skills for computer science, AI, and engineering graduate research. The first release will focus on a compact, high-quality MVP rather than a large but shallow catalog.

The user wants one skill per function, with future expansion room. The approved architecture is:

- MVP skills are flat under `skills/` for easy discovery and installation.
- Shared templates, rubrics, and references live under `shared/`.
- Future or incubating skills live under `extensions/`.

## Goals

- Create 10 independently installable skills for common graduate research workflows.
- Keep each skill focused on one research task with clear trigger conditions, workflow, outputs, and quality checks.
- Support Chinese users while remaining useful for English CS/AI/engineering research contexts.
- Produce structured artifacts that help users make research decisions: topic cards, proposal outlines, literature matrices, method taxonomies, gap analyses, experiment plans, comparison tables, and paper outlines.
- Preserve expansion space for later skills such as reviewer response, submission checks, thesis writing, reproducibility, figure generation, and grant applications.

## Non-Goals

- Do not claim to automate research end to end.
- Do not invent citations, experimental results, benchmarks, or claims.
- Do not require a custom runtime or external service for the first version.
- Do not put all workflows into one oversized skill.
- Do not include large narrative documentation inside every skill when shared templates or references can carry reusable structure.

## Repository Structure

```text
research-skills/
  README.md
  skills/
    research-topic-selection/
      SKILL.md
    research-proposal/
      SKILL.md
    research-literature-search/
      SKILL.md
    research-paper-reading/
      SKILL.md
    research-literature-matrix/
      SKILL.md
    research-method-synthesis/
      SKILL.md
    research-idea-mining/
      SKILL.md
    research-experiment-design/
      SKILL.md
    research-experiment-comparison/
      SKILL.md
    research-paper-organization/
      SKILL.md
  shared/
    references/
      cs-ai-research-principles.md
      citation-integrity.md
      venue-and-code-integrity.md
    templates/
      topic-card.md
      proposal-outline.md
      paper-reading-notes.md
      paper-deep-reading-report.md
      literature-search-results.md
      literature-matrix.md
      method-taxonomy.md
      idea-gap-analysis.md
      experiment-plan.md
      experiment-comparison.md
      paper-organization.md
    rubrics/
      topic-quality-rubric.md
      literature-quality-rubric.md
      experiment-quality-rubric.md
      paper-structure-rubric.md
  extensions/
    README.md
    future-skills/
  docs/
    superpowers/
      specs/
        2026-06-01-research-skills-design.md
```

## MVP Skills

### `research-topic-selection`

Use when the user wants help choosing, narrowing, evaluating, or comparing research topics for CS, AI, or engineering work.

Outputs:

- Research topic card
- Problem definition
- Scope boundary
- Feasibility and risk assessment
- Recommended next validation steps

Quality checks:

- Topic is neither a broad theme nor a trivial implementation task.
- Research question is stated as a testable or arguable problem.
- Required data, methods, compute, and evaluation access are explicit.

### `research-proposal`

Use when the user is preparing an opening report, proposal defense, research plan, thesis proposal, or project proposal.

Outputs:

- Proposal outline
- Research background and significance map
- Technical route
- Work plan and milestone table
- Feasibility, risks, and expected contribution list

Quality checks:

- Proposal connects problem, method, experiment, and expected contribution.
- Technical route is specific enough to execute.
- Risks are not hidden; mitigation is listed.

### `research-literature-search`

Use when the user needs literature search strategy, keywords, database planning, search expansion, or paper collection for CS/AI/engineering topics.

Default behavior when the user gives a topic:

- Search papers from the most recent 3 years unless the prompt specifies another time range.
- Return 30 papers by default unless the prompt specifies another count.
- First search for recent survey/review papers from roughly the most recent year, use them to map subtopics and terminology, then expand to primary research papers.
- Prioritize top conferences and journals when relevance is comparable.

Outputs:

- Search question
- Keyword groups and synonyms
- Database/source plan
- Inclusion/exclusion criteria
- Search log template
- Seed paper list if browsing/search tools are available
- Literature search result table with title, year, venue, venue tier, impact factor when available, open-source status, code URL, paper type, and a summary of no more than 300 Chinese characters per paper

Quality checks:

- Separates exploratory search from systematic search.
- Records search strings and source databases.
- Marks unverified metadata clearly.
- Venue tier, impact factor, CCF class, and open-source URL are verified from current sources when possible, with unknowns labeled instead of guessed.

### `research-paper-reading`

Use when the user provides or references a single paper and wants structured reading notes, critique, method understanding, or implementation-oriented extraction.

Outputs:

- Paper metadata
- Open-source code check performed before the deep reading when the paper mentions code or an official artifact may exist
- Official or likely-official repository URL, key code entry points, and artifact status when available
- Academic Chinese translation of the abstract and user-selected key passages, or a copyright-safe section-by-section Chinese paraphrase when full-text translation is not allowed
- One-paragraph summary
- Problem-method-result-contribution breakdown
- Generated principle diagram for the paper's core idea, using the `imagegen` skill by preference when visual explanation helps reading; Mermaid or text diagrams are fallbacks when image generation is unavailable or the diagram must be deterministic
- Code-level explanation of the core method, using repository file/function pointers or concise pseudocode when code exists
- Formula and algorithm explanation with symbol definitions and intuitive interpretation
- Experiment tables covering datasets, settings, baselines, metrics, key results, and conclusions
- Deep reading report covering core idea, innovation points, experiment process, limitations, and transferable ideas
- Assumptions and limitations
- Reproducibility notes
- Questions for follow-up reading

Quality checks:

- Claims are grounded in the paper text.
- Distinguishes author claims from reader interpretation.
- Does not overstate novelty or results.
- Checks open-source code before explaining implementation details; marks `No code found` or `Not checked` instead of guessing.
- Connects the core innovation to diagram, code or pseudocode, and mathematical principle.
- Makes generated principle diagrams large, readable, and original rather than copying copyrighted paper figures; original paper figures should be referenced by figure number and source.
- Presents experimental data and results as tables, with missing or unverified values marked explicitly.
- Explains the paper in accessible language without losing technical accuracy.
- Does not output a full verbatim translation of a copyrighted paper; translates short user-provided excerpts or open-licensed text and otherwise provides structured paraphrase.

### `research-literature-matrix`

Use when the user has multiple papers and needs organization, comparison, clustering, reading management, or a literature table.

Outputs:

- Literature matrix
- Theme clusters
- Method/dataset/metric comparison
- Chronological development map
- Missing-evidence list
- Publication and artifact fields: year, journal/conference tier, SCI/JCR quartile if applicable, CCF class if applicable, impact factor if available, open-source status, code URL, paper type, and concise summary

Quality checks:

- Compares across papers rather than listing summaries.
- Uses stable columns suitable for later writing.
- Makes unknown fields visible instead of filling guesses.
- Keeps each paper summary under 300 Chinese characters unless the user requests a different length.

### `research-method-synthesis`

Use when the user needs to organize research methods, model families, algorithms, pipelines, theoretical frameworks, or technical approaches from a set of surveyed papers.

Outputs:

- Method taxonomy
- Method family diagram or taxonomy chart
- Paper-to-method mapping table
- Assumption and mechanism table
- Method family explanation table
- Strength/weakness comparison
- Applicable scenarios
- Method selection guidance

Quality checks:

- Groups methods by principle, not only by paper name.
- Every major method family lists representative papers from the surveyed literature.
- Uses charts and tables to make the method landscape readable.
- Separates mechanism, implementation detail, and empirical effect.
- Notes where evidence comes from literature versus inference.

### `research-idea-mining`

Use when the user wants innovation points, research gaps, potential contributions, thesis ideas, or improvement directions based on literature and methods.

Outputs:

- Gap analysis
- Candidate innovation points
- Novelty-feasibility-risk matrix
- Validation plan
- Rejection reasons for weak ideas

Quality checks:

- Innovation points are tied to concrete gaps or limitations.
- Each idea has an evaluation path.
- Avoids vague claims such as "improve accuracy" without mechanism.

### `research-experiment-design`

Use when the user needs an experimental plan for CS/AI/engineering research, including datasets, metrics, protocols, ablations, baselines, controls, or reproducibility planning.

Outputs:

- Experiment plan
- Hypotheses
- Dataset and split plan
- Metric selection
- Baseline and ablation design
- Reproducibility checklist

Quality checks:

- Each experiment answers a research question.
- Metrics match claims.
- Confounders and failure cases are considered.

### `research-experiment-comparison`

Use when the user needs to compare experiments, baselines, ablations, metrics, tables, results, or claims across methods.

Outputs:

- Comparison table design
- Baseline fairness checklist
- Ablation interpretation
- Result narrative
- Threats-to-validity notes

Quality checks:

- Compares under consistent settings where possible.
- Distinguishes statistical, practical, and narrative significance.
- Flags unfair baseline choices or missing controls.

### `research-paper-organization`

Use when the user needs to organize a paper, thesis chapter, related work, method section, experiment section, or contribution narrative.

Outputs:

- Paper outline
- Section-level argument flow
- Related Work structure
- Method section skeleton
- Experiment section skeleton
- Claim-evidence map

Quality checks:

- Paper structure follows the argument, not only a generic template.
- Each claim has planned evidence.
- Related work positions the user's contribution rather than only summarizing papers.

## Shared Resources

Shared references should hold reusable principles that many skills need:

- `cs-ai-research-principles.md`: research questions, contribution types, empirical rigor, reproducibility expectations, and common CS/AI/engineering paper structures.
- `citation-integrity.md`: citation verification rules, anti-hallucination behavior, source confidence labels, and how to mark missing evidence.
- `venue-and-code-integrity.md`: rules for checking publication tier, SCI/JCR quartile, CCF class, impact factor, open-source availability, and code URLs.

Shared templates should be lightweight Markdown files that users can reuse directly. They should avoid long explanations and focus on tables, headings, and fields.

Shared rubrics should be concise score or checklist documents used by skills to self-check outputs. They should not replace user judgment.

## Skill Writing Rules

Each skill must include:

- YAML frontmatter with `name` and trigger-focused `description`.
- A short overview.
- Clear "When to use" and "Do not use when" guidance.
- A compact workflow.
- Required outputs.
- Quality checks.
- Failure modes.
- A short example invocation or output sketch when helpful.

Descriptions must describe triggering conditions, not summarize the workflow. This helps future agents load the right skill instead of treating the description as a shortcut.

Each skill should stay concise. Detailed tables, rubrics, and reusable templates belong in `shared/` or in that skill's own `references/` folder.

## Data Flow

The skills are independent but should compose naturally:

1. `research-topic-selection` produces candidate topic cards.
2. `research-proposal` turns a selected topic into a defensible plan.
3. `research-literature-search` builds the paper set.
4. `research-paper-reading` extracts trustworthy notes from individual papers.
5. `research-literature-matrix` organizes multiple papers.
6. `research-method-synthesis` turns papers into method-level understanding.
7. `research-idea-mining` identifies gaps and contribution candidates.
8. `research-experiment-design` turns claims into experiments.
9. `research-experiment-comparison` interprets and compares results.
10. `research-paper-organization` turns the work into an article structure.

No skill should assume previous skills were run. Each skill may accept user-provided inputs from any source and should state missing prerequisites explicitly.

## Error Handling and Integrity

Skills must handle incomplete inputs by making missing information visible. They should ask only essential clarifying questions when ambiguity blocks meaningful progress.

All research claims should be labeled as one of:

- Verified from provided source
- Retrieved from current search
- Inferred from available context
- Hypothesis requiring validation
- Unknown or missing

Skills must never fabricate citations, paper metadata, datasets, metrics, experimental results, or benchmark standings.

## Validation

Initial validation should include static checks and scenario checks:

- Every MVP skill has a valid `SKILL.md`.
- Every skill frontmatter has `name` and a trigger-focused `description`.
- Referenced shared templates and rubrics exist.
- Skill names use lowercase letters, digits, and hyphens.
- Example prompts trigger the intended skill boundaries.

Scenario checks should cover:

- A broad topic request.
- A proposal request.
- A single-paper reading request.
- A 10-paper literature organization request.
- An innovation-point request.
- An experiment design request.
- A baseline comparison request.
- A paper outline request.

## Expansion Plan

The `extensions/` directory should reserve space for future skills without bloating the MVP:

- `research-review-response`: reviewer comments and response letter.
- `research-submission-check`: submission checklist and venue formatting.
- `research-thesis-writing`: thesis chapter planning and long-form structure.
- `research-reproducibility`: code, environment, seed, and artifact checks.
- `research-figure-planning`: figure/table narrative and visual argument design.
- `research-poster-slides`: poster and defense slide planning.
- `research-grant-proposal`: funding proposal and project application writing.

Future skills should graduate from `extensions/future-skills/` to `skills/` only after they have clear trigger conditions, outputs, and validation scenarios.

## Implementation Sequence

1. Create shared templates, references, and rubrics.
2. Create the 10 MVP skill directories and `SKILL.md` files.
3. Add a repository README explaining installation and skill list.
4. Add extension documentation for future skill candidates.
5. Add lightweight validation scripts or checks if useful.
6. Run validation and revise unclear trigger descriptions.

## Open Decisions Resolved

- Target field: computer science, AI, and engineering.
- Release shape: GitHub repository containing multiple independently installable skills.
- MVP scope: 10 core skills.
- Architecture: flat `skills/` for MVP, `shared/` for reusable resources, `extensions/` for future growth.
