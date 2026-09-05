# NotebookLM Hub Project State

Status date: 2026-09-05
Branch: `consolidate/notebooklm-core`
Release target: `0.1.0-alpha`

## What exists

### Research and comprehension
- Extensive current NotebookLM/Gemini Notebook capability walkthrough.
- Internal historical NotebookLM repo synthesis.
- Inner-strata audit comparing `notebooklm`, `notebookllm`, and `notebooklm-py` lineages.
- Source/provenance map and recovered-component migration ledger.
- Agent-skills capability council and Hub workflow contract.

### Runtime foundations
- Provider-neutral backend protocol prototype.
- Canonical Hub package with source/evidence/artifact records.
- Structural `doctor` CLI.
- Deterministic release packager.

### Transformation and publishing
- First-party static-site publishing lineage preserved and reworked into a Hub publisher prototype.
- Representation model treats text, audio, video, slides, infographics, mind maps, quizzes, tables, websites, agent context, and future media as projections of evidence rather than unrelated features.

### Process and memory
- Skill-first routing via `AGENTS.md`.
- Evidence classes and research-object design in `docs/HUB_WORKFLOW.md`.
- Durable checkpoints under `checkpoints/`.
- Changelog and roadmap.

## What is still missing

### P0: make the core actually talk to knowledge backends
1. Implement `NotebookLMPyBackend` adapter without copying upstream internals.
2. Implement `ArchiveBackend` for `notebooklm-mine` exports and local knowledge trees.
3. Normalize sources into `SourceRecord` with checksum/provenance.
4. Normalize citations into evidence records.
5. Add fixture-based adapter tests.

### P1: durable knowledge substrate
1. SQLite or equivalent local catalog for source/evidence/artifact records.
2. Cross-notebook/global search.
3. contradiction/support relationship engine.
4. research-object persistence.
5. checkpoint persistence and resumable workflows.
6. migration from historical query history, notes, and source indices.

### P1: interoperability
1. Hub-native MCP adapter over semantic operations.
2. HTTP/API layer only after core semantics stabilize.
3. client adapters for agents, CLIs, workflow systems, and apps.
4. explicit parallel-agent isolation.

### P2: transformation
1. renderer registry and capability discovery.
2. NotebookLM artifact adapter for audio/video/slides/etc.
3. local/open renderer interfaces where practical.
4. artifact validation and lineage manifests.
5. website renderer evolution beyond giant embedded HTML.

### P2: observation and resilience
1. empirical product-observer harness for DOM/network/runtime evidence.
2. RPC compatibility fixtures and change detection.
3. backend health checks.
4. provider capability/version registry.

### P3: product surface
1. searchable knowledge portal.
2. timeline/version lineage UI.
3. research comparison/contradiction views.
4. portable release installer.
5. CI/CD and signed release artifacts.

## Design invariants
- Evidence and provenance survive model/provider changes.
- NotebookLM is a backend/reference, not the Hub boundary.
- MCP is an adapter, not the internal architecture.
- Provider/model names are artifact metadata, not identity.
- Derived interpretation never silently overwrites raw evidence.
- Third-party code retains original provenance and licensing.
- Authentication/session secrets never become committed knowledge artifacts.
