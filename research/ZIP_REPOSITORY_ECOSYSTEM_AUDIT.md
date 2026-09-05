# ZIP Repository Ecosystem Audit

This is the curated interpretation of the supplied repository archives. The
machine-generated inventory is in
`research/generated/ZIP_REPOSITORY_INVENTORY.md`, with hashes and file-level
metadata in `provenance/ZIP_REPOSITORY_MANIFEST.json`.

## Executive assessment

The collection is not one product and should not be merged wholesale. It is a
portfolio of distinct layers:

1. NotebookLM-compatible clients and transports.
2. Local RAG and self-hosted NotebookLM alternatives.
3. Source acquisition and ingestion utilities.
4. Educational/content workflows and prompt research.
5. Publishing, transcription, and media transformation tools.
6. Large knowledge archives and unrelated-but-adjacent PKM products.

The Hub should absorb contracts, schemas, tests, and carefully reviewed behavior;
it should preserve upstream repositories as provenance-linked references or
vendor boundaries. The initially observed 37 ZIPs included four exact
`notebooklm-py` duplicates,
two large media-heavy podcast bundles, and a 256 MB SurfSense archive. Size is
not evidence of integration value.

## Curated capability map

| Family | Sources | Reusable capability | Hub destination | Decision |
|---|---|---|---|---|
| NotebookLM transport | `notebooklm-py-main*.zip`, `notebooklm-mcp-main.zip`, `notebooklm-toolkit-main.zip`, `open-notebooklm-main.zip` | Notebook/source CRUD, chat, citations, artifacts, MCP/RPC/browser transport | `packages/client`, future `adapters/notebooklm`, `packages/mcp` | Reference and adapter only; retain upstream licenses and pin versions |
| Self-hosted RAG | `OpenNotebookLM-master.zip`, `NoteBookLM-Clone-main(1).zip`, `notebooklm-clone-main.zip`, `notebookllm-minus-main.zip`, `notebookllama-main.zip`, `rag-notebooklm-main.zip`, `gemini-api-rag-main.zip` | Ingestion, chunking, embeddings, hybrid retrieval, auth, web UI, local models | Local archive/catalog and replaceable search protocol | Compare designs; do not copy entire applications |
| Research/education | `AcademIA-main.zip`, `eduStudio-main.zip`, `professor-notebooklm-main.zip`, `miniguia-estudos-notebooklm-main*.zip`, `notebooklm-prompt-engineering-guide-main.zip` | Study guides, book processing, quizzes, reports, prompt patterns | Research skills, transformation registry, fixtures | Curate workflows and schemas; respect non-English/source licenses |
| Ingestion bridges | `5ch-to-Notebooklm-main.zip`, `cloud-updates-notebooklm-main.zip`, `qiaomu-anything-to-notebooklm-main.zip`, `wechat-to-notebooklm-main.zip`, `zlibrary-to-notebooklm-main.zip` | Forum/news/Feishu/WeChat/book-to-source pipelines | `adapters/sources` after legal and security review | Optional adapters; Z-Library requires strict lawful-use boundary |
| Media/transcription | `notebooklm-podcasts-main.zip`, `podcastfy-main.zip`, `universal-transcriber-skill-main.zip`, `t2m-research-agent-main.zip` | Audio/video generation, transcription, timestamps, academic research | Artifact/transformer contracts and external worker adapters | Keep media engines replaceable; avoid bundling huge outputs |
| Knowledge/publishing | `loackyPKM-main.zip`, `notebooklm_edson-main.zip`, `unmark-main.zip`, `unmark-main.zip`, `SurfSense-main.zip` | PKM, literature archives, static content, document cleanup, connectors | Archive catalog, publisher, evidence explorer | Use as design references; high integration and licensing burden |
| Skills/agent surfaces | `notebooklm-skill-master.zip`, `skills-main(2).zip`, `star-notebooklm-main.zip` | Claude/Codex skills, Obsidian transfer, prompts | `packages/skills`, `adapters/claude-code`, `adapters/codex` | Curate instructions; never copy credential state |

## Important comparisons

### `notebooklm-py` is the strongest transport reference

The four archives are exact duplicates by SHA-256. The bundle has a mature
surface, extensive tests, RPC fixtures, and unusually explicit authentication
guardrails. It is the best candidate for a future `NotebookLMPyBackend`, but its
credential and unofficial transport internals must remain behind a narrow
adapter. The Hub must not fork four copies or claim this upstream work as
proprietary.

### `OpenNotebookLM` is the strongest self-hosted architecture reference

It combines local ingestion, SQLite/vector storage, provider-neutral LLMs,
source citations, authentication, ownership checks, health checks, and E2E
design. Its deployment footprint is much larger than the current Hub alpha.
The Hub should borrow acceptance criteria and boundary ideas, not vendor its
full web application.

### `SurfSense` is a broad adjacent platform, not a drop-in component

It contains connectors, token accounting, browser/desktop surfaces, and a large
dependency/application footprint. It is useful for connector and workspace
design comparisons, but its size and credentials surface make wholesale
integration inappropriate for Phase 1.

### Archives and education repos provide the content model

`notebooklm_edson`, `professor-notebooklm`, `loackyPKM`, and the batch directory
show how real research is organized into books, chapters, scenes, prompts,
reports, and paired text/PDF artifacts. These are valuable fixtures for the
Hub's archive importer and static publisher, but they should be referenced or
sampled rather than committed wholesale.

### Media bundles are capability references, not source dependencies

`notebooklm-podcasts` and `podcastfy` are dominated by media/dependency weight.
Their value is the transformation contract: source set → generation job →
artifact → downloadable output → verification. The Hub should store manifests
and lineage while workers own model/runtime dependencies.

## Security and licensing findings

- The inventory flags secret-like filenames in several archives. Most are
  examples or source code names, but they require review before extraction or
  vendoring.
- `t2m-research-agent-main/ezproxy_cookies.json` contains session-cookie values
  rather than placeholders. Treat the supplied archive as compromised source
  material: do not import it, and revoke/rotate those credentials if they are
  still valid.
- `notebooklm-py` contains authentication and cookie/token guardrail code. Keep
  credentials outside Git and do not execute imported login helpers during audit.
- `t2m-research-agent` includes `ezproxy_cookies.json` and cookie-import code;
  treat that archive as sensitive and do not import those files.
- `notebookllm-minus` includes an example private SSH key path; even an example
  key must not be promoted into a product bundle without confirming it is
  non-secret and replacing it with documentation-only placeholders.
- `zlibrary-to-notebooklm` must be limited to materials the user legally owns,
  public-domain works, or openly licensed sources.
- `SurfSense`, `OpenNotebookLM`, `AcademIA`, and many smaller projects carry
  their own licenses. Any copied code must retain its notice and provenance.

## Recovery order

1. Build archive fixtures from `notebooklm_batches` and selected small
   educational repositories.
2. Define the Hub importer/catalog/evidence contracts around those fixtures.
3. Compare the Hub backend against pinned `notebooklm-py` behavior using scrubbed
   fixtures, without importing its auth implementation into core.
4. Add source adapters one at a time: YouTube/news/WeChat/Feishu only after
   policy and rate-limit boundaries are explicit.
5. Add media workers through artifact manifests, not embedded runtime stacks.
6. Evaluate self-hosted UI/RAG designs only after the local substrate is stable.

## Explicit non-actions

- Do not vendor all 37 archives.
- Do not commit raw archives, generated media, cookies, tokens, or private keys.
- Do not treat repository names, README claims, or assistant-generated research
  as proof of current provider behavior.
- Do not merge duplicate `notebooklm-py` archives as separate implementations.

## Current Hub gaps exposed by this audit

- The Hub still needs a local archive importer and catalog.
- Source checksums and duplicate aliases need persistence.
- Evidence records need source-span/citation normalization.
- The backend protocol needs a real adapter fixture suite.
- The publisher needs artifact packaging tests, now addressed for the basic path
  in the current branch.
- Generated releases need an explicit provenance manifest for selected upstream
  references, not just a ZIP checksum.
