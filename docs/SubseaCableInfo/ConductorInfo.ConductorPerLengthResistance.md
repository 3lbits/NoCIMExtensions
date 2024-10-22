# Slot: ConductorPerLengthResistance


_Resistance per unit length of this conductor at a given temperature._



URI: [cim:ConductorInfo.ConductorPerLengthResistance](http://iec.ch/TC57/CIM-generic#ConductorInfo.ConductorPerLengthResistance)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ConductorInfo](ConductorInfo.md) | Common class for rigid and flexible conductors |  no  |
[CableInfo](CableInfo.md) | Cable data |  no  |
[WireInfo](WireInfo.md) | Wire data that can be specified per line segment phase, or for the line segme... |  no  |
[MultiCoreCableInfo](MultiCoreCableInfo.md) |  |  no  |







## Properties

* Range: [ResistancePerLengthTemperaturePoint](ResistancePerLengthTemperaturePoint.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2007/profile#




## LinkML Source

<details>
```yaml
name: ConductorPerLengthResistance
description: Resistance per unit length of this conductor at a given temperature.
from_schema: http://iec.ch/TC57/2007/profile#
slot_uri: cim:ConductorInfo.ConductorPerLengthResistance
alias: ConductorPerLengthResistance
owner: ConductorInfo
domain_of:
- ConductorInfo
range: ResistancePerLengthTemperaturePoint
multivalued: true
minimum_cardinality: 0

```
</details>