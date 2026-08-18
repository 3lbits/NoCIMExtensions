# BatteryUnit

_An electrochemical energy storage device._

**URI**: [cim:BatteryUnit](http://iec.ch/TC57/CIM100#BatteryUnit)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class BatteryUnit
    click BatteryUnit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/BatteryUnit/"
    style BatteryUnit fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerElectronicsUnit <|-- BatteryUnit : inherits
            click PowerElectronicsUnit href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerElectronicsUnit/"
            style PowerElectronicsUnit fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- PowerElectronicsUnit : inherits
            click Equipment href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        BatteryUnit --> BatteryStateKind : BatteryUnit.batteryState

        BatteryStateKind
            click BatteryStateKind href "/Models/Profiles/SteadyStateHypothesis/Enumerations/BatteryStateKind/"
            style BatteryStateKind fill:#4D2D18,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        BatteryUnit : BatteryUnit.batteryState
        BatteryUnit : BatteryUnit.storedE
        Equipment : Equipment.inService
        IdentifiedObject : IdentifiedObject.mRID
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/Equipment/)
            * [PowerElectronicsUnit](/Models/Profiles/SteadyStateHypothesis/ConcreteClasses/PowerElectronicsUnit/)
                * **BatteryUnit**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| batteryState | [cim:BatteryUnit.batteryState](http://iec.ch/TC57/CIM100#BatteryUnit.batteryState) | No cardinality available BatteryStateKind | The current state of the battery (charging, full, etc.). | direct |
| storedE | [cim:BatteryUnit.storedE](http://iec.ch/TC57/CIM100#BatteryUnit.storedE) | No cardinality available RealEnergy | Amount of energy currently stored. The attribute shall be a positive value or zero and lower than BatteryUnit.ratedE. | direct |
| inService | [cim:Equipment.inService](http://iec.ch/TC57/CIM100#Equipment.inService) | No cardinality available boolean | Specifies the availability of the equipment. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. | Equipment |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile](http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EUPackage_SteadyStateHypothesisProfile)
