# InsulationScreenLayer

_A screen covering the insulation. Also called Insulation Shield._

**URI**: [cim:InsulationScreenLayer](http://iec.ch/TC57/CIM-generic#InsulationScreenLayer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class InsulationScreenLayer
    click InsulationScreenLayer href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/InsulationScreenLayer/"
    style InsulationScreenLayer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ScreenLayer <|-- InsulationScreenLayer : inherits
            click ScreenLayer href "/Models/Profiles/SubseaCableInfo/ConcreteClasses/ScreenLayer/"
            style ScreenLayer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        CableLayer <|-- ScreenLayer : inherits
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


        CableLayer : CableLayer.mRID
        CableLayer : CableLayer.diameterOverLayer
        CableLayer : CableLayer.layerOrder
```

## Inheritance
* [CableLayer](/Models/Profiles/SubseaCableInfo/AbstractClasses/CableLayer/)
    * [ScreenLayer](/Models/Profiles/SubseaCableInfo/ConcreteClasses/ScreenLayer/)
        * **InsulationScreenLayer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:CableLayer.mRID](http://iec.ch/TC57/CIM-generic#CableLayer.mRID) | 0..1 string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in IETF RFC 4122, for the mRID. The use of UUID is strongly recommended.For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | CableLayer |
| diameterOverLayer | [cim:CableLayer.diameterOverLayer](http://iec.ch/TC57/CIM-generic#CableLayer.diameterOverLayer) | 0..1 Length | Use either diameter over layer or layer thickness.Specification varies by manufacturer and manufacturing process. For extruded layers, the diameter is typically provided. For tapes, the thickness is typically applied. | CableLayer |
| layerOrder | [cim:CableLayer.layerOrder](http://iec.ch/TC57/CIM-generic#CableLayer.layerOrder) | 0..1 integer | Order of the layer outwards from the cable core.For a multi-core cable, belted layers must have their own order starting from the first belted layer.Intercalated layers (typically tapes, where each tape is both below and above the other tape) must share the same layer order. | CableLayer |

### Schema Source
* from schema: [http://iec.ch/TC57/2007/profile](http://iec.ch/TC57/2007/profile)
