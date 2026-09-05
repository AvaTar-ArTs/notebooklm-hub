# Full Product Audit and Packaging Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Reconcile the complete research history with the GitHub implementation branch, preserve durable checkpoints, and produce validated full and component release bundles.

**Architecture:** Use the research exports as one provenance-tracked source set. Compare claims against the checked-out Git history and executable tree, carry the synthesis into the implementation branch, then invoke the repository release engine and independently validate every archive.

**Tech Stack:** Git, Markdown, Python 3.11+, the Hub release CLI, ZIP integrity checks, SHA-256 manifests, and the local agent-skills memory bridge.

---

### Task 1: Establish source and repository baselines

Record export hashes, conversation structure, current branch, GitHub refs, and working-tree state.

Verification: all three exports have stable hashes; the implementation branch resolves; no private raw export is staged.

### Task 2: Compare research claims with implementation

Review the conversation chronologically, compare its claimed files/capabilities with the GitHub tree and commit history, and classify each item as verified, partial, missing, or historical/unverified.

Verification: the comparison is recorded in a checkpoint and every major product claim has a repository reference or an explicit gap status.

### Task 3: Preserve synthesis and memory

Keep the research synthesis, provenance manifest, implementation plan, and checkpoint in the repository. Record the durable architectural decision in the shared agent-skills memory database.

Verification: files parse as Markdown, the memory entry is queryable, and no credentials or private conversation payloads are included.

### Task 4: Build release bundles

Run the Hub release command from a clean product tree to generate full, research, runtime, publisher, skills, and docs ZIPs plus manifests and checksums.

Verification: six archives exist, are non-empty, pass ZIP integrity checks, and are represented in both release manifests and SHA256SUMS.

### Task 5: Independent package verification

Extract the full archive into a fresh project-local verification directory, run compile and available tests, run the structural doctor, and inspect archive membership for expected component boundaries.

Verification: report exact pass/fail counts and any environment limitations; do not claim provider execution or CI success unless directly observed.

### Task 6: Final checkpoint and handoff

Record generated artifact paths, hashes, Git diff, remaining defects, and the next implementation checkpoint. Leave commit/push as a separate explicit action.

Verification: `git diff --check` passes, only intended files are changed, and the final status distinguishes local generation from remote publication.
