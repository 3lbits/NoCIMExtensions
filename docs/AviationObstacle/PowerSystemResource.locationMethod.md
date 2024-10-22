# Slot: locationMethod


_Method used to derive geographical location for this entity._



URI: [nc-no:PowerSystemResource.locationMethod](http://cim4.eu/ns/nc-no#PowerSystemResource.locationMethod)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Structure](Structure.md) | Construction holding assets such as conductors, transformers, switchgear, etc |  no  |
[Zone](Zone.md) | Defines a system base voltage which is referenced |  no  |
[OverheadStructure](OverheadStructure.md) | An overhead structure is an element of an electric transmission or distributi... |  no  |
[LocationResource](LocationResource.md) | A spatial entity |  no  |







## Properties

* Range: [LocationMethodKind](LocationMethodKind.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: locationMethod
description: Method used to derive geographical location for this entity.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: nc-no:PowerSystemResource.locationMethod
alias: locationMethod
owner: LocationResource
domain_of:
- LocationResource
range: LocationMethodKind
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>