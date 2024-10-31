# Aviation Obstacle Vocabulary

**URI**: https://ap-no.cim4.eu/AviationObstacle/1.0

**Name**: AviationObstacle

## Classes

| Class | Description |
| --- | --- |
| [ACLineSegment](ACLineSegment.md) | A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.For symmetrical, transposed three phase lines, it is sufficient to use attributes of the line segment, which describe impedances and admittances for the entire length of the segment.  Additionally impedances can be computed by using length and associated per length impedances.The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines may have slightly different BaseVoltage.nominalVoltages and variation is allowed. Larger voltage difference in general requires use of an equivalent branch. |
| [ACLineSegmentSpan](ACLineSegmentSpan.md) | The part of a segment line between two consecutive points of support. |
| [ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | Deployment of an ACLineSegmentSpan. |
| [AssetDeployment](AssetDeployment.md) | Deployment of asset deployment in a power system resource role. |
| [BaseVoltage](BaseVoltage.md) | Defines a system base voltage which is referenced. |
| [ConductingEquipment](ConductingEquipment.md) | The parts of the AC power system that are designed to carry current or that are conductively connected through terminals. |
| [Conductor](Conductor.md) | Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system. |
| [ElementResource](ElementResource.md) | An element of an asset that has no electrical characteristic. |
| [Equipment](Equipment.md) | The parts of a power system that are physical devices, electronic or mechanical. |
| [Feature](Feature.md) | Defines a system base voltage which is referenced. |
| [Geometry](Geometry.md) | Geometric representation details. |
| [IdentifiedObject](IdentifiedObject.md) | This is a root class to provide common identification for all classes needing identification and naming attributes. |
| [LocationResource](LocationResource.md) | A spatial entity. LocationResource serves a similar purpose as PowerSystemResource but for non-electrical entites of interest to electrical utilities. |
| [OverheadStructure](OverheadStructure.md) | An overhead structure is an element of an electric transmission or distribution system that supports the overhead conductors and associated equipment used for the transmission of electricity. |
| [PowerSystemResource](PowerSystemResource.md) | A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated. |
| [SpatialObject](SpatialObject.md) | A spatial object is a physical object that has a location in space. It may have a geometric representation to describe its shape and position. |
| [Structure](Structure.md) | Construction holding assets such as conductors, transformers, switchgear, etc. |
| [StructureDeployment](StructureDeployment.md) | Deployment of a structure. |
| [Zone](Zone.md) | Defines a system base voltage which is referenced. |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AviationObstacleLightingKind](AviationObstacleLightingKind.md) | The kind of aviation obstacle lighting. |
| [AviationObstacleMarkingKind](AviationObstacleMarkingKind.md) | The kind of aviation obstacle marking. |
| [DeploymentStateKind](DeploymentStateKind.md) | Possible states of asset deployment. |
| [LocationMethodKind](LocationMethodKind.md) | The kind of aviation obstacle marking. |
| [ZoneKind](ZoneKind.md) | Kind of zone. |
| [ZoneStateKind](ZoneStateKind.md) | Current state of zone." |
