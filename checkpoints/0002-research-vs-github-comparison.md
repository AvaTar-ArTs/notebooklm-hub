# Checkpoint 0002 — Research Compared with GitHub

Captured: 2026-09-05

## Comparison baseline

- Source: the three local exports recorded in
  `provenance/RESEARCH_EXPORTS.md`.
- Repository baseline: `origin/consolidate/notebooklm-core` at the fetched
  `d4515e2` release-review commit.
- Working branch: `consolidate/full-product-audit`, based on that baseline.

## Claim comparison

| Research/conversation theme | GitHub evidence | Status |
|---|---|---|
| Hub should unify research, programmatic access, agents, and publishing | README, architecture, workflow, and capability-map documents | Verified as direction; only the alpha subset is implemented |
| NotebookLM is a grounded research/transformation surface | Capability walkthrough, provider-neutral models, backend protocol | Partially implemented; live provider and evidence substrate remain absent |
| Local archives should be independent of live Google behavior | Publisher prototype and release review recommendation | Partially implemented; importer/catalog still missing |
| Claude Code/Codex/MCP/browser transports should be replaceable | `packages/client/backend.py` protocol | Contract exists; adapters are missing |
| Provenance and artifact lineage are first-class | `SourceRecord`, `EvidenceRecord`, `ArtifactManifest`, provenance docs | Model foundation exists; persistence and citation span mapping are missing |
| Checkpoint-driven, verifiable implementation | `checkpoints/`, CI workflow, release review | Verified as process; CI structural doctor previously accepted false-success states |
| Static publication is offline-friendly | Publisher module claims relative links and artifact pages | Defect found and fixed in this branch by copying artifacts into each build |
| Repository health should gate release | `doctor` command and CI invocation | Defect found and fixed in this branch by returning nonzero on missing checks |

## Missing from the research vision

1. Local archive import and normalization.
2. Persistent catalog, deduplication, search, and evidence graph.
3. Live NotebookLM/MCP/browser adapters with compatibility fixtures.
4. Transformation registry and provider capability reporting.
5. Durable artifact verification and public knowledge portal.

## Scope decisions

- YouTube and Reddit remain research evidence about the ecosystem unless a
  separate product requirement explicitly adds them as ingestion sources.
- Historical assistant statements about provider features or repository contents
  are hypotheses until rechecked against current sources.
- The raw conversation exports remain outside Git.

## Verification state

- Publisher regression test added for copied artifacts and internal links.
- Doctor regression test added for incomplete repositories.
- Python compilation and release validation remain required before completion.
