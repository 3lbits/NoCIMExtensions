# Slot: mRID


_Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements._



URI: [cim:IdentifiedObject.mRID](https://cim.ucaiug.io/ns#IdentifiedObject.mRID)



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
name: mRID
description: Master resource identifier issued by a model authority. The mRID is unique
  within an exchange context. Global uniqueness is easily achieved by using a UUID,
  as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.For
  CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped
  to rdf:ID or rdf:about attributes that identify CIM object elements.
from_schema: https://ap-no.cim4.eu/WattApp/1.0
slot_uri: cim:IdentifiedObject.mRID
alias: mRID
owner: IdentifiedObject
domain_of:
- IdentifiedObject
range: string
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>