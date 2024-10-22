# Slot: layerOrder


_Order of the layer outwards from the cable core.For a multi-core cable, belted layers must have their own order starting from the first belted layer.Intercalated layers (typically tapes, where each tape is both below and above the other tape) must share the same layer order._



URI: [cim:CableLayer.layerOrder](http://iec.ch/TC57/CIM-generic#CableLayer.layerOrder)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[NonMetallicSheathLayer](NonMetallicSheathLayer.md) | Uniform and continuous tubular non-metallic sheath |  no  |
[MetallicSheathLayer](MetallicSheathLayer.md) | Any metallic sheath (or metal screen), including foils, braids, armours, conc... |  no  |
[InsulationLayer](InsulationLayer.md) |  |  no  |
[ScreenLayer](ScreenLayer.md) | Electrical screen of non-metallic and/or metallic material |  no  |
[CableLayer](CableLayer.md) |  |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://iec.ch/TC57/2007/profile#




## LinkML Source

<details>
```yaml
name: layerOrder
description: Order of the layer outwards from the cable core.For a multi-core cable,
  belted layers must have their own order starting from the first belted layer.Intercalated
  layers (typically tapes, where each tape is both below and above the other tape)
  must share the same layer order.
from_schema: http://iec.ch/TC57/2007/profile#
slot_uri: cim:CableLayer.layerOrder
alias: layerOrder
owner: CableLayer
domain_of:
- CableLayer
range: integer
minimum_cardinality: 0
maximum_cardinality: 1

```
</details>