# Claude Code Integration

Claude Code is an execution surface for the Hub. A Claude workflow should:

1. identify the research object and notebook/source scope;
2. query a Hub backend through the transport-neutral contract;
3. preserve citations and source spans in evidence records;
4. make repository changes only after the evidence and plan are recorded;
5. attach tests, artifact manifests, and a checkpoint to the result.

The Hub must not require Claude-specific prompt state or credentials. Provider
configuration belongs outside the repository, and live NotebookLM access must
use explicit notebook IDs with per-worker isolation.
