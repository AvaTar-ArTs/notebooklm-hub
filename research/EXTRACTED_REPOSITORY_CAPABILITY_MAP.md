# Extracted Repository Capability Map

This is the English, implementation-oriented comparison between the moved snapshots and the current Hub. It identifies what to learn, where it belongs, and what must stay excluded.

| Source snapshot | Strongest capability | Hub destination | Action |
|---|---|---|---|
| `notebooklm-py-main` (four identical copies) | Broad NotebookLM Python client, CLI, auth, sources, notes, Studio artifacts, research | `packages/client/` | Adapter reference; deduplicate to one upstream lineage. |
| `notebooklm-mcp-main` | MCP tools/resources, citations, accounts, browser watchdog | future `packages/mcp/` | Map tools to `KnowledgeBackend`; preserve license. |
| `OpenNotebookLM-master` | Local RAG, citations, SQLite/sqlite-vec, FastAPI/Next | `packages/client/` + retrieval contracts | Adopt boundaries and tests, not frontend/dependencies. |
| `AcademIA-main` | Whole-book multimodal RAG, hybrid search, OCR/STT, study artifacts | `packages/client/`, `packages/publisher/` | Adopt fallback and job semantics. |
| `professor-notebooklm-main` | Notebook + questions + notes, exam weighting and incidence | `packages/skills/` | Add as a specialized study workflow later. |
| `loackyPKM-main` | Markdown/YAML PKM, BM25/vector fallback, health/reindex concepts | `packages/publisher/` | Adapt health and indexing ideas. |
| `eduStudio-main` | Educational artifact rendering, media/STT/TTS/PPTX options | `packages/publisher/` | Use artifact job contract; do not import media assets. |
| `notebooklm_edson-main` | Fire-and-forget audio creation/download phases | runtime job layer | Generalize to provider-neutral job state; redact source metadata. |
| `podcastfy-main`, `notebooklm-podcasts-main` | Audio transformation pipelines | runtime/publisher | Contract reference only; exclude large blobs. |
| `qiaomu-anything-to-notebooklm-main` | Many source adapters and format transforms | future adapters | Keep public-source ingestion; reject circumvention. |
| `cloud-updates-notebooklm-main` | RSS/cloud-update ingestion + summarization | future source adapter | Convert to generic feed adapter with provenance. |
| `star-notebooklm-main` | Obsidian note/selection handoff | adapters | Optional integration; review upstream identity and API behavior. |
| `universal-transcriber-skill-main` | Transcription skill and bilingual operation | `packages/skills/` | Reuse language-aware workflow concepts. |
| `t2m-research-agent-main` | Research agent shape | research/runtime | No code or credentials; do security remediation first. |
| `unmark-main` | Export watermark detection/removal | nowhere yet | Quarantine pending legal and product policy. |
| `zlibrary-to-notebooklm-main` | Book-source acquisition | future lawful adapter | Preserve copyright and access-control boundaries. |
| `5ch-to-Notebooklm-main` | Scheduled forum fetch | future adapter | Low priority; inspect logging/privacy before reuse. |
| `SurfSense-main` | Large connector/MCP/browser ecosystem | architecture reference | Do not vendor; extract narrow contracts only. |

## Current Hub comparison

The Hub already has a transport-neutral backend, publisher, reusable research skill, source map, provenance ledger, release workflow, and archive audit. The extracted audit adds the missing directory-level evidence, translation index, duplicate recognition, and explicit security quarantine rules. It does not justify copying an entire upstream repository into the product.
