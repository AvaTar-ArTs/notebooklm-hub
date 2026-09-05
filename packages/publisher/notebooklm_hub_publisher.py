#!/usr/bin/env python3
"""NotebookLM Hub static knowledge-site publisher.

Hub-native successor to AvaTar-ArTs' historical
`generate_notebooklm_static_site.py`.

Goals:
- immutable numbered builds
- deterministic notebook discovery
- machine-readable manifests
- lightweight HTML pages that link to source artifacts rather than embedding
  enormous blobs directly into the page
- offline-friendly relative links

This module intentionally contains no NotebookLM RPC/browser code. It publishes
an already-exported archive. Live retrieval belongs behind `packages/client`.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


BUILD_RE = re.compile(r"^\d{4}$")
SKIP_NAMES = {".git", ".venv", "__pycache__", "site", "versions"}


@dataclass(frozen=True)
class Artifact:
    path: str
    name: str
    extension: str
    size: int
    kind: str


@dataclass(frozen=True)
class NotebookRecord:
    name: str
    slug: str
    source_path: str
    artifacts: list[Artifact]


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.strip().lower())
    return re.sub(r"-{2,}", "-", value).strip("-")[:80] or "notebook"


def classify(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}:
        return "audio"
    if ext in {".mp4", ".mov", ".webm", ".mkv"}:
        return "video"
    if ext in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
        return "image"
    if ext == ".pdf":
        return "pdf"
    if ext in {".md", ".txt", ".csv", ".json", ".xml", ".yaml", ".yml"}:
        return "text"
    if ext in {".html", ".htm"}:
        return "html"
    return "other"


def next_build_id(versions_dir: Path) -> str:
    versions_dir.mkdir(parents=True, exist_ok=True)
    nums = [int(p.name) for p in versions_dir.iterdir() if p.is_dir() and BUILD_RE.match(p.name)]
    return f"{(max(nums) if nums else 0) + 1:04d}"


def unique_slugs(names: Iterable[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    counts: dict[str, int] = {}
    for name in names:
        base = slugify(name)
        counts[base] = counts.get(base, 0) + 1
        result[name] = base if counts[base] == 1 else f"{base}-{counts[base]}"
    return result


def discover_notebooks(root: Path) -> list[NotebookRecord]:
    dirs = [
        p for p in sorted(root.iterdir(), key=lambda p: p.name.lower())
        if p.is_dir() and not p.name.startswith(".") and p.name not in SKIP_NAMES
    ]
    slugs = unique_slugs(p.name for p in dirs)
    records: list[NotebookRecord] = []

    for notebook_dir in dirs:
        artifacts: list[Artifact] = []
        for item in sorted(notebook_dir.rglob("*"), key=lambda p: str(p).lower()):
            if not item.is_file() or item.name.startswith("."):
                continue
            rel = item.relative_to(root).as_posix()
            artifacts.append(
                Artifact(
                    path=rel,
                    name=item.name,
                    extension=item.suffix.lower(),
                    size=item.stat().st_size,
                    kind=classify(item),
                )
            )
        records.append(
            NotebookRecord(
                name=notebook_dir.name,
                slug=slugs[notebook_dir.name],
                source_path=notebook_dir.relative_to(root).as_posix(),
                artifacts=artifacts,
            )
        )
    return records


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    return f"{size} B"


def render_notebook(record: NotebookRecord, archive_root: Path, page: Path) -> str:
    rows: list[str] = []
    for artifact in record.artifacts:
        target = archive_root / artifact.path
        href = Path(os.path.relpath(target, page.parent)).as_posix()
        rows.append(
            "<tr>"
            f"<td>{html.escape(artifact.kind)}</td>"
            f"<td><a href=\"{html.escape(href)}\">{html.escape(artifact.name)}</a></td>"
            f"<td>{html.escape(human_size(artifact.size))}</td>"
            "</tr>"
        )
    table = "\n".join(rows) or '<tr><td colspan="3">No artifacts discovered.</td></tr>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(record.name)}</title><link rel="stylesheet" href="../styles.css"></head>
<body><main><p><a href="../index.html">← all notebooks</a></p><h1>{html.escape(record.name)}</h1>
<p>{len(record.artifacts)} indexed artifacts</p>
<table><thead><tr><th>Kind</th><th>Artifact</th><th>Size</th></tr></thead><tbody>{table}</tbody></table>
</main></body></html>"""


def render_index(records: list[NotebookRecord], build_id: str) -> str:
    cards = "\n".join(
        f'<li><a href="notebooks/{html.escape(r.slug)}.html">{html.escape(r.name)}</a> '
        f'<small>{len(r.artifacts)} artifacts</small></li>' for r in records
    )
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NotebookLM Hub build {build_id}</title><link rel="stylesheet" href="styles.css"></head>
<body><main><h1>NotebookLM Hub</h1><p>Immutable build <strong>{build_id}</strong></p><ul>{cards}</ul></main></body></html>"""


CSS = """
:root{color-scheme:dark;font-family:Inter,ui-sans-serif,system-ui,sans-serif;background:#0b0c10;color:#e9edf1}
body{margin:0}main{max-width:1100px;margin:auto;padding:2rem}a{color:#71e6c1}small{opacity:.65}
ul{line-height:1.9;padding-left:1.2rem}table{width:100%;border-collapse:collapse;margin-top:1rem}
th,td{text-align:left;padding:.65rem;border-bottom:1px solid #2b3038}th{color:#b8c0ca}
""".strip()


def publish(archive_root: Path, output_root: Path) -> Path:
    archive_root = archive_root.resolve()
    output_root = output_root.resolve()
    versions_dir = output_root / "versions"
    build_id = next_build_id(versions_dir)
    build_dir = versions_dir / build_id
    records = discover_notebooks(archive_root)

    write(build_dir / "styles.css", CSS)
    write(build_dir / "index.html", render_index(records, build_id))

    for record in records:
        page = build_dir / "notebooks" / f"{record.slug}.html"
        write(page, render_notebook(record, archive_root, page))

    manifest = {
        "schema": 1,
        "build_id": build_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "archive_root": str(archive_root),
        "notebook_count": len(records),
        "artifact_count": sum(len(r.artifacts) for r in records),
        "notebooks": [
            {**asdict(r), "artifacts": [asdict(a) for a in r.artifacts]}
            for r in records
        ],
    }
    write(build_dir / "manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))

    latest_manifest = {
        "latest": build_id,
        "path": f"versions/{build_id}/",
        "generated_at": manifest["generated_at"],
    }
    write(output_root / "latest.json", json.dumps(latest_manifest, indent=2))

    latest = output_root / "latest"
    if latest.is_symlink() or latest.is_file():
        latest.unlink()
    elif latest.exists():
        shutil.rmtree(latest)
    try:
        latest.symlink_to(Path("versions") / build_id, target_is_directory=True)
    except OSError:
        # Windows / restricted environments can use latest.json instead.
        pass

    return build_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish a NotebookLM archive as a versioned static site")
    parser.add_argument("archive", type=Path, help="NotebookLM export/archive root")
    parser.add_argument("--output", type=Path, default=Path("site"), help="Output site root")
    args = parser.parse_args()
    build = publish(args.archive, args.output)
    print(build)


if __name__ == "__main__":
    main()
