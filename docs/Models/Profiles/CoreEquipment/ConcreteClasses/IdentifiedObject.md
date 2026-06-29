# IdentifiedObject

_This is a root class to provide common identification for all classes needing identification and naming attributes._

**URI**: [cim:IdentifiedObject](http://iec.ch/TC57/CIM100#IdentifiedObject)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class IdentifiedObject
    click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
    style IdentifiedObject fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ACDCTerminal : inherits

        ACDCTerminal
            click ACDCTerminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/ACDCTerminal/"
            style ACDCTerminal fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- BaseVoltage : inherits

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/CoreEquipment/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- BasicIntervalSchedule : inherits

        BasicIntervalSchedule
            click BasicIntervalSchedule href "/Models/Profiles/CoreEquipment/ConcreteClasses/BasicIntervalSchedule/"
            style BasicIntervalSchedule fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- BusNameMarker : inherits

        BusNameMarker
            click BusNameMarker href "/Models/Profiles/CoreEquipment/ConcreteClasses/BusNameMarker/"
            style BusNameMarker fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ConnectivityNode : inherits

        ConnectivityNode
            click ConnectivityNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/ConnectivityNode/"
            style ConnectivityNode fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ControlAreaGeneratingUnit : inherits

        ControlAreaGeneratingUnit
            click ControlAreaGeneratingUnit href "/Models/Profiles/CoreEquipment/ConcreteClasses/ControlAreaGeneratingUnit/"
            style ControlAreaGeneratingUnit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- Curve : inherits

        Curve
            click Curve href "/Models/Profiles/CoreEquipment/ConcreteClasses/Curve/"
            style Curve fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DCNode : inherits

        DCNode
            click DCNode href "/Models/Profiles/CoreEquipment/ConcreteClasses/DCNode/"
            style DCNode fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- DayType : inherits

        DayType
            click DayType href "/Models/Profiles/CoreEquipment/ConcreteClasses/DayType/"
            style DayType fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- EnergyArea : inherits

        EnergyArea
            click EnergyArea href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyArea/"
            style EnergyArea fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- EnergySchedulingType : inherits

        EnergySchedulingType
            click EnergySchedulingType href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergySchedulingType/"
            style EnergySchedulingType fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- FossilFuel : inherits

        FossilFuel
            click FossilFuel href "/Models/Profiles/CoreEquipment/ConcreteClasses/FossilFuel/"
            style FossilFuel fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- GeographicalRegion : inherits

        GeographicalRegion
            click GeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/GeographicalRegion/"
            style GeographicalRegion fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- LoadGroup : inherits

        LoadGroup
            click LoadGroup href "/Models/Profiles/CoreEquipment/ConcreteClasses/LoadGroup/"
            style LoadGroup fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- LoadResponseCharacteristic : inherits

        LoadResponseCharacteristic
            click LoadResponseCharacteristic href "/Models/Profiles/CoreEquipment/ConcreteClasses/LoadResponseCharacteristic/"
            style LoadResponseCharacteristic fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- OperationalLimit : inherits

        OperationalLimit
            click OperationalLimit href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimit/"
            style OperationalLimit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- OperationalLimitSet : inherits

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- OperationalLimitType : inherits

        OperationalLimitType
            click OperationalLimitType href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitType/"
            style OperationalLimitType fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- PhaseTapChangerTable : inherits

        PhaseTapChangerTable
            click PhaseTapChangerTable href "/Models/Profiles/CoreEquipment/ConcreteClasses/PhaseTapChangerTable/"
            style PhaseTapChangerTable fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- PowerSystemResource : inherits

        PowerSystemResource
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- RatioTapChangerTable : inherits

        RatioTapChangerTable
            click RatioTapChangerTable href "/Models/Profiles/CoreEquipment/ConcreteClasses/RatioTapChangerTable/"
            style RatioTapChangerTable fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- ReportingGroup : inherits

        ReportingGroup
            click ReportingGroup href "/Models/Profiles/CoreEquipment/ConcreteClasses/ReportingGroup/"
            style ReportingGroup fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- Season : inherits

        Season
            click Season href "/Models/Profiles/CoreEquipment/ConcreteClasses/Season/"
            style Season fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- SubGeographicalRegion : inherits

        SubGeographicalRegion
            click SubGeographicalRegion href "/Models/Profiles/CoreEquipment/ConcreteClasses/SubGeographicalRegion/"
            style SubGeographicalRegion fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- TieFlow : inherits

        TieFlow
            click TieFlow href "/Models/Profiles/CoreEquipment/ConcreteClasses/TieFlow/"
            style TieFlow fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        IdentifiedObject <|-- TransformerEnd : inherits

        TransformerEnd
            click TransformerEnd href "/Models/Profiles/CoreEquipment/ConcreteClasses/TransformerEnd/"
            style TransformerEnd fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white



        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* **IdentifiedObject**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | direct |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | direct |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | direct |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | direct |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | direct |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
