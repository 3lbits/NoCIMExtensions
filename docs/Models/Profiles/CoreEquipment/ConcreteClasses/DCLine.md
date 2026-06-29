# DCLine

_Overhead lines and/or cables connecting two or more HVDC substations._

**URI**: [cim:DCLine](http://iec.ch/TC57/CIM100#DCLine)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class DCLine
    click DCLine href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCLine/"
    style DCLine fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        DCEquipmentContainer <|-- DCLine : inherits
            click DCEquipmentContainer href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCEquipmentContainer/"
            style DCEquipmentContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EquipmentContainer <|-- DCEquipmentContainer : inherits
            click EquipmentContainer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquipmentContainer/"
            style EquipmentContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConnectivityNodeContainer <|-- EquipmentContainer : inherits
            click ConnectivityNodeContainer href "/Models/Profiles/CoreEquipment/ConcreteClasses/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- ConnectivityNodeContainer : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCLine --> SubGeographicalRegion : DCLine.Region

        SubGeographicalRegion
            click SubGeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubGeographicalRegion/"
            style SubGeographicalRegion fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        DCEquipmentContainer --> DCNode : DCEquipmentContainer.DCNodes

        DCNode
            click DCNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCNode/"
            style DCNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        EquipmentContainer --> Equipment : EquipmentContainer.Equipments

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/"
            style Equipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ConnectivityNodeContainer --> ConnectivityNode : ConnectivityNodeContainer.ConnectivityNodes

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/ConnectivityNode/"
            style ConnectivityNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNode --> ConnectivityNodeContainer : ConnectivityNode.ConnectivityNodeContainer

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/ConnectivityNode/"
            style ConnectivityNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        DCNode --> DCEquipmentContainer : DCNode.DCEquipmentContainer

        DCNode
            click DCNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCNode/"
            style DCNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/"
            style Equipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        SubGeographicalRegion --> DCLine : SubGeographicalRegion.DCLines

        SubGeographicalRegion
            click SubGeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubGeographicalRegion/"
            style SubGeographicalRegion fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        DCLine : DCLine.Region
        DCEquipmentContainer : DCEquipmentContainer.DCNodes
        EquipmentContainer : EquipmentContainer.Equipments
        ConnectivityNodeContainer : ConnectivityNodeContainer.ConnectivityNodes
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/ConcreteClasses/PowerSystemResource/)
        * [ConnectivityNodeContainer](/Models/Profiles/CoreEquipment/ConcreteClasses/ConnectivityNodeContainer/)
            * [EquipmentContainer](/Models/Profiles/CoreEquipment/ConcreteClasses/EquipmentContainer/)
                * [DCEquipmentContainer](/Models/Profiles/CoreEquipment/ConcreteClasses/DCEquipmentContainer/)
                    * **DCLine**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Region | [cim:DCLine.Region](http://iec.ch/TC57/CIM100#DCLine.Region) | No cardinality available SubGeographicalRegion | The SubGeographicalRegion containing the DC line. | direct |
| DCNodes | [cim:DCEquipmentContainer.DCNodes](http://iec.ch/TC57/CIM100#DCEquipmentContainer.DCNodes) | No cardinality available DCNode | The DC nodes contained in the DC equipment container. | DCEquipmentContainer |
| Equipments | [cim:EquipmentContainer.Equipments](http://iec.ch/TC57/CIM100#EquipmentContainer.Equipments) | No cardinality available Equipment | Contained equipment. | EquipmentContainer |
| ConnectivityNodes | [cim:ConnectivityNodeContainer.ConnectivityNodes](http://iec.ch/TC57/CIM100#ConnectivityNodeContainer.ConnectivityNodes) | No cardinality available ConnectivityNode | Connectivity nodes which belong to this connectivity node container. | ConnectivityNodeContainer |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
