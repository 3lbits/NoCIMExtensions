# LoadArea

_The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling._

**URI**: [cim:LoadArea](http://iec.ch/TC57/CIM100#LoadArea)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class LoadArea
    click LoadArea href "/Models/Profiles/CoreEquipment/ConcreteClasses/LoadArea/"
    style LoadArea fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyArea <|-- LoadArea : inherits
            click EnergyArea href "/Models/Profiles/CoreEquipment/AbstractClasses/EnergyArea/"
            style EnergyArea fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- EnergyArea : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        LoadArea --> SubLoadArea : LoadArea.SubLoadAreas

        SubLoadArea
            click SubLoadArea href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubLoadArea/"
            style SubLoadArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EnergyArea --> ControlArea : EnergyArea.ControlArea

        ControlArea
            click ControlArea href "/Models/Profiles/CoreEquipment/AbstractClasses/ControlArea/"
            style ControlArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ControlArea --> EnergyArea : ControlArea.EnergyArea

        ControlArea
            click ControlArea href "/Models/Profiles/CoreEquipment/AbstractClasses/ControlArea/"
            style ControlArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SubLoadArea --> LoadArea : SubLoadArea.LoadArea

        SubLoadArea
            click SubLoadArea href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubLoadArea/"
            style SubLoadArea fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        LoadArea : LoadArea.SubLoadAreas
        EnergyArea : EnergyArea.ControlArea
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [EnergyArea](/Models/Profiles/CoreEquipment/AbstractClasses/EnergyArea/)
        * **LoadArea**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| SubLoadAreas | [cim:LoadArea.SubLoadAreas](http://iec.ch/TC57/CIM100#LoadArea.SubLoadAreas) | No cardinality available SubLoadArea | The SubLoadAreas in the LoadArea. | direct |
| ControlArea | [cim:EnergyArea.ControlArea](http://iec.ch/TC57/CIM100#EnergyArea.ControlArea) | No cardinality available ControlArea | The control area specification that is used for the load forecast. | EnergyArea |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
