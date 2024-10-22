# Slot: installedDate


_Date and time asset was most recently installed._



URI: [nc-no:AssetDeployment.installedDate](http://cim4.eu/ns/nc-no#AssetDeployment.installedDate)



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
name: installedDate
description: Date and time asset was most recently installed.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: nc-no:AssetDeployment.installedDate
alias: installedDate
owner: AssetDeployment
domain_of:
- AssetDeployment
range: datetime
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>