# NotebookLM Hub Architecture

NotebookLM Hub is a model-agnostic research, memory, evidence, orchestration, and publishing substrate. NotebookLM is one important knowledge backend, not the definition of the system. Claude Code, Codex, Gemini, local models, MCP clients, autonomous agents, workflow engines, browser agents, desktop apps, CLIs, and future interfaces are all interchangeable clients of the same core.

```text
                           HUMAN / MACHINE INTENT
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   HUB ORCHESTRATOR   │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    ▼               ▼                ▼
               Research         Memory           Verification
                    │               │                │
                    └───────────────┼────────────────┘
                                    ▼
                         KNOWLEDGE BACKEND LAYER
                                    │
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
          NotebookLM          Local archives         Other backends
          RPC / browser       exported notebooks     vector stores
          MCP adapters        files / Git repos      APIs / databases
                                    │
                                    ▼
                           EVIDENCE / ARTIFACT MODEL
                                    │
          ┌─────────────────────────┼──────────────────────────┐
          ▼                         ▼                          ▼
      Agent Clients             Applications              Publishers
          │                         │                          │
   ┌──────┼──────┐          CLI / web / desktop       static knowledge sites
   ▼      ▼      ▼          automations / services    reports / docs / portals
Claude  Codex  Gemini
   │      │      │
   ├──────┼──────┼────── local models / future agents / MCP clients
   │
   └──────────────────────────────► Hub Core
```

## Core principles

1. **Model-agnostic by design.** No vendor, model, coding assistant, or current AI trend defines the architecture. Clients are adapters.
2. **Backends, not lock-in.** NotebookLM access may use reverse-engineered RPC, browser automation, MCP, exported archives, or future official APIs. Every mechanism sits behind a stable hub contract.
3. **Evidence is a first-class object.** Sources, claims, citations, confidence, contradictions, provenance, experiments, and decisions must survive beyond a single model session.
4. **Research becomes durable memory.** Useful findings are written to artifacts, registries, archives, or structured stores instead of disappearing into conversations.
5. **Reasoning engines are replaceable.** Different agents can research, challenge, build, simulate, verify, summarize, or publish against the same evidence substrate.
6. **Stable knowledge can compile into capabilities.** Reusable knowledge may become skills, policies, rules, templates, prompts, code, schemas, or domain packs for any compatible client.
7. **Publication is first-class.** Research can become immutable knowledge sites, documentation, APIs, reports, datasets, teaching material, product intelligence, or other interfaces.
8. **Provenance survives consolidation.** Upstream code and licenses stay attributable. Hub-native orchestration, protocols, schemas, intelligence, and publishing remain clearly separated.
9. **The filesystem is not the only memory.** Git, local archives, databases, NotebookLM, search indexes, object stores, and future memory engines may all participate.
10. **The hub is broader than coding.** Software development is one workload among research, creative systems, strategy, knowledge management, archival intelligence, content production, education, analysis, and autonomous operations.

## Core abstractions

### `packages/client`

Hub-owned interfaces for knowledge operations. Initial backends may wrap `notebooklm-py`, MCP, browser automation, exported archives, Git repositories, databases, or other research systems.

Target interface:

```python
class KnowledgeBackend:
    async def collections(self): ...
    async def query(self, collection_id: str, question: str): ...
    async def sources(self, collection_id: str): ...
    async def artifacts(self, collection_id: str): ...
    async def add_source(self, collection_id: str, source): ...
```

NotebookLM-specific methods belong in an adapter, not the universal contract.

### `packages/evidence`

Canonical data models for source provenance, claims, citations, confidence, contradictions, experiments, decisions, and lineage.

### `packages/orchestrator`

Routes work between research, memory, verification, transformation, publication, and client adapters without assuming which model performs each role.

### `packages/publisher`

Turns archives, research collections, artifacts, and evidence graphs into immutable versioned builds and machine-readable manifests.

### `packages/skills`

Reusable behavior packs for any compatible agent. Claude Code and Codex are initial adapters, not privileged architectural targets.

### `packages/mcp`

One interoperability surface among several. MCP should expose Hub capabilities, not become the Hub itself.

### `adapters/`

Client integrations may include:

- Claude Code
- Codex
- Gemini / Gemini CLI
- OpenAI-compatible agents
- Anthropic-compatible agents
- local models
- MCP clients
- browser agents
- desktop applications
- autonomous workflow engines
- Python libraries
- shell / CLI
- web applications
- future interfaces not yet invented

No adapter owns the architecture.

## System roles

A client may act as one or many roles:

- researcher
- librarian
- archivist
- critic
- verifier
- planner
- builder
- simulator
- analyst
- editor
- curator
- teacher
- publisher
- monitor
- autonomous operator

Roles are capabilities, not vendor identities.

## Migration phases

### Phase 1: Consolidate
- establish provenance
- recover first-party publishing and research behavior
- inventory Python, RPC, browser, MCP, NOI, Hermes, archive, and agent components
- create canonical package boundaries

### Phase 2: Normalize
- define universal collection/source/artifact/evidence models
- wrap `notebooklm-py`
- preserve browser automation only as fallback
- recover historical MCP behavior behind the Hub contract
- add archive and Git backends

### Phase 3: Intelligence substrate
- collection registry
- project and cross-project research contexts
- query / compare / contradiction / verification workflows
- evidence scoring and provenance graphs
- durable session and longitudinal memory
- agent/client-independent task routing

### Phase 4: Publish and expose
- build static research portals
- emit search/index manifests and machine-readable datasets
- expose Hub via CLI, Python, MCP, HTTP, and other adapters
- connect knowledge versions to Git commits and build metadata

### Phase 5: Autonomous knowledge operations
- continuously ingest approved sources
- detect changed evidence
- re-evaluate conclusions
- regenerate capabilities and publications
- allow heterogeneous agents to collaborate against shared evidence without sharing a vendor-specific context window

## North-star definition

NotebookLM Hub is not a NotebookLM plugin for coding assistants.

It is a **knowledge operating substrate** that can use NotebookLM as one cognitive backend while coordinating many kinds of intelligence, memory, tools, agents, applications, and publishing systems around a durable evidence layer.
