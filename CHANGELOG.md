# Changelog

All notable Hub-native changes are recorded here. Historical NotebookLM experiments remain documented in `research/`, `provenance/`, and source repositories.

## [0.1.0-alpha] - 2026-09-05

### Added
- Model-agnostic Hub architecture and research corpus.
- NotebookLM capability/informatics walkthrough covering sources, grounding, research, computation, Studio artifacts, audio/video, visual/data outputs, exports, limits, and representation primitives.
- Internal repo synthesis, source map, recovered-component ledger, inner-strata audit, and agent-skills capability map.
- `AGENTS.md` and `docs/HUB_WORKFLOW.md` establishing skill-first, evidence-first, provider-neutral workflow discipline.
- Backend-neutral prototype contract under `packages/client/backend.py`.
- First-party versioned static publisher prototype under `packages/publisher/`.
- NotebookLM research skill under `packages/skills/`.
- Canonical installable Python package under `src/notebooklm_hub/`.
- Provider-neutral `SourceRecord`, `EvidenceRecord`, and `ArtifactManifest` models.
- `notebooklm-hub doctor` structural audit command.
- `notebooklm-hub release` reproducible full/component ZIP packager with SHA-256 manifest.
- Test suite for models, CLI, and release packaging.
- Checkpoint ledger, project-state audit, roadmap, security policy, and proprietary-source notice.

### Verified
- TDD red phase observed missing `models`, `release`, and `cli` modules.
- Green phase: 6 tests passed locally on Python 3.13.

### Known gaps
- NotebookLM RPC adapter remains to be implemented behind the Hub backend contract.
- Archive adapter and normalized import pipeline remain to be implemented.
- Cross-notebook/global index and contradiction engine remain to be implemented.
- Audio/video/slide/infographic renderers are still external/provider capabilities, not Hub-native renderers.
- CI workflow and published release automation remain to be added.
