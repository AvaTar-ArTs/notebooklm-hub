# NotebookLM Hub Agent-Skills Capability Map

This document curates the capabilities in `AvaTar-ArTs/agent-skills` that are directly relevant to NotebookLM Hub. It intentionally does **not** vendor the whole skill ecosystem into this repository.

The goal is to make Hub workers discover the right thinking discipline, evidence source, specialist, implementation pattern, and verification gate before choosing a tool/provider.

## Canonical routing spine

```text
using-superpowers
  -> sage
  -> brainstorming / deep-research / systematic-debugging as applicable
  -> workflow-orchestrator for cross-surface work
  -> specialist skills + agents
  -> implementation skills
  -> code/research review
  -> verification-before-completion
```

## 1. Session and routing authorities

### `using-superpowers`
Role: session-level skill router.

Use before any meaningful research, implementation, debugging, consolidation, architecture, or production task. It explicitly separates skill routing from tool/provider routing.

### `sage`
Role: council/router for complex work.

Use for NotebookLM Hub architecture, repository archaeology, cross-repo consolidation, reverse engineering, product strategy, and multi-skill tasks. Sage decides who should think, what evidence should be inspected first, and what stop conditions apply.

### `workflow-orchestrator`
Role: cross-surface decomposition and handoffs.

Use when work spans multiple repos, languages, documentation surfaces, tests, protocols, media types, or tools.

### `brainstorming`
Role: design gate before new architecture/features/workflows.

Use to inspect authoritative context, classify ambiguity, compare real alternatives, freeze approved decisions, and hand off to planning without losing invariants.

## 2. NotebookLM-native authorities

### `skills/notebooklm/SKILL.md`
Role: current NotebookLM programmatic operation map.

Observed capability surface includes:

- authentication/status
- notebook create/list/use/delete
- source add/list/delete/wait/fulltext/guide
- web/deep research
- grounded chat + references
- conversation history + save-to-note
- artifact listing/waiting
- audio generation + MP3 download
- video generation + MP4 download
- slide deck generation/revision + PDF/PPTX download
- infographic generation + PNG download
- report generation + Markdown download
- mind-map generation + JSON download
- data-table generation + CSV download
- quiz/flashcard generation + JSON/Markdown/HTML download
- language settings
- programmatic sharing
- multi-account/parallel-agent isolation using explicit notebook IDs or isolated homes

This skill is an implementation/reference authority, not the definition of Hub architecture. It is currently tied to the upstream `notebooklm-py` lineage and must remain provenance-aware.

### `agents/notebooklm-enhancement-advisor.md`
Role: feature/product prioritization.

Useful for evaluating:

- notebook comparison
- global search
- health checks
- query templates
- smart question generation
- analytics dashboards
- research timelines
- productivity metrics
- cloud sync
- Notion/Obsidian/Git integration
- scheduling/report delivery

Treat its feature lists as historical/internal ideation, not current Google product facts.

## 3. Research and comprehension

### `deep-research`
Role: multi-source research reports, comparisons, learning paths, and literature-style exploration.

Useful Hub applications:

- compare official NotebookLM docs against observed RPC behavior
- research RAG/grounding/informatics primitives
- compare NotebookLM with adjacent knowledge/research systems
- produce implementation landscape reports
- investigate media-generation architectures behind audio/video/slides/visual outputs

### Research-source-first Sage style
Role: provenance, competing evidence, uncertainty, and contradiction handling.

Use when a conclusion about NotebookLM internals could be mistaken for fact.

### Ecosystem research
Use `ecosystem-intelligence` when NotebookLM must be understood in relation to memory, agents, skills, local tools, publishing, or other AvaTar-ArTs systems.

## 4. Repository archaeology and consolidation

Recommended routing family:

- Sage repository-audit route
- repository-forensics / equivalent repository audit specialists when available
- `local-ecosystem-auditor`
- workspace/ecosystem audit skills
- `content-consolidator`
- `sorty` / organization specialists
- duplicate/diff analysis

Hub applications:

- compare `notebooklm/` and `notebookllm/` by blob SHA
- recover divergent historical implementations
- identify canonical first-party vs upstream-derived code
- preserve history without importing duplicate archive strata
- build migration ledgers and provenance records

## 5. Ecosystem and architecture intelligence

### `ecosystem-intelligence`
Role: understand and evolve multi-tool AI ecosystems.

Relevant ideas:

- analyze before modifying
- preserve findings into memory
- test changes through multiple agents/tools
- track cross-tool patterns instead of optimizing for one client

### `ecosystem-clarity`
Role: clarify how agent/tool ecosystems fit together and reduce bloat.

Hub application: prevent the project from collapsing into Claude/Codex/Gemini-specific assumptions.

### `system-architect`
Role: major component boundaries, contracts, data flow, scalability, failure models.

Use for backend contracts, evidence models, representation pipeline, artifact lineage, and interoperability.

## 6. Memory and informatics

### `cross-tool-memory`
Role: durable shared decisions/patterns/preferences store across tools.

Historical schema includes:

- decisions
- patterns
- preferences

Hub lessons:

- memory belongs outside individual models
- export should be machine- and human-readable
- knowledge state should be reusable by heterogeneous clients

### `self-evolving-memory`
Role: record/query patterns and decisions over time.

Hub application: research conclusions, architectural decisions, experiment results, contradictions, and capability changes.

### Future semantic/knowledge-graph skills
Review skills related to semantic indexing, knowledge graphs, entity relationships, provenance, and content awareness before implementing a Hub knowledge graph.

## 7. Browser observation and reverse engineering

Relevant capability family:

- browser automation/testing
- CUA/browser-control skills
- Playwright/Patchright patterns
- screenshot-first workflows
- DOM/network/storage inspection methods from historical NotebookLM work
- automation recommender

Use browser automation as an **observability/fallback surface**, not the sole canonical transport.

Expected evidence streams for live observation can include:

```text
DOM
accessibility tree
network requests/responses
console
storage
runtime events
screenshots
performance timing
UI state
```

Any reverse-engineered claim must be labeled empirical and revalidated before being treated as current.

## 8. RPC / API / protocol engineering

### `build-mcp-server`
Role: MCP server design and deployment-model selection.

Hub rule: MCP is an interoperability adapter over semantic Hub operations, not the internal architecture.

Potential semantic operations:

```text
source.ingest
source.query
source.compare
evidence.trace
research.run
memory.record
artifact.generate
artifact.export
representation.render
publish.build
```

### `build-mcp-app`
Use only when interactive MCP UI/resources are genuinely useful.

### `build-mcpb`
Use for distributable local MCP packaging when/if Hub reaches that stage.

### RPC analysis
Use `notebooklm-py` RPC documentation and tests as behavioral evidence while preserving upstream attribution and instability warnings.

## 9. Python implementation

Recommended implementation path:

```text
brainstorming
  -> writing-plans
  -> test-driven-development
  -> Python specialist
  -> requesting-code-review
  -> verification-before-completion
```

Likely Hub-native Python components:

- transport-neutral backend contracts
- normalized `SourceRecord`
- evidence/provenance schemas
- archive/indexing intelligence
- publisher
- adapters around upstream NotebookLM clients
- artifact manifests
- transformation/rendering pipeline

Do not copy upstream internals where an adapter/clean implementation is sufficient.

## 10. Debugging and resilience

### `systematic-debugging`
Use for:

- RPC breakage
- auth/session changes
- NotebookLM UI drift
- source ingestion failures
- artifact generation failures
- selector breakage
- concurrency/context collisions
- publishing regressions

Rule: reproduce and establish root cause before proposing fixes.

### `quality-regression-testing` / test-result specialists
Use for maintaining compatibility when NotebookLM behavior changes.

## 11. Security and privacy

### `security-engineer`
Use when working with:

- Google auth/session state
- cookies
- OAuth-like flows
- credential persistence
- multi-account isolation
- local secrets
- sharing/permissions
- hosted Hub services

Never commit real auth material or private tokens into Hub.

Historical docs containing specific account identity should be abstracted to generic profile examples in Hub-native documentation.

## 12. Documentation and knowledge publishing

Recommended capabilities:

- `technical-writer`
- documentation-management
- session-export/handoff
- static-site/HTML publishing skills
- accessibility/information architecture skills

Hub already contains a first-party static NotebookLM site-generation lineage. Publishing should evolve into a renderer over normalized knowledge/artifact manifests rather than giant embedded HTML files.

## 13. Media and representation

NotebookLM Hub must treat these as **representation targets**, not hard-coded product buttons:

```text
text
report
data table
mind map
quiz
flashcards
audio
video
slides
infographic
website
API payload
agent context
future interactive/spatial media
```

Relevant skills should be selected based on the target medium. For example, structured asset pipelines, video/media skills, slides/document skills, and publishing skills may become renderer-specific execution layers.

## 14. Productization

Later-stage skills worth routing through when the core is stable:

- `automation-offer-workbench`
- product/revenue analysis specialists
- packaging/installers
- hosted MCP/SaaS design
- docs/demo/landing-page production

Productization must not precede evidence-grounded technical stability.

## 15. Verification

### `verification-before-completion`
No claim that Hub work is complete, fixed, published, migrated, generated, or tested is valid without fresh evidence appropriate to that claim.

For documentation/research changes, verify:

- files exist on target branch
- expected headings/content are present
- provenance statements match source material
- no sensitive credentials were copied

For code, additionally verify tests/lint/build/integration behavior as applicable.

## Recommended selection record

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

The value of this map is not the number of skills invoked. The value is choosing the smallest sufficient council while preserving evidence, architecture boundaries, and verification discipline.
