# Revision TODOs for Final Submission

This list captures the remaining paper-work items so Codex CLI sessions can start quickly and avoid rediscovering the same revision plan.

## Shepherd-feedback priorities

- [ ] Reframe forces in both patterns as genuine tensions, not as a list of constraints.
- [ ] Sharpen Pattern 6 problem statement around repeated, course-specific, accessibility-aware support rather than general visual inaccessibility.
- [ ] Rename or consistently frame Pattern 6 as `Accessibility-Aware AI Tutor`.
- [ ] Move `Custom GPT` and other tool names from the abstract solution to Known Uses / Implementation Examples.
- [ ] Rewrite Pattern 6 Resulting Context so it describes the new context and points to related/follow-up patterns.
- [ ] Reposition Pattern 7 from generic podcast generation to `Structured Audio Companion` or an equivalent structured, source-grounded audio-orientation pattern.
- [ ] Clearly differentiate BVI, ADHD, dyslexia, and fatigue-related needs in Pattern 7.
- [ ] Explain how Pattern 7 differs from generic PDF-reader or NotebookLM audio features.
- [ ] Consolidate per-pattern related work into one paper-level Related Work section.
- [ ] Add or revise a Pattern Relationships section/figure showing how the new patterns extend the EuroPLoP 2025 collection.

## Paper polish

- [ ] Rewrite abstract after pattern names and contributions are final.
- [ ] Rewrite introduction to focus on the 2025 pattern collection plus AI-mediated extensions.
- [ ] Update conclusion so it no longer says the AI extension is only future work.
- [ ] Remove all visible TODOs/placeholders.
- [ ] Fix grammar and typos in title/abstract and pattern sections.
- [ ] Update PDF metadata in `preamble.tex` from `Overleaf Example` to the final paper title.
- [ ] Check all citations and bibliography entries.
- [ ] Run `make check` and manually inspect `main.pdf`.

## Suggested Codex CLI prompts

### Pattern 6

```text
Read AGENTS.md and TODO.md. Revise 6_Pattern.tex so Pattern 6 becomes an Accessibility-Aware AI Tutor pattern. Strengthen the problem statement and forces as genuine tensions, keep the solution product-independent, move Custom GPT details to Known Uses, and update the resulting context to connect to the existing pattern collection. Run make check and summarize the changes.
```

### Pattern 7

```text
Read AGENTS.md and TODO.md. Revise 7_Pattern.tex so Pattern 7 is a Structured Audio Companion rather than a generic podcast generation pattern. Differentiate BVI, ADHD, dyslexia, and fatigue-related needs, distinguish the solution from generic PDF-reader podcast features, and strengthen forces as genuine tensions. Run make check and summarize the changes.
```

### Paper structure

```text
Read AGENTS.md and TODO.md. Consolidate related work into a paper-level section and remove long per-pattern related-work blocks. Add a pattern-relationships section that connects the two new patterns to the EuroPLoP 2025 pattern collection. Run make check and summarize the changes.
```
