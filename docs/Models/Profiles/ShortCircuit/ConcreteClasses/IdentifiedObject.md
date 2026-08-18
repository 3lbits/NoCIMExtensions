# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

**URI**: [cim:IdentifiedObject](http://iec.ch/TC57/CIM100#IdentifiedObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "/Models/Profiles/ShortCircuit/ConcreteClasses/IdentifiedObject/"
    style IdentifiedObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ACDCTerminal : inherits

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/ShortCircuit/AbstractClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- MutualCoupling : inherits

        MutualCoupling
            click MutualCoupling href "/Models/Profiles/ShortCircuit/ConcreteClasses/MutualCoupling/"
            style MutualCoupling fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- PowerSystemResource : inherits

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/ShortCircuit/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- TransformerEnd : inherits

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/ShortCircuit/ConcreteClasses/TransformerEnd/"
            style TransformerEnd fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile](http://iec.ch/TC57/ns/CIM/ShortCircuit-EUPackage_ShortCircuitProfile)
