# Slot: ratedCurrent


_Rated current._



URI: [cim:ConductingAssetInfo.ratedCurrent](http://iec.ch/TC57/CIM-generic#ConductingAssetInfo.ratedCurrent)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[CableInfo](CableInfo.md) | Cable data |  no  |
[ConductorInfo](ConductorInfo.md) | Common class for rigid and flexible conductors |  no  |
[ConductingAssetInfo](ConductingAssetInfo.md) | Generic information for conducting asset |  no  |
[MultiCoreCableInfo](MultiCoreCableInfo.md) |  |  no  |
[WireInfo](WireInfo.md) | Wire data that can be specified per line segment phase, or for the line segme... |  no  |







## Properties

* Range: [CurrentFlow](CurrentFlow.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2007/profile#




## LinkML Source

<details>
```yaml
name: ratedCurrent
description: Rated current.
from_schema: http://iec.ch/TC57/2007/profile#
slot_uri: cim:ConductingAssetInfo.ratedCurrent
alias: ratedCurrent
owner: ConductingAssetInfo
domain_of:
- ConductingAssetInfo
range: CurrentFlow
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>