# NonMetallicSheathLayer

_Uniform and continuous tubular non-metallic sheath. This class allows for the representation of any sheaths not properly defined with it's children classes.For example, separation sheaths (inner sheath applied between two metallic coverings of different materials).Note: The term sheath is only used for metallic coverings in North America, whereas the term jacket is used for non-metallic coverings._

**URI**: [cim:NonMetallicSheathLayer](http://iec.ch/TC57/CIM-generic#NonMetallicSheathLayer)<br />
**Type**: Class

```mermaid
classDiagram
    class NonMetallicSheathLayer
    click NonMetallicSheathLayer href "../NonMetallicSheathLayer"
    style NonMetallicSheathLayer fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        NonMetallicSheathLayer <|-- BindingLayer : inherits
            click NonMetallicSheathLayer href "../NonMetallicSheathLayer"
            style NonMetallicSheathLayer rx:10,ry:10

        BindingLayer
            click BindingLayer href "../BindingLayer"
            style BindingLayer rx:10,ry:10

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
    * **NonMetallicSheathLayer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:CableLayer.mRID](http://iec.ch/TC57/CIM-generic#CableLayer.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | CableLayer |
| diameterOverLayer | [cim:CableLayer.diameterOverLayer](http://iec.ch/TC57/CIM-generic#CableLayer.diameterOverLayer) | 0..1 Length | Use either diameter over layer or layer thickness.Specification varies by manufacturer and manufacturing process. For extruded layers, the diameter is typically provided. For tapes, the thickness is typically applied. | CableLayer |
| layerOrder | [cim:CableLayer.layerOrder](http://iec.ch/TC57/CIM-generic#CableLayer.layerOrder) | 0..1 integer | Order of the layer outwards from the cable core.For a multi-core cable, belted layers must have their own order starting from the first belted layer.Intercalated layers (typically tapes, where each tape is both below and above the other tape) must share the same layer order. | CableLayer |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)