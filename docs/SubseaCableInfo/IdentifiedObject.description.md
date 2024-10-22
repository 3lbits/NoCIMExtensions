# Slot: description


_The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy._



URI: [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM-generic#IdentifiedObject.description)



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
name: description
description: The description is a free human readable text describing or naming the
  object. It may be non unique and may not correlate to a naming hierarchy.
from_schema: http://iec.ch/TC57/2007/profile#
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