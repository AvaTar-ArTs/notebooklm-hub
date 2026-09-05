# NotebookLM Hub Architecture

NotebookLM Hub consolidates a research-to-execution-to-publication workflow around NotebookLM while keeping external implementations behind replaceable adapters.

```text
Sources / Docs / Research
          │
          ▼
      NotebookLM
          │
   ┌──────┴─────────┐
   ▼                ▼
Live adapter     Local archive
(RPC/MCP)        (notebooklm-mine)
   │                │
   └──────┬─────────┘
          ▼
   NotebookLM Hub Core
          │
 ┌────────┼─────────┐
 ▼        ▼         ▼
Claude   Codex   local CLI
Code
 │        │
 └───┬────┘
     ▼
Research / build / verify
     │
     ▼
Knowledge Publisher
     │
     ▼
Versioned static sites
```

## Core principles

1. **Adapters, not lock-in.** Google NotebookLM access is unofficial/unstable when performed through reverse-engineered RPC or browser automation. Every such mechanism sits behind a hub interface.
2. **Research becomes an artifact.** Agent findings, decisions, evidence, and verification results are written to files rather than disappearing inside conversations.
3. **Stable knowledge can compile into skills.** Reusable domain knowledge belongs in agent skills; changing or large corpora stay in NotebookLM or the local archive.
4. **Publication is first-class.** Notebook research can be transformed into immutable, versioned static knowledge sites.
5. **Provenance survives consolidation.** Upstream MIT code remains attributed. First-party hub orchestration and publishing logic are separated from vendor code.

## Package roles

### `packages/client`

A hub-owned abstraction for NotebookLM operations. Initial backends may wrap `notebooklm-py`, MCP, browser automation, or exported archives.

Target interface:

```python
class KnowledgeBackend:
    async def notebooks(self): ...
    async def query(self, notebook_id: str, question: str): ...
    async def sources(self, notebook_id: str): ...
    async def artifacts(self, notebook_id: str): ...
    async def add_source(self, notebook_id: str, source): ...
```

### `packages/publisher`

Turns notebook/archive directories into immutable static builds and machine-readable manifests.

### `packages/skills`

Shared research behavior for Claude Code, Codex, and other coding agents.

### `packages/mcp`

A future hub-owned MCP surface. The initial implementation should wrap the hub client rather than expose a third-party MCP implementation as the architectural core.

### `adapters/claude-code`

Claude Code setup, commands, and skill integration.

### `adapters/codex`

Codex setup, agent instructions, verification workflows, and MCP/client integration.

## Migration phases

### Phase 1: Consolidate
- establish provenance
- bring over first-party publishing and agent behavior
- document recoverable Python/MCP components
- create canonical package layout

### Phase 2: Normalize
- define a single notebook/source/artifact model
- wrap `notebooklm-py`
- preserve browser automation only as fallback
- recover old MCP behavior behind the hub client

### Phase 3: Research OS
- notebook registry
- project-scoped research contexts
- research / verify / compare / contradiction workflows
- session wrap-up and durable memory

### Phase 4: Publish
- build static research portals
- add search/index manifests
- deploy selected knowledge sites
- connect research versions to Git commits/build metadata
