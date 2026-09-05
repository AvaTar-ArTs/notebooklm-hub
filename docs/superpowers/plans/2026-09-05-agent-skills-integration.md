# Agent-Skills Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `AvaTar-ArTs/agent-skills` the explicit reasoning, research, orchestration, implementation, memory, and verification authority for NotebookLM Hub without copying the entire skill repository into Hub.

**Architecture:** NotebookLM Hub keeps its own durable architecture and knowledge artifacts while consulting `agent-skills` as an external capability/routing library. Hub records selected skill paths, evidence classes, checkpoints, and provenance; individual clients/providers remain replaceable execution surfaces.

**Tech Stack:** Markdown governance, GitHub repository structure, future Python/MCP implementations, external skill authority at `AvaTar-ArTs/agent-skills`.

**Spec:** `AGENTS.md`, `research/NOTEBOOKLM_CAPABILITY_WALKTHROUGH.md`, `research/INTERNAL_REPO_SYNTHESIS.md`, `research/INNER_STRATA_AUDIT.md`.

## Global Constraints

- Do not copy hundreds of skills into Hub merely because they exist.
- `AvaTar-ArTs/agent-skills` remains the canonical skill authority.
- Skill routing, semantic workflow, tool routing, and provider routing remain separate decisions.
- Preserve provenance and license boundaries.
- Treat current official capability, empirical observation, internal historical findings, upstream-derived behavior, and hypotheses as distinct evidence classes.
- Do not expose authentication cookies, tokens, credentials, or personal account identifiers in Hub documentation or fixtures.
- Significant implementation work must use tests and fresh verification before completion claims.

---

### Task 1: Persist Hub agent governance

**Files:**
- Create/maintain: `AGENTS.md`

**Interfaces:**
- Consumes: `agent-skills/skills/using-superpowers/SKILL.md`, `agent-skills/skills/sage/SKILL.md`, `agent-skills/docs/SKILL_WORKFLOW_CONTRACT.md`
- Produces: repository-level routing and evidence rules for every future worker

- [x] Define mandatory skill-first routing.
- [x] Define provider-neutral boundaries.
- [x] Define evidence classes and provenance requirements.
- [x] Define stop conditions for destructive actions and sensitive auth state.

### Task 2: Create NotebookLM Hub skill/council map

**Files:**
- Create: `research/AGENT_SKILLS_CAPABILITY_MAP.md`

**Interfaces:**
- Consumes: NotebookLM-specific skill, deep-research, Sage, ecosystem-intelligence, cross-tool-memory, MCP builder, debugging, verification and specialist-agent entries.
- Produces: curated routing map organized by Hub subsystem rather than by model/provider.

- [ ] Record process skills and their order.
- [ ] Record NotebookLM-native skills/agents.
- [ ] Map research, repository archaeology, informatics, protocol, browser, memory, publishing, security, testing and productization capability families.
- [ ] Mark direct-use, reference-only, and later-review entries.

### Task 3: Define Hub workflow contract

**Files:**
- Create: `docs/HUB_WORKFLOW.md`

**Interfaces:**
- Consumes: `agent-skills/docs/SKILL_WORKFLOW_CONTRACT.md`
- Produces: Hub-specific handoff/checkpoint shapes and lifecycle for research and implementation.

- [ ] Define `SkillSelectionRecord` conceptual schema.
- [ ] Define evidence acquisition and hypothesis verification stages.
- [ ] Define research-to-memory-to-representation lifecycle.
- [ ] Define checkpoint and handoff envelope.
- [ ] Define verification gates for docs, research claims and code.

### Task 4: Connect Hub README to governance and research maps

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: `AGENTS.md`, capability map, workflow doc, research docs.
- Produces: clear onboarding route for humans and agents.

- [ ] Add a `Start Here` section.
- [ ] Link governance, capability walkthrough, repo synthesis, strata audit and skill map.
- [ ] Explicitly state that provider/model integrations are adapters, not the product identity.

### Task 5: Build next implementation plans from the consolidated evidence

**Files:**
- Future plans under `docs/superpowers/plans/`

**Interfaces:**
- Consumes: NotebookLM RPC docs, historical browser automation, publisher, source intelligence, multi-account design, memory and agent skill map.
- Produces: independently testable plans for client adapters, source records, artifact representation, archive intelligence, MCP/tool surfaces and publishing.

- [ ] Plan `SourceRecord` + provenance model.
- [ ] Plan `NotebookLMPyBackend` adapter without copying upstream implementation internals.
- [ ] Plan Hub-native MCP semantic layer over backend contract.
- [ ] Plan archive/history/query-memory subsystem.
- [ ] Plan representation/artifact subsystem for audio, video, slides, data, web and future renderers.
- [ ] Plan tests and compatibility fixtures.

## Self-review

- Spec coverage: governance, skill routing, NotebookLM-specific capabilities, cross-tool memory, protocol work, research and verification are explicitly represented.
- Placeholder scan: no implementation-critical placeholder is being used as a completion claim; future code tasks are intentionally separate plans because the user requested intelligent consolidation before broad implementation.
- Type consistency: conceptual names used here (`SkillSelectionRecord`, `SourceRecord`) are intentionally future interfaces and must be formally specified in their implementation plans before code is written.
