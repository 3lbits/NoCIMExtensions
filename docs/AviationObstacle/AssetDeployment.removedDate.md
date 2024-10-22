# Slot: removedDate


_Date and time asset was most recently removed._



URI: [nc-no:AssetDeployment.removedDate](http://cim4.eu/ns/nc-no#AssetDeployment.removedDate)



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
name: removedDate
description: Date and time asset was most recently removed.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: nc-no:AssetDeployment.removedDate
alias: removedDate
owner: AssetDeployment
domain_of:
- AssetDeployment
range: datetime
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>