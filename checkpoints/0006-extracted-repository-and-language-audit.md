# Checkpoint 0006 — Extracted Repository and Language Audit

Date: 2026-09-05

## Scope

Audited the extracted snapshots under `/Users/steven/notebooklm-zip-repos` against the Hub and the local `.agent-skills` guidance. Inputs were treated as read-only. The directory contains 36 extracted repositories and 37 ZIP archives; `notebooklm_batches` is not present in this moved location.

## Completed

- Added a repeatable, non-executing directory audit at `scripts/audit_extracted_repositories.py`.
- Generated `provenance/EXTRACTED_REPOSITORY_MANIFEST.json` and `research/generated/EXTRACTED_REPOSITORY_INVENTORY.md`.
- Added the English language/translation and security audit in `research/EXTRACTED_REPOSITORY_LANGUAGE_AUDIT.md`.
- Added the implementation-oriented capability comparison in `research/EXTRACTED_REPOSITORY_CAPABILITY_MAP.md`.
- Added sanitized English summaries for AcademIA, Professor, Qiaomu, Unmark, NotebookLM Edson, and Miniguia.
- Excluded cookies, browser state, private-key-shaped files, personal identifiers, generated databases, media blobs, and paywall circumvention from the Hub.

## Verification

- Directory count verified: 36.
- ZIP intake discrepancy retained as an explicit gap; no missing source was invented.
- Sensitive paths are reported by name only.
- Existing Hub tests and release verification remain required before the checkpoint is committed.
