# TapeLayer

_Tape layer base class._

**URI**: [cim:TapeLayer](http://iec.ch/TC57/CIM-generic#TapeLayer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class TapeLayer
    click TapeLayer href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/TapeLayer/"
    style TapeLayer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapeLayer <|-- GappedTape : inherits

        GappedTape
            click GappedTape href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/GappedTape/"
            style GappedTape fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapeLayer <|-- LappedTape : inherits

        LappedTape
            click LappedTape href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/LappedTape/"
            style LappedTape fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapeLayer <|-- LongitudinallyCorrugatedTape : inherits

        LongitudinallyCorrugatedTape
            click LongitudinallyCorrugatedTape href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/LongitudinallyCorrugatedTape/"
            style LongitudinallyCorrugatedTape fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        TapeLayer <|-- TubularTape : inherits

        TubularTape
            click TubularTape href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/TubularTape/"
            style TubularTape fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        MetallicSheathLayer <|-- TapeLayer : inherits
            click MetallicSheathLayer href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/MetallicSheathLayer/"
            style MetallicSheathLayer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        CableLayer <|-- MetallicSheathLayer : inherits
            click CableLayer href "/Models/Profiles/SubseaCableInfo/AbstractClasses/CableLayer/"
            style CableLayer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        CableInfo --> CableLayer : CableInfo.Layer

        CableInfo
            click CableInfo href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/CableInfo/"
            style CableInfo fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MultiCoreCableInfo --> CableLayer : MultiCoreCableInfo.BeltedLayer

        MultiCoreCableInfo
            click MultiCoreCableInfo href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/MultiCoreCableInfo/"
            style MultiCoreCableInfo fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MetallicSheathLayer --> CableShieldMaterialKind : MetallicSheathLayer.material

        CableShieldMaterialKind
            click CableShieldMaterialKind href "/Models/Profiles/SubseaCableInfo/Enumerations/CableShieldMaterialKind/"
            style CableShieldMaterialKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        MetallicSheathLayer : MetallicSheathLayer.isArmor
        MetallicSheathLayer : MetallicSheathLayer.material
        CableLayer : CableLayer.mRID
        CableLayer : CableLayer.diameterOverLayer
        CableLayer : CableLayer.layerOrder
```

## Inheritance
* [CableLayer](/Models/Profiles/SubseaCableInfo/AbstractClasses/CableLayer/)
    * [MetallicSheathLayer](/Models/Profiles/SubseaCableInfo/ConcreteClasses/MetallicSheathLayer/)
        * **TapeLayer**

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
