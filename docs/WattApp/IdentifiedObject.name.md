# Slot: name


_The name is any free human readable and possibly non unique text naming the object._



URI: [cim:IdentifiedObject.name](https://cim.ucaiug.io/ns#IdentifiedObject.name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BaseIrregularTimeSeries](BaseIrregularTimeSeries.md) |  |  no  |
[CapacityTimePoint](CapacityTimePoint.md) |  |  no  |
[BaseTimeSeries](BaseTimeSeries.md) |  |  no  |
[PowerSystemResource](PowerSystemResource.md) | A power system resource (PSR) can be an item of equipment such as a switch, a... |  no  |
[IdentifiedObject](IdentifiedObject.md) | This is a root class to provide common identification for all classes needing... |  no  |
[EquipmentContainer](EquipmentContainer.md) | A modelling construct to provide a root class for containing equipment |  no  |
[Feeder](Feeder.md) | A collection of equipment for organizational purposes, used for grouping dist... |  no  |
[CapacitySchedule](CapacitySchedule.md) |  |  no  |
[ConnectivityNodeContainer](ConnectivityNodeContainer.md) | A base class for all objects that may contain connectivity nodes or topologic... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/WattApp/1.0




## LinkML Source

<details>
```yaml
name: name
description: The name is any free human readable and possibly non unique text naming
  the object.
from_schema: https://ap-no.cim4.eu/WattApp/1.0
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