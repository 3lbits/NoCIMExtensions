# EquipmentContainer

_A modelling construct to provide a root class for containing equipment._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:EquipmentContainer](http://iec.ch/TC57/CIM100#EquipmentContainer)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class EquipmentContainer
    click EquipmentContainer href "/Models/Profiles/CoreEquipment/AbstractClasses/EquipmentContainer/"
    style EquipmentContainer fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer <|-- Bay : inherits

        Bay
            click Bay href "/Models/Profiles/CoreEquipment/ConcreteClasses/Bay/"
            style Bay fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer <|-- DCEquipmentContainer : inherits

        DCEquipmentContainer
            click DCEquipmentContainer href "/Models/Profiles/CoreEquipment/AbstractClasses/DCEquipmentContainer/"
            style DCEquipmentContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer <|-- Line : inherits

        Line
            click Line href "/Models/Profiles/CoreEquipment/ConcreteClasses/Line/"
            style Line fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer <|-- Substation : inherits

        Substation
            click Substation href "/Models/Profiles/CoreEquipment/ConcreteClasses/Substation/"
            style Substation fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer <|-- VoltageLevel : inherits

        VoltageLevel
            click VoltageLevel href "/Models/Profiles/CoreEquipment/ConcreteClasses/VoltageLevel/"
            style VoltageLevel fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConnectivityNodeContainer <|-- EquipmentContainer : inherits
            click ConnectivityNodeContainer href "/Models/Profiles/CoreEquipment/AbstractClasses/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- ConnectivityNodeContainer : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer --> Equipment : EquipmentContainer.Equipments

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/AbstractClasses/Equipment/"
            style Equipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ConnectivityNodeContainer --> ConnectivityNode : ConnectivityNodeContainer.ConnectivityNodes

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/CoreEquipment/AbstractClasses/ConnectivityNode/"
            style ConnectivityNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        ConnectivityNode --> ConnectivityNodeContainer : ConnectivityNode.ConnectivityNodeContainer

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/CoreEquipment/AbstractClasses/ConnectivityNode/"
            style ConnectivityNode fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/AbstractClasses/Equipment/"
            style Equipment fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        EquipmentContainer : EquipmentContainer.Equipments
        ConnectivityNodeContainer : ConnectivityNodeContainer.ConnectivityNodes
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * [ConnectivityNodeContainer](/Models/Profiles/CoreEquipment/AbstractClasses/ConnectivityNodeContainer/)
            * **EquipmentContainer**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Equipments | [cim:EquipmentContainer.Equipments](http://iec.ch/TC57/CIM100#EquipmentContainer.Equipments) | No cardinality available Equipment | Contained equipment. | direct |
| ConnectivityNodes | [cim:ConnectivityNodeContainer.ConnectivityNodes](http://iec.ch/TC57/CIM100#ConnectivityNodeContainer.ConnectivityNodes) | No cardinality available ConnectivityNode | Connectivity nodes which belong to this connectivity node container. | ConnectivityNodeContainer |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
