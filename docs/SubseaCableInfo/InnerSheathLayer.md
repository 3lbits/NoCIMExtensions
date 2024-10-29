# InnerSheathLayer

_<b>Non-metallic</b> covering which surrounds the assembly of the cores (and fillers, if any) of a multiconductor cable and over which the protective covering is applied.For example, a bedding layer for an armour or reinforcement._

**URI**: [cim:InnerSheathLayer](http://iec.ch/TC57/CIM-generic#InnerSheathLayer)<br />
**Type**: Class

```mermaid
classDiagram
    class InnerSheathLayer
    click InnerSheathLayer href "../InnerSheathLayer"
    style InnerSheathLayer fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        NonMetallicSheathLayer <|-- InnerSheathLayer : inherits
            click NonMetallicSheathLayer href "../NonMetallicSheathLayer"
            style NonMetallicSheathLayer rx:10,ry:10

        InnerSheathLayer
            click InnerSheathLayer href "../InnerSheathLayer"
            style InnerSheathLayer rx:10,ry:10

        CableLayer <|-- NonMetallicSheathLayer : inherits
            click CableLayer href "../CableLayer"
            style CableLayer rx:10,ry:10


        CableInfo --> CableLayer : CableInfo.Layer

        CableInfo
            click CableInfo href "../CableInfo"
            style CableInfo fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10

        MultiCoreCableInfo --> CableLayer : MultiCoreCableInfo.BeltedLayer

        MultiCoreCableInfo
            click MultiCoreCableInfo href "../MultiCoreCableInfo"
            style MultiCoreCableInfo fill:#ffff99,stroke:#333,stroke-width:2px,rx:10,ry:10


        CableLayer : CableLayer.mRID
        CableLayer : CableLayer.diameterOverLayer
        CableLayer : CableLayer.layerOrder
```

## Inheritance
* [CableLayer](CableLayer.md)
    * [NonMetallicSheathLayer](NonMetallicSheathLayer.md)
        * **InnerSheathLayer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:CableLayer.mRID](http://iec.ch/TC57/CIM-generic#CableLayer.mRID) | 0..1 | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | CableLayer |
| diameterOverLayer | [cim:CableLayer.diameterOverLayer](http://iec.ch/TC57/CIM-generic#CableLayer.diameterOverLayer) | 0..1 | Use either diameter over layer or layer thickness.Specification varies by manufacturer and manufacturing process. For extruded layers, the diameter is typically provided. For tapes, the thickness is typically applied. | CableLayer |
| layerOrder | [cim:CableLayer.layerOrder](http://iec.ch/TC57/CIM-generic#CableLayer.layerOrder) | 0..1 | Order of the layer outwards from the cable core.For a multi-core cable, belted layers must have their own order starting from the first belted layer.Intercalated layers (typically tapes, where each tape is both below and above the other tape) must share the same layer order. | CableLayer |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile#](http://iec.ch/TC57/2007/profile#)
