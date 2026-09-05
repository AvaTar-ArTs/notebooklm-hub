"""Reproducible release bundling for NotebookLM Hub."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


COMPONENTS: dict[str, tuple[str, ...]] = {
    "research": ("research", "provenance", "README.md", "ARCHITECTURE.md", "CHANGELOG.md"),
    "runtime": ("src", "packages/client", "pyproject.toml", "README.md", "CHANGELOG.md"),
    "publisher": ("packages/publisher", "src/notebooklm_hub", "README.md", "CHANGELOG.md"),
    "skills": ("packages/skills", "AGENTS.md", "docs/HUB_WORKFLOW.md", "README.md", "CHANGELOG.md"),
    "docs": ("docs", "research", "provenance", "README.md", "ARCHITECTURE.md", "CHANGELOG.md"),
}

EXCLUDED_PARTS = {".git", "dist", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def _iter_files(root: Path, selectors: tuple[str, ...] | None = None):
    candidates: set[Path] = set()
    if selectors is None:
        candidates.update(path for path in root.rglob("*") if path.is_file())
    else:
        for selector in selectors:
            path = root / selector
            if path.is_file():
                candidates.add(path)
            elif path.is_dir():
                candidates.update(p for p in path.rglob("*") if p.is_file())
    for path in sorted(candidates):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        yield path, rel


def _write_zip(root: Path, destination: Path, selectors: tuple[str, ...] | None = None) -> None:
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path, rel in _iter_files(root, selectors):
            archive.write(path, rel.as_posix())


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_release(root: Path | str, out_dir: Path | str, *, version: str) -> dict:
    root = Path(root).resolve()
    out_dir = Path(out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    names: dict[str, tuple[str, ...] | None] = {"full": None, **COMPONENTS}
    archives: dict[str, dict[str, str | int]] = {}

    for component, selectors in names.items():
        filename = f"notebooklm-hub-{version}-{component}.zip"
        destination = out_dir / filename
        _write_zip(root, destination, selectors)
        archives[filename] = {
            "component": component,
            "sha256": _sha256(destination),
            "bytes": destination.stat().st_size,
        }

    manifest = {"product": "notebooklm-hub", "version": version, "archives": archives}
    (out_dir / "release-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (out_dir / "SHA256SUMS").write_text(
        "".join(f"{data['sha256']}  {name}\n" for name, data in sorted(archives.items())),
        encoding="utf-8",
    )
    return manifest
