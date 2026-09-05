# NotebookLM + Claude Code + Codex: Consolidated Research Synthesis

This document distills the local research conversation into implementation
requirements for `notebooklm-hub`. It is an internal design input, not a claim
that every provider capability, community project, or historical repository
observation is current.

## Executive conclusion

NotebookLM should be treated as a grounded research and transformation surface,
not as the Hub's entire application and not as the system of record. Claude
Code and Codex are execution and engineering surfaces. The Hub is the durable
boundary between them: it owns normalized sources, evidence, research objects,
artifact lineage, checkpoints, provider adapters, and publication.

The first useful product is therefore a local-first knowledge substrate that can
operate on exported NotebookLM archives without a live Google session. A live
NotebookLM adapter can be added later and tested against the same contracts.

```text
sources and archives
        ↓
normalization + checksums + provenance
        ↓
catalog + evidence relationships + research objects
        ↓
provider-neutral query and artifact contracts
        ↓
NotebookLM / MCP / browser / local execution adapters
        ↓
verified artifacts + static publication + checkpoints
```

## What the research establishes

### 1. Notebook boundaries are useful epistemic boundaries

A notebook is a curated corpus and reasoning context. The Hub should preserve
notebook identity, source membership, source snapshots, query history, and
artifact lineage instead of flattening everything into an undifferentiated
vector index.

### 2. Grounding is more valuable than generic chat

The primary contract is not merely `question → answer`; it is:

```text
question → answer → citations → source spans → evidence classification
```

Every imported answer or derived artifact should be able to state which source
records support it, what was directly observed, and what was inferred.

### 3. Agents have complementary jobs

- **NotebookLM:** corpus-grounded synthesis and provider-specific studio
  transformations.
- **Claude Code:** repository exploration, implementation, refactoring, and
  workflow automation.
- **Codex:** code changes, verification, packaging, and repeatable engineering
  operations.
- **MCP/browser/RPC adapters:** transport mechanisms, not architectural owners.
- **Hub:** durable models, provenance, orchestration boundaries, and published
  outputs.

The design must remain provider-neutral so a provider outage or API change does
not destroy the local research substrate.

### 4. The real workflow is recursive

Research produces notes, notes become questions, questions produce evidence,
evidence becomes reports or media, and the resulting artifacts become new
research inputs. This requires immutable snapshots, parent/child lineage, and
resumable checkpoints rather than one-shot scripts.

### 5. YouTube and community material are research inputs about the topic

The conversation explicitly corrected an early interpretation: YouTube and
Reddit research should inform understanding of NotebookLM + coding-agent
workflows; it should not automatically become a product ingestion feature.
That distinction belongs in scope control and source classification.

## Architecture requirements

### Required domain records

The current alpha models are a useful start, but the durable substrate needs at
least these records:

| Record | Required responsibility |
|---|---|
| `NotebookRecord` | notebook identity, provider, title, snapshot/version |
| `SourceRecord` | canonical source identity, kind, URI, checksum, content snapshot |
| `EvidenceRecord` | claim, classification, source spans, confidence, extractor |
| `ResearchObject` | question, method, status, inputs, outputs, checkpoint |
| `ArtifactManifest` | artifact type/format, parents, sources, provider, verification |
| `ConversationRecord` | query/session history and provider conversation identity |
| `Checkpoint` | resumable workflow state, evidence, failures, next action |

IDs must be stable within the Hub and provider IDs must be stored as aliases.
Checksums must support deduplication without making a provider's mutable ID the
identity of a source.

### Adapter contract

Adapters should implement capability-specific protocols rather than leak
provider SDK types through the Hub:

- list/get notebooks
- list/add/export sources
- query with citations
- retrieve source text or an archive snapshot
- generate and poll artifacts
- download artifacts with durable metadata
- report authentication, rate-limit, and provider-health state

The local archive adapter is the first implementation. The live NotebookLM
adapter should be a compatibility layer around a pinned upstream release, with
fixtures and explicit provider capability reporting.

### Publication contract

Static publication must copy or intentionally package artifacts into the output
build. Generated HTML must never depend on absolute paths in the source archive
machine. Each build should include:

- an immutable build ID
- a manifest with source and artifact checksums
- relative links that resolve inside the published root
- a latest pointer that works without symlink support
- a provenance page for each notebook and artifact

This requirement follows directly from the current alpha review: the existing
publisher records source paths but does not copy source artifacts into the site.

## Governance and safety requirements

- Use explicit notebook IDs in automation; do not rely on shared mutable context.
- Isolate accounts and provider state per worker when workflows run in parallel.
- Keep authentication state, cookies, private notebook URLs, and raw exports out
  of Git.
- Preserve upstream license and provenance before importing third-party code.
- Mark provider observations with a date and confidence level because NotebookLM
  capabilities and unofficial transports change.
- Separate live provider execution, local execution, mock execution, and dry-run
  compilation in logs and checkpoints.
- Verify generated artifacts independently for existence, parseability, lineage,
  and deployment-relative links.

## Prioritized implementation sequence

### Now: make the alpha trustworthy

1. Add a local archive importer and `SourceRecord` normalization.
2. Add checksum-based catalog persistence, initially SQLite or a documented
   filesystem index.
3. Fix publisher artifact packaging and add link-resolution tests.
4. Make `doctor` return a failing exit status when required checks are missing;
   make CI assert the expected result.
5. Move the canonical backend protocol and shared records into the installable
   `src/notebooklm_hub` package, leaving compatibility shims for prototypes.

### Next: make research useful

1. Add search/list/query over the local catalog.
2. Normalize citations into evidence records with source-span references.
3. Add resumable research objects and checkpoints.
4. Add a provider capability registry and fixture-based compatibility tests.

### Later: extend transformation and product surfaces

1. NotebookLM Studio artifact adapters for audio, video, slides, reports,
   infographics, tables, mind maps, quizzes, and flashcards.
2. Evidence explorer, notebook comparison, timeline/version views, and a
   searchable static knowledge portal.
3. Optional cloud sync and scheduled reports only after local identity,
   provenance, and conflict behavior are stable.

## Acceptance criteria for the next checkpoint

The next implementation checkpoint should not be called complete until all of
the following are demonstrated in a clean checkout:

- an archive fixture imports into normalized records;
- duplicate content resolves to one canonical source with aliases;
- a query or imported answer retains citations and source spans;
- a checkpoint can resume after a simulated failure;
- a published build contains its referenced artifacts and all links resolve;
- an incomplete repository causes `doctor` and CI to fail;
- provider execution mode is explicit in logs and manifests;
- tests cover the importer, catalog, evidence mapping, publisher, and CLI;
- no private credentials or raw conversation exports enter the Git diff.

## Open questions to resolve empirically

These are not settled by the conversation export alone:

1. Which NotebookLM capabilities are currently available through official
   interfaces versus unofficial RPC, browser, or community tooling?
2. What exact archive formats and source metadata are emitted by the local
   `notebooklm-mine` lineage?
3. Which citation coordinates remain stable across source reprocessing?
4. What rate limits, authentication boundaries, and account-isolation rules
   apply to the chosen live adapter?
5. Should the Hub's first search implementation be SQLite FTS, an external
   index, or a replaceable search protocol backed by both?

The answers should be recorded as dated evidence and compatibility fixtures,
not silently encoded as assumptions in adapter code.
