# Slot: hasGeometry


_Geometric representation of the spatial object._



URI: [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PowerSystemResource](PowerSystemResource.md) | A power system resource (PSR) can be an item of equipment such as a switch, a... |  no  |
[OverheadStructure](OverheadStructure.md) | An overhead structure is an element of an electric transmission or distributi... |  no  |
[Conductor](Conductor.md) | Combination of conducting material with consistent electrical characteristics... |  no  |
[Feature](Feature.md) | Defines a system base voltage which is referenced |  no  |
[ConductingEquipment](ConductingEquipment.md) | The parts of the AC power system that are designed to carry current or that a... |  no  |
[LocationResource](LocationResource.md) | A spatial entity |  no  |
[Structure](Structure.md) | Construction holding assets such as conductors, transformers, switchgear, etc |  no  |
[Equipment](Equipment.md) | The parts of a power system that are physical devices, electronic or mechanic... |  no  |
[ACLineSegmentSpan](ACLineSegmentSpan.md) | The part of a segment line between two consecutive points of support |  no  |
[Zone](Zone.md) | Defines a system base voltage which is referenced |  no  |
[ACLineSegment](ACLineSegment.md) | A wire or combination of wires, with consistent electrical characteristics, b... |  no  |







## Properties

* Range: [Geometry](Geometry.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: hasGeometry
description: Geometric representation of the spatial object.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: geo:hasGeometry
alias: hasGeometry
owner: Feature
domain_of:
- Feature
range: Geometry
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>