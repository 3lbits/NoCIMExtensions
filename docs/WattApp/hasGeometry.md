# Slot: hasGeometry


_Geometric representation of the spatial object._



URI: [geo:hasGeometry](http://www.opengis.net/ont/geosparql#hasGeometry)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PowerSystemResource](PowerSystemResource.md) | A power system resource (PSR) can be an item of equipment such as a switch, a... |  no  |
[Feature](Feature.md) | Defines a system base voltage which is referenced |  no  |
[EquipmentContainer](EquipmentContainer.md) | A modelling construct to provide a root class for containing equipment |  no  |
[Feeder](Feeder.md) | A collection of equipment for organizational purposes, used for grouping dist... |  no  |
[ConnectivityNodeContainer](ConnectivityNodeContainer.md) | A base class for all objects that may contain connectivity nodes or topologic... |  no  |







## Properties

* Range: [Geometry](Geometry.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0




## LinkML Source

<details>
```yaml
name: hasGeometry
description: Geometric representation of the spatial object.
from_schema: https://ap-no.cim4.eu/WattApp/1.0
slot_uri: geo:hasGeometry
alias: hasGeometry
owner: Feature
domain_of:
- Feature
range: Geometry
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>