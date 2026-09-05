# Recovered NotebookLM Component Map

This ledger records NotebookLM-related components discovered across AvaTar-ArTs repositories and their proposed destination in NotebookLM Hub.

## High-value Python components

### RPC client family

Found in:

- `AvaTar-ArTs/notebooklm-mine/notebooklm-py/`
- `AvaTar-ArTs/pythons/MERGED_FROM_PYTHON/`

Observed capabilities:

- async `NotebookLMClient`
- notebook CRUD/listing
- source operations
- note operations
- artifact/Studio operations
- sharing
- research operations
- CLI
- bulk import example
- research-to-podcast example
- VCR-backed CLI integration tests

Status: **upstream-derived (Teng Lin, MIT)**.

Hub action: wrap behind `packages/client/KnowledgeBackend`; preserve upstream license if vendored. Do not present as wholly first-party proprietary code.

### Historical browser/CLI automation

Found primarily through:

- `AvaTar-ArTs/my-supremepowers/agents/notebooklm/notebooklm/`
- consolidated copies in `notebooklm-mine`
- architecture records in `pythons/PythonKnowledge/NOTEBOOKLM_FRACTAL_ANALYSIS.md`

Observed capabilities:

- `run.py` automatic environment/bootstrap wrapper
- `auth_manager.py`
- `notebook_manager.py`
- `ask_question.py`
- `batch_query.py`
- `query_history.py`
- `export_manager.py`
- `cleanup_manager.py`
- `profile_manager.py`
- `conversation_logger.py`
- browser factory / Patchright automation
- source extraction/diagnostics
- multi-account profiles (`nlma`, `nlmcho` historical design)

Status: **mixed health**. Historical architecture analysis reported widespread newline/minification collapse in many scripts.

Hub action: recover behavior and tests, not damaged files blindly. Prefer RPC/backend access for canonical operations; preserve browser control as fallback and diagnostics.

### Static site generator

Found in:

- `AvaTar-ArTs/notebooklm-mine/scripts/generate_notebooklm_static_site.py`
- `AvaTar-ArTs/pythons/generate_notebooklm_static_site.py`

Observed capabilities:

- versioned `0001`, `0002`, ... builds
- `latest` pointer
- grid/list views
- notebook discovery
- media/artifact rendering
- offline relative paths

Status: **first-party, healthy historical implementation**.

Hub action: clean successor implemented at `packages/publisher/notebooklm_hub_publisher.py` with manifests and lightweight artifact links.

### Duplicate cleaner

Found in:

- `AvaTar-ArTs/pythons/notebooklm_dedup_cleaner.py`

Role: identify `(1)` / `(2)` suffix duplicate files and compare them with originals.

Hub action: candidate for `packages/archive/cleanup.py` after review/tests.

## Agent and skill components

### NotebookLM Claude Code skill

Found in:

- `AvaTar-ArTs/my-supremepowers/agents/notebooklm/notebooklm/SKILL.md`
- copies/descendants in `all-agent-skills`, `my-codex`, and `notebooklm-mine`

Important behavior worth retaining:

- trigger on NotebookLM URLs/tasks
- notebook library awareness
- source-grounded answers
- mandatory completeness/follow-up loop
- batch research
- history/export/report concepts

Hub action: behavior rewritten transport-neutrally as `packages/skills/notebooklm-research/SKILL.md`.

### NotebookLM enhancement advisor

Found in:

- `my-supremepowers`
- `all-agent-skills`
- `my-codex`
- `notebooklm-mine`

Hub action: review later as a product/architecture advisor skill; deduplicate before importing.

### YouTube NotebookLM skill

Found in:

- `notebooklm-youtube-skill-og`
- `notebooklm-youtube-skill`

Historical behavior:

- video research
- person/entity research
- browser-driven notebook creation
- add YouTube + copied-text research sources
- generate Audio Overview
- screenshot-first UI control

Hub action: preserve as specialized workflow, not core architecture.

## MCP lineage

Repository:

- `AvaTar-ArTs/notebooklm-mcp`

Historical state:

- genuine NotebookLM MCP server lineage from `PleasePrompto/notebooklm-mcp`
- v1.2.1 history
- tool profiles
- resources/completions support
- Claude Code skill references
- Patchright/browser integration

Current state:

- main branch content appears overwritten by unrelated `seo-trend-analyzer` code.

Hub action:

1. recover historical NotebookLM commit(s) for behavioral comparison;
2. preserve original license/copyright;
3. do not make recovered third-party MCP code the Hub core;
4. implement future `packages/mcp` over the Hub backend contract.

## NOI / Hermes signals

`AvaTar-ArTs/noi-mine` audits identified NotebookLM as a large research/knowledge root and referenced:

- `.hermes/skills/note-taking/notebooklm-consolidation/`

Hub action: deep-review Hermes/NOI tooling in a later pass for archive consolidation, filesystem intelligence, indexing, and productization features.

## Immediate next migration targets

1. inspect and adapt `notebooklm_dedup_cleaner.py`;
2. build `NotebookLMPyBackend` adapter without copying upstream internals;
3. recover multi-profile/account model;
4. recover query history/export schemas;
5. recover source intelligence/observer ideas;
6. inspect Hermes `notebooklm-consolidation` implementation;
7. inspect NOI for orchestration/indexing components reusable by Hub;
8. recover old MCP feature surface and map it onto the Hub backend contract;
9. add tests for publisher and backend adapters;
10. add Claude Code and Codex setup packages.
