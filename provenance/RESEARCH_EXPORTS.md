# Research Export Provenance

This manifest records the local source material used to create the Hub synthesis
in `research/NOTEBOOKLM_CLAUDE_CODE_CODEX_SYNTHESIS.md`.

## Source set

All three files are exports of the conversation titled **NotebookLM Claude Code
Codex Research**. They are alternate representations of one conversation, not
three independent research sources.

| Export | Format | Size | SHA-256 |
|---|---|---:|---|
| `/Users/steven/Downloads/NotebookLM_Claude_Code_Codex_Research.compact.jsonl` | compact JSONL | 184 KB | `f8cc7a681bae2ff610ab7b2bb39114a121d3b1b6c9df378cabd2c085f600cd29` |
| `/Users/steven/Downloads/NotebookLM_Claude_Code_Codex_Research.tavern.jsonl` | Tavern JSONL | 367 KB | `16269f48aff3f3757dcf38ca0be92cbe8530127a23d058f13fe2bd71702558f6` |
| `/Users/steven/Downloads/NotebookLM_Claude_Code_Codex_Research.json` | conversation JSON | 3.0 MB | `2d99265f41904574b59a7bf2cc08c6681842fa91591c98f6574f1c8f832a9a78` |

The JSON export contains one conversation with 627 mapping nodes and 336
text-bearing messages. Each JSONL export contains 31 records. The larger JSON
export is the canonical analysis input because it preserves conversation
structure, tool messages, URLs, and message roles.

## Handling rules

- The original exports remain in Downloads and are not copied into this
  repository.
- The synthesis distinguishes observed evidence, documented claims, and future
  hypotheses. Historical assistant claims are not treated as verified facts
  without a current repository or provider check.
- Private NotebookLM URLs, credentials, cookies, and conversation content must
  not be committed to the Hub.
- If the source files are regenerated, update this manifest and rerun the
  synthesis review before changing architecture or implementation decisions.

## Related artifacts

- Synthesis: `research/NOTEBOOKLM_CLAUDE_CODE_CODEX_SYNTHESIS.md`
- Ingestion checkpoint: `checkpoints/0001-research-export-ingestion.md`
