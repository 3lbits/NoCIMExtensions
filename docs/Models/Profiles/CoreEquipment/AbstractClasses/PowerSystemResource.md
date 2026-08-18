# PowerSystemResource

_A power system resource (PSR) can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated._

*__NOTE__: this is an abstract class and should not be instantiated directly

**URI**: [cim:PowerSystemResource](http://iec.ch/TC57/CIM100#PowerSystemResource)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class PowerSystemResource
    click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
    style PowerSystemResource fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- BoundaryPoint : inherits

        BoundaryPoint
            click BoundaryPoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/BoundaryPoint/"
            style BoundaryPoint fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- CAESPlant : inherits

        CAESPlant
            click CAESPlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/CAESPlant/"
            style CAESPlant fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- CogenerationPlant : inherits

        CogenerationPlant
            click CogenerationPlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/CogenerationPlant/"
            style CogenerationPlant fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- CombinedCyclePlant : inherits

        CombinedCyclePlant
            click CombinedCyclePlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/CombinedCyclePlant/"
            style CombinedCyclePlant fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- ConnectivityNodeContainer : inherits

        ConnectivityNodeContainer
            click ConnectivityNodeContainer href "/Models/Profiles/CoreEquipment/AbstractClasses/ConnectivityNodeContainer/"
            style ConnectivityNodeContainer fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- ControlArea : inherits

        ControlArea
            click ControlArea href "/Models/Profiles/CoreEquipment/AbstractClasses/ControlArea/"
            style ControlArea fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- Equipment : inherits

        Equipment
            click Equipment href "/Models/Profiles/CoreEquipment/AbstractClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- HydroPowerPlant : inherits

        HydroPowerPlant
            click HydroPowerPlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroPowerPlant/"
            style HydroPowerPlant fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- RegulatingControl : inherits

        RegulatingControl
            click RegulatingControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulatingControl/"
            style RegulatingControl fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- SolarPowerPlant : inherits

        SolarPowerPlant
            click SolarPowerPlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/SolarPowerPlant/"
            style SolarPowerPlant fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- TapChanger : inherits

        TapChanger
            click TapChanger href "/Models/Profiles/CoreEquipment/AbstractClasses/TapChanger/"
            style TapChanger fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        PowerSystemResource <|-- WindPowerPlant : inherits

        WindPowerPlant
            click WindPowerPlant href "/Models/Profiles/CoreEquipment/ConcreteClasses/WindPowerPlant/"
            style WindPowerPlant fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * **PowerSystemResource**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
