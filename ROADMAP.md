# NotebookLM Hub Roadmap

## Phase 0 - Comprehend and preserve
Status: substantially complete, continuing.

- audit historical NotebookLM strata
- classify first-party vs upstream-derived work
- capture current NotebookLM capabilities
- preserve architectural discoveries and failures
- establish skills/provenance/checkpoint workflow

## Phase 1 - Canonical core
Status: started.

- provider-neutral records and protocols
- installable Python package
- CLI doctor/release commands
- deterministic packaging
- tests
- add archive and NotebookLM-Python adapters
- local catalog and provenance store

Exit criteria: a user can ingest/query a local archive through the Hub core without depending on NotebookLM UI automation.

## Phase 2 - Evidence intelligence
- source normalization and hashing
- citation/evidence graph
- cross-notebook search
- compare/support/contradiction operations
- research objects and confidence
- version/change detection

Exit criteria: Hub can explain not only an answer, but which evidence supports/conflicts with it and how the conclusion changed over time.

## Phase 3 - Representation engine
- renderer registry
- NotebookLM artifact renderer adapter
- report/table/mind-map native exporters
- media-provider adapters
- artifact manifests and verification
- versioned knowledge-site publisher v2

Exit criteria: one research object can be intentionally transformed into multiple validated representations with common lineage.

## Phase 4 - Interoperability
- Hub MCP server
- optional HTTP API
- agent/workflow connectors
- local-model and external-model adapters
- event hooks and autonomous knowledge operations

Exit criteria: heterogeneous clients can consume the same semantic operations without owning Hub memory.

## Phase 5 - Product surfaces
- searchable portal
- visual provenance graph
- timeline and notebook comparison
- research-to-media workspace
- release installer and updater
- optional hosted deployment

## Research lanes that continue throughout
- current Google NotebookLM/Gemini Notebook behavior
- RPC/API change archaeology
- browser/runtime observation
- information science / RAG / provenance
- learning systems
- multimodal narrative generation
- media transformation
- knowledge graphs and content awareness
