# Checkpoint 0005 — Archive-Aware Product Verification

Captured: 2026-09-05

## Scope completed

Compared the supplied NotebookLM ecosystem archives with the Hub's current
implementation and added a safe, non-executing archive inventory path.

## Product changes

- `zip-repos/` and macOS metadata are excluded from Git and release bundles.
- `scripts/audit_zip_repositories.py` inventories ZIP hashes, counts, file
  classes, duplicate groups, suspicious names, and path traversal without
  extraction or execution.
- Generated inventory: 36 currently present ZIP archives; the initial intake
  had also shown `notebooklm_batches.zip` and a `notebooklm_batches/` directory,
  which disappeared before the second scan and remain an external-state gap.
- Added curated ecosystem analysis across transport, RAG, ingestion, media,
  education, publishing, skills, licensing, and security boundaries.
- Release packaging now excludes raw source archives and scratch/build metadata.

## Critical security finding

`t2m-research-agent-main.zip` contains non-placeholder session-cookie values in
`ezproxy_cookies.json`. It was not copied or executed. Revoke/rotate the
credential if it is still active.

## Verification evidence

- `uv run --no-project --with pytest python -m pytest -q` → **8 passed**.
- `python3 -m compileall -q src packages adapters scripts` → passed.
- `doctor --root . --json` → all eight categories true, exit 0.
- Release version `0.1.0-alpha.2` generated six bundles.
- All six bundles passed manifest SHA-256 checks, non-empty checks, and ZIP
  integrity checks.
- Full bundle extracted with 54 members; required governance, research,
  provenance, audit, adapter, and walkthrough files were present.
- No `zip-repos/` entries were present in any release bundle.

## Remaining gaps

- Restore and rescan the missing batch inputs before using them as importer
  fixtures.
- Implement the local archive importer, checksum catalog, and evidence graph.
- Add the pinned live NotebookLM/MCP adapter and compatibility fixtures.
- Attach release artifacts to a GitHub release separately if distribution is
  desired; generated ZIPs remain local under ignored `dist/`.
