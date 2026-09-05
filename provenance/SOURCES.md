# Source Provenance

This file tracks the lineage of components being consolidated into `AvaTar-ArTs/notebooklm-hub`.

## First-party AvaTar-ArTs sources

### Static knowledge-site publisher

Historical implementations:

- `AvaTar-ArTs/notebooklm-mine/scripts/generate_notebooklm_static_site.py`
- `AvaTar-ArTs/notebooklm-mine/notebooklm/scripts/generate_notebooklm_static_site.py`
- `AvaTar-ArTs/pythons/generate_notebooklm_static_site.py`

The hub publisher is a clean hub-native implementation inspired by the behavior of those scripts: immutable numbered builds, notebook discovery, generated indexes, and a latest-build pointer/manifest.

### Claude / agent NotebookLM skill

Historical implementation:

- `AvaTar-ArTs/my-supremepowers/agents/notebooklm/notebooklm/SKILL.md`

Related copies and descendants also exist in `all-agent-skills`, `my-codex`, and `notebooklm-mine`.

### Research and architecture records

- `AvaTar-ArTs/pythons/PythonKnowledge/NOTEBOOKLM_FRACTAL_ANALYSIS.md`
- `AvaTar-ArTs/pythons/PythonKnowledge/NOTEBOOKLM_ECOSYSTEM_GUIDE.md`
- `AvaTar-ArTs/notebooklm-mine/NOTEBOOKLM_INVENTORY.md`
- `AvaTar-ArTs/notebooklm-mine/CHANGELOG.md`
- `AvaTar-ArTs/noi-mine/docs/*` NotebookLM audit references

### Historical browser automation

Found in the consolidated NotebookLM skill/archive family:

- authentication/profile management
- Patchright/Playwright browser control
- query automation
- source extraction
- batch querying
- query history
- export/report generation
- multi-account profile support

These are being treated as design lineage. Broken/minified historical copies should not be promoted to canonical code without repair and tests.

## Upstream-derived components

### `notebooklm-py`

Historical copy:

- `AvaTar-ArTs/notebooklm-mine/notebooklm-py/`
- merged copies also appear in `AvaTar-ArTs/pythons`

Upstream copyright: **Teng Lin (2026)**, MIT License.

The MIT notice must remain with any copied or substantially derived implementation. The hub should prefer a clean adapter boundary around this code while the proprietary client abstraction is developed independently.

### Historical `notebooklm-mcp`

The repository `AvaTar-ArTs/notebooklm-mcp` historically contained the `PleasePrompto/notebooklm-mcp` lineage and later appears to have been overwritten by unrelated SEO Trend Analyzer code. Any recovery of the old MCP implementation must retain upstream license/copyright information and should initially be placed under `vendor/` or used only as implementation reference.

## Proprietary boundary

The proprietary value of NotebookLM Hub should live in first-party components such as:

- orchestration and workflow policies
- unified client interfaces
- multi-agent research/verification loops
- source and notebook registry
- local research-memory/archive integration
- publishing pipeline
- versioned knowledge sites
- Claude Code / Codex adapters
- research-to-product workflows
- cross-notebook intelligence and provenance

Third-party MIT components can be used commercially, modified, and distributed, but their copyright/license notices cannot be erased or represented as wholly original AvaTar-ArTs code.
