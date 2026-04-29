# EuroPLoP 2026 Paper

LaTeX sources for the EuroPLoP 2026 paper **A Pattern Collection for Generating Accessible Teaching Materials in STEM**.

The repository is intended to be edited locally and with Codex CLI. The root file is `main.tex`.

## Repository layout

| Path | Purpose |
|---|---|
| `main.tex` | Root LaTeX document |
| `preamble.tex` | Packages, commands, PDF metadata |
| `title_abstract.tex` | Title, authors, abstract, keywords |
| `introduction.tex` | Introduction |
| `6_Pattern.tex` | Pattern 6: AI Tutor / accessibility-aware AI tutor |
| `7_Pattern.tex` | Pattern 7: Podcast/audio companion pattern |
| `Conclusion_and_Future_Work.tex` | Conclusion and future work |
| `acronyms.tex` | Acronym definitions |
| `literature.bib` | BibTeX database |
| `AGENTS.md` | Codex/agent instructions |
| `scripts/` | Lightweight local checks |

## Requirements

Install a reasonably complete TeX Live distribution with:

- `latexmk`
- `pdflatex`
- BibTeX
- Springer LNCS class/style support: `llncs.cls` and `splncs04.bst`

On Debian/Ubuntu, the following packages are usually sufficient:

```bash
sudo apt-get update
sudo apt-get install latexmk texlive-latex-recommended texlive-latex-extra texlive-publishers texlive-fonts-recommended
```

Check LNCS availability:

```bash
kpsewhich llncs.cls
kpsewhich splncs04.bst
```

Both commands should print a path. If they do not, install `texlive-publishers` or add the Springer LNCS files locally according to the EuroPLoP/Springer author instructions.

## Build

Recommended:

```bash
make pdf
```

This produces `main.pdf` locally. Generated PDFs and auxiliary files are ignored by Git.

Direct equivalent:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Checks

Run:

```bash
make check
```

This currently performs:

1. LaTeX build through `latexmk`.
2. Duplicate BibTeX-key check for `literature.bib`.
3. Lightweight text scan for common unresolved manuscript markers.

The checks are intentionally lightweight. They do **not** replace manual PDF review.

## Clean build artifacts

```bash
make clean
```

## Codex CLI workflow

Start Codex CLI from the repository root and ask it to follow `AGENTS.md`.

Suggested prompt pattern:

```text
Read AGENTS.md and the current paper sources. Revise Pattern 6 according to the shepherd feedback. Keep the solution product-independent, strengthen the forces as real tensions, and run make check before summarizing changes.
```

Recommended revision order:

1. Strengthen pattern forces and problem statements.
2. Move tool-specific details to examples/known uses.
3. Consolidate related work at paper level.
4. Add or revise the pattern-relationship figure/section.
5. Rewrite abstract and introduction after the pattern content is stable.
6. Run `make check` and manually inspect `main.pdf`.

## Submission readiness checklist

Before final submission:

- [ ] `make check` passes.
- [ ] `main.pdf` was manually reviewed.
- [ ] No visible TODOs or placeholders remain.
- [ ] All citations and references are resolved.
- [ ] No duplicate BibTeX keys remain.
- [ ] PDF metadata has the final paper title.
- [ ] The abstract, introduction, and conclusion reflect the revised pattern names and contribution.
- [ ] Pattern forces are formulated as genuine tensions.
- [ ] Tool-specific implementations are clearly separated from pattern solutions.
- [ ] Related work is consolidated and does not interrupt the pattern form.

## Notes on LNCS files

The repository does not intentionally vendor Springer template files unless they are already part of the project or permitted by the applicable license. Prefer installing LNCS support through the TeX distribution (`texlive-publishers`) or downloading the official author package from Springer/EuroPLoP instructions when required.
