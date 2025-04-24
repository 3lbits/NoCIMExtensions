from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json

@dataclass
class Vocabulary:
    id: str
    name: str
    title: str
    comments: Optional[str] = None
    prefixes: Dict[str, str] = field(default_factory=dict)
    imports: List[str] = field(default_factory=list)
    default_curi_maps: List[str] = field(default_factory=list)
    default_range: Optional[str] = None
    default_prefix: Optional[str] = None
    classes: Dict[str, 'ClassDefinition'] = field(default_factory=dict)
    enums: Dict[str, 'EnumDefinition'] = field(default_factory=dict)
    types: Dict[str, 'TypeDefinition'] = field(default_factory=dict)

@dataclass
class Attribute:
    description: Optional[str] = None
    slot_uri: Optional[str] = None
    range: Optional[str] = None
    minimum_cardinality: Optional[int] = None
    maximum_cardinality: Optional[int] = None

@dataclass
class ClassDefinition:
    description: Optional[str] = None
    comments: Optional[str] = None
    abstract: Optional[bool] = False
    class_uri: Optional[str] = None
    attributes: Optional[Dict[str, Attribute]] = None

@dataclass
class PermissibleValue:
    meaning: Optional[str] = None
    description: Optional[str] = None

@dataclass
class EnumDefinition:
    description: Optional[str] = None
    enum_uri: Optional[str] = None
    permissible_values: Dict[str, PermissibleValue] = field(default_factory=dict)

@dataclass
class TypeAnnotation:
    cim_data_type: Optional[bool] = None
    uri: Optional[str] = None

@dataclass
class TypeDefinition:
    uri: Optional[str] = None
    base: Optional[str] = None
    description: Optional[str] = None
    annotations: Optional[TypeAnnotation] = None

class Controller:

    def main():
        enum = EnumDefinition(
            description="The kind of aviation obstacle lighting.",
            enum_uri="https://ap-no.cim4.eu/AviationObstacle/1.0#AviationObstacleLightingKind",
            permissible_values={
            "AviationObstacleLightingKind": PermissibleValue(
                meaning="AviationObstacleLightingKind",
                description="The kind of aviation obstacle lighting."
            )
            }
        )
        print(json.dumps(enum, default=lambda o: o.__dict__, indent=4))

if __name__ == "__main__":
    Controller.main()