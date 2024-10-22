# Slot: notYetInstalledDate


_Date and time of asset deployment transition to not yet installed._



URI: [nc-no:AssetDeployment.notYetInstalledDate](http://cim4.eu/ns/nc-no#AssetDeployment.notYetInstalledDate)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[AssetDeployment](AssetDeployment.md) | Deployment of asset deployment in a power system resource role |  no  |
[ACLineSegmentSpanDeployment](ACLineSegmentSpanDeployment.md) | Deployment of an ACLineSegmentSpan |  no  |
[StructureDeployment](StructureDeployment.md) | Deployment of a structure |  no  |







## Properties

* Range: [Datetime](Datetime.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: notYetInstalledDate
description: Date and time of asset deployment transition to not yet installed.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: nc-no:AssetDeployment.notYetInstalledDate
alias: notYetInstalledDate
owner: AssetDeployment
domain_of:
- AssetDeployment
range: datetime
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>