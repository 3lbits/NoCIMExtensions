# DCTopologicalNode

_DC bus._

**URI**: [cim:DCTopologicalNode](http://iec.ch/TC57/CIM100#DCTopologicalNode)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#4169E1'}}}%%
classDiagram
    class DCTopologicalNode
    click DCTopologicalNode href "/Models/Profiles/Topology/ConcreteClasses/DCTopologicalNode/"
    style DCTopologicalNode fill:#163289,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- DCTopologicalNode : inherits
            click IdentifiedObject href "/Models/Profiles/Topology/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#4169E1,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DCTopologicalNode --> DCBaseTerminal : DCTopologicalNode.DCTerminals

        DCBaseTerminal
            click DCBaseTerminal href "/Models/Profiles/Topology/AbstractClasses/DCBaseTerminal/"
            style DCBaseTerminal fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        DCTopologicalNode --> DCEquipmentContainer : DCTopologicalNode.DCEquipmentContainer

        DCEquipmentContainer
            click DCEquipmentContainer href "/Models/Profiles/Topology/AbstractClasses/DCEquipmentContainer/"
            style DCEquipmentContainer fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white
        DCTopologicalNode --> DCNode : DCTopologicalNode.DCNodes

        DCNode
            click DCNode href "/Models/Profiles/Topology/ConcreteClasses/DCNode/"
            style DCNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DCBaseTerminal --> DCTopologicalNode : DCBaseTerminal.DCTopologicalNode

        DCBaseTerminal
            click DCBaseTerminal href "/Models/Profiles/Topology/AbstractClasses/DCBaseTerminal/"
            style DCBaseTerminal fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DCEquipmentContainer --> DCTopologicalNode : DCEquipmentContainer.DCTopologicalNode

        DCEquipmentContainer
            click DCEquipmentContainer href "/Models/Profiles/Topology/AbstractClasses/DCEquipmentContainer/"
            style DCEquipmentContainer fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white

        DCNode --> DCTopologicalNode : DCNode.DCTopologicalNode

        DCNode
            click DCNode href "/Models/Profiles/Topology/ConcreteClasses/DCNode/"
            style DCNode fill:#00D156,stroke:#1F2A37,stroke-width:2px,rx:10,ry:10,color:white


        DCTopologicalNode : DCTopologicalNode.DCTerminals
        DCTopologicalNode : DCTopologicalNode.DCEquipmentContainer
        DCTopologicalNode : DCTopologicalNode.DCNodes
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/Topology/AbstractClasses/IdentifiedObject/)
    * **DCTopologicalNode**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| DCTerminals | [cim:DCTopologicalNode.DCTerminals](http://iec.ch/TC57/CIM100#DCTopologicalNode.DCTerminals) | No cardinality available DCBaseTerminal | See association end TopologicalNode.Terminal. | direct |
| DCEquipmentContainer | [cim:DCTopologicalNode.DCEquipmentContainer](http://iec.ch/TC57/CIM100#DCTopologicalNode.DCEquipmentContainer) | No cardinality available DCEquipmentContainer | The connectivity node container to which the topological node belongs. | direct |
| DCNodes | [cim:DCTopologicalNode.DCNodes](http://iec.ch/TC57/CIM100#DCTopologicalNode.DCNodes) | No cardinality available DCNode | The DC connectivity nodes combined together to form this DC topological node.  May depend on the current state of switches in the network. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile](http://iec.ch/TC57/ns/CIM/Topology-EUPackage_TopologyProfile)
