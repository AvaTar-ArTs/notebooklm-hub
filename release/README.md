# Release Bundles

`notebooklm-hub release --version <version>` creates logical bundles in `dist/`:

- `full`: entire product source excluding build/cache directories
- `research`: research + provenance + architecture
- `runtime`: installable core + backend contract
- `publisher`: publisher and core records
- `skills`: agent/skill workflow surface
- `docs`: docs + research + provenance

It also writes `release-manifest.json` and `SHA256SUMS`.

Release ZIPs are generated artifacts and should normally be attached to releases or supplied separately rather than repeatedly committed to source history.
