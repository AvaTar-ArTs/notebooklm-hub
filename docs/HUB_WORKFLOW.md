# NotebookLM Hub Workflow Contract

NotebookLM Hub uses the process architecture defined by `AvaTar-ArTs/agent-skills/docs/SKILL_WORKFLOW_CONTRACT.md`, adapted here for evidence-grounded research and knowledge transformation.

## Core flow

```text
intent
  -> skill discovery
  -> evidence acquisition
  -> research / observation / comparison
  -> semantic operation
  -> tool / protocol
  -> provider or local backend
  -> durable artifact + provenance
  -> verification
  -> memory / publication / handoff
```

## SkillSelectionRecord

For complex work, persist or include this conceptual record in the relevant plan/handoff:

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

This prevents accidental collapse of four different questions:

1. How should we think about the task?
2. What semantic operation is needed?
3. What interface/tool can perform it?
4. Which provider/backend should execute it?

## Evidence lifecycle

```text
candidate source
  -> classify authority
  -> ingest / inspect
  -> extract claims
  -> compare / contradict
  -> verify
  -> record confidence + provenance
  -> promote to durable knowledge if warranted
```

### Evidence classes

- `OFFICIAL_CURRENT`: current first-party vendor/product documentation.
- `EMPIRICAL_OBSERVATION`: behavior reproduced from the live product, RPC traffic, UI, network, or controlled experiment.
- `INTERNAL_HISTORICAL`: findings from AvaTar-ArTs repos, handoffs, logs, notes, exports, and prior experiments.
- `UPSTREAM_DERIVED`: behavior/code learned from third-party or open-source implementations.
- `HYPOTHESIS`: plausible interpretation awaiting verification.

A claim can move between classes only when new evidence justifies it. Historical or upstream-derived claims must not silently become current facts.

## Research workflow

```text
question
  -> route through research skills
  -> gather official + empirical + internal evidence
  -> identify agreements / contradictions / gaps
  -> synthesize
  -> record citations/provenance
  -> optionally convert synthesis into memory/source
  -> generate one or more representations
```

### Research object

```yaml
research_object:
  question: ""
  evidence:
    official_current: []
    empirical_observation: []
    internal_historical: []
    upstream_derived: []
  established_facts: []
  likely_facts: []
  contradictions: []
  unknowns: []
  hypotheses: []
  implementation_implications: []
  recommended_experiments: []
  confidence: null
```

## Semantic operation boundary

The Hub should define operations independently from concrete clients or vendors.

Examples:

```text
source.ingest
source.normalize
source.classify
source.search
source.compare
source.trace
research.discover
research.synthesize
research.verify
memory.record
memory.query
artifact.generate
artifact.inspect
artifact.export
representation.render
publish.build
publish.version
```

A NotebookLM RPC client, browser automation, MCP server, local RAG engine, Gemini backend, OpenAI-backed process, or future system may implement an operation. The operation remains stable even when the executor changes.

## Representation workflow

```text
evidence + synthesis
  -> representation intent
  -> target medium
  -> renderer selection
  -> generation
  -> verification
  -> artifact manifest
  -> export / publish
```

Example target media:

- report
- dataset
- audio
- video
- slide deck
- infographic
- mind map
- quiz
- flashcards
- website
- API response
- agent context

The Hub should model these as projections of knowledge, not unrelated features.

## Artifact lineage

Every durable generated artifact should eventually support metadata resembling:

```yaml
artifact:
  id: ""
  type: ""
  created_at: ""
  source_ids: []
  parent_artifact_ids: []
  research_object_ids: []
  prompt_or_instruction: null
  generator: null
  provider: null
  model: null
  format: null
  checksum: null
  verification_status: null
  provenance: []
```

Provider/model fields are metadata, not identity.

## Memory loop

NotebookLM demonstrates a useful recursive pattern:

```text
sources
  -> grounded reasoning
  -> useful synthesis
  -> note / decision / artifact
  -> verified durable memory
  -> future source/context
```

Hub should preserve this recursion while distinguishing raw evidence from derived interpretation.

## Parallel-agent safety

Parallel workers must not share mutable implicit context when explicit IDs are available.

Prefer:

- explicit notebook/source/artifact IDs
- isolated temporary homes/profiles when a client relies on shared context files
- immutable evidence references
- checkpoint files rather than chat-only state
- deterministic artifact paths and IDs

## Checkpoint model

```yaml
checkpoint:
  id: ""
  workflow: ""
  stage: ""
  completed: []
  remaining: []
  evidence_refs: []
  artifact_ids: []
  attempt: 1
  last_error: null
  verification_remaining: []
```

A checkpoint records state. It is never itself proof of success.

## Handoff envelope

```yaml
handoff:
  from_skill: ""
  to_skill: ""
  intent: ""
  approved_approach: ""
  constraints: []
  protected_invariants: []
  evidence_refs: []
  source_artifacts: []
  required_outputs: []
  unresolved_questions: []
  verification_requirements: []
  checkpoint_id: null
```

## Verification gates

### Research/documentation
Before claiming completion:

- verify the target files/changes exist
- verify links/paths refer to real sources where practical
- verify current-vs-historical distinctions
- verify licensing/provenance statements
- verify no secrets/account credentials were copied
- verify the output covers the requested scope

### Code
Additionally:

- tests must be run fresh
- regression claims require reproduction evidence
- builds/lint/type checks must match the specific completion claim
- adapters must be tested against mocks/fixtures and live providers separately
- provider success must not be confused with Hub-level artifact verification

### Publishing/media
Additionally:

- output artifact exists
- format is valid/readable
- manifest points to the correct source/version lineage
- generation success is distinct from approval/quality acceptance

## Security boundary

Authentication/session material may be necessary for local providers but must not become durable Hub source data.

Never commit:

- cookies
- OAuth tokens
- passwords
- private API keys
- real browser storage states
- user-private authentication payloads

Use placeholders, secret stores, environment variables, and local ignored state instead.

## Completion principle

The Hub is successful when knowledge, evidence, lineage, workflow state, and representations survive changes in models, tools, providers, clients, and interfaces.
