# NotebookLM Hub

AvaTar-ArTs' consolidated NotebookLM research, automation, agent, and publishing workspace.

## Purpose

This repository is the integration hub for a proprietary NotebookLM-oriented research and development stack assembled from Steven Chaplinski / AvaTar-ArTs projects, experiments, automation, and research assets.

The hub is designed to unify four layers:

1. **Research & knowledge** — notebook archives, metadata, source intelligence, and project memory.
2. **Programmatic access** — Python/RPC and CLI adapters for NotebookLM workflows.
3. **Agent access** — Claude Code, Codex, MCP, skills, and related agent integrations.
4. **Publishing** — static knowledge-site generation from NotebookLM archives and artifacts.

## Consolidation rule

First-party AvaTar-ArTs code may be integrated directly. Third-party or upstream-derived code must retain its original license and provenance and will initially live behind explicit `vendor/`, `adapters/`, or compatibility boundaries until replaced or substantially reimplemented.

## Planned layout

```text
notebooklm-hub/
├── packages/
│   ├── client/       # proprietary access abstraction
│   ├── publisher/    # NotebookLM → static knowledge sites
│   ├── skills/       # agent skills and workflows
│   └── mcp/          # MCP-facing integration layer
├── adapters/
│   ├── claude-code/
│   ├── codex/
│   └── notebooklm/
├── provenance/       # source lineage and licensing notes
├── research/         # architecture audits and migration notes
└── vendor/           # preserved upstream-derived components, if needed
```

## Initial source family

The first consolidation pass is drawing from these AvaTar-ArTs repositories and histories:

- `AvaTar-ArTs/notebooklm-mine`
- `AvaTar-ArTs/pythons`
- `AvaTar-ArTs/my-supremepowers`
- `AvaTar-ArTs/my-codex`
- `AvaTar-ArTs/notebooklm-mcp`
- `AvaTar-ArTs/notebooklm-skill`
- `AvaTar-ArTs/notebooklm-youtube-skill`
- `AvaTar-ArTs/notebooklm-youtube-skill-og`
- `AvaTar-ArTs/noi-mine`

This repository starts as the consolidation point, not as a claim that every historical component is first-party or relicensable.
