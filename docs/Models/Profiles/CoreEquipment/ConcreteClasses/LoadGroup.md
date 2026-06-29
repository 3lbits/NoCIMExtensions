# LoadGroup

_The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling._

**URI**: [cim:LoadGroup](http://iec.ch/TC57/CIM100#LoadGroup)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class LoadGroup
    click LoadGroup href "/Models/Profiles/CoreEquipment/ConcreteClasses/LoadGroup/"
    style LoadGroup fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LoadGroup <|-- ConformLoadGroup : inherits

        ConformLoadGroup
            click ConformLoadGroup href "/Models/Profiles/CoreEquipment/ConcreteClasses/ConformLoadGroup/"
            style ConformLoadGroup fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LoadGroup <|-- NonConformLoadGroup : inherits

        NonConformLoadGroup
            click NonConformLoadGroup href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonConformLoadGroup/"
            style NonConformLoadGroup fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- LoadGroup : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LoadGroup --> SubLoadArea : LoadGroup.SubLoadArea

        SubLoadArea
            click SubLoadArea href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubLoadArea/"
            style SubLoadArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SubLoadArea --> LoadGroup : SubLoadArea.LoadGroups

        SubLoadArea
            click SubLoadArea href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubLoadArea/"
            style SubLoadArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        LoadGroup : LoadGroup.SubLoadArea
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * **LoadGroup**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SubLoadArea | [cim:LoadGroup.SubLoadArea](http://iec.ch/TC57/CIM100#LoadGroup.SubLoadArea) | No cardinality available SubLoadArea | The SubLoadArea where the Loadgroup belongs. | direct |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
