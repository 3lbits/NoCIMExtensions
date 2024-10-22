# Slot: height


_Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc._



URI: [nc-no:Structure.height](http://cim4.eu/ns/nc-no#Structure.height)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Structure](Structure.md) | Construction holding assets such as conductors, transformers, switchgear, etc |  no  |
[OverheadStructure](OverheadStructure.md) | An overhead structure is an element of an electric transmission or distributi... |  no  |







## Properties

* Range: [Length](Length.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://ap-no.cim4.eu/AviationObstacle/1.0




## LinkML Source

<details>
```yaml
name: height
description: Visible height of structure above ground level for overhead construction
  (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc.
from_schema: https://ap-no.cim4.eu/AviationObstacle/1.0
slot_uri: nc-no:Structure.height
alias: height
owner: Structure
domain_of:
- Structure
range: Length
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>