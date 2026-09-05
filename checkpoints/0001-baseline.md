# Checkpoint 0001 - Consolidation Baseline

Captured: 2026-09-05

## Conversation-derived objective
Create `AvaTar-ArTs/notebooklm-hub` as a proprietary, model-agnostic evidence and knowledge transformation system assembled from the strongest NotebookLM research, automation, RPC, skill, publishing, memory, and observability work scattered across AvaTar-ArTs repositories.

## Baseline findings before productization pass
- Hub branch was 17 commits ahead of `main`.
- Existing branch contained architecture, research, provenance, backend contract, publisher prototype, and research skill.
- `notebooklm-mine/notebooklm` and `notebookllm` contain substantial duplicate historical strata plus first-party research/automation documentation.
- `notebooklm-py` is a distinct upstream-derived RPC/API implementation with extensive CLI/API/RPC/stability documentation.
- Historical first-party work already explored multi-account isolation, query history, source extraction, browser observation, local publishing, MCP-vs-skill tradeoffs, and recursive knowledge amplification.
- `agent-skills` provides the governing process architecture and NotebookLM-specific operation/advisor assets.

## Missing at baseline
- installable Hub package
- canonical source/evidence/artifact schemas
- tests
- CLI
- reproducible ZIP packaging
- project state audit
- roadmap
- changelog
- security/proprietary boundaries
- durable checkpoint files

## Protected invariants
- do not disguise third-party code as proprietary
- do not make Claude/Codex/Gemini the architectural center
- do not commit authentication material
- preserve research lineage and contradictory evidence
