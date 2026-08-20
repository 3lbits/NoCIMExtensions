# DCTopologicalNode

_DC bus._

**URI**: [cim:DCTopologicalNode](http://iec.ch/TC57/CIM100#DCTopologicalNode)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class DCTopologicalNode
    click DCTopologicalNode href "/Models/Profiles/StateVariables/ConcreteClasses/DCTopologicalNode/"
    style DCTopologicalNode fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- DCTopologicalNode : inherits
            click IdentifiedObject href "/Models/Profiles/StateVariables/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DCTopologicalNode --> DCTopologicalIsland : DCTopologicalNode.DCTopologicalIsland

        DCTopologicalIsland
            click DCTopologicalIsland href "/Models/Profiles/StateVariables/ConcreteClasses/DCTopologicalIsland/"
            style DCTopologicalIsland fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DCTopologicalIsland --> DCTopologicalNode : DCTopologicalIsland.DCTopologicalNodes

        DCTopologicalIsland
            click DCTopologicalIsland href "/Models/Profiles/StateVariables/ConcreteClasses/DCTopologicalIsland/"
            style DCTopologicalIsland fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        DCTopologicalNode : DCTopologicalNode.DCTopologicalIsland
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/StateVariables/AbstractClasses/IdentifiedObject/)
    * **DCTopologicalNode**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCTopologicalIsland | [cim:DCTopologicalNode.DCTopologicalIsland](http://iec.ch/TC57/CIM100#DCTopologicalNode.DCTopologicalIsland) | No cardinality available DCTopologicalIsland | A DC topological node belongs to a DC topological island. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile](http://iec.ch/TC57/ns/CIM/StateVariables-EUPackage_StateVariablesProfile)
