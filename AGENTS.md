# AGENTS.md

Guidance for Codex CLI and other coding agents working on this EuroPLoP 2026 LaTeX repository.

## Project purpose

This repository contains the EuroPLoP 2026 paper:

> A Pattern Collection for Generating Accessible Teaching Materials in STEM

The paper extends the EuroPLoP 2025 pattern collection for accessible STEM teaching materials. The current revision goal is to prepare a polished final submission that responds to the shepherd feedback, especially by strengthening the pattern form, the forces, the problem statements, the resulting contexts, and the relationship to the existing pattern language.

## Primary source files

- `main.tex` is the root LaTeX file.
- `preamble.tex` contains package configuration and PDF metadata.
- `title_abstract.tex` contains title, authors, abstract, and keywords.
- `introduction.tex` contains the introduction.
- `6_Pattern.tex` contains the AI Tutor pattern.
- `7_Pattern.tex` contains the audio-summary pattern.
- `Conclusion_and_Future_Work.tex` contains the conclusion/future-work section.
- `acronyms.tex` contains acronyms.
- `literature.bib` contains BibTeX entries.

Do not rename included `.tex` files unless you also update `main.tex`.

## Build commands

Use the Makefile targets whenever possible:

```bash
make pdf      # build main.pdf with latexmk
make check    # build and run lightweight repository checks
make clean    # remove LaTeX build artifacts
```

Equivalent direct command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The project assumes a TeX Live installation with at least:

- `latexmk`
- `pdflatex`
- BibTeX
- Springer LNCS support (`llncs.cls`, `splncs04.bst`, usually via `texlive-publishers`)
- common LaTeX packages used in `preamble.tex`, including `acronym`, `comment`, `graphicx`, `hyperref`, `listings`, `mdframed`, `subcaption`, `tabularx`, `todonotes`, and `xcolor`

## Required checks before a PR is ready

Run:

```bash
make check
```

Then inspect the generated `main.pdf` manually. A successful build alone is not sufficient.

Before marking a PR as ready, verify:

- no visible `TODO`, `todo`, `\todo{...}`, or placeholder text remains in the PDF,
- all citations and cross-references are resolved,
- `literature.bib` contains no duplicate BibTeX keys,
- the PDF title metadata is no longer `Overleaf Example`,
- generated artifacts such as `main.pdf`, `.aux`, `.bbl`, `.blg`, `.fdb_latexmk`, `.fls`, `.log`, `.out`, and `.synctex.gz` are not committed,
- the paper still uses the Springer LNCS style correctly.

## Writing and revision guidelines

### Pattern-writing priorities

The shepherd feedback makes the following points central for the revision:

1. Forces are the heart of the pattern. They must describe genuine tensions, not just constraints or requirements.
2. Problem statements must be sharp and should not merely describe a situation.
3. Tool names such as Custom GPT, NotebookLM, or PDF-reader podcast features should appear as examples or known uses, not as the abstract solution itself.
4. Resulting contexts should describe the new situation after applying a pattern and should point to follow-up patterns or remaining tensions.
5. Related work should be consolidated into one paper-level section instead of long per-pattern related-work sections.
6. The relationship to the EuroPLoP 2025 pattern collection must be explicit.

### Preferred pattern structure

For each pattern, keep the structure regular:

```text
Pattern name
Context
Problem
Forces
Solution
Resulting Context
Known Uses
Consequences / Liabilities
Related Patterns
```

### Terminology

Use terminology consistently:

- `BVI students` = blind and visually impaired students.
- `STEM` = Science, Technology, Engineering, and Mathematics.
- Prefer `accessibility-aware AI tutor` over generic `AI tutor` when referring to the revised Pattern 6.
- Prefer `structured audio companion` over generic `podcast-like summary` when referring to the revised Pattern 7, unless discussing the old wording.

### Style

- Write in clear academic English.
- Avoid overclaiming evaluation results that are not in the paper.
- Distinguish between implemented known uses, examples, and future work.
- Keep product-specific implementation details separate from the reusable pattern solution.
- Preserve accessibility-sensitive language.

## Repository hygiene

- Do not commit generated PDFs or LaTeX build artifacts.
- Keep changes focused and reviewable.
- Prefer one conceptual change per commit when working manually.
- When using Codex CLI, ask it to run `make check` after substantial LaTeX or bibliography edits.

## If the build fails

1. Run `make clean`.
2. Run `make pdf` again.
3. Check for duplicate BibTeX keys:

   ```bash
   python3 scripts/check_bib_keys.py literature.bib
   ```

4. Check whether the local TeX installation contains LNCS files:

   ```bash
   kpsewhich llncs.cls
   kpsewhich splncs04.bst
   ```

5. If LNCS files are missing, install the publisher package, for example on Debian/Ubuntu:

   ```bash
   sudo apt-get install texlive-publishers
   ```
