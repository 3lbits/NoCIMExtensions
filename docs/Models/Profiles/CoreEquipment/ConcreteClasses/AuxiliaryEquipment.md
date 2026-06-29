# AuxiliaryEquipment

_AuxiliaryEquipment describe equipment that is not performing any primary functions but support for the equipment performing the primary function.
AuxiliaryEquipment is attached to primary equipment via an association with Terminal._

**URI**: [cim:AuxiliaryEquipment](http://iec.ch/TC57/CIM100#AuxiliaryEquipment)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AuxiliaryEquipment
    click AuxiliaryEquipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/AuxiliaryEquipment/"
    style AuxiliaryEquipment fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AuxiliaryEquipment <|-- FaultIndicator : inherits

        FaultIndicator
            click FaultIndicator href "/Models/Profiles/CoreEquipment/ConcreteClasses/FaultIndicator/"
            style FaultIndicator fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AuxiliaryEquipment <|-- Sensor : inherits

        Sensor
            click Sensor href "/Models/Profiles/CoreEquipment/ConcreteClasses/Sensor/"
            style Sensor fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AuxiliaryEquipment <|-- SurgeArrester : inherits

        SurgeArrester
            click SurgeArrester href "/Models/Profiles/CoreEquipment/ConcreteClasses/SurgeArrester/"
            style SurgeArrester fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AuxiliaryEquipment <|-- WaveTrap : inherits

        WaveTrap
            click WaveTrap href "/Models/Profiles/CoreEquipment/ConcreteClasses/WaveTrap/"
            style WaveTrap fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- AuxiliaryEquipment : inherits
            click Equipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        AuxiliaryEquipment --> Terminal : AuxiliaryEquipment.Terminal

        Terminal
            click Terminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Equipment --> EquipmentContainer : Equipment.EquipmentContainer

        EquipmentContainer
            click EquipmentContainer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquipmentContainer/"
            style EquipmentContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        Equipment --> OperationalLimitSet : Equipment.OperationalLimitSet

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer --> Equipment : EquipmentContainer.Equipments

        EquipmentContainer
            click EquipmentContainer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquipmentContainer/"
            style EquipmentContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> Equipment : OperationalLimitSet.Equipment

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> AuxiliaryEquipment : Terminal.AuxiliaryEquipment

        Terminal
            click Terminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        AuxiliaryEquipment : AuxiliaryEquipment.Terminal
        Equipment : Equipment.aggregate
        Equipment : Equipment.normallyInService
        Equipment : Equipment.EquipmentContainer
        Equipment : Equipment.OperationalLimitSet
        IdentifiedObject : IdentifiedObject.description
        IdentifiedObject : IdentifiedObject.energyIdentCodeEic
        IdentifiedObject : IdentifiedObject.mRID
        IdentifiedObject : IdentifiedObject.name
        IdentifiedObject : IdentifiedObject.shortName
```

## Inheritance
* [IdentifiedObject](/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/ConcreteClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/)
            * **AuxiliaryEquipment**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| Terminal | [cim:AuxiliaryEquipment.Terminal](http://iec.ch/TC57/CIM100#AuxiliaryEquipment.Terminal) | No cardinality available Terminal | The Terminal at the equipment where the AuxiliaryEquipment is attached. | direct |
| aggregate | [cim:Equipment.aggregate](http://iec.ch/TC57/CIM100#Equipment.aggregate) | No cardinality available boolean | The aggregate flag provides an alternative way of representing an aggregated (equivalent) element. It is applicable in cases when the dedicated classes for equivalent equipment do not have all of the attributes necessary to represent the required level of detail.  In case the flag is set to “true” the single instance of equipment represents multiple pieces of equipment that have been modelled together as an aggregate equivalent obtained by a network reduction procedure. Examples would be power transformers or synchronous machines operating in parallel modelled as a single aggregate power transformer or aggregate synchronous machine.  
The attribute is not used for EquivalentBranch, EquivalentShunt and EquivalentInjection. | Equipment |
| normallyInService | [cim:Equipment.normallyInService](http://iec.ch/TC57/CIM100#Equipment.normallyInService) | No cardinality available boolean | Specifies the availability of the equipment under normal operating conditions. True means the equipment is available for topology processing, which determines if the equipment is energized or not. False means that the equipment is treated by network applications as if it is not in the model. | Equipment |
| EquipmentContainer | [cim:Equipment.EquipmentContainer](http://iec.ch/TC57/CIM100#Equipment.EquipmentContainer) | No cardinality available EquipmentContainer | Container of this equipment. | Equipment |
| OperationalLimitSet | [cim:Equipment.OperationalLimitSet](http://iec.ch/TC57/CIM100#Equipment.OperationalLimitSet) | No cardinality available OperationalLimitSet | The operational limit sets associated with this equipment. | Equipment |
| description | [cim:IdentifiedObject.description](http://iec.ch/TC57/CIM100#IdentifiedObject.description) | No cardinality available string | The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. | IdentifiedObject |
| energyIdentCodeEic | [eu:IdentifiedObject.energyIdentCodeEic](http://iec.ch/TC57/CIM100-European#IdentifiedObject.energyIdentCodeEic) | No cardinality available string | The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. For details on EIC scheme please refer to ENTSO-E web site. | IdentifiedObject |
| mRID | [cim:IdentifiedObject.mRID](http://iec.ch/TC57/CIM100#IdentifiedObject.mRID) | No cardinality available string | Master resource identifier issued by a model authority. The mRID is unique within an exchange context. Global uniqueness is easily achieved by using a UUID, as specified in RFC 4122, for the mRID. The use of UUID is strongly recommended.
For CIMXML data files in RDF syntax conforming to IEC 61970-552, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. | IdentifiedObject |
| name | [cim:IdentifiedObject.name](http://iec.ch/TC57/CIM100#IdentifiedObject.name) | No cardinality available string | The name is any free human readable and possibly non unique text naming the object. | IdentifiedObject |
| shortName | [eu:IdentifiedObject.shortName](http://iec.ch/TC57/CIM100-European#IdentifiedObject.shortName) | No cardinality available string | The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. | IdentifiedObject |

### Schema Source
* from schema: [http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile](http://iec.ch/TC57/ns/CIM/CoreEquipment-EUPackage_CoreEquipmentProfile)
