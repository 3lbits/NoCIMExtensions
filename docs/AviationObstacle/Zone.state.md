# Slot: state


_Current state of zone._



URI: [cim:Zone.state](https://cim.ucaiug.io/ns#Zone.state)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Zone](Zone.md) | Defines a system base voltage which is referenced |  no  |







## Properties

* Range: [ZoneStateKind](ZoneStateKind.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: state
description: Current state of zone.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: cim:Zone.state
alias: state
owner: Zone
domain_of:
- Zone
range: ZoneStateKind
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>