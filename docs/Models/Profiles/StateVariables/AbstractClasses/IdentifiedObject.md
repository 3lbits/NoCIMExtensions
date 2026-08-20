# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:IdentifiedObject](http://iec.ch/TC57/CIM100#IdentifiedObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "/Models/Profiles/StateVariables/AbstractClasses/IdentifiedObject/"
    style IdentifiedObject fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ACDCTerminal : inherits

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/StateVariables/AbstractClasses/ACDCTerminal/"
            style ACDCTerminal fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DCTopologicalIsland : inherits

        DCTopologicalIsland
            click DCTopologicalIsland href "/Models/Profiles/StateVariables/ConcreteClasses/DCTopologicalIsland/"
            style DCTopologicalIsland fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DCTopologicalNode : inherits

        DCTopologicalNode
            click DCTopologicalNode href "/Models/Profiles/StateVariables/ConcreteClasses/DCTopologicalNode/"
            style DCTopologicalNode fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- TopologicalIsland : inherits

        TopologicalIsland
            click TopologicalIsland href "/Models/Profiles/StateVariables/ConcreteClasses/TopologicalIsland/"
            style TopologicalIsland fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
