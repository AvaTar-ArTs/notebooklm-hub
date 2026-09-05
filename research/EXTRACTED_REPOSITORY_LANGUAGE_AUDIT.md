# Extracted Repository Language and Curation Audit

Date: 2026-09-05  
Input: `/Users/steven/notebooklm-zip-repos` (read-only)  
Method: `scripts/audit_extracted_repositories.py`, README inspection, targeted source inspection. No extracted project was executed or modified.

## Result

The moved directory contains **36 extracted repositories** and **37 ZIP archives**. The previously observed `notebooklm_batches/` directory is absent from the moved location, so it remains an intake gap rather than an assumed component. The inventory is recorded in `provenance/EXTRACTED_REPOSITORY_MANIFEST.json` and `research/generated/EXTRACTED_REPOSITORY_INVENTORY.md`.

Translation is needed where the primary documentation is Portuguese, Chinese, Korean, Arabic, or Italian. English summaries in `research/translations/` are curated interpretations, not line-by-line translations and not a license to vendor source code.

## Translation decisions

| Repository | Documentation signal | Decision |
|---|---|---|
| `AcademIA-main` | Portuguese | Translate capability model and fallback/RAG ideas; do not vendor its implementation. |
| `eduStudio-main` | English + Traditional Chinese | English README is sufficient; retain as bilingual reference. |
| `loackyPKM-main` | Italian + English | Translate only architecture concepts if reused; mostly documentation. |
| `miniguia-estudos-notebooklm-main` | Portuguese | Translate study methodology and prompt experiments. |
| `miniguia-estudos-notebooklm-main 2` | Portuguese placeholder | Record as duplicate/low-signal; no product extraction. |
| `notebookllm-minus-main` | English + Arabic fragments | English is sufficient; security review required before any reuse. |
| `notebooklm_edson-main` | Portuguese | Translate workflow concepts only; redact account, notebook, plan, and personal metadata. |
| `professor-notebooklm-main` | Portuguese | Translate its exam-tutor data model and cross-source workflow. |
| `qiaomu-anything-to-notebooklm-main` | Chinese | Translate lawful ingestion/transform concepts; exclude paywall-bypass techniques. |
| `star-notebooklm-main` | English + Korean | English README is sufficient; Korean is a parallel translation. |
| `universal-transcriber-skill-main` | English + Arabic | English is sufficient; preserve language-aware transcription as a capability. |
| `unmark-main` | Chinese | Do not integrate; watermark-removal behavior needs explicit legal/product policy. |
| `zlibrary-to-notebooklm-main` | English + Chinese | English is sufficient; retain lawful-use and copyright boundary. |
| `SurfSense-main`, `skills-main` | English plus translations | English primary docs exist; do not mistake localized copies for missing documentation. |

## Safety and provenance findings

- `t2m-research-agent-main/ezproxy_cookies.json` is a credential-bearing browser/session artifact. Do not open, execute, package, or publish it; rotate the session if it may still be valid.
- `notebookllm-minus-main/private_ssh_aws.example/notebookllm-minus-dev-ssh.pem` is private-key-shaped even though it is presented as an example. Keep it outside the Hub.
- `notebooklm_edson-main/README.md` contains personal account and NotebookLM metadata. The English summary intentionally omits those identifiers.
- `.env.example` files are configuration templates, not automatically secrets, but they remain excluded from the product until reviewed.
- `qiaomu-anything-to-notebooklm-main` advertises paywall-bypass workflows. The Hub adopts source provenance and lawful-access checks, never circumvention instructions.
- `unmark-main` removes NotebookLM export watermarks. It is excluded from the core product pending ownership, attribution, and user-rights policy.
- Large media and generated stores in `notebooklm-podcasts-main`, `podcastfy-main`, `notebooklm_edson-main`, and `rag-notebooklm-main` are reference inputs only; the Hub stores contracts and metadata, not their blobs or databases.

## Curated outcome

The extracted ecosystem contributes four reusable patterns:

1. transport-neutral source and artifact contracts (`notebooklm-py`, `notebooklm-mcp`);
2. local-first, fallback-first ingestion and retrieval (`AcademIA`, `OpenNotebookLM`, `rag-notebooklm`);
3. durable study and assessment memory (`professor`, `miniguia`, `loackyPKM`);
4. asynchronous media transformation with observable jobs (`notebooklm_edson`, `podcastfy`, `eduStudio`).

These are mapped onto existing Hub packages rather than copied wholesale. The Hub remains the integration and provenance layer; upstream licenses and attribution must be preserved for any future vendored code.
