"""Compatibility entry point for the Hub's transport-neutral backend contract.

The canonical protocol currently lives in :mod:`packages.client.backend` while
the installable ``src/notebooklm_hub`` package is being consolidated.
"""

from .backend import (
    ArtifactInfo,
    BackendUnavailable,
    KnowledgeBackend,
    NotebookInfo,
    QueryResult,
    SourceInfo,
)

__all__ = [
    "ArtifactInfo",
    "BackendUnavailable",
    "KnowledgeBackend",
    "NotebookInfo",
    "QueryResult",
    "SourceInfo",
]
