# NotebookLM Hub Research Source Map

This file is the navigation layer for research used to build NotebookLM Hub. It separates **official/current product evidence**, **AvaTar-ArTs historical research**, **upstream implementations**, and **adjacent systems** so future agents can understand where a claim or design idea came from.

## A. Official/current NotebookLM / Gemini Notebook references

Use these to understand what Google currently ships. Treat product behavior as time-sensitive.

### Product identity and evolution
- Gemini Notebook / NotebookLM transition: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
- Advanced research and secure cloud-computer capabilities: https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/

### Core notebook and sources
- Notebook / Studio overview: https://support.google.com/gemininotebook/answer/16206563
- Add/discover sources and supported source behavior: https://support.google.com/gemininotebook/answer/16215270
- Notes: https://support.google.com/gemininotebook/answer/16262519

### Studio artifacts
- Audio Overviews: https://support.google.com/gemininotebook/answer/16212820
- Video Overviews: https://support.google.com/gemininotebook/answer/16454555
- Cinematic Video Overviews: https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/
- Infographics: https://support.google.com/gemininotebook/answer/16758265
- Slide Decks: https://support.google.com/gemininotebook/answer/16757456
- Mind Maps: https://support.google.com/gemininotebook/answer/16212283
- Flashcards / Quizzes: https://support.google.com/gemininotebook/answer/16958963

### Why these matter

These sources define the present capability surface: ingestion, grounding, Deep Research, notes, computation, media generation, visual artifacts, structured data, and export behavior.

See: `research/NOTEBOOKLM_CAPABILITY_WALKTHROUGH.md`.

---

## B. AvaTar-ArTs historical NotebookLM research and implementation docs

These documents describe our own experiments, discoveries, workflows, and architecture. Treat historical feature claims as dated evidence rather than current Google documentation.

### 1. Main historical NotebookLM skill tree

Repository:
- `AvaTar-ArTs/my-supremepowers`

Primary path:
- `agents/notebooklm/notebooklm/`

Important files:

#### `START_HERE.md`
Historical entry point to the NotebookLM automation documentation tree.

#### `BROWSE_DOCS.md`
Curated navigation layer for guides, sessions, architecture, and development notes.

#### `CODEBASE_ANALYSIS.md`
Detailed January 2026 analysis of the custom Python NotebookLM skill. Documents module boundaries, managers, query flow, browser layer, export/history systems, and code-quality/testing gaps.

Key ideas:
- modular business-logic layer;
- notebook registry;
- auth manager;
- query history;
- export manager;
- batch querying;
- environment bootstrap;
- browser/session abstraction.

#### `COMPARISON_MCP_VS_SKILL.md`
Compares the Python skill with the PleasePrompto TypeScript MCP server.

Key lessons:
- MCP excels at interoperability and persistent sessions;
- custom Python tooling excelled at account profiles, analytics, reporting, and local workflow integration;
- the strongest architecture combines roles instead of forcing one integration mechanism to own the system.

#### `IMPROVEMENT_ROADMAP.md`
Extensive enhancement roadmap.

Key ideas:
- interactive CLI/TUI;
- health checks;
- contextual error messages;
- query templates;
- analytics dashboard;
- smart follow-up suggestions;
- cloud backup;
- scheduling;
- external productivity/knowledge integrations;
- performance optimization.

#### `LIVE_OBSERVER_PLAN.md`
Ten-layer runtime-observation design for understanding NotebookLM as it operates.

Layers:
1. console;
2. network;
3. DOM mutation;
4. storage;
5. events;
6. API interception;
7. Shadow DOM;
8. performance;
9. accessibility tree;
10. screenshot timeline.

Major insight:
- move from "What HTML can I scrape?" to "What is happening across the system?"

#### `AVATARARTS_NOTEBOOKLM_INTEGRATION_GUIDE.md`
Connects NotebookLM research to the broader automation ecosystem.

Key ideas:
- semantic organization;
- vector search;
- local LLMs;
- RAG;
- agentic workflows;
- creative automation;
- export/history/batch research;
- project and content coordination.

#### `source_narratives_index.md`
Index to large narrative documents generated from NotebookLM research.

Key idea:
- **recursive knowledge amplification**: grounded research becomes structured narrative, which becomes durable knowledge and can later re-enter the research loop.

#### `docs/sessions/MASTER_HANDOFF_2026-01-14.md`
Documents the "Layered Foundations" breakthrough.

Key ideas:
- simplify brittle UI extraction;
- use a simple rendered-text reader where appropriate;
- preserve a Python command-line edge and a protocol-based universal interface;
- organize session discoveries as durable knowledge rather than leaving them hidden in conversations.

### 2. Historical duplicates and mirrors

Equivalent or descendant material also exists under:
- `AvaTar-ArTs/notebooklm-mine/notebooklm/`
- `AvaTar-ArTs/notebooklm-mine/skill/`
- `AvaTar-ArTs/notebooklm-mine/notebookllm/`
- backup folders inside `my-supremepowers`
- `AvaTar-ArTs/all-agent-skills`
- `AvaTar-ArTs/my-codex`

Policy for Hub:
- reference canonical copies;
- deduplicate mirrors;
- preserve meaningful divergences only when they contain new behavior or history.

---

## C. AvaTar-ArTs Python knowledge/research docs

Repository:
- `AvaTar-ArTs/pythons`

### `PythonKnowledge/NOTEBOOKLM_FRACTAL_ANALYSIS.md`
May 2026 deep analysis of the NotebookLM automation/archive system.

Important findings:
- mapped browser automation, source extraction, account management, analytics, static publishing, documentation, and RPC access as one ecosystem;
- identified source-extraction evolution from selector-heavy versions to a simple foundation reader;
- documented a proposed ten-layer live observer;
- identified a dual-engine Python + MCP architecture;
- reported historical script-format collapse in many browser-automation files;
- identified the static-site generator as a healthy first-party component.

### `PythonKnowledge/Knowledge Agent - Development Plan.md`
Platform-agnostic evolution of the NotebookLM skill into a general research/knowledge agent.

Important ideas:
- guided interface;
- system doctor/health checks;
- query templates;
- analytics;
- smart follow-ups;
- cross-source comparison;
- cloud backup/sync;
- Obsidian/Notion-style knowledge sync;
- scheduling;
- browser pooling;
- query caching;
- daemon mode;
- security hardening;
- unit/integration/E2E testing.

### `notebooklm_dedup_cleaner.py`
First-party archive utility for detecting `(1)` / `(2)`-style duplicate files and comparing them with originals.

### `generate_notebooklm_static_site.py`
First-party NotebookLM archive-to-site generator.

Key behavior:
- immutable numbered builds;
- `latest` pointer;
- notebook discovery;
- artifact rendering;
- grid/list views;
- offline-friendly output.

---

## D. Notebook archive and generated-site corpus

Repository:
- `AvaTar-ArTs/notebooklm-mine`

### Role
This is primarily a **historical research/archive corpus**, not merely application code.

Important areas:
- consolidated notebook exports;
- notebook metadata;
- HTML source material;
- generated artifacts;
- historical NotebookLM skill copies;
- `notebooklm-py` checkout;
- first-party static-site generator;
- generated site builds.

### `CHANGELOG.md`
Documents the May 2026 consolidation of scattered NotebookLM directories into one archive.

### `NOTEBOOKLM_INVENTORY.md`
Inventory/structure notes for NotebookLM export material.

### `notebookLms/versions/`
Generated knowledge-site history. At time of inspection contained numbered builds `0001` through `0005` plus an index.

This directory demonstrates **versioned publication of knowledge**, a concept retained in the Hub publisher.

---

## E. Python RPC client lineage

Found under:
- `AvaTar-ArTs/notebooklm-mine/notebooklm-py/`
- merged copies in `AvaTar-ArTs/pythons/MERGED_FROM_PYTHON/`

Observed capabilities:
- async `NotebookLMClient`;
- notebooks;
- sources;
- notes;
- artifacts;
- sharing;
- research operations;
- CLI;
- bulk import;
- research-to-podcast;
- integration tests/VCR recordings.

License/provenance:
- upstream Teng Lin project;
- MIT licensed;
- not wholly first-party AvaTar-ArTs code.

Hub policy:
- use through explicit adapter/vendor boundary;
- preserve attribution/license;
- build proprietary value in the Hub data model, orchestration, memory, research protocols, provenance, verification, and publishing layers.

---

## F. MCP lineage

Repository:
- `AvaTar-ArTs/notebooklm-mcp`

Historical state:
- NotebookLM MCP lineage from `PleasePrompto/notebooklm-mcp`;
- persistent sessions;
- tools/resources;
- profiles/tool-surface optimization;
- MCP protocol compatibility;
- Patchright/browser integration.

Important historical commit:
- v1.2.1 lineage preserved in Git history.

Current main-branch anomaly:
- repository contents were later overwritten by an unrelated SEO Trend Analyzer implementation.

Hub policy:
- recover historical behavior for comparison;
- preserve upstream license;
- build future Hub MCP as an adapter over Hub core instead of using third-party MCP internals as the core architecture.

---

## G. Specialized NotebookLM skills

Repositories:
- `AvaTar-ArTs/notebooklm-youtube-skill-og`
- `AvaTar-ArTs/notebooklm-youtube-skill`
- `AvaTar-ArTs/notebooklm-skill`

### YouTube skill OG
Historical workflow:
- inspect a YouTube video;
- identify people/entities;
- research them;
- create a NotebookLM notebook;
- add the video and research text;
- generate an Audio Overview;
- use screenshot-first browser automation.

Important lesson:
- specialized workflows should compose core primitives rather than become core architecture.

---

## H. NOI / Hermes signals

Repository:
- `AvaTar-ArTs/noi-mine`

Audits identified NotebookLM as a large knowledge/research root and referenced:
- `.hermes/skills/note-taking/notebooklm-consolidation/`

This suggests additional recoverable work around:
- filesystem inventory;
- archive consolidation;
- deduplication;
- indexing;
- knowledge organization;
- productization/repository assessment.

These are intentionally listed as **next-depth sources** because they have not yet been fully mined into Hub.

---

## I. Adjacent systems to search next

Without assuming they are NotebookLM-specific, these repo families may contain concepts valuable to Hub:

- NOI and content-awareness tooling;
- Hermes note-taking/consolidation skills;
- Engram/memory work;
- agent/skill registries;
- repository indexers;
- knowledge graphs;
- archive/dedup systems;
- multimodal transcription pipelines;
- audio/video generation workflows;
- static-site and documentation generators;
- research automation;
- local RAG/vector systems;
- cross-model orchestration.

The rule is to mine these **after** the NotebookLM-native corpus has been understood thoroughly enough to know what gaps actually remain.

---

## J. Hub synthesis documents

Read in this order:

1. `research/NOTEBOOKLM_CAPABILITY_WALKTHROUGH.md`
   - What NotebookLM currently does and the informatics model underneath it.

2. `research/INTERNAL_REPO_SYNTHESIS.md`
   - What AvaTar-ArTs already researched, built, or proposed.

3. `research/RECOVERED_COMPONENTS.md`
   - Concrete component migration/recovery ledger.

4. `ARCHITECTURE.md`
   - Current Hub architectural direction.

5. `provenance/SOURCES.md`
   - Licensing and provenance boundaries.

This source map should be expanded continuously rather than replaced by a one-time audit.