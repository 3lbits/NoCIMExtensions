# SkidWireLayer

_Layer with wires or assembly of wires, usually D-shaped, applied with a long length of lay over the cores of a pipe-type cable, to provide mechanical protection and to facilitate sliding while the cores are being pulled into the pipe.  Reference: IEC 60050-461_

**URI**: [cim:SkidWireLayer](http://iec.ch/TC57/CIM-generic#SkidWireLayer)<br />
**Type**: Class

```mermaid
classDiagram
    class SkidWireLayer
    click SkidWireLayer href "../SkidWireLayer"
    style SkidWireLayer fill:#9fdf9f,stroke:#333,stroke-width:2px,rx:10,ry:10

        ConcentricWireLayer <|-- SkidWireLayer : inherits
            click ConcentricWireLayer href "../ConcentricWireLayer"
            style ConcentricWireLayer rx:10,ry:10

        SkidWireLayer
            click SkidWireLayer href "../SkidWireLayer"
            style SkidWireLayer rx:10,ry:10

        MetallicSheathLayer <|-- ConcentricWireLayer : inherits
            click MetallicSheathLayer href "../MetallicSheathLayer"
            style MetallicSheathLayer rx:10,ry:10

        CableLayer <|-- MetallicSheathLayer : inherits
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

        MetallicSheathLayer --> CableShieldMaterialKind : MetallicSheathLayer.material

        CableShieldMaterialKind
            click CableShieldMaterialKind href "../CableShieldMaterialKind"
            style CableShieldMaterialKind fill:#FFCCCB,stroke:#333,stroke-width:2px,rx:10,ry:10

        MetallicSheathLayer : MetallicSheathLayer.isArmor
        MetallicSheathLayer : MetallicSheathLayer.material
        CableLayer : CableLayer.mRID
        CableLayer : CableLayer.diameterOverLayer
        CableLayer : CableLayer.layerOrder
```

## Inheritance
* [CableLayer](CableLayer.md)
    * [MetallicSheathLayer](MetallicSheathLayer.md)
        * [ConcentricWireLayer](ConcentricWireLayer.md)
            * **SkidWireLayer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| isArmor | [cim:MetallicSheathLayer.isArmor](http://iec.ch/TC57/CIM-generic#MetallicSheathLayer.isArmor) | 0..1 boolean | Indicates whether this metallic sheath is an armor, which is a covering consisting of a metal tape(s) or wires, generally used to protect the cable from external mechanical effects | MetallicSheathLayer |
| material | [cim:MetallicSheathLayer.material](http://iec.ch/TC57/CIM-generic#MetallicSheathLayer.material) | 0..1 CableShieldMaterialKind | Material og this metallic sheath layer. | MetallicSheathLayer |
| mRID | [cim:CableLayer.mRID](http://iec.ch/TC57/CIM-generic#CableLayer.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | CableLayer |
| diameterOverLayer | [cim:CableLayer.diameterOverLayer](http://iec.ch/TC57/CIM-generic#CableLayer.diameterOverLayer) | 0..1 Length | Use either diameter over layer or layer thickness.Specification varies by manufacturer and manufacturing process. For extruded layers, the diameter is typically provided. For tapes, the thickness is typically applied. | CableLayer |
| layerOrder | [cim:CableLayer.layerOrder](http://iec.ch/TC57/CIM-generic#CableLayer.layerOrder) | 0..1 integer | Order of the layer outwards from the cable core.For a multi-core cable, belted layers must have their own order starting from the first belted layer.Intercalated layers (typically tapes, where each tape is both below and above the other tape) must share the same layer order. | CableLayer |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)