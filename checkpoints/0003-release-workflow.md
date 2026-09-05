# Checkpoint 0003 - Reproducible Verification and Packaging

Captured: 2026-09-05

## Purpose
Move release verification and ZIP creation from ad-hoc local packaging into the repository's own CI boundary.

## Added release gate
`.github/workflows/verify-and-package.yml` performs:
1. exact-branch checkout
2. Python 3.13 setup
3. editable Hub install plus pytest
4. full test suite
5. `notebooklm-hub doctor --json`
6. six release ZIP builds
7. ZIP integrity/non-empty validation
8. release manifest and SHA-256 checksum generation
9. artifact upload as `notebooklm-hub-0.1.0-alpha-packages`

## Why this matters
A release artifact must be derived from the exact Git tree being reviewed. This avoids packaging a partial reconstruction or a developer workstation state that differs from GitHub.

## Verification requirement
Do not mark this checkpoint complete until the workflow run for the packaging commit has succeeded and its uploaded artifact has been inspected.
