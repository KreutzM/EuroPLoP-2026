# Changelog

All notable changes to this paper repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses calendar-style unreleased paper revisions rather than software versioning.

## [Unreleased]

### Added

- Codex/agent instructions in `AGENTS.md`.
- Local build workflow via `Makefile` and `latexmkrc`.
- Repository README with local build, check, and Codex CLI workflow instructions.
- Lightweight checks for duplicate BibTeX keys and unresolved manuscript markers.
- Revision TODO list for final EuroPLoP 2026 submission work.

### Changed

- Documented expected local TeX/LNCS requirements and final-submission readiness checks.
- Made Makefile checks more portable on Windows by auto-detecting `python3`, `python`, or `py` and documenting `make PYTHON=py check`.

### Fixed

- `make check` no longer depends unconditionally on a `python3` executable being available on Windows.

## [Initial repository import]

### Added

- Initial LaTeX sources for the EuroPLoP 2026 paper.
