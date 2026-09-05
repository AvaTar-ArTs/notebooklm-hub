# NotebookLM Inner Strata Audit

This audit focuses on the three core trees inside `AvaTar-ArTs/notebooklm-mine` that currently contain the densest NotebookLM-specific material:

- `notebooklm/`
- `notebookllm/`
- `notebooklm-py/`

The fourth URL supplied for review points to `notebooklm/` again, so the canonical comparison is between these three distinct trees.

## Executive finding

`notebooklm/` and `notebookllm/` are largely duplicate archive strata. Many top-level files have identical blob SHAs, including account, authentication, cleanup, codebase-analysis, MCP-comparison, and browsing documents. They should therefore not be treated as separate product lines.

`notebooklm-py/` is genuinely different. It is an upstream-derived Python/RPC implementation and documentation corpus with a full package layout, tests, CLI/API documentation, RPC references, stability notes, and development guidance. It represents the non-browser programmatic access layer and must retain its MIT provenance.

The Hub should therefore treat these trees as:

```text
notebooklm/ + notebookllm/
        ↓
HISTORICAL FIRST-PARTY RESEARCH / AUTOMATION STRATA
        ↓
recover behavior, lessons, schemas, workflows

notebooklm-py/
        ↓
UPSTREAM-DERIVED RPC / API STRATUM
        ↓
wrap, study, test, attribute
```

## 1. `notebooklm/`: canonical historical browser/skill research tree

This tree contains the strongest historical documentation for the custom NotebookLM research system. It includes:

- account indexes and account summaries
- authentication guides
- multi-account support
- profile mapping
- query and conversation logging
- source-extraction evolution
- source narratives
- codebase analyses
- MCP-vs-skill comparisons
- cleanup and maintenance documentation
- session summaries and master handoffs
- project-specific integration guides
- a docs hierarchy organized into guides, development notes, and session history

The most important architectural ideas recovered from this tree are documented below.

### Identity context as a first-class object

The historical multi-account system isolated each account's:

- browser state
- auth metadata
- notebook library
- query history

The earlier implementation used profile-specific wrappers and separate data roots. The important Hub lesson is not the historical account names or shell aliases, but the general abstraction:

```text
IdentityContext
├── auth
├── library
├── history
├── credentials
├── preferences
└── backend session state
```

This should eventually become provider-agnostic rather than being tied to Google accounts or Chrome profiles.

### Source extraction evolved through observation, not selector worship

`SOURCE_EXTRACTION_VERSIONS.md` records the progression from a fast but empty first extractor to slower, screenshot-assisted extraction with lazy-load scrolling, context capture, source-type classification, confidence scores, and structured CSV/Markdown outputs.

The crucial design lesson is that source discovery is an observation problem:

```text
rendered page
+ timing
+ lazy loading
+ screenshots
+ semantic context
+ confidence
```

not merely a DOM-selector problem.

This idea later matured into the Live Observer architecture documented elsewhere in the archive.

### Historical output schema from source extraction

The V2 extractor tracked fields including:

```text
id
notebook_name
notebook_url
source_title
source_url
source_type
file_extension
domain
path
context
extracted_at
extraction_method
confidence
```

This is a useful seed for a future Hub `SourceRecord`, but should be generalized beyond NotebookLM.

### Conversation and query history are durable research assets

The historical browser skill tracked query history, success rate, average answer length, per-notebook activity, and generated reports. The Hub should preserve this concept as a first-class research log rather than allowing agent interactions to disappear inside transient conversations.

A future generalized record should preserve at least:

```text
query
context / notebook / workspace
backend
answer
citations
success/failure
timestamp
latency
agent/model/tool identity
follow-up lineage
human disposition
```

### Recursive knowledge amplification

The source-narrative system explicitly documented a loop in which NotebookLM was used to analyze its own source corpus, synthesize narratives, and then turn those narratives into future inputs.

That loop can be generalized as:

```text
sources
  ↓
research
  ↓
synthesis
  ↓
durable artifact
  ↓
new source / memory
  ↓
future research
```

This is one of the strongest conceptual precursors to the current Hub architecture.

## 2. `notebookllm/`: duplicate preservation stratum

The `notebookllm/` tree appears to be a duplicate or near-duplicate archival copy of `notebooklm/` rather than a meaningfully separate implementation.

Evidence from the current default branch includes matching blob SHAs for files such as:

- `.gitignore`
- `ACCOUNTS_INDEX.md`
- `ACCOUNTS_SUMMARY.md`
- `ACCOUNT_TOKENS.md`
- `AUTHENTICATION.md`
- `BROWSE_DOCS.md`
- `CHANGELOG.md`
- `CLEANUP_COMPLETE.md`
- `CODEBASE_ANALYSIS.md`
- `COMPARISON_MCP_VS_SKILL.md`

Because matching Git blob SHAs imply byte-identical contents, Hub should treat `notebookllm/` as preservation evidence, not a separate canonical source.

### Canonicalization rule

When both trees contain an identical file:

```text
prefer notebooklm/<path>
record notebookllm/<path> as duplicate lineage
```

When their blob SHAs differ:

```text
compare contents
preserve unique deltas
record divergence explicitly
```

This prevents duplicated documentation from inflating the Hub while still protecting historical variants.

## 3. `notebooklm-py/`: RPC/API implementation stratum

This tree is structurally and functionally different from the historical browser skill. It includes:

- `src/`
- `tests/`
- `scripts/`
- `pyproject.toml`
- `AGENTS.md`
- `CLAUDE.md`
- `SKILL.md`
- `CHANGELOG.md`
- `SECURITY.md`
- `CONTRIBUTING.md`
- extensive developer documentation

Its `docs/` directory currently includes:

- `cli-reference.md`
- `configuration.md`
- `development.md`
- `python-api.md`
- `rpc-development.md`
- `rpc-reference.md`
- `stability.md`
- `troubleshooting.md`
- `releasing.md`
- examples

This makes it the best source for understanding how NotebookLM can be manipulated without relying on browser-visible UI flows.

### Why the RPC layer matters

The browser skill tells us how to operate NotebookLM as a human-facing application.

The RPC client tells us how its internal operation can be represented as programmable capabilities:

```text
notebook operations
source operations
notes
querying
research
Studio artifacts
sharing
bulk workflows
```

That separation is strategically important.

The Hub should not equate NotebookLM with its UI.

### Provenance requirement

`notebooklm-py` is upstream-derived MIT code and must not be relabeled as first-party proprietary implementation.

Hub strategy:

1. keep its license and source lineage explicit;
2. use it as reference/adapter material;
3. expose a Hub-owned backend contract above it;
4. progressively reimplement only where there is a concrete reason;
5. test behavioral compatibility rather than copying internals blindly.

## 4. Combined architecture recovered from the three trees

Taken together, these directories reveal three distinct layers that had already emerged historically:

```text
                    HUMAN / AGENT CLIENTS
                            │
                            ▼
             historical CLI / skill / MCP ideas
                            │
        ┌───────────────────┼───────────────────┐
        ▼                                       ▼
 BROWSER OBSERVATION                        RPC / API
 human-like control                        programmatic control
 source extraction                         notebook/source/artifact ops
 auth profiles                              client library
 screenshots                                tests / references
        │                                       │
        └───────────────────┬───────────────────┘
                            ▼
                       NOTEBOOKLM
                            │
                            ▼
                 archives / exports / sites
```

The proprietary opportunity is not any one of these pieces. It is the layer above them that can normalize all knowledge operations behind durable interfaces.

## 5. Hub abstractions suggested by the historical material

### `IdentityContext`

Separates authentication, libraries, history, and provider-specific session data.

### `SourceRecord`

A generalized source object with provenance, type, extraction method, confidence, authority, dates, and content/asset pointers.

### `ObservationRecord`

Captures what an observer saw and how it saw it:

```text
observer_type
location
timestamp
raw payload
normalized facts
confidence
correlations
```

### `ResearchInteraction`

Stores questions, answers, citations, backend/model/tool context, follow-ups, and human evaluation.

### `KnowledgeArtifact`

Represents reports, notes, audio, video, slides, websites, datasets, code, graphs, or any other transformation derived from evidence.

### `KnowledgeBackend`

The existing Hub interface should evolve from a NotebookLM-specific client abstraction toward a provider-neutral evidence/research backend contract.

## 6. Near-term recovery priorities from these exact trees

1. Build a machine-readable manifest comparing `notebooklm/` and `notebookllm/` by path + blob SHA.
2. Extract only divergent files from `notebookllm/` for manual review.
3. Deep-read the `notebooklm/` docs tree, especially source narratives, session handoffs, logging, account/profile, extraction, and architecture material.
4. Deep-read `notebooklm-py/docs/rpc-reference.md`, `python-api.md`, `stability.md`, and its tests.
5. Convert historical schemas into generalized Hub data models.
6. Preserve browser observation as a fallback/diagnostic backend, not the canonical truth source.
7. Use the RPC client as an adapter/reference, not as the proprietary core.
8. Connect the archive/static-site pipeline so every research artifact can be published and versioned.

## Working conclusion

These directories confirm that the earlier NotebookLM work had already evolved beyond a single automation script. It contained separate ideas for identity isolation, observation, source intelligence, research history, report generation, publishing, browser interaction, and programmatic RPC access.

`notebooklm-hub` should therefore consolidate **concepts and behaviors**, not simply copy directories.

The goal is to recover the architecture hiding inside the historical layers and turn it into a coherent, provider-agnostic information system.