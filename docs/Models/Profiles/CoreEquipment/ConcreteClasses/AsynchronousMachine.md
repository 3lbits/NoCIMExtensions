# AsynchronousMachine

_A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g. squirrel-cage induction machine._

**URI**: [cim:AsynchronousMachine](http://iec.ch/TC57/CIM100#AsynchronousMachine)<br />
**Type**: Class

```mermaid
%%{init: {'theme':'base','themeVariables': {'lineColor': '#FF0000'}}}%%
classDiagram
    class AsynchronousMachine
    click AsynchronousMachine href "/Models/Profiles/CoreEquipment/ConcreteClasses/AsynchronousMachine/"
    style AsynchronousMachine fill:#102820,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RotatingMachine <|-- AsynchronousMachine : inherits
            click RotatingMachine href "/Models/Profiles/CoreEquipment/AbstractClasses/RotatingMachine/"
            style RotatingMachine fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        RegulatingCondEq <|-- RotatingMachine : inherits
            click RegulatingCondEq href "/Models/Profiles/CoreEquipment/AbstractClasses/RegulatingCondEq/"
            style RegulatingCondEq fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        EnergyConnection <|-- RegulatingCondEq : inherits
            click EnergyConnection href "/Models/Profiles/CoreEquipment/AbstractClasses/EnergyConnection/"
            style EnergyConnection fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        ConductingEquipment <|-- EnergyConnection : inherits
            click ConductingEquipment href "/Models/Profiles/CoreEquipment/AbstractClasses/ConductingEquipment/"
            style ConductingEquipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        Equipment <|-- ConductingEquipment : inherits
            click Equipment href "/Models/Profiles/CoreEquipment/AbstractClasses/Equipment/"
            style Equipment fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        PowerSystemResource <|-- Equipment : inherits
            click PowerSystemResource href "/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/"
            style PowerSystemResource fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
     
        IdentifiedObject <|-- PowerSystemResource : inherits
            click IdentifiedObject href "/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/"
            style IdentifiedObject fill:#8F9779,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        RotatingMachine --> GeneratingUnit : RotatingMachine.GeneratingUnit

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/AbstractClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
        RotatingMachine --> HydroPump : RotatingMachine.HydroPump

        HydroPump
            click HydroPump href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroPump/"
            style HydroPump fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white
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
            click EquipmentContainer href "/Models/Profiles/CoreEquipment/AbstractClasses/EquipmentContainer/"
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
            click EquipmentContainer href "/Models/Profiles/CoreEquipment/AbstractClasses/EquipmentContainer/"
            style EquipmentContainer fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        GeneratingUnit --> RotatingMachine : GeneratingUnit.RotatingMachine

        GeneratingUnit
            click GeneratingUnit href "/Models/Profiles/CoreEquipment/AbstractClasses/GeneratingUnit/"
            style GeneratingUnit fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

        HydroPump --> RotatingMachine : HydroPump.RotatingMachine

        HydroPump
            click HydroPump href "/Models/Profiles/CoreEquipment/ConcreteClasses/HydroPump/"
            style HydroPump fill:#A52A2A,stroke:#333,stroke-width:2px,rx:10,ry:10,color:white

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


        AsynchronousMachine : AsynchronousMachine.nominalFrequency
        AsynchronousMachine : AsynchronousMachine.nominalSpeed
        RotatingMachine : RotatingMachine.GeneratingUnit
        RotatingMachine : RotatingMachine.HydroPump
        RotatingMachine : RotatingMachine.ratedPowerFactor
        RotatingMachine : RotatingMachine.ratedS
        RotatingMachine : RotatingMachine.ratedU
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
* [IdentifiedObject](/Models/Profiles/CoreEquipment/AbstractClasses/IdentifiedObject/)
    * [PowerSystemResource](/Models/Profiles/CoreEquipment/AbstractClasses/PowerSystemResource/)
        * [Equipment](/Models/Profiles/CoreEquipment/AbstractClasses/Equipment/)
            * [ConductingEquipment](/Models/Profiles/CoreEquipment/AbstractClasses/ConductingEquipment/)
                * [EnergyConnection](/Models/Profiles/CoreEquipment/AbstractClasses/EnergyConnection/)
                    * [RegulatingCondEq](/Models/Profiles/CoreEquipment/AbstractClasses/RegulatingCondEq/)
                        * [RotatingMachine](/Models/Profiles/CoreEquipment/AbstractClasses/RotatingMachine/)
                            * **AsynchronousMachine**

## Attributes
| Name | URI | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- | --- |
| nominalFrequency | [cim:AsynchronousMachine.nominalFrequency](http://iec.ch/TC57/CIM100#AsynchronousMachine.nominalFrequency) | No cardinality available Frequency | Nameplate data indicates if the machine is 50 Hz or 60 Hz. | direct |
| nominalSpeed | [cim:AsynchronousMachine.nominalSpeed](http://iec.ch/TC57/CIM100#AsynchronousMachine.nominalSpeed) | No cardinality available RotationSpeed | Nameplate data.  Depends on the slip and number of pole pairs. | direct |
| GeneratingUnit | [cim:RotatingMachine.GeneratingUnit](http://iec.ch/TC57/CIM100#RotatingMachine.GeneratingUnit) | No cardinality available GeneratingUnit | A synchronous machine may operate as a generator and as such becomes a member of a generating unit. | RotatingMachine |
| HydroPump | [cim:RotatingMachine.HydroPump](http://iec.ch/TC57/CIM100#RotatingMachine.HydroPump) | No cardinality available HydroPump | The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. | RotatingMachine |
| ratedPowerFactor | [cim:RotatingMachine.ratedPowerFactor](http://iec.ch/TC57/CIM100#RotatingMachine.ratedPowerFactor) | No cardinality available float | Power factor (nameplate data). It is primarily used for short circuit data exchange according to IEC 60909. The attribute cannot be a negative value. | RotatingMachine |
| ratedS | [cim:RotatingMachine.ratedS](http://iec.ch/TC57/CIM100#RotatingMachine.ratedS) | No cardinality available ApparentPower | Nameplate apparent power rating for the unit.
The attribute shall have a positive value. | RotatingMachine |
| ratedU | [cim:RotatingMachine.ratedU](http://iec.ch/TC57/CIM100#RotatingMachine.ratedU) | No cardinality available Voltage | Rated voltage (nameplate data, Ur in IEC 60909-0). It is primarily used for short circuit data exchange according to IEC 60909.
The attribute shall be a positive value. | RotatingMachine |
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
