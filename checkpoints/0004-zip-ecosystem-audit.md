# Checkpoint 0004 — ZIP Ecosystem Audit

Captured: 2026-09-05

## Scope

Audited the supplied `zip-repos/` directory and its `notebooklm_batches`
directory. The audit read ZIP central directories, selected manifests/README
files, small source files, and security-sensitive filenames. It did not execute
untrusted archive code or copy the raw repositories into the Hub.

## Inventory evidence

- The initial intake contained 37 ZIP archives and 1 source directory.
- A later rescan found 36 ZIP archives and no `notebooklm_batches` directory;
  those two previously observed inputs are currently missing from the supplied
  path and are recorded as an external-state discrepancy, not silently treated
  as audited in the generated manifest.
- Initial observation of `notebooklm_batches`: 20 files, 6,592,457 bytes.
- Exact duplicate groups:
  - `notebooklm-py-main.zip` = `notebooklm-py-main(1).zip`.
  - `notebooklm-py-main(2).zip` = `notebooklm-py-main(3).zip`.
- The four `notebooklm-py` archives have the same file tree but two exact
  archive-byte groups; they are not four independent implementations.
- Largest compressed sources: `notebooklm-podcasts` (~319 MB), `SurfSense`
  (~256 MB), `podcastfy` (~135 MB), `notebooklm_edson` (~68 MB), and
  `loackyPKM` (~56 MB).
- No ZIP path-traversal entries were detected by the inventory tool.

The current generated manifest therefore reports only the 36 ZIPs that are
present now. Re-run the inventory after restoring the missing batch inputs.

## Security evidence

- `t2m-research-agent-main/ezproxy_cookies.json` contains session-cookie values.
  It is excluded from Hub integration and must be treated as exposed
  credential material.
- `notebookllm-minus-main/private_ssh_aws.example/notebookllm-minus-dev-ssh.pem`
  is a private-key-shaped placeholder and must never become a real credential.
- Multiple archives contain `.env.example`, cookie/auth documentation, or
  credential-handling code. These are reference material only.

## Architecture conclusions

1. `notebooklm-py` is the strongest live transport reference and should be
   wrapped behind a pinned adapter, not duplicated.
2. `OpenNotebookLM` is the strongest self-hosted RAG/reference architecture.
3. `notebooklm-mcp` provides a rich MCP capability surface: citations, source
   operations, artifacts, libraries, resources, multi-account handling, and
   browser watchdog patterns.
4. `notebooklm_edson`, `professor-notebooklm`, and `notebooklm_batches` are
   valuable archive/import fixtures.
5. `SurfSense`, `eduStudio`, and the clone projects are broad application
   references, not Phase 1 drop-in dependencies.
6. Podcast/transcriber projects should contribute artifact contracts and
   verification patterns while their heavyweight runtime/media files remain
   external workers.

## Product changes

- Added the machine-readable archive inventory generator:
  `scripts/audit_zip_repositories.py`.
- Added generated inventory and provenance manifest:
  `research/generated/ZIP_REPOSITORY_INVENTORY.md` and
  `provenance/ZIP_REPOSITORY_MANIFEST.json`.
- Added curated capability/licensing/security analysis:
  `research/ZIP_REPOSITORY_ECOSYSTEM_AUDIT.md`.
- Added `zip-repos/` to Git ignore rules.
- Updated release packaging to exclude `zip-repos/`, scratch directories, and
  metadata files, preventing source archives from entering product bundles.

## Next checkpoint

Use `notebooklm_batches` as the first fixture corpus for a local archive
importer, checksum catalog, and evidence-span normalization. Do not begin by
vendoring the large application archives.
