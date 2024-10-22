# Slot: name


_The name is any free human readable and possibly non unique text naming the object._



URI: [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM-generic#IdentifiedObject.name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[CableInfo](CableInfo.md) | Cable data |  no  |
[ConductorInfo](ConductorInfo.md) | Common class for rigid and flexible conductors |  no  |
[ConductingAssetInfo](ConductingAssetInfo.md) | Generic information for conducting asset |  no  |
[MultiCoreCableInfo](MultiCoreCableInfo.md) |  |  no  |
[IdentifiedObject](IdentifiedObject.md) | This is a root class to provide common identification for all classes needing... |  no  |
[ProductAssetModel](ProductAssetModel.md) | Asset model by a specific manufacturer |  no  |
[WireInfo](WireInfo.md) | Wire data that can be specified per line segment phase, or for the line segme... |  no  |
[AssetInfo](AssetInfo.md) | Set of attributes of an asset, representing typical datasheet information of ... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2007/profile#




## LinkML Source

<details>
```yaml
name: name
description: The name is any free human readable and possibly non unique text naming
  the object.
from_schema: http://iec.ch/TC57/2007/profile#
slot_uri: cim:IdentifiedObject.name
alias: name
owner: IdentifiedObject
domain_of:
- IdentifiedObject
range: string
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>