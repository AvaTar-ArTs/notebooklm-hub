"""Provider-neutral records for evidence-grounded knowledge workflows."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class SourceRecord:
    id: str
    title: str
    kind: str | None = None
    uri: str | None = None
    provider: str | None = None
    checksum: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EvidenceRecord:
    id: str
    claim: str
    classification: str
    source_ids: list[str] = field(default_factory=list)
    confidence: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ArtifactManifest:
    id: str
    kind: str
    source_ids: list[str] = field(default_factory=list)
    parent_artifact_ids: list[str] = field(default_factory=list)
    research_object_ids: list[str] = field(default_factory=list)
    format: str | None = None
    provider: str | None = None
    model: str | None = None
    checksum: str | None = None
    verification_status: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
