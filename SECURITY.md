# Security and Privacy

NotebookLM Hub may interoperate with services that require browser sessions, cookies, OAuth-style tokens, local credentials, or provider API keys. Those secrets are execution state, not knowledge artifacts.

## Never commit
- browser cookies or storage state
- OAuth/access/refresh tokens
- passwords
- API keys
- private session payloads
- `.env` files containing real values
- exports whose primary purpose is credential recovery

## Historical research
Historical documentation may discuss authentication architecture. When consolidating it into Hub, preserve the architectural lesson while replacing personal account identifiers and credentials with generic examples.

## Provider adapters
Adapters must keep credentials outside provider-neutral records. `SourceRecord`, `EvidenceRecord`, and `ArtifactManifest` may contain provider names and stable public identifiers, but never authentication secrets.

## Reporting
For vulnerabilities in Hub-native code, open a private security report where available rather than publishing exploit details in a public issue.
