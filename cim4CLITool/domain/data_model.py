from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ReferenceClass:
    mRID: Optional[str] = None


@dataclass
class TypedValueClass:
    value: str
    type: str


@dataclass
class GeometryClass:
    asWKT: Optional[TypedValueClass] = None
    asGeoJSON: Optional[TypedValueClass] = None
    asGML: Optional[TypedValueClass] = None


@dataclass
class IdentifiedObjectClass:
    mRID: str
    description: Optional[str] = None
    name: Optional[str] = None


@dataclass
class OverheadStructureClass(IdentifiedObjectClass):
    aviationObstacleLightingKind: Optional[str] = None
    hasGeometry: Optional[GeometryClass] = None


@dataclass
class ACLineSegmentSpanClass(IdentifiedObjectClass):
    ACLineSegment: Optional[List[ReferenceClass]] = None


@dataclass
class DataModel:
    OverheadStructure: List[OverheadStructureClass] = field(default_factory=list)
    ACLineSegmentSpan: List[ACLineSegmentSpanClass] = field(default_factory=list)
