"""Stable Hub import path for the static site publisher prototype."""

from .notebooklm_hub_publisher import (
    Artifact,
    NotebookRecord,
    classify,
    discover_notebooks,
    publish,
    slugify,
)

__all__ = [
    "Artifact",
    "NotebookRecord",
    "classify",
    "discover_notebooks",
    "publish",
    "slugify",
]
