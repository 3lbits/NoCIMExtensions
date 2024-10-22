# Slot: description


_The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy._



URI: [cim:IdentifiedObject.description](https://cim.ucaiug.io/ns#IdentifiedObject.description)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PowerSystemResource](PowerSystemResource.md) | A power system resource (PSR) can be an item of equipment such as a switch, a... |  no  |
[OverheadStructure](OverheadStructure.md) | An overhead structure is an element of an electric transmission or distributi... |  no  |
[Conductor](Conductor.md) | Combination of conducting material with consistent electrical characteristics... |  no  |
[AssetDeployment](AssetDeployment.md) | Deployment of asset deployment in a power system resource role |  no  |
[StructureDeployment](StructureDeployment.md) | Deployment of a structure |  no  |
[ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | Deployment of an ACLineSegmentSpan |  no  |
[ConductingEquipment](ConductingEquipment.md) | The parts of the AC power system that are designed to carry current or that a... |  no  |
[LocationResource](LocationResource.md) | A spatial entity |  no  |
[Structure](Structure.md) | Construction holding assets such as conductors, transformers, switchgear, etc |  no  |
[Equipment](Equipment.md) | The parts of a power system that are physical devices, electronic or mechanic... |  no  |
[ElementResource](ElementResource.md) | An element of an asset that has no electrical characteristic |  no  |
[IdentifiedObject](IdentifiedObject.md) | This is a root class to provide common identification for all classes needing... |  no  |
[ACLineSegmentSpan](ACLineSegmentSpan.md) | The part of a segment line between two consecutive points of support |  no  |
[BaseVoltage](BaseVoltage.md) | Defines a system base voltage which is referenced |  no  |
[Zone](Zone.md) | Defines a system base voltage which is referenced |  no  |
[ACLineSegment](ACLineSegment.md) | A wire or combination of wires, with consistent electrical characteristics, b... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: description
description: The description is a free human readable text describing or naming the
  object. It may be non unique and may not correlate to a naming hierarchy.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: cim:IdentifiedObject.description
alias: description
owner: IdentifiedObject
domain_of:
- IdentifiedObject
range: string
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>