# NonlinearShuntCompensator

_A non linear shunt compensator has bank or section admittance values that differ. The attributes g, b, g0 and b0 of the associated NonlinearShuntCompensatorPoint describe the total conductance and admittance of a NonlinearShuntCompensatorPoint at a section number specified by NonlinearShuntCompensatorPoint.sectionNumber._

**URI**: [cim:NonlinearShuntCompensator](http://iec.ch/TC57/CIM100#NonlinearShuntCompensator)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class NonlinearShuntCompensator
    click NonlinearShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensator/"
    style NonlinearShuntCompensator fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ShuntCompensator <|-- NonlinearShuntCompensator : inherits
            click ShuntCompensator href "/Models/Profiles/CoreEquipment/ConcreteClasses/ShuntCompensator/"
            style ShuntCompensator fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- ShuntCompensator : inherits
            click RegulatingCondEq href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
            click EnergyConnection href "/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyConnection/"
            style EnergyConnection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
            click ConductingEquipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/CoreEquipment/ConcreteClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/ConcreteClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/ConcreteClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensator --> NonlinearShuntCompensatorPoint : NonlinearShuntCompensator.NonlinearShuntCompensatorPoints

        NonlinearShuntCompensatorPoint
            click NonlinearShuntCompensatorPoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensatorPoint/"
            style NonlinearShuntCompensatorPoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ShuntCompensator --> Seconds : ShuntCompensator.aVRDelay

        Seconds
            click Seconds href "/Models/Profiles/CoreEquipment/ConcreteClasses/Seconds/"
            style Seconds fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ShuntCompensator --> Voltage : ShuntCompensator.nomU

        Voltage
            click Voltage href "/Models/Profiles/CoreEquipment/ConcreteClasses/Voltage/"
            style Voltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ShuntCompensator --> VoltagePerReactivePower : ShuntCompensator.voltageSensitivity

        VoltagePerReactivePower
            click VoltagePerReactivePower href "/Models/Profiles/CoreEquipment/ConcreteClasses/VoltagePerReactivePower/"
            style VoltagePerReactivePower fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        RegulatingCondEq --> RegulatingControl : RegulatingCondEq.RegulatingControl

        RegulatingControl
            click RegulatingControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulatingControl/"
            style RegulatingControl fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ConductingEquipment --> BaseVoltage : ConductingEquipment.BaseVoltage

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/CoreEquipment/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        ConductingEquipment --> Terminal : ConductingEquipment.Terminals

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

        BaseVoltage --> ConductingEquipment : BaseVoltage.ConductingEquipment

        BaseVoltage
            click BaseVoltage href "/Models/Profiles/CoreEquipment/ConcreteClasses/BaseVoltage/"
            style BaseVoltage fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        EquipmentContainer --> Equipment : EquipmentContainer.Equipments

        EquipmentContainer
            click EquipmentContainer href "/Models/Profiles/CoreEquipment/ConcreteClasses/EquipmentContainer/"
            style EquipmentContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        NonlinearShuntCompensatorPoint --> NonlinearShuntCompensator : NonlinearShuntCompensatorPoint.NonlinearShuntCompensator

        NonlinearShuntCompensatorPoint
            click NonlinearShuntCompensatorPoint href "/Models/Profiles/CoreEquipment/ConcreteClasses/NonlinearShuntCompensatorPoint/"
            style NonlinearShuntCompensatorPoint fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        OperationalLimitSet --> Equipment : OperationalLimitSet.Equipment

        OperationalLimitSet
            click OperationalLimitSet href "/Models/Profiles/CoreEquipment/ConcreteClasses/OperationalLimitSet/"
            style OperationalLimitSet fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RegulatingControl --> RegulatingCondEq : RegulatingControl.RegulatingCondEq

        RegulatingControl
            click RegulatingControl href "/Models/Profiles/CoreEquipment/ConcreteClasses/RegulatingControl/"
            style RegulatingControl fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        Terminal --> ConductingEquipment : Terminal.ConductingEquipment

        Terminal
            click Terminal href "/Models/Profiles/CoreEquipment/ConcreteClasses/Terminal/"
            style Terminal fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white


        NonlinearShuntCompensator : NonlinearShuntCompensator.NonlinearShuntCompensatorPoints
        ShuntCompensator : ShuntCompensator.aVRDelay
        ShuntCompensator : ShuntCompensator.grounded
        ShuntCompensator : ShuntCompensator.maximumSections
        ShuntCompensator : ShuntCompensator.nomU
        ShuntCompensator : ShuntCompensator.normalSections
        ShuntCompensator : ShuntCompensator.voltageSensitivity
        RegulatingCondEq : RegulatingCondEq.RegulatingControl
        ConductingEquipment : ConductingEquipment.BaseVoltage
        ConductingEquipment : ConductingEquipment.Terminals
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
            * [ConductingEquipment](/Models/Profiles/CoreEquipment/ConcreteClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/CoreEquipment/ConcreteClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/CoreEquipment/ConcreteClasses/RegulatingCondEq/)
                        * [ShuntCompensator](/Models/Profiles/CoreEquipment/ConcreteClasses/ShuntCompensator/)
                            * **NonlinearShuntCompensator**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| NonlinearShuntCompensatorPoints | [cim:NonlinearShuntCompensator.NonlinearShuntCompensatorPoints](http://iec.ch/TC57/CIM100#NonlinearShuntCompensator.NonlinearShuntCompensatorPoints) | No cardinality available NonlinearShuntCompensatorPoint | All points of the non-linear shunt compensator. | direct |
| aVRDelay | [cim:ShuntCompensator.aVRDelay](http://iec.ch/TC57/CIM100#ShuntCompensator.aVRDelay) | No cardinality available Seconds | An automatic voltage regulation delay (AVRDelay) which is the time delay from a change in voltage to when the capacitor is allowed to change state. This filters out temporary changes in voltage. | ShuntCompensator |
| grounded | [cim:ShuntCompensator.grounded](http://iec.ch/TC57/CIM100#ShuntCompensator.grounded) | No cardinality available boolean | Used for Yn and Zn connections. True if the neutral is solidly grounded. | ShuntCompensator |
| maximumSections | [cim:ShuntCompensator.maximumSections](http://iec.ch/TC57/CIM100#ShuntCompensator.maximumSections) | No cardinality available integer | The maximum number of sections that may be switched in. | ShuntCompensator |
| nomU | [cim:ShuntCompensator.nomU](http://iec.ch/TC57/CIM100#ShuntCompensator.nomU) | No cardinality available Voltage | The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the voltage at which the capacitor is connected to the network. | ShuntCompensator |
| normalSections | [cim:ShuntCompensator.normalSections](http://iec.ch/TC57/CIM100#ShuntCompensator.normalSections) | No cardinality available integer | The normal number of sections switched in. The value shall be between zero and ShuntCompensator.maximumSections. | ShuntCompensator |
| voltageSensitivity | [cim:ShuntCompensator.voltageSensitivity](http://iec.ch/TC57/CIM100#ShuntCompensator.voltageSensitivity) | No cardinality available VoltagePerReactivePower | Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. | ShuntCompensator |
| RegulatingControl | [cim:RegulatingCondEq.RegulatingControl](http://iec.ch/TC57/CIM100#RegulatingCondEq.RegulatingControl) | No cardinality available RegulatingControl | The regulating control scheme in which this equipment participates. | RegulatingCondEq |
| BaseVoltage | [cim:ConductingEquipment.BaseVoltage](http://iec.ch/TC57/CIM100#ConductingEquipment.BaseVoltage) | No cardinality available BaseVoltage | Base voltage of this conducting equipment.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. | ConductingEquipment |
| Terminals | [cim:ConductingEquipment.Terminals](http://iec.ch/TC57/CIM100#ConductingEquipment.Terminals) | No cardinality available Terminal | Conducting equipment have terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. | ConductingEquipment |
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
