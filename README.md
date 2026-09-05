# NotebookLM Hub

AvaTar-ArTs' consolidated research, evidence, memory, transformation, automation, and publication workspace inspired by and interoperating with NotebookLM / Gemini Notebook.

## Purpose

NotebookLM Hub is not intended to be a thin wrapper around NotebookLM, a Claude/Codex/Gemini integration project, or a trend-driven coding assistant.

The long-term goal is a **model-agnostic, evidence-aware knowledge transformation system** that can:

- ingest heterogeneous sources;
- normalize and index information;
- preserve provenance and source lineage;
- retrieve and compare evidence;
- perform grounded research and computation;
- track contradictions, hypotheses, decisions, and research history;
- accumulate durable memory;
- transform knowledge into multiple representations;
- expose capabilities to agents, applications, CLIs, APIs, workflow engines, and future systems;
- publish versioned knowledge artifacts and sites.

NotebookLM / Gemini Notebook is both a powerful backend and an important architectural reference point. It is not the boundary of the Hub.

## Core mental model

```text
sources / repos / media / web / observations
                    │
                    ▼
           acquisition + normalization
                    │
                    ▼
         evidence + provenance substrate
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
    retrieval    research     observation
       │            │            │
       └────────────┼────────────┘
                    ▼
       reasoning / comparison / compute
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       memory              artifacts
          │                   │
          └─────────┬─────────┘
                    ▼
          transformation layer
                    │
   ┌────────────────┼────────────────────┐
   ▼                ▼                    ▼
 text/audio/video   apps/agents          publishing/data
```

Models and protocols are replaceable computational organs. Evidence, memory, provenance, and research history belong to the substrate.

## Research first

Before expanding implementation, read the research corpus in this order:

1. [`research/NOTEBOOKLM_CAPABILITY_WALKTHROUGH.md`](research/NOTEBOOKLM_CAPABILITY_WALKTHROUGH.md)
   - Detailed walkthrough of how NotebookLM functions today: sources, normalization, grounding, notes, Deep Research, computation, Audio/Video Overviews, infographics, slides, mind maps, quizzes, reports, exports, limitations, and the representation-compiler model.

2. [`research/INTERNAL_REPO_SYNTHESIS.md`](research/INTERNAL_REPO_SYNTHESIS.md)
   - Synthesis of historical AvaTar-ArTs NotebookLM research and experiments across Python automation, MCP, skills, live observation, multi-account profiles, query history, publishing, knowledge synchronization, and recursive knowledge amplification.

3. [`research/SOURCE_MAP.md`](research/SOURCE_MAP.md)
   - Navigation and provenance map for official Google sources, internal AvaTar-ArTs research/docs, upstream NotebookLM implementations, and adjacent systems still to mine.

4. [`research/RECOVERED_COMPONENTS.md`](research/RECOVERED_COMPONENTS.md)
   - Concrete component recovery/migration ledger.

5. [`ARCHITECTURE.md`](ARCHITECTURE.md)
   - Current architectural direction for the Hub.

6. [`provenance/SOURCES.md`](provenance/SOURCES.md)
   - Licensing and source-lineage boundaries.

## Capability layers

The Hub is currently being organized around these durable layers:

1. **Evidence & knowledge**
   - notebook archives
   - sources and normalized representations
   - metadata
   - research memory
   - provenance

2. **Programmatic access**
   - backend-neutral client interfaces
   - Python/RPC adapters
   - browser/runtime observation fallback
   - future APIs/SDKs

3. **Research & intelligence**
   - retrieval
   - comparison
   - contradictions
   - verification
   - research protocols
   - history/analytics
   - computation

4. **Transformation**
   - text
   - audio
   - video
   - visual artifacts
   - structured data
   - websites
   - future representations

5. **Interfaces**
   - CLI
   - MCP
   - agents
   - apps
   - workflow engines
   - local models
   - future protocols

6. **Publication**
   - static knowledge sites
   - immutable versioned builds
   - manifests/search indexes
   - research lineage
   - export/share/deployment

## Consolidation rule

First-party AvaTar-ArTs code and research may be integrated directly.

Third-party or upstream-derived code must retain its original license and provenance and should initially live behind explicit `vendor/`, `adapters/`, or compatibility boundaries until replaced or substantially reimplemented.

The goal is not to disguise upstream code as proprietary. Proprietary value should emerge from the Hub's data model, orchestration, provenance, research protocols, memory, verification, transformation, observability, and publication layers.

## Current layout

```text
notebooklm-hub/
├── packages/
│   ├── client/       # backend-neutral access abstraction
│   ├── publisher/    # evidence/archive → knowledge sites
│   ├── skills/       # reusable research behavior
│   └── mcp/          # future MCP adapter over Hub core
├── adapters/         # future backend/client/protocol adapters
├── provenance/       # source lineage and licensing notes
├── research/         # capability research, repo synthesis, audits
└── vendor/           # preserved upstream-derived components if needed
```

## Initial source family

The first consolidation passes draw from:

- `AvaTar-ArTs/notebooklm-mine`
- `AvaTar-ArTs/pythons`
- `AvaTar-ArTs/my-supremepowers`
- `AvaTar-ArTs/my-codex`
- `AvaTar-ArTs/all-agent-skills`
- `AvaTar-ArTs/notebooklm-mcp`
- `AvaTar-ArTs/notebooklm-skill`
- `AvaTar-ArTs/notebooklm-youtube-skill`
- `AvaTar-ArTs/notebooklm-youtube-skill-og`
- `AvaTar-ArTs/noi-mine`
- related Hermes/knowledge/archive/indexing systems discovered through those repos

This repository is the consolidation and evolution point, not a claim that every historical component is first-party or relicensable.
