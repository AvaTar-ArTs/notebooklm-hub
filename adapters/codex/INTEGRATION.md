# Codex Integration

Codex is the Hub's implementation and verification surface. A Codex workflow
should:

1. read the repository instructions and current checkpoint;
2. inspect source and provenance before changing adapters or models;
3. implement behavior behind Hub-native contracts with regression tests;
4. distinguish local, mock, dry-run, and live provider execution;
5. verify generated files, ZIP contents, checksums, and Git diffs before
   committing or pushing.

Codex should consume the same evidence and artifact manifests as Claude Code;
neither agent is the system of record.
