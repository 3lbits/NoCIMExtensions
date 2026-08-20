# DCBaseTerminal

_An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model requires that DC connections are distinct from AC connections._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:DCBaseTerminal](http://iec.ch/TC57/CIM100#DCBaseTerminal)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class DCBaseTerminal
    click DCBaseTerminal href "/Models/Profiles/Topology/AbstractClasses/DCBaseTerminal/"
    style DCBaseTerminal fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCBaseTerminal <|-- ACDCConverterDCTerminal : inherits

        ACDCConverterDCTerminal
            click ACDCConverterDCTerminal href "/Models/Profiles/Topology/ConcreteClasses/ACDCConverterDCTerminal/"
            style ACDCConverterDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCBaseTerminal <|-- DCTerminal : inherits

        DCTerminal
            click DCTerminal href "/Models/Profiles/Topology/ConcreteClasses/DCTerminal/"
            style DCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ACDCTerminal <|-- DCBaseTerminal : inherits
            click ACDCTerminal href "/Models/Profiles/Topology/AbstractClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- ACDCTerminal : inherits
            click IdentifiedObject href "/Models/Profiles/Topology/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCBaseTerminal --> DCTopologicalNode : DCBaseTerminal.DCTopologicalNode

        DCTopologicalNode
            click DCTopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/DCTopologicalNode/"
            style DCTopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCTopologicalNode --> DCBaseTerminal : DCTopologicalNode.DCTerminals

        DCTopologicalNode
            click DCTopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/DCTopologicalNode/"
            style DCTopologicalNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DCBaseTerminal : DCBaseTerminal.DCTopologicalNode
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Topology/AbstractClasses/IdentifiedObject/)
    * [ACDCTerminal](/Models/Profiles/Topology/AbstractClasses/ACDCTerminal/)
        * **DCBaseTerminal**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCTopologicalNode | [cim:DCBaseTerminal.DCTopologicalNode](http://iec.ch/TC57/CIM100#DCBaseTerminal.DCTopologicalNode) | No cardinality available DCTopologicalNode | See association end Terminal.TopologicalNode. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile](http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile)
