# Slot: BaseVoltage


_The associated Base Voltage._



URI: [cim:AssetDeployment.BaseVoltage](https://cim.ucaiug.io/ns#AssetDeployment.BaseVoltage)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AssetDeployment](AssetDeployment.md) | Deployment of asset deployment in a power system resource role |  no  |
[ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | Deployment of an ACLineSegmentSpan |  no  |
[StructureDeployment](StructureDeployment.md) | Deployment of a structure |  no  |







## Properties

* Range: [BaseVoltage](BaseVoltage.md)

## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AssetDeployment](AssetDeployment.md) | [BaseVoltage](BaseVoltage.md) | range | [BaseVoltage](BaseVoltage.md) |
| [ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | [BaseVoltage](BaseVoltage.md) | range | [BaseVoltage](BaseVoltage.md) |
| [StructureDeployment](StructureDeployment.md) | [BaseVoltage](BaseVoltage.md) | range | [BaseVoltage](BaseVoltage.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: BaseVoltage
description: The associated Base Voltage.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: cim:AssetDeployment.BaseVoltage
alias: BaseVoltage
owner: AssetDeployment
domain_of:
- AssetDeployment
range: BaseVoltage
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>