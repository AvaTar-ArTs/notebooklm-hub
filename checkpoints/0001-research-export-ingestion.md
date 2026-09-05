# Checkpoint 0001 — Research Export Ingestion

Captured: 2026-09-05

## Scope

Read and analyzed the three local exports of the NotebookLM + Claude Code +
Codex research conversation. The exports were treated as one source set with
alternate serialization formats.

## Evidence

- Compact JSONL: 31 records, 184 KB.
- Tavern JSONL: 31 records, 367 KB.
- Conversation JSON: one conversation, 627 mapping nodes, 336 text-bearing
  messages, 3.0 MB.
- SHA-256 values and handling rules are recorded in
  `provenance/RESEARCH_EXPORTS.md`.
- The current local checkout is `main`, which still contains only the original
  README plus this checkpoint and synthesis work; the alpha implementation is
  on the separate `consolidate/notebooklm-core` remote branch.

## Created

- `research/NOTEBOOKLM_CLAUDE_CODE_CODEX_SYNTHESIS.md`
- `provenance/RESEARCH_EXPORTS.md`
- `checkpoints/0001-research-export-ingestion.md`

## Key decisions

1. Build the local archive/catalog/evidence path before depending on live
   NotebookLM transport behavior.
2. Keep agent providers and transports behind Hub-native contracts.
3. Treat source provenance, execution mode, and artifact lineage as required
   metadata.
4. Do not commit raw conversation exports or private NotebookLM material.

## Known gaps

- No archive importer or persistent catalog has been implemented in this
  checkout yet.
- The current alpha publisher and doctor defects remain on the remote alpha
  branch and are not fixed here.
- The source conversation includes historical provider and repository claims;
  those require fresh verification before implementation decisions depend on
  them.

## Next action

Implement the local archive fixture/importer and its tests on the consolidation
implementation branch, then merge or cherry-pick this research checkpoint into
that branch after reviewing the resulting diff.
