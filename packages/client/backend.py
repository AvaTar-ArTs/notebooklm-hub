"""NotebookLM Hub backend contracts.

The hub never assumes one specific NotebookLM transport. Implementations can
wrap an unofficial RPC client, MCP server, browser automation, exported local
archives, or future official APIs without changing callers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(slots=True)
class NotebookInfo:
    id: str
    title: str
    url: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SourceInfo:
    id: str
    title: str
    kind: str | None = None
    url: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ArtifactInfo:
    id: str
    title: str
    kind: str
    path: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class QueryResult:
    notebook_id: str
    question: str
    answer: str
    citations: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class KnowledgeBackend(Protocol):
    """Minimal backend contract required by NotebookLM Hub."""

    async def list_notebooks(self) -> list[NotebookInfo]: ...

    async def get_notebook(self, notebook_id: str) -> NotebookInfo: ...

    async def list_sources(self, notebook_id: str) -> list[SourceInfo]: ...

    async def list_artifacts(self, notebook_id: str) -> list[ArtifactInfo]: ...

    async def query(self, notebook_id: str, question: str) -> QueryResult: ...

    async def add_source(self, notebook_id: str, source: Any) -> SourceInfo: ...


class BackendUnavailable(RuntimeError):
    """Raised when a configured transport cannot currently access NotebookLM."""
