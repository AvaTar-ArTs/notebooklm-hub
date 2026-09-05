# NotebookLM Hub Agent Governance

This repository is governed by the canonical AvaTar-ArTs `agent-skills` ecosystem at `AvaTar-ArTs/agent-skills`.

The Hub must not treat Claude, Codex, Gemini, Cursor, Hermes, GPT, local models, MCP clients, browser agents, workflow engines, or future systems as the architecture. They are interchangeable clients/providers around a durable knowledge system.

## Mandatory routing discipline

Before research, implementation, debugging, cleanup, migration, documentation, or release work:

1. Consult `AvaTar-ArTs/agent-skills/skills/using-superpowers/SKILL.md`.
2. Use `sage` for multi-repository, multi-skill, research-heavy, or architectural work.
3. Use `brainstorming` before new design, feature, workflow, representation, or architecture decisions unless the design is already explicitly approved.
4. Use the relevant research/evidence discipline before making claims about NotebookLM internals or current capabilities.
5. Use `workflow-orchestrator` when work spans multiple repositories, tools, code languages, research surfaces, or artifact types.
6. Use domain/specialist skills only after the process skill establishes the approach.
7. Use `systematic-debugging` before proposing fixes for broken behavior.
8. Use `test-driven-development` for new implementation or behavior changes when applicable.
9. Use review skills before promotion/merge of significant implementation changes.
10. Use `verification-before-completion` before claiming anything is complete, fixed, migrated, published, generated, tested, or successfully executed.

## Shared workflow contract

Follow `AvaTar-ArTs/agent-skills/docs/SKILL_WORKFLOW_CONTRACT.md`.

Keep these layers separate:

```text
user intent
  -> skill discovery
  -> process/domain workflow
  -> semantic operation
  -> tool / MCP
  -> provider or local backend
  -> artifacts + provenance
  -> verification
```

A provider being available is never a reason to bypass skill/process routing.

## Hub-specific skill selection record

For complex tasks, preserve a lightweight record:

```yaml
skill_selection:
  intent: ""
  process_skills: []
  research_skills: []
  domain_skills: []
  implementation_skills: []
  verification_skills: []
  specialist_agents: []
  semantic_capabilities: []
  evidence_sources: []
  provider_decisions_deferred: []
```

## Recommended NotebookLM Hub council

Use these as routing families, not a fixed closed list.

### Research and comprehension
- `using-superpowers`
- `sage`
- `deep-research`
- `brainstorming`
- research-source-first routing
- ecosystem-intelligence
- source/provenance analysis

### Repository archaeology and consolidation
- repository-forensics / repository audit specialists where available
- workspace/ecosystem audit skills
- local-ecosystem-auditor
- content-consolidator
- sorty/content organization skills
- duplicate/diff analysis

### Architecture
- workflow-orchestrator
- system-architect
- ecosystem-intelligence
- ecosystem-clarity
- writing-plans

### NotebookLM observation and reverse engineering
- browser automation specialists
- API/RPC analysis specialists
- network/DOM/storage observation methods
- source extraction and comparison workflows
- security/privacy review before persisting authentication/session material

### Python and protocol implementation
- Python specialist skills/agents
- MCP/protocol skills
- test-driven-development
- systematic-debugging
- requesting-code-review

### Memory and informatics
- cross-tool-memory
- self-evolving-memory
- knowledge graph / semantic indexing skills where relevant
- provenance/lineage preservation

### Documentation and publishing
- technical-writer
- documentation-management
- session-export/handoff skills
- static-site / HTML publishing skills
- accessibility and information architecture skills where relevant

### Verification
- verification-before-completion
- test-results-analyzer
- code-reviewer
- artifact verification

## Evidence classes

Every important Hub conclusion should distinguish among:

- `OFFICIAL_CURRENT`: current official product/vendor documentation.
- `EMPIRICAL_OBSERVATION`: reproduced browser/network/RPC/tool behavior.
- `INTERNAL_HISTORICAL`: findings from AvaTar-ArTs repos, handoffs, logs, experiments, and archives.
- `UPSTREAM_DERIVED`: behavior or code inherited from third-party/open-source implementations.
- `HYPOTHESIS`: plausible but not yet verified interpretation.

Never silently promote a hypothesis or historical observation into a current fact.

## Provenance

Preserve source repository, path, commit/blob SHA when practical for migrated findings or code.

Third-party/upstream code must retain its original license and attribution. First-party concepts may be reimplemented as Hub-native components, but ancestry should still be documented when useful.

## Checkpoints

Long migrations/research passes should persist checkpoints containing completed work, remaining work, evidence/artifacts, current failures, and next verification requirements.

## Stop conditions

Do not perform destructive cleanup, overwrite historical source repos, rewrite provenance, expose credentials/auth state, force-push, merge major architectural changes, or promote unverified reverse-engineering conclusions without the appropriate evidence and explicit approval when required.
